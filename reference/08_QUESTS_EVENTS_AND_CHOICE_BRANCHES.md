# OVERLORD Franchise Quest, Event, and Choice Reference

Status: PRIMARY-SOURCE SYNTHESIS

Date: 2026-09-11

Authority: franchise reference only. This file does not make OVERLORD REIGN canon decisions.

## Evidence base

This reference is derived from decoded localization workbooks and map-script evidence in the supplied Overlord I, Raising Hell, and Overlord II source material.

Evidence classes used here:

- `PRIMARY-TEXT`: decoded localization workbook content
- `PRIMARY-IMPLEMENTATION`: map scripts, quest IDs, state transitions, trigger conditions
- `ANALYTICAL-INFERENCE`: conclusions about how the games structure quests, explicitly distinguished from source facts

## Overlord I quest architecture

### PRIMARY-IMPLEMENTATION

A comment-aware source-level pass across the 30 supplied non-multiplayer base-game maps finds:

- 668 live recognized quest-state API occurrences
- 86 unique live internal quest IDs
- explicit enabled, completed, silent-completed, Evil-completed, enabled-state, completed-state, Evil-completed-state, and counter operations
- no live `SetQuestDisabled` calls in the reviewed source strings
- localization references tied to scripted events

The earlier 692-call / 87-ID count included commented implementation material and one commented typo ID, `D3_KHAN`. The live quest is `D3_KAHN`.

Representative internal IDs include domain objectives, Tower progression, Minion progression, resource recovery, and choice-state objectives. These identifiers are implementation terminology unless separately corroborated as player-facing names.

The direct state ledger is maintained in `corpus/overlord1/QUEST_STATE_LEDGER.md`.

### Speaker-routing correction

`ShowMinionMasterText(...)` must not be treated as a Gnarl-speaker function. Decoded localization actor fields prove that the maps route dialogue from many speakers through it.

For quest reconstruction the calls remain useful as event/localization routing. For speaker identity they require independent actor evidence.

The reconciliation is documented in `corpus/overlord1/MINIONMASTER_ROUTING_RECONCILIATION.md`.

### PRIMARY-TEXT

The localization workbooks preserve dialogue and production metadata associated with the events. `Tower_Titles.8ld` also demonstrates an explicit consequence-feedback layer: the Minion Jester has alternate titles associated with particular player choices and outcomes.

The title material is not itself a conventional quest log. It is persistent/reactive characterization of what the Overlord has done.

### Source-proven dependency model

The complete source survey deliberately distinguishes direct quest dependencies from world events, cutscene flags, area entry, object recovery, and other meta-state prerequisites.

Confirmed direct or state-synchronized relationships include:

- `D1_WORKSHOP` -> `D1_FORGE`
- `D1_GETROSE` -> activation of `D3_PLAGUE` when that state is not already active/completed
- `D5_SPEAKJEWEL` -> `TOWER_WIZARD1`, with the same Tower sequence also ensuring `D1_KAHN` is active
- Wizard cutscene meta-state -> `TOWER_WIZARD2`, `TOWER_SPELLS`, `TOWER_MINIONS`
- `D3_WILLIAM` as the explicit prerequisite for Brewery opening/progression
- `D4_QUARRY` as the explicit prerequisite for Royal Halls / `D4_GOLDO` progression
- `D4_MINE` and `D4S1_MINECARTS` use a main/subquest synchronization/handoff pattern rather than a simple one-way dependency
- the Grove scripts branch between `D2_GROVE` Evil completion and `D2_GROVE_BETRAYER` Evil completion depending on prior Grove state

Other local sequences, such as the Blue Cave objectives, are event-ordered but are not promoted to formal prerequisite edges unless the script explicitly states that relationship.

The auditable graph is maintained in `corpus/overlord1/QUEST_DEPENDENCY_AND_BRANCH_LEDGER.md`.

### Evil/corruption state

Thirteen live internal quest IDs are written through `SetQuestCompletedEvil`:

```text
BAR_FIGHT
D1_FOOD
D1_TRAITORS_FATE
D2_GROVE
D2_GROVE_BETRAYER
D3S5_MISTRESSES
D4_FEMALE_ELVES
D5_RETRIEVESTATUE
HARRASS_PEASANTS
SLUG_FEEDER
SUPRESS_SPREE
TRASH_HOMES
TRASH_TOWNS
```

