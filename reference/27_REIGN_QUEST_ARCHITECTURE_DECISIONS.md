# OVERLORD REIGN Quest Architecture and Tone Decisions

Status: PROJECT DECISION MIRROR

Date: 2026-09-11

Authority: mirrors explicit OVERLORD REIGN decisions. Numbered project canon files remain authoritative.

## Q-044 - Main Quest markers

Status: CANON DESIGN / PLANNED IMPLEMENTATION

A Main Quest marker has no in-universe object, title, or phenomenon.

It is the runtime representation of a real narrative fact that has become true, such as:

- discovery of a civilization;
- defeat or intimidation of a local ruler;
- resolution of a crisis;
- opening of a campaign phase;
- restoration of part of the Tower;
- completion of another major political or story event.

NPCs and Gnarl do not refer to "markers" in dialogue.

Markers exist so the quest runtime can determine which sidequests, dialogue, providers, services, and branch choices are now valid.

Example:

```text
ILLAGER_BASTILLE_COWED
```

may unlock fearful Illager providers because the political event actually occurred.

## Q-045 - Why NPCs give the Overlord sidequests

Status: CANON WRITING RULE

NPCs are motivated by their own interests rather than by a generic heroic-adventurer convention.

Valid motives include:

- fear;
- greed;
- desperation;
- ambition;
- flattery;
- revenge;
- opportunism;
- coercion;
- genuine submission;
- self-preservation;
- attempts to manipulate the Overlord;
- recognition that the Overlord is the only force capable of solving a particular problem.

NPCs frequently fail to understand who they are dealing with until the consequences become unavoidable, matching the tone and recurring structure of the original games.

Do not default to generic "helpful hero" quest framing.

## Q-046 - Sidequests and civilization disposition

Status: CANON DESIGN / PLANNED IMPLEMENTATION

There is no hidden sidequest reputation score.

Sidequests may set explicit story facts and conditional markers.

Those facts may:

- unlock later main-quest options;
- close incompatible options;
- alter provider access;
- affect local services or dialogue;
- change future quest prerequisites;
- create a political circumstance that a later major quest resolves.

Major civilization quests ordinarily resolve broad states such as HOSTILE, NEUTRAL, or SUBJUGATED.

An exceptional sidequest may directly change disposition only when the sidequest itself is explicitly authored as a political event significant enough to justify that result.

Repeated minor sidequests must not silently accumulate into friendship, reputation, or another disguised numeric system.

## Q-047 - Minimum sidequest persistence

Status: CANON DESIGN

Every completed sidequest must leave at least:

- a persistent quest fact or completion state;
- provider-specific follow-up dialogue/state where the provider survives;
- correct future prerequisites for any quest that refers back to the outcome.

Additional persistence is authored only where appropriate, including:

- new or removed services;
- spawned or removed NPCs;
- local hostility changes;
- physical structure or block changes;
- gifts or tribute;
- new sidequest pools;
- Gnarl reactions;
- authored ghost continuation after death.

Not every sidequest requires a physical world remodel.

## Q-048 - Quest failure and consequence states

Status: CANON DESIGN / PLANNED IMPLEMENTATION

OVERLORD REIGN should prefer consequence states over generic fail screens whenever possible.

Examples:

- deliberate killing of an important NPC may write `NPC_DEAD` rather than merely `QUEST_FAILED`;
- that death may close one branch, open another, change disposition, alter services, or create an authored ghost path;
- mutually exclusive objectives should resolve into authored branches rather than remain contradictory active objectives;
- abandonment may return a quest to available state when abandonment itself carries no narrative consequence;
- retryable mechanical failures remain retryable when no meaningful world-state consequence occurred.

Permanent mistakes should create a different story rather than automatically force a reload whenever technically and narratively feasible.

### Sparse conditional architecture

Status: PLANNED TECHNICAL RULE

Branching must remain sparse rather than combinatorial.

A quest should inspect only the small set of explicit facts that materially affect that quest.

Do not author a separate copy of each quest for every possible global world-state permutation.

Use:

- reusable prerequisite predicates;
- explicit world-state markers;
- local branch junctions;
- shared dialogue templates with conditional inserts where appropriate;
- civilization-state checks only when relevant;
- provider-state checks only when relevant;
- named exceptional markers for unusually important prior outcomes.

The quest graph should therefore grow approximately with authored consequences, not with the theoretical Cartesian product of every marker in the campaign.

This is the required implementation strategy for keeping the consequence-heavy design maintainable.

## Q-049 - Optional lore distribution

Status: CANON PRESENTATION RULE

Mandatory Gnarl dialogue should remain concise and contain what the player needs to understand the immediate objective.

Deeper lore should be distributed through:

- optional NPC follow-up dialogue;
- authored ghost dialogue;
- books and readable records;
- environmental evidence;
- optional conversations;
- later quest callbacks.

Deep franchise continuity remains optional unless a current objective actually depends on it.

Main quests should not become exposition dumps merely because the source corpus is extensive.

## Q-050 - Sidequest darkness and tone

Status: CANON WRITING RULE

Ordinary sidequests may use the full tonal range of the Overlord games.

Common lower-stakes material should disproportionately involve:

- petty selfishness;
- stupidity;
- greed;
- revenge;
- absurd requests;
- local feuds;
- theft;
- drunkenness;
- cheating;
- monsters;
- questionable favors;
- opportunities for disproportionate cruelty.

Serious arcs may escalate into slavery, plague, mutilation, soul abuse, massacres, magical atrocities, destruction, and other severe consequences when justified by the story.

Do not write every sidequest at maximum atrocity, and do not sanitize the setting into generic heroic adventuring.

## Q-051 - Gnarl seriousness and the joke inside it

Status: CANON CHARACTER RULE

Gnarl can become genuinely serious, but his seriousness is fundamentally selective and self-interested.

He becomes grave when the danger concerns:

- the Overlord;
- Minions;
- the Netherworld;
- Gnarl's own survival or fate;
- a threat capable of causing catastrophic damage to those interests;
- a boss or enemy whose danger to the Overlord is substantial enough to require an unambiguous warning.

He does not automatically become solemn merely because other peoples have suffered terribly.

For example, the Imperial massacre of the Elves is not inherently a tragedy to Gnarl. His characteristic complaint would be closer to regretting that he and the Minions were themselves being persecuted and therefore unable to properly enjoy the massacre.

This selective seriousness is itself part of the humor.

A solemn Gnarl scene should not be written as evidence that he has acquired broad humanitarian concern.

Once immediate danger to his actual priorities has passed, sarcasm, contempt, bureaucratic cruelty, or retrospective mockery may return immediately.

Therefore the writing rule is not "Gnarl sometimes stops being funny." It is that Gnarl can be genuinely serious about Evil's own survival, and the narrowness of what he considers worthy of seriousness often becomes the joke.

## Authoring consequence

The combination of persistent consequences and sparse marker dependencies is mandatory for efficient quest production.

Quest authors should define, for every quest:

```text
required_markers
forbidden_markers
provider_state
civilization_state_if_relevant
local_world_state_if_relevant
completion_markers
branch_outputs
persistent_effects
```

Only the fields relevant to that quest should be populated.

This prevents the conditional architecture from expanding into thousands of manually duplicated branches while retaining meaningful long-term consequence.