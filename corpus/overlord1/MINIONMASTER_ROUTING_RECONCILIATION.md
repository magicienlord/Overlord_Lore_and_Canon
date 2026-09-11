# Overlord I `ShowMinionMasterText` Routing Reconciliation

Status: PRIMARY-IMPLEMENTATION CORRECTION

Date: 2026-09-11

This file closes the earlier task concerning unresolved Overlord I `ShowMinionMasterText(...)` references.

## Critical correction

`ShowMinionMasterText(...)` is **not a reliable speaker-identity function**.

The supplied maps route many localization references through this function whose decoded workbook `ACTOR` field explicitly identifies speakers other than Gnarl. Examples include Melvin, Brown Minions, the Minion Jester, peasants, Elf ghosts, Rose, Velvet, Sir William, the Wizard, Jewel, Oberon, and Kahn.

Therefore the earlier interpretation that every call was a direct Minion Master/Gnarl attribution was incorrect.

For speaker identity, the decoded workbook `ACTOR` field remains authoritative when present. Map routing can supplement it only when the map explicitly names the actor/entity or speaker role.

## Correct live-call totals

The 30 supplied non-multiplayer Overlord I maps contain:

- 451 executable `ShowMinionMasterText(...)` call occurrences after Lua comments are removed;
- 365 unique live localization references;
- 359 unique live references that resolve to a decoded localization row after conservative source-group normalization;
- 6 unique live references with no decoded localization row;
- 18 call occurrences, representing 16 unique references, that occur only inside commented-out Lua and are excluded from live routing evidence.

Among the 359 resolved live references, the workbook actor distribution includes:

- `GNARL`: 288
- `BROWN_MINION`: 16
- `MINION_JESTER`: 12
- `TOMB_ELF_GHOST`: 11
- `MELVIN`: 8
- `ROSE`: 5
- `SIR_WILLIAM`: 4
- `WIZARD`: 3
- smaller numbers for Velvet, priests, refugees, Jewel, Oberon, Kahn, and others.

This distribution is direct evidence that the function name describes a presentation/routing mechanism rather than a guaranteed speaker identity.

## The six live unresolved references

### `D0_TUT_MM@106@55`

Source: `Maps/Tower/Tower_Spawnpit.omp`.

The live script calls the reference after all tutorial mushrooms are killed. A developer comment says the sequence should now direct the player toward the Jester.

No corresponding `.8ld` row and no matching MP3 filename exist in the supplied source set.

Status: `PRIMARY-IMPLEMENTATION`, exact text and speaker unresolved. Do not invent a line.

### `D0_TUT_MM@106@60`

Source: `Maps/Tower/Tower_Spawnpit.omp`.

The live reference occurs inside the early tutorial cutscene between surviving `Tower_Awakening` dialogue and a Minion Master animation event.

No corresponding `.8ld` row and no matching MP3 filename exist.

Status: `PRIMARY-IMPLEMENTATION`, exact text unresolved. The surrounding cutscene makes Gnarl plausible but does not provide the missing text, so the corpus does not promote it to primary dialogue.

### `D1_SD1_TheMoistHollows@100@10`

Source: both supplied Blue Cave map copies.

The map uses a `D1_` source prefix even though the area and surviving localization file are `D3_SD1_TheMoistHollows`. Correcting only that obvious domain-prefix discrepancy still leaves `D3_SD1_TheMoistHollows@100@10` absent from the workbook and audio filename set.

Status: stale/removed implementation reference or source-version mismatch. Exact text unknown.

### `D1_SD2_HalflingHomes@203@20`

Source: `HalflingHomes2of2.omp`.

The live call occurs in the explicitly Evil completion path for the recovered-food choice immediately before `D1FOODEVIL` is written true.

The workbook contains `@203@10`, the non-Evil reaction, but not `@203@20`. No matching audio filename exists.

Status: missing branch reaction in the supplied localization build. Speaker/text unknown despite clear branch context.

### `D5_MAIN@203@40`

Source: `WarriorMain.omp`.

The live event is labelled `a1_mm_203_40`. The map source comment preserves the intended line: `Capture her and I think I can persuade her to be a little more... talkative.` The matching MP3 filename also exists, but the workbook row is absent.

Status: `PRIMARY-IMPLEMENTATION TEXT RECOVERY`. The `mm` event label strongly indicates Minion Master intent, but because the localization actor row is absent this line is kept separate from the explicit-workbook Gnarl corpus.

### `D5_MAIN@302@20`

Source: `WarriorMain.omp`.

The map event is labelled `f2_jewel_302_20` and its source comment preserves the line `Having things is not nearly as much fun as stealing them!` A matching MP3 filename exists.

Although the implementation calls `ShowMinionMasterText`, the event label explicitly identifies Jewel and the wording is consistent with Jewel's surrounding scene. This is the clearest demonstration that the function cannot be used as a Gnarl-speaker test.

Status: `PRIMARY-IMPLEMENTATION`, Jewel-intended line; not part of the Gnarl corpus.

## Commented-out references

Five of the formerly reported unresolved references are dead/commented implementation remnants rather than live calls:

```text
D0_TUT_MM@105@30
D0_TUT_MM@108@40
D3_SD1_TheMoistHollows@101@10
D3_SD1_TheMoistHollows@104@10
D4_SD3_TheBrewery@101@50
```

They are excluded from executable dialogue-routing counts.

## Final evidence rule

For Overlord I speaker attribution:

1. decoded workbook `ACTOR` is authoritative when present;
2. explicit map actor/entity labels may supplement missing actor data;
3. `ShowMinionMasterText(...)` alone is not speaker evidence;
4. commented-out calls are not live content;
5. missing localization text remains missing unless exact wording is preserved by another primary implementation source.

This closes the earlier unresolved-Minionspeaker task. The remaining missing references are documented source gaps, not pending attribution work.