# OVERLORD REIGN Minion Type Unlock Anchor Decisions

Status: AUTHORITATIVE IMPLEMENTATION / QUEST DESIGN DECISION

Date: 2026-09-13

Authority: this file records the explicit OVERLORD REIGN decision governing how traditional Minion-type unlocks are divided between the Minion implementation and Overlord Quests.

This decision refines and supersedes any older wording in `reference/32_REIGN_QUESTLINE_COVERAGE_LEDGER.md`, `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md`, and `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` that implies the Quest Maker must wait for Minions Remastered or another Minion mod to implement its own native Brown / Red / Green / Blue unlock progression.

## 1. Four traditional Minion types

Status: CANON IN-UNIVERSE

Brown, Red, Green, and Blue Minions all exist in OVERLORD REIGN.

Their existence is not conditional on a quest implementation detail.

## 2. Unlock ownership

Status: PLANNED IMPLEMENTATION / AUTHORITATIVE QUEST BOUNDARY

The Minion implementation deliberately does not own the narrative progression that unlocks the traditional Minion types.

Instead, it exposes anchors / hooks intended for Overlord Quests to use.

The Quest Maker is therefore responsible for deciding, within established lore and campaign constraints:

- when each Minion type becomes available;
- which authored quest, event, discovery, recovery, Hive-related milestone, or other progression condition activates that unlock;
- how Gnarl and other personnel acknowledge the recovery of that capability;
- whether the unlock is tied to Tower restoration, a field quest, recovered infrastructure, another established campaign objective, or a combination of those elements.

The quest system should use the provided anchors rather than waiting for a native Minion-mod questline that is intentionally absent.

## 3. No duplicated unlock system

Status: IMPLEMENTATION GOVERNANCE

Do not add a second independent Brown / Red / Green / Blue progression system inside the Minion mod merely because the quest system needs authored unlocks.

Do not interpret the absence of a native unlock quest as unfinished Minion-mod content.

The separation is deliberate:

- MINION MOD / INTEGRATION LAYER: provides the playable capability and quest-facing anchors / hooks;
- OVERLORD QUESTS: provides the authored narrative, prerequisites, ordering, state, dialogue, and unlock decisions.

## 4. Quest Maker freedom and constraints

Status: CANON DESIGN / IMPLEMENTATION DESIGN

The Quest Maker has substantial freedom to construct the actual recovery sequence using those anchors.

That freedom is bounded by existing OVERLORD REIGN authority:

- Minion recovery is core campaign progression;
- the four traditional tribes already exist in-universe;
- the campaign is semi-open rather than one rigid tutorial corridor;
- sequence-breaking should be recognized where technically possible;
- the quest system should not invent unsupported Minion mechanics merely to make a quest work;
- Dark Tower room ownership remains governed by `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md`;
- the spoiler firewall remains in force for detailed campaign construction.

## 5. Tower / Hive implication

Status: CANON DESIGN REFINEMENT

The Tower Restoration questline does not need four artificial room-restoration chains merely because four traditional tribes exist.

However, where the implemented Minion system exposes anchors corresponding to recovery or activation of Brown, Red, Green, or Blue capability, Tower Restoration and the broader Minion campaign may acknowledge those anchors when narratively appropriate.

The exact recovery structure belongs to the Quest Maker.

The governing principle is therefore not `only acknowledge types if the Minion mod itself implements a native unlock path`.

The governing principle is:

`the Minion implementation exposes the anchors; Overlord Quests authors and triggers the unlock path.`

## 6. Completion requirement

Before Overlord Quests is considered complete, the Quest Maker must inspect the actual Minion integration anchors available in the implemented build and deliberately assign the intended Brown / Red / Green / Blue recovery behavior.

Those decisions may remain internally spoiler-heavy within the Overlord Quests implementation repository. They do not require exposing detailed quest outcomes to the Overlord for approval unless a genuinely unresolved lore, gameplay, or technical decision is encountered.
