# Overlord II Speaker Attribution Index

Status: PRIMARY-IMPLEMENTATION EXTRACTION, HIGH-PRECISION SUBSET

Date: 2026-09-11

Sources: supplied Overlord II single-player `.omp` maps correlated against decoded `.8ld` localization.

## Method

The map cutscene data contains strict printable-string records of the form:

```text
Face Expression...
<speaker routing role>
<LOCALIZATION_GROUP@SCENE@TEXT>
<map actor/entity alias>
```

`tools/extract_o2_map_speakers.py` extracts only this local structure. It does not infer speakers from dialogue content or voice.

A representative primary-implementation pattern is:

```text
Face Expression
minionmaster
NW_TR@START@15
GNARL
```

This provides direct speaker-routing evidence for that localization reference.

## Validation totals

Across the 26 supplied non-multiplayer Overlord II maps:

- 195 strict cutscene routing occurrences were found before role/reference de-duplication.
- 184 unique localization-reference plus routing-role pairs remain after de-duplication.
- 183 of those 184 resolve to a decoded localization row after normalizing source-group punctuation and underscore/space variants.
- 1 map reference is absent from the supplied localization row set: `Nordberg_Sanctuary@110@10`, routed through `borius`.
- 32 unique localization references are routed through `minionmaster` and therefore can be attributed directly to Gnarl.

The single unmatched Borius reference appears to be a source/version mismatch or removed line rather than a failure of the routing method, because adjacent `Nordberg_Sanctuary@110@20` and `@30` rows exist in the localization source.

## Major routing roles in the matched subset

| Map routing role | Matched unique refs | Interpretation |
| --- | ---: | --- |
| `minionmaster` | 32 | Gnarl / Minion Master |
| `marius` | 21 | Marius |
| `NB_MALE` | 18 | Generic Nordberg male role |
| `Juno` | 16 | Juno |
| `elf_florian` | 15 | Florian Greenheart |
| `centurionFX` | 14 | Centurion / Empire role variant |
| `Kelda` | 13 | Kelda |
| `GhostFay` | 12 | Ghost Fay |
| `Nordberg_Male_1_head_A` | 6 | Generic Nordberg male visual/actor variant |
| `quaver` | 4 | Quaver |
| `Empire_Fat_Fem_A` | 4 | Generic Empire female role |
| `borius` | 4 matched, 1 unresolved | Borius |
| `Rainbow_Warrior` variant | 4 | source actor-role label retained as implementation terminology |
| `governess` | 3 | Everlight Governess |
| `Imperial guard` | 3 | Imperial Guard role |
| `centurion` | 3 | Centurion |

Other generic visual/face-role labels occur in smaller numbers. They are retained as implementation evidence rather than converted into invented named NPC identities.

## Direct Gnarl references

The following 32 decoded localization references have direct `minionmaster` routing evidence:

```text
NW_TR@START@15
NW_TR@START@20
NW_TR@START@40
NW_TR@START@55
NW_TR@START@70
NW_TR@START@80
NW_TR@START@90
NW_TR@MM1@ACC2
NW_TR@MM1@DEC2
NW_TR@MM1@DEC3
NW_TR@K_A@10
NW_TR@MM2@ACC2
NW_TR@MM2@DEC2
NW_TR@MM5@ACC2
NW_TR@MM5@DEC
NW_TR@ROSE@10
NW_TR@ROSE@15
NW_TR@ROSE@30
NW_TR@ROSE@45
NW_TR@ROSE@50
NW_TR@ROSE@55
NW_TR@ROSE@65
NW_TR@ROSE@70
NW_TR@CHUNK5@60A
NW_TR@CHUNK5@70A
NW_TR@PREP2@10
NW_TR@PREP2@20
NW_TR@PREP2@30
NW_TR@PREP2@50
NW_TR@BRIDGE@10
NW_TR@BRIDGE@30
NW_TR@BRIDGE@40
```

All 32 resolve to decoded `NW_TR.8ld` text.

## Gnarl subset statistics

For this directly routed Overlord II subset only:

- rows: 32
- median line length: 15 words
- average line length: 15.4 words
- lines containing an exclamation mark: 15
- lines containing a question mark: 3
- lines using `Sire`: 12
- lines using `Master`: 6
- lines using `Overlord`: 2

This subset is too small and too Netherworld-heavy to stand in for Gnarl's entire Overlord II voice. It is, however, strong enough to confirm that the earlier Overlord I / Raising Hell patterns of `Sire` and `Master` remain present in Overlord II.

## Evidence rule

Only the 32 `minionmaster` rows above are added to the direct Gnarl corpus by this pass.

Other Overlord II lines remain unattributed unless another direct routing pattern, actor label, or unambiguous scripted source identifies the speaker. Similar vocabulary alone is not evidence.

## Next speaker work

The strict `Face Expression` pattern prioritizes precision. Additional actor-routing structures may exist elsewhere in the maps, including non-cutscene `Speak` and narrative systems. Those should be reverse engineered separately rather than weakening this extractor with proximity heuristics.
