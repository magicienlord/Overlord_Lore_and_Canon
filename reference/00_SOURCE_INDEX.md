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
- the Overlord I Tower map used as the first decoder validation fixture;
- minimal supporting metadata.

Bulk map files, audio payloads, manuals, and unrelated installation files are not required for ordinary text-corpus work and are added only when a specific source question requires them.

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

Overlord I and Raising Hell workbooks frequently include explicit actor fields. Those actor values may be used directly.

The supplied Overlord II narrative workbooks generally leave actor cells blank. Missing actors remain missing until independently reconstructed from map/event context. Speaker identity must not be filled from memory simply because a line sounds characteristic of a known character.

## 8. Major source coverage

The current reference layer covers:

- chronology from the pre-Overlord-I ruler through Overlord II;
- Overlord succession and lineage evidence;
- Minions, Lifeforce, Hives, souls, Gates, and the Netherworld;
- peoples, factions, cultures, and political institutions;
- named franchise locations and geographic relationships;
- magic, Mana, Evil energy, Light magic, Spell Stones, Tower Hearts, and anti-magic;
- major quest-relevant characters;
- quest architecture and branch-specific outcomes;
- Gnarl's explicitly attributed dialogue and production-direction metadata.

Files `10` through `13` extend the corpus into non-Gnarl dialogue practice, everyday-world rules, ambiguities, and the OVERLORD REIGN adoption ledger.

## 9. Canon boundary

A franchise fact can be historically true in the original continuity without being adopted unchanged into OVERLORD REIGN.

The adoption ledger therefore uses a second vocabulary:

- `ADOPTED`
- `ADAPTED`
- `REJECTED`
- `RESERVED`
- `UNDECIDED`

Source truth and REIGN adaptation truth must remain separate throughout quest authorship.
