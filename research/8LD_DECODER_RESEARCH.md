# 8LD Decoder Research

Status: DECODER SOLVED FOR READ-ONLY EXTRACTION

Date: 2026-09-11

The previous technical blocker is resolved.

The supplied `.8ld` localization files are `M8LD` containers holding XOR-obfuscated Microsoft SpreadsheetML XML. The payload uses a repeating seven-byte key whose value is one of seven rotations of the base key `4e e2 99 a5 4d 38 4f`.

`tools/decode_8ld.py` reproduces the conversion locally and has validated all 96 selected Overlord I, Raising Hell, and Overlord II `.8ld` files with zero failures.

Historical O2Tools references remain useful corroboration that `.8ld -> XML` conversion was the established modding workflow, but O2Tools is no longer required for this project.

Open reverse-engineering questions are limited to the meaning of the leading decoded metadata byte and the original encoder's key-rotation selection rule. Neither blocks lore or quest extraction.
