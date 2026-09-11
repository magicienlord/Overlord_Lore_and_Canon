# OVERLORD Franchise Gnarl Dialogue and Voice Bible

Status: PRIMARY-SOURCE SYNTHESIS, VERSION 2

Date: 2026-09-11

Authority: franchise reference only. This file describes the source character and does not automatically establish new OVERLORD REIGN dialogue or canon.

## Corpus boundary

This version uses only dialogue whose speaker identity is directly established by primary source data.

Accepted speaker evidence:

- explicit workbook `ACTOR` values in Overlord I and Raising Hell;
- direct Overlord II map speaker-role routing;
- explicit Overlord II `Speak` actor entities;
- conservative Overlord II character-specific `GNARL_*`, `INITIAL_GNARL`, or `CS_GNARL_*` implementation labels that resolve to decoded localization.

Dialogue wording, voice recognition, and memory are not used to assign speakers.

### Important Overlord I correction

`ShowMinionMasterText(...)` is **not** a speaker-identity function.

A comment-aware map pass finds 365 unique live references routed through it, of which 359 resolve to localization. Only 288 of those resolved rows have workbook actor `GNARL`; 71 have explicit non-Gnarl actors including Brown Minions, the Minion Jester, Melvin, Elf ghosts, Rose, Sir William, the Wizard, Jewel, Oberon, and Kahn.

Accordingly, earlier claims that all such calls were direct Gnarl references are superseded.

Full reconciliation: `corpus/overlord1/MINIONMASTER_ROUTING_RECONCILIATION.md`.

## Direct source-attributed corpus

### Overlord I

- 759 English localization rows explicitly identify actor `GNARL`.
- median line length: 11 words
- average line length: 11.6 words
- rows containing an exclamation mark: 426
- rows containing a question mark: 29
- rows using `Sire`: 188
- rows using `Master`: 102
- rows using `Overlord`: 12
- rows mentioning Minions: 166
- rows mentioning the Tower: 42
- rows explicitly using `evil`: 29
- rows referring to Lifeforce: 10

### Raising Hell

- 152 English localization rows explicitly identify actor `GNARL`.
- median line length: 15 words
- average line length: 15.7 words
- rows containing an exclamation mark: 93
- rows containing a question mark: 11
- rows using `Sire`: 52
- rows using `Master`: 19
- rows using `Overlord`: 1

### Overlord II

The localization workbooks generally omit actor values, so speaker identity was reconstructed from direct map implementation structures.

The completed high-confidence pass yields 173 unique decoded Gnarl references across:

- `NW_TR`: 62
- `Ambient_NW`: 38
- `Wasteland_Sanctuary`: 32
- `Hunting_Grounds`: 19
- `Empire_Heartlands`: 6
- `Empire_Endbattle`: 3
- `Empire Arena`: 2
- `Everlight_Gates`: 2
- nine additional source groups with one line each

Statistics for those 173 directly source-attributed rows:

- median line length: 15 words
- average line length: 15.1 words
- lines containing an exclamation mark: 101
- lines containing a question mark: 13
- lines using `Sire`: 62
- lines using `Master`: 13
- lines using `Overlord`: 4

This is a direct subset, not a claim that every Overlord II Gnarl line has been recovered.

Full method: `corpus/overlord2/SPEAKER_ATTRIBUTION_INDEX.md`.

## Forms of address

### PRIMARY-EXPLICIT

Across all three reviewed source phases, `Sire` is Gnarl's dominant direct honorific.

`Master` is also common, especially when service, Minion hierarchy, succession, or the Overlord's authority is foregrounded.

`Overlord` itself is comparatively uncommon as a vocative. It is an office/title, but not Gnarl's default way of beginning every sentence.

### Writing rule

For source-faithful new dialogue, default to `Sire` rather than repeatedly calling the player `Overlord`. Use `Master` when the service relationship or command hierarchy matters. Avoid inventing ornate recurring honorifics unless REIGN deliberately establishes them.

## Line length and pacing

The explicitly attributed source supports a consistent tendency toward compact, actionable lines.

Overlord I is especially terse, with an 11-word median. Raising Hell and the directly attributed Overlord II subset sit around a 15-word median because more lines explain unfamiliar supernatural threats, Netherworld systems, or strategic context.

### Writing consequence

Gnarl can deliver longer historical or ominous exposition when necessary, but routine quest direction should not default to paragraph-length speeches.

## Functional range

Gnarl is not merely a quest giver.

Primary-source material establishes him as:

- Minion Master;
- adviser;
- tutorial voice;
- tactical observer;
- Tower/Netherworld administrator;
- keeper of institutional memory;
- succession authority and continuity witness;
- narrator of opportunity and threat;
- commentator on resources, Minion losses, and recovered infrastructure;
- evaluator of the Overlord's conduct;
- comic pressure valve;
- reminder system when the player stalls or ignores an objective.

