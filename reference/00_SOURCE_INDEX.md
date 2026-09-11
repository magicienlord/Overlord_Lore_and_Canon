# OVERLORD Franchise Primary Source Index

Status: PRIMARY-SOURCE REFERENCE

Date: 2026-09-11

Authority: franchise evidence only. Nothing in this repository becomes OVERLORD REIGN canon merely by being present here.

## 1. Master source set

The working corpus is derived from two user-supplied game-data archives:

- `Overlord 1.zip`: Overlord I base-game language/audio/map material plus overlapping Raising Hell language/audio.
- `Overlord_Quests_Lore_Ressources.zip`: Overlord II language/maps, dedicated Raising Hell maps, official PC manuals, and one alternate Overlord I Tower map variant.

The original game archives and MP3 payloads are intentionally kept outside this repository. The repository contains only the compact active source subset needed for reproducible source work.

## 2. Active repository source

The `source/` tree contains:

- all selected Overlord I / Raising Hell `.8ld` localization binaries;
- all selected Overlord II `.8ld` localization binaries;
- selected map/source fixtures required for reproducible implementation analysis;
- minimal supporting metadata.

Bulk audio payloads and unrelated installation files are not required for ordinary text-corpus work. Additional maps are imported or consulted only when a specific source-analysis pass requires them.

## 3. Localization format status

The `.8ld` technical blocker is resolved.

All selected files use Triumph Studios' `M8LD` wrapper around Microsoft SpreadsheetML XML. The payload is XOR-obfuscated with a repeating seven-byte key. `tools/decode_8ld.py` reproduces the conversion transparently and has validated all 96 selected Overlord I, Raising Hell, and Overlord II localization files with zero failures.

The validated binary format and remaining encoder unknowns are documented in:

- `research/8LD_FORMAT.md`
- `research/8LD_DECODER_RESEARCH.md`
- `research/decoder_validation_manifest.csv`

## 4. Corpus extraction

`tools/extract_localization.py` converts decoded SpreadsheetML into normalized source rows while preserving the original workbook's sparse column layout.

The normalized row schema preserves, where present:

```text
game
source file
worksheet
source group
order
scene ID
text ID
localization reference
actor
English text
scene context
trigger
direction
directed-to field
timing
mode
developer notes
localisation notes
```

The generated working corpus is indexed in `corpus/CORPUS_INDEX.md`.

## 5. Evidence classes

The reference layer uses evidence labels separate from OVERLORD REIGN's `CANON / PLANNED / PROPOSAL / UNKNOWN` statuses.

### PRIMARY-EXPLICIT

Directly stated by original game text, system text, objective text, or unambiguous scripted behavior.

### PRIMARY-IMPLIED

Strongly supported by multiple primary-source facts but not stated in one unambiguous sentence.

### PRIMARY-IMPLEMENTATION

Established by map scripts, internal quest states, aliases, triggers, developer comments, or other implementation data. Internal terminology is not automatically player-facing lore terminology.

### BRANCH-DEPENDENT

True only under one or more player-choice outcomes.

### PRIMARY-CONFLICT

Two primary-source statements appear inconsistent and cannot yet be reconciled safely.

### RESOLVED-SURFACE-CONFLICT

Two statements initially appear inconsistent, but later primary material explicitly explains the discrepancy.

### UNVERIFIED / UNKNOWN

Not established by the currently reviewed primary corpus.

## 6. Source hierarchy

For factual franchise claims, use the following order:

1. decoded original localization and quest/system text;
2. original map/script implementation where available;
3. official manuals;
4. original English audio only when text/speaker attribution requires it;
5. external secondary material only for indexing or locating primary evidence.

Wiki summaries and memory are not acceptable sole authority for a claim that can be checked against the supplied source corpus.

## 7. Speaker-attribution rule

Overlord I and Raising Hell workbooks frequently include explicit actor fields. Those actor values are authoritative for the corresponding localization rows.

Implementation function names are not sufficient by themselves. In particular, `ShowMinionMasterText(...)` routes lines spoken by multiple actors and must not be interpreted as a guarantee that Gnarl is speaking. The corrected analysis is in `corpus/overlord1/MINIONMASTER_ROUTING_RECONCILIATION.md`.

The supplied Overlord II narrative workbooks generally leave actor cells blank. Speaker identity is accepted only when direct map implementation identifies the speaker through structures such as:

- face-expression speaker routing;
- explicit `Speak` actor entities;
- conservative character-specific implementation labels adjacent to a resolved localization reference.

`tools/extract_o2_map_speakers.py` and `tools/extract_o2_named_gnarl_labels.py` reproduce those source-attribution passes.

Missing actors remain missing when no direct source mechanism identifies them. Similar vocabulary is not evidence.

## 8. Major source coverage

The current reference layer covers:

- chronology from the pre-Overlord-I ruler through Overlord II;
- Overlord succession and lineage evidence;
- Minions, Lifeforce, Hives, souls, Gates, and the Netherworld;
- peoples, factions, cultures, and political institutions;
- named franchise locations and geographic relationships;
- magic, Mana, Evil energy, Light magic, Spell Stones, Tower Hearts, and anti-magic;
- major and quest-relevant secondary characters;
- quest architecture, live Overlord I state logic, source-proven dependency relationships, and branch-specific outcomes;
- Gnarl's directly attributed dialogue and production-direction metadata across all three supplied campaign phases;
- non-Gnarl dialogue practice and ordinary-world social stakes;
- unresolved source ambiguities and franchise-to-REIGN adoption status.

## 9. Canon boundary

A franchise fact can be historically true in the original continuity without being adopted unchanged into OVERLORD REIGN.

The adoption ledger therefore uses a second vocabulary:

- `ADOPTED`
- `ADAPTED`
- `REJECTED`
- `RESERVED`
- `UNDECIDED`

Source truth and REIGN adaptation truth must remain separate throughout quest authorship.
