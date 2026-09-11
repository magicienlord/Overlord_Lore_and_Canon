# OVERLORD Franchise Gnarl Dialogue and Voice Bible

Status: PRIMARY-SOURCE SYNTHESIS, VERSION 1

Date: 2026-09-11

Authority: franchise reference only. This file describes the source character and does not automatically establish new OVERLORD REIGN dialogue or canon.

## Corpus boundary

This version uses only source rows whose actor attribution is explicit in the supplied localization workbooks, plus map-script evidence that directly routes a localization reference through the Minion Master dialogue function.

Overlord II narrative sheets in the supplied English data leave actor cells blank. They are therefore excluded from quantitative speaker-style claims until speaker attribution is independently reconstructed.

### Explicitly actor-labelled material

Overlord I:

- 759 English rows explicitly identify actor `GNARL`.

Raising Hell:

- 152 English rows explicitly identify actor `GNARL`.

Overlord I map scripts additionally expose 379 unique direct Minion Master localization references. Source-name normalization currently reconciles 368 of them to localization rows. Eleven remain unresolved and are not guessed.

## Quantitative voice profile

### Overlord I

- rows: 759
- median line length: 11 words
- average line length: 11.6 words
- rows containing an exclamation mark: 426
- rows containing a question mark: 29
- rows using `Sire`: 188
- rows using `Master`: 102
- rows using `Overlord`: 12
- rows mentioning Minions: 166
- rows mentioning the Tower: 42
- rows explicitly using the word evil: 29
- rows referring to Lifeforce: 10

### Raising Hell

- rows: 152
- median line length: 15 words
- average line length: 15.7 words
- rows containing an exclamation mark: 93
- rows containing a question mark: 11
- rows using `Sire`: 52
- rows using `Master`: 19
- rows using `Overlord`: 1

The statistics reinforce a visible pattern in the source: Gnarl generally speaks in short, emphatic bursts rather than extended speeches. Raising Hell allows him somewhat longer explanatory lines because he is introducing unfamiliar Abyss situations.

## Forms of address

### PRIMARY-EXPLICIT

`Sire` is Gnarl's dominant direct honorific in the explicitly labelled corpus.

`Master` is also common, especially when emphasizing service, Minion hierarchy, or the Overlord's authority.

`Overlord` itself is comparatively uncommon as direct address. It is a title and identity, but not Gnarl's default vocative.

### Writing rule

For source-faithful new dialogue, default to `Sire` rather than repeatedly calling the player `Overlord`. Use `Master` when the relationship of service or command is foregrounded. Avoid inventing ornate recurring honorifics unless REIGN deliberately establishes them.

## Functional range

The following categories are analytical coding of source rows and developer trigger notes, not original game labels.

The Overlord I Gnarl corpus contains roughly:

- 345 field-narrative / objective-context rows
- 266 Tower, tutorial, or administrative rows
- 90 reactive hints or ambient banter rows
- 26 progression/reward reaction rows
- 18 finale rows
- 9 death/failure reaction rows
- a small number of explicitly quest-state-labelled rows

This breadth is important. Gnarl is not only a quest giver.

He acts simultaneously as:

- adviser;
- tutorial voice;
- tactical observer;
- Tower administrator;
- narrator of opportunity and threat;
- keeper of institutional memory;
- commentator on Minion losses and resources;
- evaluator of the Overlord's conduct;
- comic pressure valve;
- reminder system when the player stalls or ignores an objective.

## Delivery and performance

### PRIMARY-EXPLICIT

The localization production sheets contain direction notes calling for delivery such as chuckling, cackling, disgust, sarcasm, sighing, whispering, exaggerated pronunciation, mock sweetness, and sudden changes in tone.

Developer notes also explicitly request alternate performances for repeated gameplay reminders so that mechanically repeated information does not sound identical.

### Writing consequence

Gnarl's humor is performative, not merely lexical. A line can be structurally simple while its direction turns it into mockery, disgust, relish, impatience, or false sympathy.

For REIGN, dialogue scripts should therefore preserve a delivery/direction field wherever practical rather than treating text alone as the complete character performance.

## Core speech characteristics

### 1. Objective first

