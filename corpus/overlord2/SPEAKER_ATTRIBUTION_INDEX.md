# Overlord II Speaker Attribution Index

Status: PRIMARY-IMPLEMENTATION EXTRACTION, COMPLETE HIGH-CONFIDENCE PASS

Date: 2026-09-11

Sources: supplied Overlord II single-player `.omp` maps correlated against decoded `.8ld` localization.

## Evidence rule

The supplied narrative workbooks generally leave actor cells blank. Speaker identity is accepted only when the map implementation itself supplies a direct character/speaker structure.

Three direct structures are used. Dialogue wording, memory, and voice recognition are not speaker evidence.

## 1. Face-expression routing

Observed structure:

```text
Face Expression...
<speaker routing role>
<LOCALIZATION_GROUP@SCENE@TEXT>
<map actor/entity alias>
```

Representative pattern:

```text
Face Expression
minionmaster
NW_TR@START@15
GNARL
```

Validation across the 26 supplied non-multiplayer maps:

- 195 strict routing occurrences before role/reference de-duplication
- 184 unique localization-reference plus role pairs
- 183 resolve to a decoded localization row
- one missing/version-mismatched reference: `Nordberg_Sanctuary@110@10`, routed through `borius`
- 32 unique decoded references routed through `minionmaster`

Major matched routing roles include `minionmaster`, `marius`, `Juno`, `elf_florian`, `Kelda`, `GhostFay`, `quaver`, `governess`, Centurion/Imperial roles, and generic NPC actor variants.

## 2. Explicit `Speak` routing

Observed structure:

```text
Speak
<map actor/entity alias>
...
<LOCALIZATION_GROUP@SCENE@TEXT>
```

`tools/extract_o2_map_speakers.py` accepts only the first localization reference inside the bounded `Speak` record. A line enters the attributed corpus only if the reference also resolves to decoded localization.

Gnarl-specific actor entities include forms such as:

```text
GNARL
GNARL_CK4
GNARL_ROSE
CS_BU_GNARL
CS_AU_GNARL
```

The matched `Speak` pass contributes 17 unique decoded Gnarl references before union with the other direct methods.

Map-side markers without matching decoded localization rows are not promoted into dialogue.

## 3. Named Gnarl implementation labels

A broader but still direct map structure uses character-specific event labels located immediately beside a localization reference.

Representative labels include:

```text
GNARL_ANNOUNCEMENT
GNARL_MAGIC_AMBIENT
GNARL_GENERAL
GNARL_KELDA_*
GNARL_JUNO_*
GNARL_DFAY_*
GNARL_GFAY_*
GNARL_DOM_*
GNARL_DES_*
INITIAL_GNARL
CS_GNARL_*
```

The extractor accepts only labels beginning with `GNARL`, `INITIAL_GNARL`, or `CS_GNARL`, rejects obvious waypoint/control labels such as `_WP`, `POINT`, `HOME`, `PORT`, and `AUDITION`, and takes only the first localization reference within the next four printable records.

The result is then validated against the decoded localization corpus.

Tool: `tools/extract_o2_named_gnarl_labels.py`.

Validated against the extracted 26 single-player maps and normalized Overlord II localization corpus:

- 173 de-duplicated conservative named-label records
- 165 of those records resolve to decoded localization
- 149 unique decoded localization references are represented by the matched named-label records

The one-reference difference from the earlier exploratory count is due to final de-duplication/filter ordering in the reproducible extractor. The combined corpus total below is unchanged.

This structure recovers Gnarl material outside the Netherworld-heavy face-routing subset, including ambient Netherworld lines, Hunting Grounds material, Wasteland Sanctuary material, and smaller numbers from Empire and Everlight contexts.

## Combined direct Gnarl corpus

The normalized union of all three direct implementation methods contains **173 unique decoded Overlord II Gnarl references**.

No line enters this set because it merely sounds like Gnarl.

Source-group distribution:

| Source group | Direct Gnarl rows |
| --- | ---: |
| `NW_TR` | 62 |
| `Ambient_NW` | 38 |
| `Wasteland_Sanctuary` | 32 |
| `Hunting_Grounds` | 19 |
| `Empire_Heartlands` | 6 |
| `Empire_Endbattle` | 3 |
| `Empire Arena` | 2 |
| `Everlight_Gates` | 2 |
| `Empire Assault` | 1 |
| `Everlight_Facility` | 1 |
| `Everlight_Jungle` | 1 |
| `Everlight_Temple` | 1 |
| `MM_2` | 1 |
| `MiniMission_1` | 1 |
| `MiniMission_9` | 1 |
| `NW_B` | 1 |
| `NW_F` | 1 |

## Direct Overlord II Gnarl statistics

For these 173 source-attributed rows:

- median line length: 15 words
- average line length: 15.1 words
- lines containing an exclamation mark: 101
- lines containing a question mark: 13
- lines using `Sire`: 62
- lines using `Master`: 13
- lines using `Overlord`: 4

This independently confirms the pattern already visible in Overlord I and Raising Hell: `Sire` remains Gnarl's dominant direct honorific, `Master` remains common, and repetitive direct-address use of `Overlord` remains rare.

The Overlord II subset is broad enough to cover multiple gameplay contexts, but it remains a source-attributed subset rather than a claim that every Gnarl line in the game has been recovered.

## Other speakers

The same direct structures provide reliable attribution for portions of dialogue belonging to Marius, Juno, Florian, Kelda, Ghost Fay, Quaver, Borius, the Everlight Governess, Centurions, Imperial Guards, and generic NPC roles.

Generic visual/actor labels remain implementation terminology. They are not converted into invented named characters.

## Completion boundary

The high-confidence speaker-recovery task is complete for the current source corpus.

A remaining actorless line is not treated as an unfinished attribution task merely because a speaker could perhaps be guessed. It remains unattributed unless an additional direct map structure is discovered.

This preserves the distinction:

```text
direct source-attributed speaker
unattributed primary text
inferred speaker, not admitted to corpus
```

Only the first category is used for quantitative named-character voice analysis.
