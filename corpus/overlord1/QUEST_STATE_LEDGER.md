# Overlord I Quest State Ledger

Status: PRIMARY-IMPLEMENTATION EXTRACTION

Date: 2026-09-11

Source: 30 supplied non-multiplayer Overlord I `.omp` maps.

This ledger records every internal quest ID touched by the recognized quest-state API. Internal IDs are implementation terminology, not automatically player-facing quest names.

## Summary

- recognized quest-state calls: 692
- unique internal quest IDs: 87
- maps scanned: 30

Recognized operations: `SetQuestEnabled`, `SetQuestCompleted`, `SetQuestCompletedSilent`, `SetQuestCompletedEvil`, `SetQuestDisabled`, `GetQuestEnabled`, `GetQuestCompleted`, `GetQuestCompletedEvil`, and `GetQuestCounter`.

## Ledger

| Quest ID | Maps | Enable | Complete | Silent | Evil | Disable | Query enabled | Query complete | Query evil | Counter |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `BAR_FIGHT` | Red Light Inn, Tower | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 2 | 0 |
| `D1S2_WHEELSPOKES` | HalflingHomes1of2 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| `D1S4_ENDRAID` | SpreeDungeon | 2 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1S4_LUGGAGE` | SpreeDungeon | 1 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| `D1_CHECKCASTLE` | HalflingMain, SpreeDungeon | 1 | 1 | 0 | 0 | 0 | 3 | 2 | 0 | 0 |
| `D1_CHECKVILLAGE` | HalflingMain, SlaveCamp | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_CRANE` | SlaveCamp, Tower | 1 | 1 | 0 | 0 | 0 | 3 | 8 | 0 | 0 |
| `D1_FINDEVERNIGHT` | ElfMain, HalflingMain | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_FINDHEAVENSPEAK` | PaladinMain, Tower | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| `D1_FINDREDS` | HalflingMain, HellsKitchen | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_FOOD` | HalflingHomes2of2, HalflingMain, Tower | 1 | 1 | 0 | 2 | 0 | 6 | 11 | 9 | 0 |
| `D1_FORGE` | HalflingMain | 2 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `D1_GETROSE` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D1_KAHN` | HalflingMain, Tower | 1 | 1 | 0 | 0 | 0 | 5 | 8 | 0 | 0 |
| `D1_LADY` | HalflingMain, SpreeDungeon | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_MELVIN` | HalflingMain, HellsKitchen, Tower | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| `D1_PARTYMELVIN` | HalflingMain | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `D1_PILLAR` | HalflingMain | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D1_REDMINIONS` | HellsKitchen, Tower | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D1_SERVANTS` | HalflingMain, Tower | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D1_SLAVECAMP` | HalflingMain, SlaveCamp | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `D1_TRAITORS_FATE` | HalflingMain, Tower | 1 | 2 | 0 | 1 | 0 | 1 | 1 | 4 | 0 |
| `D1_WORKSHOP` | HalflingMain | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D1_WORLDSTONE` | HalflingMain, Tower | 2 | 1 | 0 | 0 | 0 | 4 | 5 | 0 | 0 |
| `D2S1_GREENHIVE` | GreenCave, Tower | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2S3_KEYS` | TrollTemple | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| `D2_FINDGOLDENHALLS` | DwarfMain, ElfMain | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D2_GREENLAIR` | ElfMain, GreenCave | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2_GROVE` | ElfMain, Tower | 1 | 2 | 0 | 1 | 0 | 3 | 9 | 3 | 0 |
| `D2_GROVE_BETRAYER` | ElfMain | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D2_KILLUNICORNS` | ElfMain | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D2_MOTHERGODDESS` | TrollTemple, Tower | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| `D2_OBERON` | ElfMain, Tower | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D2_TROLLTEMPLE` | ElfMain, TrollTemple | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3S1_BLUEHIVE` | BlueCave, Tower | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D3S1_GEYSER` | BlueCave | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S1_SAVEBLUES` | BlueCave | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S1_SERPENT` | BlueCave | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3S4_SLAYSUCCUBI` | Red Light Inn | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_BLUECAVE` | BlueCave, PaladinMain | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D3_HEAVENSPEAK` | PaladinMain, Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_INN` | PaladinMain, Red Light Inn | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D3_PLAGUE` | PaladinMain, Tower | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 0 | 0 |
| `D3_SEWERS` | PaladinMain, Sewers2of2 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3_SIRWILLIAM` | Citadel, PaladinMain, Tower | 1 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| `D3_SUCCUBUS` | PaladinMain, Red Light Inn | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D3_WILLIAM` | Citadel, PaladinMain | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| `D4S1_MINECARTS` | GoldMine | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D4_ARCANIUM` | ArcaniumMine, DwarfMain | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D4_BREWERY` | DwarfMain, HomeyHalls1of2 | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D4_FEMALE_ELVES` | RoyalHalls | 1 | 1 | 0 | 1 | 0 | 1 | 2 | 2 | 0 |
| `D4_GOLDO` | DwarfMain, RoyalHalls | 1 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 0 |
| `D4_MINE` | DwarfMain, GoldMine | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D4_OPEN_BREWERY` | DwarfMain | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `D4_QUARRY` | DwarfMain, Quarry | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `D5_CAPTUREJEWEL1` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 2 | 4 | 0 | 0 |
| `D5_CAPTUREJEWEL2` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 2 | 3 | 0 | 0 |
| `D5_FINDJEWEL` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 0 |
| `D5_KAHN` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `D5_SPEAKJEWEL` | Tower, WarriorMain | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `DUNGEON_BEETLE` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_DWARF` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_ELF` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_HALFLING` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_KAHN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_PALADIN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_TROLL` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `DUNGEON_UNICORN` | Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TOWER_BLUEHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_CRANE` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TOWER_DUNGEON` | Tower, Tower_Dungeon | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `TOWER_FORGE` | Tower | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_GREENHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_HEART` | Tower | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_MINIONS` | Tower | 1 | 1 | 0 | 0 | 0 | 2 | 3 | 0 | 0 |
| `TOWER_REDHIVE` | Tower, Tower_Spawnpit | 1 | 1 | 0 | 0 | 0 | 2 | 5 | 0 | 0 |
| `TOWER_SPELLS` | Tower | 1 | 1 | 0 | 0 | 0 | 3 | 4 | 0 | 0 |
| `TOWER_WIZARD1` | Tower | 1 | 1 | 0 | 0 | 0 | 2 | 3 | 0 | 0 |
| `TOWER_WIZARD2` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 4 | 0 | 0 |
| `TOWER_WORLDSTONE` | Tower | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| `TOWER_YELLOWHIVE` | Tower, Tower_Spawnpit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_BROWNMINIONS` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_GATE` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| `WORLD_SPELLS` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_TOWERHEART` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_TOWEROBJECTS` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| `WORLD_WORLDSTONE` | Tower | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

## Interpretation rules

- A quest ID appearing in a map proves only that the implementation reads or writes that state there.
- `SetQuestCompletedEvil` is direct implementation evidence for an authored evil/corruption branch, but the player-facing meaning must be taken from matching localization/context.
- Proximity between two quest-state calls is not by itself proof that one quest unlocks the other. Dependency edges are recorded only when the surrounding script condition supports the relationship.
- Map names are implementation source locations, not necessarily exact in-universe place names.

## High-confidence dependency examples

The raw scripts already expose several direct conditional chains. Examples:

- `D3S1_SAVEBLUES` is checked before completion in the Blue Cave sequence; the same area then handles `D3S1_SERPENT`, `D3S1_GEYSER`, and enables `D3S1_BLUEHIVE` when it is neither already enabled nor completed.
- `D4_QUARRY`, `D4_BREWERY`, and `D4_ARCANIUM` are conditionally enabled from Dwarf-domain map scripts when not already active/completed.
- `D4_OPEN_BREWERY` is completed when its active-state condition is satisfied in `DwarfMain.omp`.
- `D4_MINE`, `D4_QUARRY`, `D4_BREWERY`, and `D4_ARCANIUM` are each completed in their corresponding sub-domain maps.
- `D4_FEMALE_ELVES` supports both normal completion and `SetQuestCompletedEvil`, proving a branch-sensitive state in the Royal Halls implementation.

## Next extraction

A separate dependency-edge ledger should preserve the actual surrounding Lua condition for each high-confidence transition rather than infer a graph from call ordering alone.
