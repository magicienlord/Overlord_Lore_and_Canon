#!/usr/bin/env python3
"""
Extract English localization rows from decoded Overlord SpreadsheetML XML.

The game localization workbooks are Excel 2003 XML documents. This extractor
respects SpreadsheetML ss:Index gaps, detects the script header row, and emits
a normalized CSV suitable for source-corpus analysis.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
import xml.etree.ElementTree as ET

SS_NS = "urn:schemas-microsoft-com:office:spreadsheet"
SS = f"{{{SS_NS}}}"


def normalize(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).upper()


def row_values(row: ET.Element) -> list[str | None]:
    values: list[str | None] = []
    column = 1
    for cell in row.findall(f"{SS}Cell"):
        index = cell.attrib.get(f"{SS}Index")
        if index:
            target = int(index)
            while column < target:
                values.append(None)
                column += 1
        data = cell.find(f"{SS}Data")
        values.append(data.text if data is not None else None)
        column += 1
    return values


def extract(xml_bytes: bytes, source_group: str, source_file: str, game: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes.decode("utf-8"))
    extracted: list[dict[str, str]] = []

    for worksheet in root.findall(f"{SS}Worksheet"):
        worksheet_name = worksheet.attrib.get(f"{SS}Name", "")
        table = worksheet.find(f"{SS}Table")
        if table is None:
            continue
        rows = [row_values(row) for row in table.findall(f"{SS}Row")]

        header_index = None
        headers = None
        for index, row in enumerate(rows):
            normalized = [normalize(value) for value in row]
            if "SCENE ID" in normalized and (
                "TEXT / SPEECH" in normalized or "TEXT/SPEECH" in normalized
            ):
                header_index = index
                headers = row
                break

        if header_index is None or headers is None:
            continue

        positions = {normalize(header): index for index, header in enumerate(headers) if header}

        def get(row: list[str | None], *names: str) -> str:
            for name in names:
                index = positions.get(normalize(name))
                if index is not None and index < len(row):
                    return row[index] or ""
            return ""

        for row in rows[header_index + 1:]:
            scene_id = get(row, "SCENE ID")
            text_id = get(row, "TEXT ID")
            text = get(row, "TEXT / SPEECH", "TEXT/SPEECH")
            actor = get(row, "ACTOR")
            if not text:
                continue

            reference = f"{source_group}@{scene_id}@{text_id}" if scene_id and text_id else ""
            extracted.append({
                "game": game,
                "source_file": source_file,
                "worksheet": worksheet_name,
                "source_group": source_group,
                "order": get(row, "ORDER"),
                "scene_id": scene_id,
                "text_id": text_id,
                "localization_ref": reference,
                "actor": actor,
                "text": text,
                "scene_context": get(row, "SCENE CONTEXT"),
                "trigger": get(row, "TRIGGER"),
                "direction": get(row, "DIRECTION"),
                "directed_to": get(row, "DIRECTED TO"),
                "timing": get(row, "TIMING"),
                "mode": get(row, "MODE"),
                "dev_notes": get(row, "DEV TEAM / MISC NOTES"),
                "localisation_notes": get(row, "LOCALISATION NOTES"),
            })

    return extracted


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("--game", required=True)
    parser.add_argument("--group")
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()

    group = args.group or args.xml.stem
    rows = extract(args.xml.read_bytes(), group, str(args.xml), args.game)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    fields = list(rows[0]) if rows else []
    with args.output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
