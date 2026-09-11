# Overlord I Quest State Ledger

Status: PRIMARY-IMPLEMENTATION EXTRACTION, COMMENT-AWARE LIVE SOURCE

Date: 2026-09-11

Source: 30 supplied non-multiplayer Overlord I `.omp` maps.

This ledger records every internal quest ID touched by the recognized live quest-state API after Lua comments are removed. Internal IDs are implementation terminology, not automatically player-facing quest names.

## Summary

- live recognized quest-state API occurrences: 668
- unique live internal quest IDs: 86
- maps scanned: 30

Recognized live operations:

```text
GetQuestCompleted: 266
GetQuestEnabled: 133
SetQuestEnabled: 90
SetQuestCompleted: 73
GetQuestCompletedEvil: 45
SetQuestCompletedEvil: 34
GetQuestCounter: 18
SetQuestCompletedSilent: 9
```

No live `SetQuestDisabled` call was found in the reviewed source strings.

The previous 692-call / 87-ID ledger included commented implementation code and the commented typo `D3_KHAN`. The live quest ID is `D3_KAHN`. The previous Evil-state list also included `D4_FREE_ELVES` from commented code; it is not a live `SetQuestCompletedEvil` target.

## Ledger

| Quest ID | Maps | Enable | Complete | Silent | Evil | Query enabled | Query complete | Query evil | Counter |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `BAR_FIGHT` | Red Light Inn, Tower | 0 | 0 | 0 | 2 | 0 | 1 | 2 | 0 |
| `D1S2_WHEELSPOKES` | HalflingHomes1of2 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| `D1S4_ENDRAID` | SpreeDungeon | 2 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1S4_LUGGAGE` | SpreeDungeon | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| `D1_CHECKCASTLE` | HalflingMain, SpreeDungeon | 1 | 1 | 0 | 0 | 3 | 2 | 0 | 0 |
| `D1_CHECKVILLAGE` | HalflingMain, SlaveCamp | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_CRANE` | SlaveCamp, Tower | 1 | 1 | 0 | 0 | 3 | 8 | 0 | 0 |
| `D1_FINDEVERNIGHT` | ElfMain, HalflingMain | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_FINDHEAVENSPEAK` | PaladinMain, Tower | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| `D1_FINDREDS` | HalflingMain, HellsKitchen | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_FOOD` | HalflingHomes2of2, HalflingMain, Tower | 1 | 1 | 0 | 2 | 6 | 11 | 9 | 0 |
| `D1_FORGE` | HalflingMain | 2 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| `D1_GETROSE` | Tower | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D1_KAHN` | HalflingMain, Tower | 1 | 1 | 0 | 0 | 5 | 8 | 0 | 0 |
| `D1_LADY` | HalflingMain, SpreeDungeon | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_MELVIN` | HalflingMain, HellsKitchen, Tower | 2 | 1 | 0 | 0 | 0 | 3 | 0 | 0 |
| `D1_PARTYMELVIN` | HalflingMain | 1 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| `D1_PILLAR` | HalflingMain | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D1_REDMINIONS` | HellsKitchen, Tower | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D1_SERVANTS` | HalflingMain, Tower | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_SLAVECAMP` | HalflingMain, SlaveCamp | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_TRAITORS_FATE` | HalflingMain, Tower | 1 | 2 | 0 | 1 | 1 | 1 | 4 | 0 |
| `D1_WORKSHOP` | HalflingMain | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| `D1_WORLDSTONE` | HalflingMain, Tower | 2 | 1 | 0 | 0 | 4 | 5 | 0 | 0 |
| `D2S1_GREENHIVE` | GreenCave, Tower | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2S3_KEYS` | TrollTemple | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| `D2_FINDGOLDENHALLS` | DwarfMain, ElfMain | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D2_GREENLAIR` | ElfMain, GreenCave | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2_GROVE` | ElfMain, Tower | 1 | 2 | 0 | 1 | 3 | 9 | 3 | 0 |
| `D2_GROVE_BETRAYER` | ElfMain | 1 | 1 | 0 | 1 | 1 | 1 | 2 | 0 |
| `D2_KILLUNICORNS` | ElfMain | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2_MOTHERGODDESS` | Tower, TrollTemple | 1 | 1 | 0 | 0 | 0 | 4 | 0 | 0 |
| `D2_OBERON` | ElfMain, Tower | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D2_TROLLTEMPLE` | ElfMain, TrollTemple | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3S1_BLUEHIVE` | BlueCave, Tower | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D3S1_GEYSER` | BlueCave | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S1_SAVEBLUES` | BlueCave | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S1_SERPENT` | BlueCave | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S4_SLAYSUCCUBI` | Red Light Inn | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_BLUECAVE` | BlueCave, PaladinMain | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D3_HEAVENSPEAK` | PaladinMain, Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_INN` | PaladinMain, Red Light Inn | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_PLAGUE` | PaladinMain, Tower | 1 | 1 | 0 | 0 | 1 | 3 | 0 | 0 |
| `D3_SEWERS` | PaladinMain, Sewers2of2 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3_SIRWILLIAM` | Citadel, PaladinMain, Tower | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 |
| `D3_SUCCUBUS` | PaladinMain, Red Light Inn | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3_WILLIAM` | Citadel, PaladinMain | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D3S5_MISTRESSES` | Tower | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| `D4S1_MINECARTS` | GoldMine | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D4_ARCANIUM` | ArcaniumMine, DwarfMain | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D4_BREWERY` | DwarfMain, HomeyHalls1of2 | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D4_FEMALE_ELVES` | RoyalHalls | 1 | 1 | 0 | 1 | 1 | 2 | 2 | 0 |
| `D4_FREE_ELVES` | RoyalHalls, Tower | 0 | 0 | 0 | 0 | 4 | 3 | 0 | 0 |
| `D4_GOLDO` | DwarfMain, RoyalHalls | 1 | 1 | 0 | 0 | 1 | 4 | 0 | 0 |
| `D4_MINE` | DwarfMain, GoldMine | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| `D4_OPEN_BREWERY` | DwarfMain | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D4_OPEN_ROYALHALLS` | DwarfMain | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D4_QUARRY` | DwarfMain, Quarry | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D5_CAPTUREJEWEL1` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 2 | 4 | 0 | 0 |
| `D5_CAPTUREJEWEL2` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 2 | 3 | 0 | 0 |
| `D5_FINDJEWEL` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 1 | 4 | 0 | 0 |
| `D5_KAHN` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D5_RETRIEVESTATUE` | Tower | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| `D5_SPEAKJEWEL` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `DUNGEON_BEETLE` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_DWARF` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_ELF` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_HALFLING` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_KAHN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_PALADIN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_TROLL` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_UNICORN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `HARRASS_PEASANTS` | HalflingMain, Tower | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 |
| `PEASANT_KILLS_1` | Tower | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `PEASANT_KILLS_20` | Tower | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `PEASANT_KILLS_100` | Tower | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `PEASANT_KILLS_500` | Tower | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `SLUG_FEEDER` | HalflingMain | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| `SUPRESS_SPREE` | HalflingMain, Tower | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| `TOWER_BLUEHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_CRANE` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TOWER_DUNGEON` | Tower, Tower_Dungeon | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TOWER_FORGE` | Tower | 1 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_GREENHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_HEART` | Tower | 1 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_MINIONS` | Tower | 1 | 1 | 0 | 0 | 2 | 3 | 0 | 0 |
| `TOWER_REDHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_SPELLS` | Tower | 1 | 1 | 0 | 0 | 3 | 4 | 0 | 0 |
| `TOWER_WIZARD1` | Tower | 1 | 1 | 0 | 0 | 2 | 3 | 0 | 0 |
| `TOWER_WIZARD2` | Tower | 1 | 1 | 0 | 0 | 1 | 4 | 0 | 0 |
| `TOWER_WORLDSTONE` | Tower | 1 | 1 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_YELLOWHIVE` | Tower, Tower_Spawnpit | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TRASH_HOMES` | HalflingHomes2of2, Tower | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 |
| `TRASH_TOWNS` | HalflingMain, Tower | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 |
| `WORLD_BROWNMINIONS` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_GATE` | Tower | 1 | 1 | 0 | 0 | 1 | 2 | 0 | 0 |
| `WORLD_SPELLS` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_TOWERHEART` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_TOWEROBJECTS` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_WORLDSTONE` | Tower | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |

## Evil-resolution writers

The following 13 live quest IDs are written through `SetQuestCompletedEvil`:

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

This demonstrates that branch/conduct state is stored separately from ordinary completion.

## Interpretation rule

Counts alone do not define dependency. A quest may be enabled by area entry, object recovery, cutscene state, boss state, a timer, or another quest. Cross-quest relationships are promoted only when the surrounding live Lua condition directly supports them.

See `QUEST_DEPENDENCY_AND_BRANCH_LEDGER.md` for those source-proven relationships.