Overlord I production metadata alone places his lines across field narrative, Tower administration, tutorials, reactive hints, progression/reward reactions, finales, and failure/death contexts.

## Delivery and performance

### PRIMARY-EXPLICIT

The localization production sheets contain direction notes calling for delivery such as:

- chuckling and cackling;
- disgust;
- sarcasm;
- sighing;
- whispering;
- exaggerated pronunciation;
- mock sweetness;
- sudden tonal changes.

Developer notes explicitly request alternate performances for repeated gameplay reminders so mechanically repeated information does not sound identical.

### Writing consequence

Gnarl's humor is performative, not merely lexical. A structurally simple line can become mockery, relish, impatience, false sympathy, or disgust through delivery.

REIGN dialogue authoring should therefore preserve a delivery/direction field wherever practical.

## Core speech characteristics

### 1. Objective first

Gnarl usually communicates the actionable fact early. Characterization wraps around the instruction instead of obscuring it.

Useful source-derived structures include:

```text
observation -> actionable instruction -> malicious/comic interpretation
problem -> why it matters to the Overlord -> what should be done
```

### 2. Hierarchical deference without passivity

Gnarl acknowledges the Overlord's superiority but readily corrects, warns, redirects, explains, and criticizes.

He is not a frightened courtier. His confidence comes from age, expertise, Minion institutional authority, and service across multiple Masters, while ultimate authority remains with the Overlord.

### 3. Evil as ordinary administration

Tyranny, punishment, pillage, sacrifice, casualties, and domination are frequently discussed as practical administrative matters rather than solemn declarations of villainy.

The comedy often comes from treating grotesque or cruel activity as routine management.

### 4. Contempt is targeted

Gnarl mocks weakness, incompetence, sanctimony, enemies, inconveniences, and Minions when context supports it. His contempt usually reinforces an objective, diagnosis, or the Overlord's superiority.

He is not a random-insult generator.

### 5. Minions are resources, subjects, and an institution

Gnarl can be callous about individual Minion deaths while caring strongly about Minion strength, Hives, Lifeforce, training, resurrection, and the continuity of Minion society under an Overlord.

### 6. Humor does not replace information

A comic Gnarl line normally still tells the player what changed, what matters, or what to do.

### 7. Repetition is intentionally varied

Recurring reminders and state reactions use variant lines or requested alternate performances. REIGN should likewise use contextual pools rather than one endlessly repeated reminder.

### 8. Gnarl is knowledgeable, not omniscient

The source sometimes has him discover, infer, reconsider, or react to new information. Quest writing should not grant him knowledge merely because the writer needs exposition.

## Recommended REIGN Gnarl registers

Status: DESIGN PROPOSAL derived from source evidence.

- `CEREMONIAL`: enthronement, major victory, Tower milestones, succession.
- `DIRECTIVE`: immediate objective instruction.
- `TACTICAL`: combat, Minion use, enemy weakness, route warning.
- `ADMINISTRATIVE`: Tower systems, resources, prisoners, tribute, Minion capacity.
- `HISTORICAL`: old Overlords, civilizations, disasters, remembered places.
- `MOCKING`: context-specific ridicule.
- `REACTIVE`: idling, failure, death, shortages, repeated mistakes.
- `REWARD`: acquisition, upgrade, recovered artifact, conquest success.
- `CHOICE`: frames alternatives and reacts to resolution.
- `OMINOUS`: threats/discoveries where comedy is reduced.

A line may combine registers, but one should normally dominate.

## Anti-patterns

Avoid:

- making every Gnarl line a monologue;
- repeatedly opening with `Overlord`;
- generic faux-Shakespearean diction;
- constant purple gothic prose;
- random cruelty unrelated to the situation;
- neutral tutorial text with a joke pasted on afterward;
- reducing him to comic relief;
- treating him as omniscient;
- making him servile or afraid to correct the Overlord;
- forcing jokes into scenes that need genuine threat or historical weight.

## Quest-system implementation recommendation

Status: PROPOSAL.

Each authored REIGN Gnarl line should eventually support metadata similar to:

```text
speaker: GNARL
register: DIRECTIVE | REACTIVE | ...
quest_id:
trigger:
player_state:
world_state:
primary_information:
form_of_address:
delivery_direction:
repeat_pool:
source_inspiration:
```

This mirrors information already present in the original production sheets and makes voice drift auditable.

## Research completion boundary

The baseline Gnarl voice research required for quest authorship is complete.

Completed:

- explicit Overlord I actor corpus;
- explicit Raising Hell actor corpus;
- high-confidence direct Overlord II speaker-recovery pass;
- correction of the false `ShowMinionMasterText == Gnarl` assumption;
- operational REIGN writing rules in `GNARL_WRITING_RULES.md`.

Actorless Overlord II lines without direct implementation attribution remain unattributed primary text. They are not a blocker and will not be guessed into the Gnarl corpus.
