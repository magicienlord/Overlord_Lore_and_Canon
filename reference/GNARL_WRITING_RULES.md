# Gnarl Operational Writing Rules for OVERLORD REIGN

Status: DESIGN REFERENCE DERIVED FROM PRIMARY SOURCE

Date: 2026-09-11

This is the compact authoring layer derived from `09_GNARL_DIALOGUE_AND_VOICE.md`, the 911 explicitly actor-labelled Overlord I / Raising Hell Gnarl rows, and the directly map-attributed Overlord II subset.

It is a writing constraint document, not an independent lore authority.

## 1. Default address

Preferred direct vocatives, in order:

1. `Sire`
2. `Master`
3. context-specific alternatives such as `Lord`

Do not use `Overlord` as Gnarl's repetitive default form of address.

Primary corpus evidence:

- Overlord I explicit Gnarl rows: `Sire` 188, `Master` 102, `Overlord` 12.
- Raising Hell explicit Gnarl rows: `Sire` 52, `Master` 19, `Overlord` 1.
- directly attributed Overlord II subset: `Sire` 22, `Master` 7, `Overlord` 2.

## 2. Normal line length

Default to a compact line that can be understood during gameplay.

Observed medians:

- Overlord I: 11 words.
- Raising Hell: 15 words.
- direct Overlord II subset: 14 words.

Longer speeches are appropriate for ceremonies, major revelations, historical explanation, and serious threats. They should not become the default for ordinary quest direction.

## 3. Information order

Preferred structures:

```text
observation -> actionable instruction -> malicious/comic interpretation
```

or:

```text
problem -> why it matters to the Overlord -> required action
```

The player should normally understand the gameplay information even if the joke is removed.

## 4. Hierarchy

Gnarl recognizes the Overlord's superior rank without becoming timid.

He may:

- instruct;
- remind;
- correct;
- warn;
- explain;
- recommend;
- criticize delay or foolishness;
- express relief or frustration.

He should not behave like a courtier frightened to offer expertise. His authority derives from age, Minion leadership, administrative responsibility, and institutional memory.

## 5. Cruelty and evil

Treat evil as ordinary policy more often than as theatrical self-description.

Source-faithful Gnarl tends to frame:

- punishment;
- pillage;
- domination;
- destruction;
- Minion casualties;
- subject management;
- resource extraction;
- enemy suffering;

as practical administrative matters.

Do not make every line explicitly announce how evil something is.

## 6. Humor

Humor should arise from the situation, objective, target, or delivery.

Strong source patterns include:

- contempt for incompetence;
- mock sympathy;
- bureaucratic treatment of cruelty;
- delight at useful destruction;
- irritation with Minion or NPC behavior;
- grotesque understatement;
- sudden enthusiasm;
- cynical reinterpretation of apparently moral choices.

Avoid detached joke-writing that does not help frame the current objective.

## 7. Contempt must have a target

Gnarl's insults normally reinforce one of the following:

- why the enemy deserves conquest;
- why an NPC is weak, pompous, useless, or exploitable;
- why the Overlord should act;
- why a failed approach was foolish;
- why Minions or subjects require management.

Do not generate random insult strings merely to make him sound malicious.

## 8. Minions

Gnarl is simultaneously:

- callous about individual casualties;
- protective of Minion strength as a strategic resource;
- responsible for Hives, summoning, numbers, abilities, losses, and training;
- the principal institutional spokesman for Minion society.

He may joke about deaths while still treating depletion of the horde as a real operational problem.

## 9. Knowledge limits

Do not make Gnarl omniscient.

He can plausibly know information through:

- direct observation;
- Minion reports;
- Tower/Netherworld systems;
- his own historical memory;
- previously established intelligence;
- magical communication that the quest has established.

If the source of his knowledge matters, the quest should establish it.

## 10. Registers

Every authored line should have one primary register:

- `CEREMONIAL`: accession, Tower milestones, major victory, succession.
- `DIRECTIVE`: immediate quest instruction.
- `TACTICAL`: enemies, combat, Minion capability, route/hazard.
- `ADMINISTRATIVE`: Tower, tribute, prisoners, resources, subjects, Minion capacity.
- `HISTORICAL`: old rulers, factions, catastrophes, remembered places.
- `MOCKING`: contextual ridicule.
- `REACTIVE`: idling, shortage, failure, death, repeated mistake.
- `REWARD`: artifact, upgrade, recovered object, conquest milestone.
- `CHOICE`: presentation or reaction to an authored branch.
- `OMINOUS`: threat/revelation with reduced comedy.

Secondary registers may be tagged, but one function should dominate.

## 11. Quest lifecycle coverage

A major quest should not have only an acceptance line and a completion line.

Where useful, prepare Gnarl pools for:

```text
introduction
objective clarification
first reminder
repeat reminder variants
new information / objective update
warning
branch framing
success
branch-specific success
failure or retreat reaction
post-quest world-state comment
```

The source production sheets explicitly use alternate formulations and performance directions for repetitive triggers.

## 12. Delivery direction

Preserve a delivery field in authored data.

Useful source-backed performance modes include:

- chuckle/cackle;
- disgust;
- sarcasm;
- sigh;
- whisper;
- mock sweetness;
- exaggerated emphasis;
- sudden tonal shift;
- reduced humor / genuine concern.

The text alone is not the complete character performance.

## 13. Serious scenes

Gnarl can become genuinely grave when the subject warrants it.

Do not force a punchline into:

- major succession revelations;
- existential threats;
- Overlord loss;
- catastrophic magic;
- history carrying emotional weight;
- moments where his concern for the Master is the point.

Raising Hell's ending is strong precedent for allowing unusual personal attachment and concern to surface without changing his overall character.

## 14. Choice framing

Gnarl may advocate, mock, or interpret choices, but the branch should remain intelligible as a real decision.

For Domination/Destruction-style choices:

- Domination may mean preserving useful subjects, enslaving, subjugating, exploiting, or compelling labor.
- Destruction may mean killing, annihilation, burning, or choosing a destructive solution.

Do not automatically frame Domination as kindness.

## 15. Historical exposition

Break exposition into quest-useful pieces.

Preferred behavior:

- tell the player what past event matters now;
- identify the useful threat/object/person;
- leave irrelevant chronology out of the active dialogue;
- store deeper optional history in follow-up dialogue, codex-like material, or later conversations.

Gnarl is an institutional memory, not an encyclopedia dump.

## 16. Anti-patterns

Reject drafts that rely on:

- faux-Shakespearean vocabulary as a substitute for voice;
- constant gothic purple prose;
- sentence after sentence beginning with `Overlord`;
- generic neutral tutorial prose followed by a cruelty joke;
- random cruelty unrelated to the task;
- permanent cackling or exclamation;
- long monologues for routine objectives;
- modern meme/slang voice;
- servile fear of correcting the player;
- unexplained omniscience;
- treating Gnarl solely as comic relief.

## 17. Recommended quest-data fields

```text
speaker: GNARL
register:
secondary_register:
quest_id:
trigger:
player_state:
world_state:
primary_information:
recommended_action:
form_of_address:
delivery_direction:
repeat_pool:
branch_state:
source_inspiration:
source_fact_dependencies:
```

The final two fields are especially important for OVERLORD REIGN. They allow new dialogue to be audited against the franchise reference and current project canon without confusing inspiration with authority.
