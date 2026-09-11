# OVERLORD REIGN Runtime Quest and Endgame Decisions

Status: PROJECT DECISION MIRROR

Date: 2026-09-11

Authority: mirrors explicit OVERLORD REIGN decisions. Numbered project canon files remain authoritative.

This file extends the campaign-structure decisions while preserving the spoiler firewall.

## Concurrent major objectives

Status: CANON DESIGN / PLANNED IMPLEMENTATION

The semi-open central campaign may expose several major objectives at the same time.

There is no requirement for one permanently designated current main quest that blocks all other major progress.

The player may choose which available major objective to pursue, subject only to real prerequisite, capability, world-state, or native-mod constraints.

## Player death

Status: CANON GAMEPLAY RULE

Ordinary Minecraft player death has no narrative consequence by itself.

Respawning does not automatically:

- fail quests;
- reset political states;
- create cowardice or defeat markers;
- alter civilization disposition;
- become a canonical death of the Overlord.

A specific authored encounter may define a special failure condition only when explicitly designed to do so.

## Gnarl delivery surface

Status: CANON PRESENTATION / IMPLEMENTATION RULE

Gnarl does not require a physical in-world NPC body for normal quest delivery.

His ordinary presence is delivered through Questlog popups and related quest-system presentation.

Important objectives, warnings, reactions, reminders, and branch commentary may therefore reach the Overlord remotely through Questlog without requiring a return to the Tower after every quest.

Tower returns should be required only when the actual story event, location, ceremony, artifact, or world-state change genuinely requires the Tower.

## Native-mod progression tracking

Status: CANON DESIGN / PLANNED IMPLEMENTATION

When another mod exposes reliable progression signals, OVERLORD REIGN should track them directly rather than alter the native progression.

Preferred signals include:

- advancements;
- boss death states;
- obtained items;
- structure discovery or entry;
- capabilities;
- documented APIs;
- stable entity or world-state events.

When no clean signal exists, use the narrowest reliable compatibility hook available.

Do not modify another mod's progression merely to simplify REIGN tracking.

## Questlog completed-history support

Status: IMPLEMENTED BASELINE

The current Questlog system already supports completed quest history.

OVERLORD REIGN should use that capability to preserve meaningful completed main quests and sidequests, including branch-specific completion text where supported by the authored quest data.

Completed records should describe what the Overlord actually did rather than only repeat the original objective.

## Optional objectives

Status: CANON DESIGN / IMPLEMENTATION UNKNOWN

Optional objectives are desirable when they produce a concrete reward, consequence, shortcut, extra cruelty, useful opportunity, or later remembered fact.

The current technical ability of Questlog to represent optional objectives cleanly has not yet been confirmed.

Therefore:

- do not make optional-objective support a hard dependency of the central campaign until verified;
- if Questlog supports them cleanly, use them selectively;
- if not, equivalent optional actions may be implemented as side conditions, hidden/explicit markers, alternate interactions, or small linked sidequests where technically appropriate;
- avoid generic bonus-condition scoring such as arbitrary XP checklists.

## Quest rewards

Status: CANON DESIGN RULE

Quest rewards should primarily arise from the actual world consequence of the action.

Examples include:

- access;
- loot;
- services;
- subjects;
- artifacts;
- information;
- political control;
- native-mod progression;
- Tower functionality;
- new quest providers or pools;
- local-world changes.

Generic XP or item rewards may supplement these where appropriate but should not replace meaningful in-world outcomes.

## Central ending mechanical trigger

Status: CANON CAMPAIGN RULE

The central campaign's final mechanical resolution is tied to the defeat of the Ender Dragon.

This uses Minecraft's existing final-boss and ending infrastructure rather than inventing a separate disconnected terminal state.

The End is already canonically connected to the Great Cataclysm in OVERLORD REIGN. Therefore the central campaign may build toward the End and the Ender Dragon in whatever lore-consistent way the hidden main-quest design requires.

Detailed narrative framing remains behind the spoiler firewall.

## Overlord-specific end presentation

Status: PLANNED IMPLEMENTATION

After the Ender Dragon is defeated, the ordinary Minecraft end presentation should be replaced or modified into an OVERLORD REIGN-specific ending screen/sequence.

Design goals:

- unmistakably conclude the central campaign;
- preserve the Ender Dragon defeat as the underlying Minecraft completion event;
- present an Overlord-specific conclusion rather than the ordinary vanilla end text;
- return the player to the same persistent world afterward;
- preserve unresolved civilization arcs, sidequests, native progression, Tower work, exploration, and sandbox play.

This resolves the campaign-ending problem without requiring New Game+, a pre-ending reload, or a separate disposable world state.

## End and Cataclysm continuity

Status: CANON CONTINUITY CONSTRAINT

The End is a consequence or dimensional result of the Great Cataclysm in OVERLORD REIGN lore.

The exact hidden central-campaign explanation, route, and revelations may use this established relationship, but should not be exposed during spoiler-safe planning unless the Overlord explicitly requests review.

## Spoiler-preserving authoring consequence

These rules are sufficient to let detailed central-campaign construction proceed privately at the design level.

Only genuine unresolved lore decisions, technical blockers, or implementation capabilities that materially change player-facing behavior should be returned to the Overlord for approval.