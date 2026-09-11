#!/usr/bin/env python3
"""
Decode Triumph Studios M8LD localization files used by Overlord and Overlord II.

Observed format for the supplied English corpus:
    4 bytes  ASCII magic "M8LD"
    1 byte   opaque metadata after XOR decoding
    N bytes  SpreadsheetML XML after XOR decoding

The XOR key is a 7-byte repeating key. Every observed file uses one of the
seven rotations of the same base key:

    4e e2 99 a5 4d 38 4f

This tool identifies the correct rotation by checking for the XML declaration
after the metadata byte. It is a decoder only. The meaning of the metadata
byte and the original encoder's rotation-selection rule remain unresolved.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

MAGIC = b"M8LD"
BASE_KEY = bytes.fromhex("4ee299a54d384f")
XML_PREFIX = b'<?xml version="1.0"?>'


def rotations(value: bytes) -> list[bytes]:
    return [value[i:] + value[:i] for i in range(len(value))]


def xor_repeating(data: bytes, key: bytes) -> bytes:
    return bytes(byte ^ key[i % len(key)] for i, byte in enumerate(data))


def decode_bytes(data: bytes) -> tuple[int, bytes, int, bytes]:
    """Return (rotation_index, key, metadata_byte, xml_bytes)."""
    if not data.startswith(MAGIC):
        raise ValueError("input does not begin with M8LD")
    payload = data[len(MAGIC):]
    if len(payload) < 1 + len(XML_PREFIX):
        raise ValueError("M8LD payload is too short")

    for rotation_index, key in enumerate(rotations(BASE_KEY)):
        decoded = xor_repeating(payload, key)
        if not decoded[1:].startswith(XML_PREFIX):
            continue
        xml_bytes = decoded[1:]
        ET.fromstring(xml_bytes.decode("utf-8"))
        return rotation_index, key, decoded[0], xml_bytes

    raise ValueError("no valid 7-byte key rotation produced SpreadsheetML XML")


def decode_file(source: Path, destination: Path | None = None) -> Path:
    rotation, key, metadata, xml_bytes = decode_bytes(source.read_bytes())
    if destination is None:
        destination = source.with_suffix(".xml")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(xml_bytes)
    print(
        f"{source} -> {destination} "
        f"(rotation={rotation}, key={key.hex()}, metadata=0x{metadata:02x})"
    )
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description="Decode Overlord M8LD files to XML")
    parser.add_argument("input", type=Path, help=".8ld file or directory")
    parser.add_argument("-o", "--output", type=Path, help="output file or directory")
    args = parser.parse_args()

    if args.input.is_file():
        decode_file(args.input, args.output)
        return 0

    if not args.input.is_dir():
        parser.error("input must be a file or directory")

    output_root = args.output or args.input
    for source in sorted(args.input.rglob("*.8ld")):
        rel = source.relative_to(args.input).with_suffix(".xml")
        decode_file(source, output_root / rel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
