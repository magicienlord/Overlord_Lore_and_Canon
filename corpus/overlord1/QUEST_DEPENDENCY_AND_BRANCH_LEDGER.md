# Overlord I Quest Dependency and Branch Ledger

Status: PRIMARY-IMPLEMENTATION EXTRACTION, HIGH-CONFIDENCE EDGES

Date: 2026-09-11

This file records only relationships directly supported by the surrounding Lua/script condition in the supplied Overlord I `.omp` maps. It deliberately does not convert byte proximity into a quest graph.

## 1. Direct progression edges

### `D1_WORKSHOP` -> `D1_FORGE`

Source: `HalflingMain.omp`, workshop event.

The script checks whether `D1_WORKSHOP` is incomplete, silently completes it, and enables `D1_FORGE` in the same conditional block.

Evidence: `PRIMARY-IMPLEMENTATION`, direct state transition.

### `D5_SPEAKJEWEL` -> `TOWER_WIZARD1`

Source: `Tower.omp`, Jewel cutscene end.

When the active `D5_SPEAKJEWEL` state is resolved, the script silently completes it and enables `TOWER_WIZARD1` in the same block.

Evidence: `PRIMARY-IMPLEMENTATION`, direct state transition.

### Wizard cutscene -> `TOWER_WIZARD2`, `TOWER_SPELLS`, `TOWER_MINIONS`

Source: `Tower.omp`, Tower simulation/fix logic.

When `Tower_CS_Wizard_Played` is true and `TOWER_SPELLS` is not already active/completed, the script enables all three quest states:

```text
TOWER_WIZARD2
TOWER_SPELLS
TOWER_MINIONS
```

This is an event-state fan-out rather than a quest-ID-to-quest-ID edge, so the prerequisite is recorded as the Wizard cutscene meta-state.

### `D3_WILLIAM` -> Brewery access/progression

Source: `DwarfMain.omp`.

The Dwarf-domain script explicitly comments that the Paladin domain must be conquered before the Brewery unlock condition is satisfied.

Observed logic includes:

- if `D3_WILLIAM` is incomplete and the Brewery-opening quest is neither active nor completed, a cutscene gives the opening requirement;
- when `D4_OPEN_BREWERY` is active and `D3_WILLIAM` is completed, a timer advances the Brewery unlock sequence;
- when `D3_WILLIAM` is completed and `D4_BREWERY` is not already active/completed, the Brewery quest-introduction dialogue is permitted;
- `D4_BREWERY` is then enabled through the Brewery opening sequence.

Evidence: `PRIMARY-IMPLEMENTATION`, explicit prerequisite relation.

### `D4_QUARRY` -> Royal Halls access / `D4_GOLDO`

Source: `DwarfMain.omp`.

The script explicitly comments that the Quarry sub-domain must be finished before Royal Halls unlock progression.

Observed logic includes:

- if `D4_QUARRY` is incomplete and `D4_OPEN_ROYALHALLS` is neither active nor completed, the Royal Halls opening requirement is introduced;
- when `D4_OPEN_ROYALHALLS` is active and `D4_QUARRY` is completed, the Royal Halls unlock timer advances;
- when `D4_QUARRY` is completed and `D4_GOLDO` is not already active/completed, the Royal quest cutscene is started.

Evidence: `PRIMARY-IMPLEMENTATION`, explicit prerequisite relation.

## 2. Local quest chains that are event-ordered but not yet promoted to hard dependency edges

### Blue Cave sequence

Source: `BlueCave.omp`.

The same map contains separately named event handlers for:

```text
D3S1_SAVEBLUES
D3S1_SERPENT
D3S1_GEYSER
D3S1_BLUEHIVE
```

Each has explicit start/progress/completion logic, and their event handlers occur in a coherent local sequence. However, the extracted start handlers do not themselves state a cross-quest prerequisite such as `if Completed(A) then Enable(B)`.

Status: `PRIMARY-IMPLEMENTATION ORDER`, not yet a hard graph edge.

This distinction prevents source order from being misrepresented as a formal prerequisite.

## 3. Explicit Evil/corruption quest states

The base-map implementation writes or reads `CompletedEvil` for 14 internal quest IDs:

```text
BAR_FIGHT
D1_FOOD
D1_TRAITORS_FATE
D2_GROVE
D2_GROVE_BETRAYER
D3S5_MISTRESSES
D4_FEMALE_ELVES
D4_FREE_ELVES
D5_RETRIEVESTATUE
HARRASS_PEASANTS
SLUG_FEEDER
SUPRESS_SPREE
TRASH_HOMES
TRASH_TOWNS
```

All 14 are directly written through `SetQuestCompletedEvil` somewhere in the supplied implementation.

This is important structural evidence: Overlord I already carries authored choice/conduct state separately from ordinary quest completion.

## 4. Confirmed branch relationships

### Grove state

Source: `ElfMain.omp` and Tower follow-up logic.

The implementation jointly reads:

```text
D2_GROVE completed
D2_GROVE completed evil
D2_GROVE_BETRAYER completed evil
```

Different combinations are explicitly distinguished by scripts. The Grove outcome is therefore not a simple binary complete/incomplete state.

### Traitors' Fate

Source: `Tower.omp`.

The script explicitly labels a `Corruption Choice Warrior - Good Variant`. If `D1_TRAITORS_FATE` has not already been completed Evil, it writes ordinary completion and logs the spared-traitors outcome.

The same quest ID can therefore preserve the distinction between normal/redemptive and Evil resolution.

### Female Elves

Source: `RoyalHalls.omp`.

`D4_FEMALE_ELVES` supports both ordinary completion and `SetQuestCompletedEvil`.

This is direct implementation evidence for branch-sensitive treatment of the captured/female Elf objective.

### Food

Source: `HalflingMain.omp`, `HalflingHomes2of2.omp`, and Tower follow-up.

`D1_FOOD` is heavily queried both as normal completion and Evil completion and can be written Evil. This matches the campaign's authored choice around what is done with the recovered food rather than treating food recovery as one invariant outcome.

## 5. Threshold and consequence states

Tower scripts also query cumulative behavior states such as:

```text
PEASANT_KILLS_1
PEASANT_KILLS_20
PEASANT_KILLS_100
PEASANT_KILLS_500
```

These are used for reactive title/consequence logic. They demonstrate persistent recognition of accumulated conduct but are not ordinary linear quests.

Do not model them as four mandatory story objectives.

## 6. Design implications for OVERLORD REIGN

Status: ANALYTICAL-INFERENCE / DESIGN INPUT.

The original implementation already separates at least four concepts that a REIGN quest runtime should also keep distinct:

```text
quest active/completed state
hard prerequisite/world-state condition
branch or Evil-resolution state
cumulative behavior/consequence state
```

This supports the current REIGN decision to use authored quest markers and civilization states rather than a single hidden reputation value.

A faithful generalized runtime should permit a quest to be complete while still retaining how it was completed.

## 7. Remaining graph work

- reconstruct additional cross-domain dependencies from explicit Lua conditions;
- correlate each internal quest ID with displayed objective/dialogue text;
- distinguish cutscene/meta-state prerequisites from ordinary quest prerequisites;
- retain comments and source map/offset for each final graph edge so later quest-mod implementation can be audited.
