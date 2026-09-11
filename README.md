# Overlord Lore and Canon

Private working repository for OVERLORD REIGN franchise-source research, lore reconciliation, quest-source reconstruction, and Gnarl dialogue analysis.

## Authority boundary

This repository is a reference and research workspace. Original Overlord franchise evidence does not automatically become OVERLORD REIGN canon.

OVERLORD REIGN canon remains governed by the canonical project files and the Overlord's explicit decisions.

## Repository layout

```text
source/
  overlord1/
  companion/
tools/
  decode_8ld.py
  extract_localization.py
research/
  8LD_FORMAT.md
  8LD_DECODER_RESEARCH.md
  decoder_validation_manifest.csv
corpus/
  CORPUS_INDEX.md
  overlord1/
  raising_hell/
  overlord2/
reference/
  pass01/
  pass02/
```

The `source/` tree intentionally contains only the minimal active non-audio research subset. Original game archives and MP3 payloads remain outside the repository.

## M8LD status

Read-only `.8ld` decoding is solved.

The supplied `M8LD` files contain Microsoft SpreadsheetML XML XOR-obfuscated with a repeating seven-byte key. All 96 selected Overlord I, Raising Hell, and Overlord II language files decode and parse successfully with `tools/decode_8ld.py`.

See `research/8LD_FORMAT.md` for the validated format description and remaining unknowns.

## Current corpus

Searchable primary-source CSVs can be generated directly from the supplied localization workbooks. Current extraction covers Overlord I dialogue and Gnarl material, Raising Hell dialogue and Gnarl material, Overlord II dialogue, and Overlord II quest/objective text from `System_Quests.8ld`.

Speaker fields are preserved only where the original source supplies them. Overlord II actor cells are blank in the supplied narrative sheets, so speaker identity is not invented.

## Source discipline

Internal quest IDs, debug labels, aliases, map comments, and developer-facing names are `PRIMARY-IMPLEMENTATION` evidence, not automatically player-facing franchise terminology.

Decoded localization text is `PRIMARY-TEXT`.

Nothing in this repository becomes OVERLORD REIGN `CANON` merely by being present here.
