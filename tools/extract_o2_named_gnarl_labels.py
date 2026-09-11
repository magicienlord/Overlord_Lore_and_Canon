#!/usr/bin/env python3
"""Extract Overlord II Gnarl dialogue refs from character-specific map labels.

The supplied Overlord II maps contain implementation labels such as:

    GNARL_GENERAL
    GNARL_KELDA_1
    GNARL_JUNO_2
    INITIAL_GNARL
    CS_GNARL_CHOICE1

These labels are frequently followed within a few printable-string records by
the localization reference used by that Gnarl event. This extractor accepts
only explicitly Gnarl-named labels and rejects obvious waypoint/control labels.

It does not infer speaker identity from dialogue wording.

For maximum precision, pass a normalized localization CSV with
--localization-csv. A row is then emitted as matched only when the reference
resolves to a real decoded localization row after conservative normalization.
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


def norm_group(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def norm_ref(value: str) -> tuple[str, str, str] | None:
    parts = clean(value).rsplit("@", 2)
    if len(parts) != 3:
        return None
    group, scene, text_id = parts
    return norm_group(group), scene.upper(), text_id.upper()


def is_gnarl_label(value: str) -> bool:
    upper = value.upper()
    if not (
        upper.startswith("GNARL")
        or upper.startswith("INITIAL_GNARL")
        or upper.startswith("CS_GNARL")
    ):
        return False

    # These are placement/control labels, not dialogue-event identities.
    if any(token in upper for token in ("_WP", "POINT", "HOME", "PORT", "AUDITION")):
        return False
    return True


def load_localization(path: Path | None) -> dict[tuple[str, str, str], str]:
    if path is None:
        return {}

    result: dict[tuple[str, str, str], str] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            ref = row.get("localization_ref", "")
            key = norm_ref(ref)
            if key:
                result[key] = ref
    return result


def extract_map(path: Path, localization: dict[tuple[str, str, str], str]) -> list[dict[str, str | int]]:
    data = path.read_bytes()
    runs = [(m.start(), m.group().decode("latin1")) for m in PRINTABLE.finditer(data)]
    rows: list[dict[str, str | int]] = []

    for index, (offset, value) in enumerate(runs):
        label = clean(value)
        if not is_gnarl_label(label):
            continue

        # The observed event structures place the dialogue ref very close to
        # the named Gnarl label. Accept the first reference in the next four
        # printable records only.
        found_ref = ""
        distance = 0
        for step in range(1, 5):
            if index + step >= len(runs):
                break
            candidate = clean(runs[index + step][1])
            if REF.match(candidate):
                found_ref = candidate
                distance = step
                break

        if not found_ref:
            continue

        key = norm_ref(found_ref)
        resolved = localization.get(key, "") if key and localization else ""
        rows.append({
            "map": str(path),
            "offset": offset,
            "gnarl_label": label,
            "localization_ref": found_ref,
            "distance_runs": distance,
            "resolved_localization_ref": resolved,
            "matched_localization": "true" if resolved else ("unknown" if not localization else "false"),
            "evidence": "DIRECT_NAMED_GNARL_LABEL",
        })

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract direct named-Gnarl routing from Overlord II maps")
    parser.add_argument("maps", type=Path, help="Overlord II .omp file or map directory")
    parser.add_argument("-o", "--output", type=Path, required=True, help="CSV output")
    parser.add_argument("--localization-csv", type=Path, help="normalized decoded O2 localization CSV for exact validation")
    args = parser.parse_args()

    localization = load_localization(args.localization_csv)

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
        rows.extend(extract_map(path, localization))

    # Keep distinct map/label/reference evidence while eliminating duplicate
    # copies of the same record encountered through the binary string table.
    seen = set()
    deduped = []
    for row in rows:
        key = (
            row["map"],
            row["gnarl_label"],
            norm_ref(str(row["localization_ref"])),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "map", "offset", "gnarl_label", "localization_ref", "distance_runs",
        "resolved_localization_ref", "matched_localization", "evidence",
    ]
    with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(deduped)

    print(f"wrote {len(deduped)} named-Gnarl routing records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
