# OVERLORD REIGN Campaign Progression Constraints

Status: PROJECT DECISION MIRROR

Date: 2026-09-11

Authority: mirrors explicit OVERLORD REIGN decisions. Numbered project canon files remain authoritative.

This file extends `29_REIGN_CAMPAIGN_STRUCTURE_DECISIONS.md` while preserving the campaign spoiler firewall.

## Internal phases, not visible acts

Status: CANON DESIGN / PLANNED IMPLEMENTATION

The central campaign may use internal phases for authoring, pacing, prerequisite control, and validation.

Those internal phases should not normally be presented to the player as a rigid Act I / Act II / Act III chapter menu.

The quest experience should feel like one continuous reign whose available problems and opportunities expand over time.

## Capability gates instead of civilization gates

Status: CANON CAMPAIGN RULE

Central campaign progression should normally depend on actual capabilities and relevant story facts rather than on a required count of resolved civilizations.

Valid central progression gates may include:

- Minions Remastered progression actually available in the installed mod;
- important equipment or artifacts;
- magical capabilities;
- dimension access;
- native-mod progression milestones;
- restored functional infrastructure;
- explicit central-story facts;
- completed boss or dungeon states where the central plot genuinely depends on them.

Civilization disposition remains parallel political content unless a specific authored story fact requires otherwise.

## Minion fiction versus Minions Remastered gameplay

Status: CANON CONTINUITY / IMPLEMENTATION PRESENT, RUNTIME QUALIFICATION ONGOING

OVERLORD REIGN fiction retains all four traditional Minion tribes: Browns, Reds, Greens, and Blues.

The active Overlord Minions implementation now exposes four stable Minions Remastered roster slots and maps them directly to Brown, Red, Green, and Blue progression identities. Its public server API owns permanent unlock state for those four slots, and its summon gate applies the same four-slot ordering to Minions Remastered's authoritative roster. This supersedes the earlier temporary assumption that only one directly playable Minion type existed in the pack.

Current rules:

- quests and dialogue may treat the Overlord's Minion society as containing all four traditional tribes;
- Questlog may observe and request Brown, Red, Green, and Blue slot unlocks only through the Overlord Minions owner API rather than duplicating that state as narrative facts;
- restoration of Minion strength remains core Overlord progression;
- the exact diegetic recovery route for Red, Green, and Blue remains unresolved and must not be invented from biome, boss, item, or unrelated-mod associations;
- Green and Blue progression must continue to respect the owner-state sequence checks already defined by the cross-mod contract;
- the complete Brown -> Red -> reload -> Green -> reload -> Blue -> reload runtime sequence, rejection behavior, idempotency, login reconciliation, and final in-pack behavior still require full-instance qualification;
- no quest should require a tribe-specific interaction beyond what the validated owner implementation actually exposes.

The remaining uncertainty is therefore recovery authoring and full runtime qualification, not the existence of the four progression slots.

## Dimension sequence breaking

Status: CANON DESIGN / PLANNED IMPLEMENTATION

Dimensions should not be artificially blocked merely because the central campaign has not formally introduced them.

If the player legitimately reaches a relevant dimension early, the campaign should recognize that fact where technically possible.

Later story beats may still require a specific purpose, artifact, encounter, or progression state inside that dimension, but dialogue should not pretend the player has never visited a place already reached.

Native mod gates remain valid and should not be bypassed merely for narrative convenience.

## Boss integration

Status: CANON DESIGN

Appropriate vanilla and modded bosses may be incorporated into the central campaign when their lore, mechanics, location, and progression role fit.

The central campaign must not become a checklist requiring every boss in the modpack.

Bosses not required by the central story may remain:

- native progression;
- civilization content;
- sidequest content;
- optional challenge content;
- ordinary world exploration.

If a relevant boss is killed before its formal quest introduction, the sequence-break rule applies and its death should be recognized rather than undone.

## Tower artifacts and Tower development

Status: CANON DESIGN

Tower progression should follow the broad precedent of Overlord I rather than becoming a mandatory construction checklist.

The Overlord may encounter Tower artifacts, relics, functional objects, upgrades, or restoration opportunities while pursuing other goals.

The central campaign does not normally order the player to scour the world specifically to collect every Tower artifact.

Functional or magical Tower milestones may matter when a quest genuinely depends on them, but completion of the central story must not require the player to finish every architectural portion of the physical Dark Tower build.

The player's actual Minecraft construction of the Tower remains a major sandbox/building project rather than a forced quest quota.

## Sidequest pool model

Status: CANON DESIGN / PLANNED IMPLEMENTATION

Sidequest content uses two broad classes.

### Finite authored sidequests

These are the primary narrative sidequests.

They may contain:

- named providers;
- persistent consequences;
- branch-specific outcomes;
- authored ghost continuations;
- civilization or local-world effects;
- unique dialogue;
- later callbacks.

They are finite and should feel deliberately written.

### Limited repeatable local tasks

Repeatable tasks are allowed only where repetition makes contextual and mechanical sense.

They should preferably reuse cheap existing mechanics and must not dominate the quest experience.

The framework must not devolve into endlessly generated generic collection errands merely because repeatable quest generation is technically possible.

## Quest-provider density

Status: CANON PRESENTATION / DESIGN RULE

Not every named NPC should function as a permanent quest dispenser.

Provider eligibility depends on relevant factors such as:

- NPC role or class;
- settlement or civilization;
- local state;
- campaign markers;
- disposition where relevant;
- unlocked sidequest pool;
- provider survival or ghost state;
- the NPC having a plausible motive to involve the Overlord.

An NPC may have no quest available until circumstances change.

This is intended to preserve an authored world rather than an MMO-style field of constant quest markers.

## Spoiler-preserving authoring consequence

These rules define the player-facing structure without exposing detailed campaign content.

Detailed central-quest ordering, reveals, boss framing, betrayals, branch traps, dialogue payoffs, and surprise outcomes remain behind the established spoiler firewall unless the Overlord explicitly requests review.
