# Overlord I Quest Dependency and Branch Ledger

Status: PRIMARY-IMPLEMENTATION EXTRACTION, COMPLETE HIGH-CONFIDENCE CROSS-QUEST PASS

Date: 2026-09-11

This file records relationships directly supported by live Lua/script conditions in the supplied Overlord I `.omp` maps. Commented code, debug/cheat handlers, and byte proximity are excluded from progression claims.

The purpose is not to force every quest into a linear graph. Many original quests are activated by area entry, object recovery, boss state, world flags, cutscenes, or timers rather than another quest ID.

## 1. Direct quest/state transitions

### `D1_WORKSHOP` -> `D1_FORGE`

Source: `HalflingMain.omp`.

The live workshop event checks whether `D1_WORKSHOP` is incomplete, silently completes it, and enables `D1_FORGE` in the same conditional block.

Evidence: `PRIMARY-IMPLEMENTATION`, direct transition.

### `D1_GETROSE` -> `D3_PLAGUE`

Source: `Tower.omp`, Rose entry/cutscene logic.

The Tower sequence completes `D1_GETROSE` and, when `D3_PLAGUE` is neither already active nor completed, enables `D3_PLAGUE`.

Evidence: `PRIMARY-IMPLEMENTATION`, direct transition with guard condition.

### `D5_SPEAKJEWEL` -> `TOWER_WIZARD1`

Source: `Tower.omp`, Jewel cutscene end.

When active `D5_SPEAKJEWEL` is resolved, the script silently completes it and enables `TOWER_WIZARD1`.

The same Tower event also ensures `D1_KAHN` is active when it has not already been enabled/completed. `D1_KAHN` is therefore part of the same event fan-out rather than evidence that `TOWER_WIZARD1` itself causes Kahn progression.

Evidence: `PRIMARY-IMPLEMENTATION`.

### Wizard cutscene meta-state -> `TOWER_WIZARD2`, `TOWER_SPELLS`, `TOWER_MINIONS`

Source: `Tower.omp`.

When the Wizard cutscene has played, the end/fix logic ensures all three states are enabled when not already active/completed:

```text
TOWER_WIZARD2
TOWER_SPELLS
TOWER_MINIONS
```

This is a cutscene/world-state fan-out, not a quest-ID-to-quest-ID dependency.

## 2. Dwarf-domain prerequisite chains

### `D3_WILLIAM` gates Brewery progression

Source: `DwarfMain.omp`.

The implementation explicitly treats conquest/completion of the Paladin domain as the prerequisite for Brewery access.

Observed live logic:

- when `D3_WILLIAM` is incomplete and `D4_OPEN_BREWERY` is neither active nor completed, the Brewery-opening requirement is introduced;
- when `D4_OPEN_BREWERY` is active and `D3_WILLIAM` becomes completed, the timed Brewery unlock sequence can advance;
- when `D3_WILLIAM` is complete and `D4_BREWERY` is not active/completed, the Brewery quest-introduction path is permitted;
- the opening sequence then enables `D4_BREWERY`.

Evidence: `PRIMARY-IMPLEMENTATION`, explicit prerequisite relation mediated by an opening/meta quest.

### `D4_QUARRY` gates Royal Halls / `D4_GOLDO`

Source: `DwarfMain.omp`.

The implementation explicitly treats completion of the Quarry sub-domain as the prerequisite for Royal Halls progression.

Observed live logic:

- when `D4_QUARRY` is incomplete and `D4_OPEN_ROYALHALLS` is neither active nor completed, the Royal Halls opening requirement is introduced;
- when `D4_OPEN_ROYALHALLS` is active and `D4_QUARRY` becomes completed, the unlock timer can advance;
- when `D4_QUARRY` is complete and `D4_GOLDO` is not active/completed, the Royal quest cutscene may start.

Evidence: `PRIMARY-IMPLEMENTATION`, explicit prerequisite relation.

### `D4_MINE` <-> `D4S1_MINECARTS` synchronization/handoff

Source: `GoldMine.omp`.

On Gold Mine quest initialization, if `D4S1_MINECARTS` is neither active nor completed, the script silently completes `D4_MINE` and enables `D4S1_MINECARTS`.

A separate conquest/check handler tests `D4S1_MINECARTS` completion and can complete `D4_MINE` when the main state remains active.

The source therefore contains compatibility/synchronization behavior between the main-domain and sub-domain states. It should not be simplified into an ordinary one-way prerequisite edge.

