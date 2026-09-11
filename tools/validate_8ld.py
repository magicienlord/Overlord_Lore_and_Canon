#!/usr/bin/env python3
"""Validate every M8LD file below a source directory and report decoder metadata."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

from decode_8ld import decode_bytes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    rows = []
    failures = []
    for source in sorted(args.root.rglob("*.8ld")):
        try:
            rotation, key, metadata, xml_bytes = decode_bytes(source.read_bytes())
            rows.append({
                "source_file": str(source.relative_to(args.root)),
                "size": source.stat().st_size,
                "key_rotation": rotation,
                "key_hex": key.hex(),
                "metadata_byte": metadata,
                "xml_bytes": len(xml_bytes),
            })
        except Exception as exc:
            failures.append((source, str(exc)))

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
            fields = list(rows[0]) if rows else ["source_file"]
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    print(f"decoded={len(rows)} failures={len(failures)}")
    for source, error in failures:
        print(f"FAIL {source}: {error}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
