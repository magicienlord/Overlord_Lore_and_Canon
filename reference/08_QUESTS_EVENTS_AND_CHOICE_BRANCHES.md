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

The 30 supplied non-multiplayer base-game maps expose:

- 590 recognized quest-state function calls
- 87 unique internal quest IDs
- explicit enable, complete, silent-complete, disable, enabled-state, and completed-state operations
- localization sequence references tied to scripted events
- direct Minion Master dialogue calls for Gnarl

Representative internal IDs include domain objectives, Tower progression, Minion progression, resource recovery, and choice-state objectives. These identifiers are implementation terminology unless separately corroborated as player-facing names.

### PRIMARY-TEXT

The localization workbooks preserve the dialogue and production metadata associated with those events. `Tower_Titles.8ld` also demonstrates an explicit consequence-feedback layer: the Minion Jester has alternate titles associated with particular player choices and outcomes.

The title material is not itself a conventional quest log. It is persistent/reactive characterization of what the Overlord has done.

### ANALYTICAL-INFERENCE

Overlord I distributes quest communication across several systems rather than concentrating it in one UI surface:

1. map-script state controls what is active and complete;
2. Gnarl provides objective framing, reminders, warnings, and interpretation;
3. world changes provide physical consequence;
4. Tower dialogue and titles react to accumulated accomplishments and choices.

This is important for OVERLORD REIGN quest design because reproducing only objective text would reproduce the state machine but not the narrative delivery style.

## Raising Hell

### PRIMARY-IMPLEMENTATION

The expansion maps preserve large amounts of inherited base-campaign state while adding `EXP_*` localization and event namespaces.

Expansion reconstruction therefore must distinguish newly authored Abyss material from inherited base-game hooks. The presence of a base quest reference inside a Raising Hell map does not make that quest new expansion content.

### PRIMARY-TEXT

Eight supplied `EXP_*` language workbooks decode successfully. They preserve 483 English text rows, including 152 rows explicitly naming `GNARL` as actor.

### ANALYTICAL-INFERENCE

Raising Hell is particularly useful for learning how the original writers resume a completed campaign. It has to acknowledge an already-established Overlord, recontextualize known places and characters, and introduce a new threat without resetting the player's identity. That makes it a useful structural reference for REIGN even though REIGN is not narratively Raising Hell.

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

Thirteen quest IDs contain a branch-specific completion form. Eleven have paired Domination and Destruction completion text, while two use an `EVIL`-specific completion form.

### PRIMARY-IMPLEMENTATION

The supplied Overlord II maps do not use the same simple quest-state function vocabulary as Overlord I. An Overlord I-style parser therefore substantially undercounts their state logic. Overlord II quest reconstruction must use its own event/state model rather than forcing the first game's scripting assumptions onto it.

### ANALYTICAL-INFERENCE

Overlord II formalizes the quest-log layer more strongly than Overlord I while still preserving in-world narrative framing. Its source data shows that the quest system itself is branch-aware: a quest may have one objective description but different recorded completion text depending on the form of tyranny used to resolve it.

For OVERLORD REIGN, this is direct structural precedent for storing an authored outcome state rather than reducing a civilization or quest to a single numeric reputation value.

## Quest-writing implications for OVERLORD REIGN

Status: PROPOSAL / DESIGN INFERENCE, not automatically canon.

A source-faithful REIGN quest should normally have four distinct layers:

1. **State layer**: exact prerequisites, objectives, branches, completion markers, and persistent consequences.
2. **Gnarl layer**: why the Overlord should care, what contempt or opportunity Gnarl sees, reminders, warnings, and reaction to success or failure.
3. **World layer**: NPC hostility, services, settlement condition, structures, encounters, tribute, or other persistent changes that make the outcome visible.
4. **Record layer**: concise quest-log wording that records what is required and, where relevant, what kind of resolution occurred.

The source games support branch-specific completion records. Therefore a REIGN sidequest or main quest can preserve the same objective while recording materially different resolutions such as destruction, domination, subjugation, mercy-for-usefulness, or another authored civilization-specific outcome.

This does not require a hidden reputation score.

## Open source tasks

- reconstruct the Overlord I 87-ID quest graph with exact enable/completion dependencies;
- map the thirteen Overlord II branch-specific completion quest IDs to their narrative contexts;
- build an Overlord II state/event extractor;
- reconcile the eleven unresolved Overlord I direct Minion Master references;
- connect quest outcomes to the later franchise/adoption ledger rather than importing them automatically into REIGN canon.
