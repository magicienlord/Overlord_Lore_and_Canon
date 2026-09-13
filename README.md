# Overlord Lore and Canon

Private working repository for OVERLORD REIGN franchise-source research, lore reconciliation, quest-source reconstruction, and Gnarl dialogue analysis.

## Authority boundary

This repository is a reference and research workspace. Original Overlord franchise evidence does not automatically become OVERLORD REIGN canon.

OVERLORD REIGN canon remains governed by the canonical project files and the Overlord's explicit decisions.

## Current quest-integration authorities

For Overlord Quests design and implementation, start with:

- `reference/39_REIGN_QUEST_AUTHORITY_AND_INTENTIONAL_DISCRETION.md` - master interpretation and authority-order file. It distinguishes genuine unknowns from implementation-dependent details and deliberately delegated Quest Maker decisions.

Then consult the specialized authorities it orders:

- `reference/38_REIGN_MINION_TYPE_UNLOCK_ANCHORS.md` - authoritative division of responsibility for Brown / Red / Green / Blue unlocks: the Minion implementation exposes anchors, while Overlord Quests authors and triggers the unlock progression;
- `reference/37_REIGN_PERSONAL_MOD_SIDEQUEST_DECISIONS.md` - authoritative Overlord Depths / Fathoms and Overlord NightWalker / Nycto sidequest decisions;
- `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` - authoritative final assignment for reviewed mods: dedicated questline, absorbed content, popup acknowledgement, systemic/ambient treatment, or no quest-facing treatment;
- `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md` - authoritative Dark Tower restoration ownership and the boundary between room activation and deeper system progression;
- `reference/32_REIGN_QUESTLINE_COVERAGE_LEDGER.md` - minimum coverage and completion checklist.

`reference/33_REIGN_MOD_QUESTLINE_ASSIGNMENTS.md` and `reference/35_REIGN_MOD_ASSIGNMENT_CONTINUATION.md` are interview-history mirrors and are superseded by the later authority files for assignment decisions.

Where an older coverage or implementation statement conflicts with a later explicit decision file, follow the authority order in `reference/39_REIGN_QUEST_AUTHORITY_AND_INTENTIONAL_DISCRETION.md`.

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
  ...current REIGN decision ledgers...
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
