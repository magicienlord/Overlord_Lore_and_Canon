# Franchise Source Corpus Index

Status: PRIMARY-SOURCE EXTRACTION

Generated: 2026-09-11

This corpus is derived directly from the user-supplied Overlord game localization and map files. It is franchise evidence, not automatically OVERLORD REIGN canon.

## Overlord I

Current extraction totals:

- extracted English text rows: 2,588
- original localization workbook rows explicitly naming actor `GNARL`: 759
- direct map-script Minion Master references matched exactly or through source-name normalization: 368 of 379
- remaining direct references requiring source reconciliation: 11

The normalized dialogue schema preserves scene ID, text ID, actor, English text, trigger/context, timing, mode, and developer notes where present.

## Raising Hell

Current extraction totals:

- extracted English text rows: 483
- localization workbook rows explicitly naming actor `GNARL`: 152
- current Gnarl-attributed/source-linked working set: 187 rows

Expansion maps retain base-campaign state, so expansion-specific map attribution must continue to distinguish `EXP_*` references from inherited hooks.

## Overlord II

Current extraction totals:

- extracted English narrative/interface text rows outside `Resources/System_Quests.8ld`: 8,587
- quest/objective text rows from `Resources/System_Quests.8ld`: 499

The supplied Overlord II narrative spreadsheets leave actor cells blank. Speaker attribution therefore remains a separate source-correlation task and is not inferred from memory.

`System_Quests.8ld` preserves internal quest IDs, text identifiers such as `DESC` and `DESC_DONE`, English quest strings, ordering, and developer notes.

## Source discipline

The extracted text is `PRIMARY-TEXT` from the supplied game data.

Actor values are preserved exactly when the source workbook supplies them.

Missing actor values remain missing.

Internal quest IDs remain `PRIMARY-IMPLEMENTATION` terminology unless corroborated as player-facing terms.

Large generated CSV tables are reproducible working artifacts and do not need to be treated as canon files. Curated lore and quest conclusions should cite their exact source file, scene/text ID, and evidence class.
