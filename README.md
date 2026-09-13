# Overlord Lore and Canon

Private working repository for OVERLORD REIGN franchise-source research, lore reconciliation, quest-source reconstruction, and character dialogue analysis.

## Authority boundary

This repository is a reference and research workspace. Original Overlord franchise evidence does not automatically become OVERLORD REIGN canon.

OVERLORD REIGN canon remains governed by the canonical project files and the Overlord's explicit decisions.

## Current quest-integration authorities

For Overlord Quests design and implementation, start with:

- `reference/39_REIGN_QUEST_AUTHORITY_AND_INTENTIONAL_DISCRETION.md` - master interpretation and authority-order file. It distinguishes genuine unknowns from implementation-dependent details and deliberately delegated Quest Maker decisions.

Then consult the specialized authorities it orders, plus later specialized authorities where applicable:

- `reference/44_REIGN_LESTAT_CONTINUITY_AUTHORITY_FINAL.md` - authoritative final REIGN-native Lestat continuity for the NightWalker sidequest. It controls what IWTV-derived history actually happened in REIGN and supersedes older generic statements that Lestat's pre-Tower history is wholly unknown;
- `reference/38_REIGN_MINION_TYPE_UNLOCK_ANCHORS.md` - authoritative division of responsibility for Brown / Red / Green / Blue unlocks: the Minion implementation exposes anchors, while Overlord Quests authors and triggers the unlock progression;
- `reference/37_REIGN_PERSONAL_MOD_SIDEQUEST_DECISIONS.md` - authoritative Overlord Depths / Fathoms and Overlord NightWalker / Nycto sidequest decisions;
- `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` - authoritative final assignment for reviewed mods: dedicated questline, absorbed content, popup acknowledgement, systemic/ambient treatment, or no quest-facing treatment;
- `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md` - authoritative Dark Tower restoration ownership and the boundary between room activation and deeper system progression;
- `reference/32_REIGN_QUESTLINE_COVERAGE_LEDGER.md` - minimum coverage and completion checklist.

`reference/33_REIGN_MOD_QUESTLINE_ASSIGNMENTS.md` and `reference/35_REIGN_MOD_ASSIGNMENT_CONTINUATION.md` are interview-history mirrors and are superseded by the later authority files for assignment decisions.

`reference/41_REIGN_LESTAT_CONTINUITY_DECISIONS.md`, `reference/42_REIGN_LESTAT_CONTINUITY_INTERVIEW_CONTINUATION.md`, and `reference/43_REIGN_LESTAT_CONTINUITY_FINAL_INTERVIEW_BLOCK.md` are Lestat continuity interview-history records. Use `reference/44_REIGN_LESTAT_CONTINUITY_AUTHORITY_FINAL.md` for implementation rather than independently reconciling those three records.

Where an older coverage or implementation statement conflicts with a later explicit decision file, follow the authority order in `reference/39_REIGN_QUEST_AUTHORITY_AND_INTENTIONAL_DISCRETION.md` together with later explicit specialized authorities such as `44`.

## Character-writing references

- `reference/GNARL_WRITING_RULES.md` - operational source-grounded Gnarl voice rules for OVERLORD REIGN.
- `reference/40_REIGN_LESTAT_CHARACTER_AND_WRITING_RULES.md` - transcript-grounded television-series Lestat character sheet and REIGN adaptation rules for voice, psychology, dialogue mechanics, and source-confidence discipline.
- `reference/44_REIGN_LESTAT_CONTINUITY_AUTHORITY_FINAL.md` - final continuity authority for what REIGN-native Lestat actually lived, who exists in his history, and which source-continuity facts are adapted, rejected, or deliberately left unknown.
- `reference/IWTV_Complete_Attributed_Transcripts/` - supplied 22-episode IWTV transcript corpus used for Lestat characterization. Attribution confidence must be respected when deriving dialogue rules.

For Lestat, use `40` and `44` together: `40` governs how he is written; `44` governs what happened to him in REIGN.

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
  ...current REIGN decision ledgers and character-writing references...
```

The `source/` tree intentionally contains only the minimal active non-audio research subset. Original game archives and MP3 payloads remain outside the repository.

## M8LD status

Read-only `.8ld` decoding is solved.

The supplied `M8LD` files contain Microsoft SpreadsheetML XML XOR-obfuscated with a repeating seven-byte key. All 96 selected Overlord I, Raising Hell, and Overlord II language files decode and parse successfully with `tools/decode_8ld.py`.

See `research/8LD_FORMAT.md` for the validated format description and remaining unknowns.

## Current corpus

Searchable primary-source CSVs can be generated directly from the supplied localization workbooks. Current extraction covers Overlord I dialogue and Gnarl material, Raising Hell dialogue and Gnarl material, Overlord II dialogue, and Overlord II quest/objective text from `System_Quests.8ld`.

The repository also contains the supplied IWTV episode-transcript corpus used specifically for the NightWalker Lestat characterization work. Its attribution-confidence metadata is part of the source and must not be discarded during character analysis.

Speaker fields are preserved only where the original source supplies them or where a separate reconstruction explicitly records its confidence. Do not silently upgrade inferred attribution to primary certainty.

## Source discipline

Internal quest IDs, debug labels, aliases, map comments, and developer-facing names are `PRIMARY-IMPLEMENTATION` evidence, not automatically player-facing franchise terminology.

Decoded Overlord localization text is `PRIMARY-TEXT` for franchise research.

The supplied IWTV corpus is an external character-reference corpus for the REIGN Lestat adaptation and is not Overlord franchise canon.

Nothing in this repository becomes OVERLORD REIGN `CANON` merely by being present here.
