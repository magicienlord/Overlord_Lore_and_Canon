# OVERLORD REIGN Civilization Interview Decisions

Status: PROJECT DECISION MIRROR

Date opened: 2026-09-11

Authority: this file mirrors explicit civilization decisions made during the revised quest-lore interview. Numbered canonical project files remain authoritative.

## Interview Method

Franchise lore, vanilla Minecraft behavior, and installed-mod behavior should be treated as prefilled evidence where they already answer a civilization question.

The interview should ask the Overlord only about genuine REIGN choices or technical/gameplay limitations needed to translate that source material into Overlord Quests.

## Villagers / Humans

Status: CANON / PLANNED IMPLEMENTATION

Political organization:

- decentralized villages across the wider human-inhabited world;
- no single universal human kingdom or government is imposed;
- local institutions can vary by settlement.

Historical memory:

- knowledge of old Overlords and Minions is civilization-specific and uneven;
- among humans it may survive through folklore, distorted legends, records, ruins, place-names, religious warnings, and scholarship rather than one universal account.

Baseline relationship:

- suspicious rather than universally attack-on-sight.

Motivations:

- ordinary human motivations should remain grounded in Overlord franchise precedent;
- greed is important in the broad human sense, not the Dwarven gold-obsession sense;
- food, farms, trade, family, safety, religion, opportunity, status, local authority, corruption, survival, and self-interest are valid recurring concerns.

Providers:

- all compatible Villager professions, including modded professions, may provide sidequests when appropriate.

Disposition model:

- NEUTRAL;
- SUBJUGATED;
- HOSTILE.

Local settlements may be destroyed, but DESTROYED is not a civilization-wide human state.

SUBJUGATED:

- Villagers remain productive and culturally recognizable;
- they pay tribute;
- reduced prices and useful services are desirable where they can be implemented cheaply;
- Overlord banners or other visual occupation markers are desirable if they can be applied as one-time world-state edits;
- no autonomous revolt simulation.

NEUTRAL:

- normal Minecraft Villager behavior with Overlord-franchise human identity and personality in quest writing.

HOSTILE:

- Guard Villagers and ordinary Minecraft defensive behavior should provide physical hostility where possible;
- trade prices should become substantially worse where existing mechanics can support it;
- peaceful quest pools close and hostile/destruction or reconciliation quests become available.

State changes:

- only from explicit player actions and quests;
- no autonomous disposition drift.

Recurring Overlord tension:

- productive domination versus destructive indulgence, derived from source precedent rather than invented as a new human cultural trait.

## Illagers

Status: CANON / PLANNED IMPLEMENTATION

Political organization:

- decentralized warbands, camps, strongholds, and local leaders rather than one universal nation;
- the intended feel resembles Fable III's local mercenary warbands, where breaking one major camp does not pacify every independent hostile band.

Quest anchor:

- one designated Take a Pillage Bastille is the principal Illager civilization quest anchor and explicit quest starter;
- arbitrary combat, patrols, raids, camps, mansions, outposts, or unrelated Bastilles must not automatically begin the civilization arc.

Opening relationship:

- initially hostile;
- the Overlord establishes authority through force, intimidation, leadership defeat, or related hostile action.

Progression:

- continued hostile pursuit may lead to local destruction;
- overpowering the Bastille may create a fearful/cowed non-hostile phase;
- peaceful interaction can open after that point;
- choosing to keep the Illagers useful can lead to SUBJUGATED.

The exact storage of the fearful/cowed intermediary phase remains a technical design question. Current recommendation is to represent it as a quest-state phase layered over NEUTRAL rather than create an additional global disposition.

Inter-civilization behavior:

- nothing about subjugation changes normal Illager hostility toward Villagers unless a later authored quest explicitly changes that relationship.

Subjugation reward direction:

- no generalized allied-warband AI system is required;
- raid infrastructure and raiding tools are a natural benefit of making the Bastille safe/friendly to the Overlord;
- installed Take a Pillage code confirms the Ravager Horn applies or increments vanilla Bad Omen, allowing existing vanilla raid logic to provide the raid benefit without a new persistent simulation.

Providers:

- use Illager class/role identity rather than jobs;
- providers only become interactable when quest state permits.
