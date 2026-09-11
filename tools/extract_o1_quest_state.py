#!/usr/bin/env python3
"""Extract live Overlord I quest-state API calls from .omp maps.

The supplied maps embed readable Lua source alongside compiled data. This tool
extracts source-like printable runs, removes Lua comments, and records calls to
the observed quest-state API.

The comment-removal step is required. Counting raw binary strings otherwise
promotes dead/commented calls such as the `D3_KHAN` typo and a commented
`D4_FREE_ELVES` Evil completion into the live quest graph.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re

SOURCE_RUN = re.compile(rb"[\x09\x0a\x0d\x20-\x7e]{5,}")

FUNCTIONS = [
    ("GetQuestCompletedEvil", "get_completed_evil"),
    ("GetQuestCompleted", "get_completed"),
    ("GetQuestEnabled", "get_enabled"),
    ("GetQuestCounter", "get_counter"),
    ("SetQuestCompletedSilent", "set_completed_silent"),
    ("SetQuestCompletedEvil", "set_completed_evil"),
    ("SetQuestCompleted", "set_completed"),
    ("SetQuestEnabled", "set_enabled"),
    ("SetQuestDisabled", "set_disabled"),
]


def strip_lua_comments(source: str) -> str:
    # Remove block comments first, then line comments. In the reviewed source
    # strings `--` is used as Lua comment syntax rather than inside quoted
    # dialogue values involved in quest API calls.
    source = re.sub(r"--\[\[.*?\]\]", "", source, flags=re.S)
    cleaned = []
    for line in source.splitlines() or [source]:
        marker = line.find("--")
        if marker >= 0:
            line = line[:marker]
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_map(path: Path) -> list[dict[str, str | int]]:
    data = path.read_bytes()
    rows: list[dict[str, str | int]] = []

    for run in SOURCE_RUN.finditer(data):
        raw = run.group().decode("latin1")
        source = strip_lua_comments(raw)

        for function, operation in FUNCTIONS:
            pattern = re.compile(rf'{re.escape(function)}\s*\(\s*"([^"]+)"')
            for match in pattern.finditer(source):
                rows.append({
                    "map": str(path),
                    "offset": run.start() + match.start(),
                    "function": function,
                    "operation": operation,
                    "quest_id": match.group(1),
                    "source_fragment": source.strip(),
                })

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract live O1 quest-state calls")
    parser.add_argument("maps", type=Path, help="Overlord I .omp file or map directory")
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

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["map", "offset", "function", "operation", "quest_id", "source_fragment"]
    with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    unique_ids = {str(row["quest_id"]) for row in rows}
    print(f"wrote {len(rows)} live quest-state calls across {len(unique_ids)} quest IDs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
