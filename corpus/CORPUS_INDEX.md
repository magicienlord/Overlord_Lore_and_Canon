# Franchise Source Corpus Index

Status: PRIMARY-SOURCE EXTRACTION

Generated: 2026-09-11

This corpus is derived directly from the user-supplied Overlord game localization and map files. It is franchise evidence, not automatically OVERLORD REIGN canon.

## Overlord I

Current localization extraction totals:

- extracted English text rows: 2,588
- localization workbook rows explicitly naming actor `GNARL`: 759

### Map-routing correction

`ShowMinionMasterText(...)` is not a speaker-identity function.

After stripping commented Lua, the maps contain 451 live call occurrences representing 365 unique references. Of those, 359 resolve to decoded localization rows. Only 288 of those resolved rows have workbook actor `GNARL`; 71 have explicit non-Gnarl actors such as Brown Minions, the Minion Jester, Melvin, Elf ghosts, Rose, Sir William, the Wizard, Jewel, Oberon, and Kahn.

Accordingly, map calls through `ShowMinionMasterText(...)` are retained as routing/presentation evidence only. They are not added to the Gnarl corpus unless independent actor evidence identifies Gnarl.

Six live references have no decoded localization row. They are individually resolved/documented in `corpus/overlord1/MINIONMASTER_ROUTING_RECONCILIATION.md`. Five previously reported unresolved references were only commented-out code and are excluded from live counts.

The normalized dialogue schema preserves scene ID, text ID, actor, English text, trigger/context, timing, mode, and developer notes where present.

## Raising Hell

Current extraction totals:

- extracted English text rows: 483
- localization workbook rows explicitly naming actor `GNARL`: 152

Expansion maps retain base-campaign state, so expansion-specific map attribution must distinguish `EXP_*` references from inherited hooks.

## Overlord II

Current extraction totals:

- extracted English narrative/interface text rows outside `Resources/System_Quests.8ld`: 8,587
- quest/objective text rows from `Resources/System_Quests.8ld`: 499
- unique internal quest IDs in `System_Quests.8ld`: 243

The narrative workbooks generally leave actor cells blank. Speaker identity is therefore reconstructed only where map implementation directly identifies a speaker role, actor entity, or character-specific source label.

The completed direct implementation pass currently attributes 173 unique decoded Overlord II lines to Gnarl. The method and evidence boundary are documented in `corpus/overlord2/SPEAKER_ATTRIBUTION_INDEX.md`.

`System_Quests.8ld` preserves internal quest IDs, text identifiers such as `DESC` and `DESC_DONE`, English quest strings, ordering, and developer notes.

## Source discipline

The extracted text is `PRIMARY-TEXT` from the supplied game data.

Actor values are preserved exactly when the source workbook supplies them.

Missing actor values remain missing unless direct implementation evidence identifies the speaker.

Internal quest IDs remain `PRIMARY-IMPLEMENTATION` terminology unless corroborated as player-facing terms.

Function names alone are not speaker identity. The Overlord I `ShowMinionMasterText(...)` correction is an explicit example of why implementation semantics must be validated against source actor data.

Large generated CSV tables are reproducible working artifacts and do not need to be treated as canon files. Curated lore and quest conclusions should cite their exact source file, scene/text ID, and evidence class.
