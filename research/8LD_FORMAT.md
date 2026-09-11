# Triumph M8LD Format: Decoding Findings

Status: VALIDATED DECODER FOR THE SUPPLIED ENGLISH OVERLORD I / RAISING HELL / OVERLORD II CORPUS

Date: 2026-09-11

## Result

The `.8ld` localization format used by the supplied Overlord games is now decoded reproducibly without O2Tools.

Every one of the 96 selected `.8ld` files in the active source corpus was successfully converted to valid UTF-8 Microsoft SpreadsheetML XML and parsed with a standard XML parser.

The same method also validated the duplicated copies present in the original archive set, for 106 successful decode/parse operations total and zero failures.

## Binary layout observed

```text
offset  size  meaning
0x00    4     ASCII magic: M8LD
0x04    1     encrypted/obfuscated metadata byte
0x05    ...   encrypted/obfuscated SpreadsheetML XML
```

The complete payload after `M8LD` is XORed with a repeating seven-byte key.

Base key:

```text
4e e2 99 a5 4d 38 4f
```

Observed files use one of the seven cyclic rotations of this same key.

The correct rotation is detectable deterministically because, after decoding, byte 0 is the metadata byte and byte 1 begins:

```text
<?xml version="1.0"?>
```

The decoder therefore tries the seven rotations, selects the one producing the XML declaration at payload position 1, and then validates the resulting document with an XML parser.

## Key rotations observed

```text
4e e2 99 a5 4d 38 4f
e2 99 a5 4d 38 4f 4e
99 a5 4d 38 4f 4e e2
a5 4d 38 4f 4e e2 99
4d 38 4f 4e e2 99 a5
38 4f 4e e2 99 a5 4d
4f 4e e2 99 a5 4d 38
```

All seven rotations occur in the source set.

## Decoded document type

The decrypted data is not a bespoke dialogue binary. It is Excel 2003 XML / Microsoft SpreadsheetML.

The narrative workbooks preserve localization-production fields such as:

- ORDER
- SCENE ID
- TEXT ID
- SCENE CONTEXT
- TRIGGER
- DIRECTION
- ACTOR
- TEXT / SPEECH
- TIMING
- MODE
- DEV TEAM / MISC NOTES
- LOCALISATION NOTES
- translated language columns

This is substantially richer evidence than subtitles alone because it preserves original scene identifiers, actors where populated, trigger/context notes, and developer-facing sequencing.

`Resources/System_Quests.8ld` in Overlord II similarly preserves internal quest identifiers and objective/completion strings.

## Remaining unknowns

### Metadata byte

The first decoded payload byte before the XML declaration varies by file. Its semantic purpose has not yet been established.

It is not required for read-only decoding.

### Encoder rotation selection

The original rule used to choose which key rotation is written to a file has not yet been established.

It is not required for read-only decoding because the rotation can be identified from the XML declaration.

### Repacking

This pass establishes a reliable unpacker/decoder only.

No claim is made yet that arbitrary modified XML can be repacked into a byte-identical or game-valid `.8ld`. Repacking is unnecessary for the current lore/quest-source objective.

## Validation

Validation performed on:

- 50 Overlord I / Raising Hell `.8ld` files from `Overlord 1.zip`
- 46 Overlord II `.8ld` files from the companion source archive
- duplicated source copies where available

Selected corpus result:

```text
files decoded: 96
valid XML documents: 96
failures: 0
```

This resolves the previous `GAP-002: .8ld decoding` blocker for read-only source extraction.
