# Overlord II Speaker Attribution Index

Status: PRIMARY-IMPLEMENTATION EXTRACTION, HIGH-PRECISION SUBSET

Date: 2026-09-11

Sources: supplied Overlord II single-player `.omp` maps correlated against decoded `.8ld` localization.

## Method

Two direct map structures are accepted.

### Face-expression routing

```text
Face Expression...
<speaker routing role>
<LOCALIZATION_GROUP@SCENE@TEXT>
<map actor/entity alias>
```

Representative source pattern:

```text
Face Expression
minionmaster
NW_TR@START@15
GNARL
```

### Explicit Speak routing

```text
Speak
<map actor/entity alias>
...
<LOCALIZATION_GROUP@SCENE@TEXT>
```

For this pattern the extractor accepts only the first localization reference within the bounded Speak record. A line enters the dialogue corpus only if that reference also resolves to an actual decoded localization row.

`tools/extract_o2_map_speakers.py` implements both structures. It does not infer speakers from dialogue content or voice.

## Face-expression validation totals

Across the 26 supplied non-multiplayer Overlord II maps:

- 195 strict face-expression routing occurrences were found before role/reference de-duplication.
- 184 unique localization-reference plus routing-role pairs remain after de-duplication.
- 183 of those 184 resolve to a decoded localization row after normalizing source-group punctuation and underscore/space variants.
- 1 map reference is absent from the supplied localization row set: `Nordberg_Sanctuary@110@10`, routed through `borius`.
- 32 unique localization references are routed through `minionmaster` and therefore can be attributed directly to Gnarl.

The unmatched Borius reference appears to be a source/version mismatch or removed line because adjacent `Nordberg_Sanctuary@110@20` and `@30` rows exist in the localization source.

## Major face-expression routing roles

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

Other generic visual/face-role labels occur in smaller numbers. They remain implementation evidence rather than invented named NPC identities.

## Direct Gnarl references from face-expression routing

The following 32 decoded localization references have direct `minionmaster` evidence:

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

## Additional Gnarl references from explicit Speak routing

The map data also contains explicit `Speak` records whose actor entity is `GNARL` or a Gnarl-specific alias such as `GNARL_CK4`, `GNARL_ROSE`, `CS_BU_GNARL`, or `CS_AU_GNARL`.

After requiring an exact decoded localization-row match, this adds 16 unique Gnarl references not already present in the face-expression set:

```text
NW_TR@ROSE@35
NW_TR@KELDAR1@ACC2
NW_TR@KELDAR1@DEC2
NW_TR@KELDAR2@ACC2
NW_TR@KELDAR2@DEC2
NW_TR@JUNOR1@ACC2
NW_TR@JUNOR1@DEC2
NW_TR@JUNOR2@ACC2
NW_TR@JUNOR2@DEC2
NW_TR@DFAYR1@ACC2
NW_TR@DFAYR1@DEC2
NW_TR@DFAYR2@ACC2
NW_TR@DFAYR2@DEC2
NW_TR@GFAYR1@ACC2
NW_TR@GFAYR1@DEC2
NW_TR@GFAYR2@DEC
```

Some additional `Speak` records point at map-side event markers such as `...@DECA` or `...@10A` that have no corresponding decoded localization row. Those markers are not promoted into the dialogue corpus.

## Combined direct Overlord II Gnarl subset

The union of the two independently direct map-routing methods contains 48 unique decoded Gnarl lines.

For this source-attributed subset:

- rows: 48
- median line length: 14 words
- average line length: 14.3 words
- lines containing an exclamation mark: 24
- lines containing a question mark: 4
- lines using `Sire`: 22
- lines using `Master`: 7
- lines using `Overlord`: 2

This subset is still Netherworld-heavy and must not be treated as a complete quantitative profile of all Overlord II Gnarl dialogue. It does independently confirm continued preference for `Sire` and `Master` over repetitive use of `Overlord` as direct address.

## Evidence rule

Only localization rows backed by direct map routing enter the Overlord II named-speaker corpus in this pass.

Other Overlord II lines remain unattributed unless another actor-routing structure or unambiguous source record identifies the speaker. Similar vocabulary alone is not evidence.

## Next speaker work

The two current extractors cover cutscene face-routing and explicit Speak records. Other narrative/ambient systems may encode speaker ownership differently. Those systems should be reverse engineered separately rather than weakened with proximity heuristics.