Evidence: `PRIMARY-IMPLEMENTATION`, state synchronization.

## 3. Grove branch graph

Source: `ElfMain.omp` and Tower follow-up logic.

The live Grove scripts explicitly distinguish ordinary completion and Evil completion.

A critical branch handler performs the following logic:

```text
if D2_GROVE is not completed:
    complete D2_GROVE as Evil
else:
    complete D2_GROVE_BETRAYER as Evil
```

Other scripts jointly query:

```text
D2_GROVE completed
D2_GROVE completed Evil
D2_GROVE_BETRAYER completed Evil
```

Therefore the Grove outcome is a multi-state branch, not a binary complete/incomplete objective.

Evidence: `PRIMARY-IMPLEMENTATION`.

## 4. Other confirmed branch-sensitive quest states

A comment-aware live-source pass identifies 13 quest IDs written through `SetQuestCompletedEvil`:

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

The former list of fourteen incorrectly included `D4_FREE_ELVES`; its Evil write exists only in commented code.

### `D1_TRAITORS_FATE`

Source: `Tower.omp`.

The script explicitly contains a corruption-choice good variant. If the state has not already been completed Evil, ordinary completion records the spared/non-Evil resolution.

### `D1_FOOD`

Sources: `HalflingMain.omp`, `HalflingHomes2of2.omp`, Tower follow-up.

The food state is queried and written both as normal and Evil completion, preserving what was done with the recovered food rather than merely whether it was recovered.

### `D4_FEMALE_ELVES`

Source: `RoyalHalls.omp`.

The live objective supports both ordinary completion and Evil completion.

### Mistress and conduct states

`D3S5_MISTRESSES`, `HARRASS_PEASANTS`, `SLUG_FEEDER`, `SUPRESS_SPREE`, `TRASH_HOMES`, and `TRASH_TOWNS` demonstrate that the same quest-state API also records long-term conduct and choice consequences, not only conventional mission completion.

## 5. Threshold/consequence states

Tower scripts query persistent behavior thresholds such as:

```text
PEASANT_KILLS_1
PEASANT_KILLS_20
PEASANT_KILLS_100
PEASANT_KILLS_500
```

These feed reactive title/consequence logic. They are persistent conduct markers, not four mandatory story objectives.

## 6. Event-ordered local sequences that are NOT promoted to hard edges

### Blue Cave sequence

Source: `BlueCave.omp`.

The map contains named event handlers for:

```text
D3S1_SAVEBLUES
D3S1_SERPENT
D3S1_GEYSER
D3S1_BLUEHIVE
```

The sequence is coherent in the local implementation, but the reviewed live start conditions do not express every step as `Completed(A) -> Enable(B)`. It remains `PRIMARY-IMPLEMENTATION ORDER`, not an invented hard dependency chain.

The same rule applies elsewhere: event order, byte order, or narrative plausibility alone is insufficient to create a dependency edge.

## 7. Debug and commented code exclusion

Cheat/debug handlers such as Dwarf-domain conquer helpers can explicitly set quest states. They are useful for understanding intended state combinations but are not normal gameplay progression and are excluded from the canonical quest graph.

Likewise, commented Lua is not counted as live behavior. This removes the typo `D3_KHAN` and the commented `D4_FREE_ELVES` Evil write from the live graph.

## 8. Graph completion boundary

The live source survey has been completed for direct cross-quest references in the supplied 30 non-multiplayer maps.

The resulting model deliberately contains fewer hard edges than a conventional RPG dependency graph because much of Overlord I progression is world/event-driven.

For the current quest-authoring baseline, the graph is considered complete at the following evidentiary boundary:

- direct quest-to-quest conditions: recorded;
- quest-to-opening/meta-state conditions: recorded;
- branch/Evil resolution state: recorded;
- cumulative conduct states: recorded separately;
- event/world/cutscene triggers: not converted into quest dependencies unless the source states the relationship;
- debug/cheat/commented code: excluded from normal progression.

## 9. Design implications for OVERLORD REIGN

Status: ANALYTICAL-INFERENCE / DESIGN INPUT.

The original implementation separates at least these concepts:

```text
quest active/completed state
world/event prerequisite
branch or Evil-resolution state
cumulative conduct/consequence state
```

A source-faithful REIGN runtime should likewise permit a quest to be complete while retaining how it was completed, and should not require every unlock to be represented as a quest-to-quest edge.