The previously listed `D4_FREE_ELVES` Evil write occurs only in commented code and is excluded from live state behavior.

### ANALYTICAL-INFERENCE

Overlord I distributes quest communication across several systems rather than concentrating it in one UI surface:

1. map-script state controls what is active and complete;
2. dialogue supplies objective framing, reminders, warnings, and interpretation;
3. world changes provide physical consequence;
4. Tower dialogue and titles react to accumulated accomplishments and choices.

This is important for OVERLORD REIGN because reproducing only objective text would reproduce part of the state machine but not the narrative delivery style.

## Raising Hell

### PRIMARY-IMPLEMENTATION

The expansion maps preserve large amounts of inherited base-campaign state while adding `EXP_*` localization and event namespaces.

Expansion reconstruction therefore distinguishes newly authored Abyss material from inherited base-game hooks. A base quest reference inside a Raising Hell map is not automatically new expansion content.

### PRIMARY-TEXT

Eight supplied `EXP_*` language workbooks decode successfully. They preserve 483 English text rows, including 152 rows explicitly naming `GNARL` as actor.

### ANALYTICAL-INFERENCE

Raising Hell is particularly useful for learning how the original writers resume a completed campaign. It acknowledges an established Overlord, recontextualizes known places and characters, and introduces a new threat without resetting player identity.

## Overlord II quest architecture

### PRIMARY-TEXT

`Resources/System_Quests.8ld` contains 499 quest/objective text rows across 243 unique internal quest IDs.

Observed text-ID distribution:

- `DESC`: 241
- `DESC_DONE`: 216
- `DESC_DONE_DES`: 11
- `DESC_DONE_DOM`: 11
- `DESC_DONE_EVIL`: 2
- other specialized entries: 18

216 internal quest IDs contain both a normal description and a normal completion entry.

Thirteen quest IDs contain branch-specific completion forms. Eleven have paired Domination and Destruction completion text, while two use an `EVIL`-specific completion form.

All thirteen have been mapped to their narrative contexts in `corpus/overlord2/BRANCH_OUTCOME_LEDGER.md`.

### PRIMARY-IMPLEMENTATION

Overlord II does not use the same simple quest-state API vocabulary as Overlord I. Its narrative and speaker systems are being reconstructed from its own structures rather than by forcing the first game's scripting assumptions onto it.

Direct speaker-routing structures have been extracted from cutscene face-routing, explicit `Speak` records, and named character implementation labels. See `corpus/overlord2/SPEAKER_ATTRIBUTION_INDEX.md`.

### ANALYTICAL-INFERENCE

Overlord II formalizes the quest-log layer more strongly than Overlord I while preserving in-world narrative framing. Its source data shows that the quest system itself is branch-aware: one objective can record materially different completion text depending on how the Overlord resolved it.

For OVERLORD REIGN, this is direct structural precedent for authored outcome state rather than a single numeric reputation score.

## Quest-writing implications for OVERLORD REIGN

Status: PROPOSAL / DESIGN INFERENCE, not automatically canon.

A source-faithful REIGN quest should normally have four distinct layers:

1. **State layer**: prerequisites, objectives, branches, completion markers, and persistent consequences.
2. **Gnarl layer**: why the Overlord should care, opportunity/threat framing, reminders, warnings, and reaction.
3. **World layer**: hostility, services, settlement condition, structures, encounters, tribute, or other persistent changes.
4. **Record layer**: concise quest-log wording recording what is required and, where relevant, how it was resolved.

The source games support branch-specific completion records. A REIGN quest can therefore preserve the same objective while recording destruction, domination, subjugation, mercy-for-usefulness, or another authored civilization-specific outcome without requiring hidden reputation.

## Source-task status

Completed for the current quest-authoring baseline:

- Overlord I live quest-state inventory and comment-aware counts
- high-confidence Overlord I direct dependency / branch graph
- Overlord I `ShowMinionMasterText` reconciliation and speaker-attribution correction
- all thirteen Overlord II branch-specific completion contexts
- high-confidence Overlord II named-speaker reconstruction where direct map implementation evidence exists
- franchise-to-REIGN adoption ledger

Remaining gaps are source limitations or optional deeper reconstruction rather than blockers for REIGN lore/quest work. They remain documented instead of being filled by inference.
