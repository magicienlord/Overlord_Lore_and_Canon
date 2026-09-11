#!/usr/bin/env python3
"""Extract high-confidence Overlord II speaker routing from .omp maps.

Two direct implementation patterns are accepted.

Face-expression routing:
    Face Expression...
    <speaker role / face type>
    <LOCALIZATION_GROUP@SCENE@TEXT>
    <map actor/entity alias>

Explicit Speak routing:
    Speak
    <map actor/entity alias>
    ...
    <LOCALIZATION_GROUP@SCENE@TEXT>

For Speak records, only the first localization reference within the next 12
printable strings is emitted, and the search stops if another Speak record is
encountered. This tool does not infer speakers from dialogue content or voice.
It deliberately favors precision over recall.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re

PRINTABLE = re.compile(rb"[\x20-\x7e]{4,}")
REF = re.compile(r"^[A-Za-z0-9_ ()\-]+@[A-Za-z0-9_]+@[A-Za-z0-9_]+[`\\]?$")


def clean(value: str) -> str:
    return value.strip().strip("`\\")


def extract_map(path: Path) -> list[dict[str, str | int]]:
    data = path.read_bytes()
    runs = [(match.start(), match.group().decode("latin1")) for match in PRINTABLE.finditer(data)]
    rows: list[dict[str, str | int]] = []

    # Pattern 1: face-expression speaker routing.
    for index, (offset, value) in enumerate(runs):
        if not REF.match(value):
            continue
        if index < 2 or "Face Expression" not in runs[index - 2][1]:
            continue
        rows.append({
            "map": str(path),
            "offset": offset,
            "localization_ref": clean(value),
            "routing_role": clean(runs[index - 1][1]),
            "map_entity": clean(runs[index + 1][1]) if index + 1 < len(runs) else "",
            "evidence": "DIRECT_MAP_ACTOR_ROUTING",
        })

    # Pattern 2: explicit Speak actor routing.
    for index, (offset, value) in enumerate(runs):
        if value != "Speak" or index + 1 >= len(runs):
            continue
        actor = clean(runs[index + 1][1])
        for cursor in range(index + 2, min(len(runs), index + 13)):
            candidate = runs[cursor][1]
            if candidate == "Speak":
                break
            if not REF.match(candidate):
                continue
            rows.append({
                "map": str(path),
                "offset": offset,
                "localization_ref": clean(candidate),
                "routing_role": "",
                "map_entity": actor,
                "evidence": "DIRECT_MAP_SPEAK_ACTOR",
            })
            break

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract high-confidence O2 speaker routing from OMP maps")
    parser.add_argument("maps", type=Path, help="Overlord II map file or directory")
    parser.add_argument("-o", "--output", type=Path, required=True, help="CSV output")
    args = parser.parse_args()

    if args.maps.is_file():
        paths = [args.maps]
    elif args.maps.is_dir():
        paths = sorted(args.maps.rglob("*.omp"))
    else:
        parser.error("maps must be an .omp file or directory")

    rows: list[dict[str, str | int]] = []
    for path in paths:
        if "mpmaps" in {part.lower() for part in path.parts}:
            continue
        rows.extend(extract_map(path))

    seen = set()
    deduped = []
    for row in rows:
        key = (
            row["map"],
            row["localization_ref"].upper(),
            row["routing_role"],
            row["map_entity"],
            row["evidence"],
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["map", "offset", "localization_ref", "routing_role", "map_entity", "evidence"]
    with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(deduped)

    print(f"wrote {len(deduped)} high-confidence speaker-routing rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