Gnarl usually communicates the actionable fact early. Characterization wraps around the instruction instead of obscuring it.

A useful writing pattern is:

`observation -> actionable instruction -> malicious/comic interpretation`

or:

`problem -> why it matters to the Overlord -> what should be done`

### 2. Hierarchical deference without passivity

Gnarl consistently acknowledges the Overlord's superiority, but he is comfortable correcting, warning, redirecting, and explaining things to him.

He does not behave like a frightened courtier waiting for permission to speak. His authority comes from age, expertise, and his role as Minion Master while ultimate authority remains with the Overlord.

### 3. Evil as ordinary administration

The source frequently treats tyranny, punishment, pillage, casualties, and domination as practical matters rather than solemn declarations of villainy.

The comedy works because Gnarl often discusses grotesque or cruel things with the tone of an experienced administrator handling routine business.

### 4. Contempt is targeted

Gnarl mocks incompetence, weakness, sanctimony, enemies, inconveniences, and sometimes Minions. His contempt usually serves the current objective or reinforces the Overlord's superiority rather than becoming random insult generation.

### 5. Minions are resources and subjects, not disposable noise

Gnarl is casual about Minion casualties and frequently reacts to shortages, deaths, hives, caps, and summoning. The source also makes him their manager and institutional spokesman.

For writing purposes, he can be callous about individual Minions while still caring strongly about Minion strength as the foundation of the Overlord's power.

### 6. Humor does not replace information

Many gameplay lines are funny, but the joke rarely removes the instruction. The player can normally still tell what changed, what is wrong, or what to do next.

### 7. Repetition is intentionally varied

The source production notes explicitly call for multiple recordings or formulations for recurring triggers such as low Minion availability, Minion deaths, player idling, resource acquisition, and Tower interactions.

REIGN should follow the same principle for recurrent quest reminders and ambient reactions: use pools of context-equivalent lines rather than one endlessly repeated sentence.

## Recommended REIGN Gnarl registers

Status: DESIGN PROPOSAL derived from source evidence.

These registers are useful tags for the quest-writing system:

- `CEREMONIAL`: enthronement, major victory, Tower milestones, succession.
- `DIRECTIVE`: immediate objective instruction.
- `TACTICAL`: combat, Minion use, enemy weakness, route warning.
- `ADMINISTRATIVE`: Tower systems, resources, prisoners, tribute, Minion capacity.
- `HISTORICAL`: old Overlords, civilizations, past disasters, remembered places.
- `MOCKING`: enemy or NPC ridicule tied to context.
- `REACTIVE`: player idling, failure, death, shortages, repeated mistakes.
- `REWARD`: acquisition, upgrade, recovered artifact, successful conquest.
- `CHOICE`: frames alternatives and later comments on the selected outcome.
- `OMINOUS`: threats or discoveries where humor is intentionally reduced.

A single line may carry more than one register, but one should normally be primary.

## Anti-patterns for future writing

The source corpus gives us reason to avoid:

- making every Gnarl line a long monologue;
- using `Overlord` as a repetitive sentence-opening vocative;
- generic faux-Shakespearean speech;
- constant purple gothic prose;
- random cruelty with no objective or situational connection;
- modern neutral tutorial language with a joke pasted onto the end;
- treating him as merely comic relief;
- treating him as omniscient when the source situation gives him no basis to know something;
- making him servile or afraid to correct the Overlord;
- forcing a joke into scenes that need genuine threat or historical weight.

## Quest-system implementation recommendation

Status: PROPOSAL.

Every authored Gnarl line in OVERLORD REIGN should eventually carry structured metadata similar to:

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

This mirrors information already present in the original localization production sheets and will make the new quest corpus easier to audit for voice drift.

## Remaining work

- classify all 911 explicitly actor-labelled Overlord I / Raising Hell Gnarl rows by function and register;
- reconcile the eleven unresolved Overlord I direct Minion Master map references;
- reconstruct Overlord II speaker ownership before incorporating it into quantitative Gnarl voice statistics;
- isolate how Gnarl's language changes between tutorial, mid-game administration, major choices, finales, and post-game/Abyss material;
- use the resulting evidence to produce a smaller operational `GNARL_WRITING_RULES.md` for the actual quest authorship phase.
