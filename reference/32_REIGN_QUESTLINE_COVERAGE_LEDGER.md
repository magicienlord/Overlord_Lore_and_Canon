# OVERLORD REIGN Questline Coverage Ledger

Status: AUTHORITATIVE COVERAGE CHECKLIST

Date refreshed: 2026-09-13

Authority: this file defines the minimum content that the Overlord Quests implementation must consciously review before being considered content-complete. It is a coverage inventory, not the authority for deciding which reviewed mod receives a dedicated questline.

Final quest-facing assignments are governed by `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` together with later explicit refinements such as `reference/37_REIGN_PERSONAL_MOD_SIDEQUEST_DECISIONS.md`.

Dark Tower room ownership and the boundary between room restoration and deeper system progression are governed by `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md`.

Where an older classification or description from this coverage pass conflicts with `34`, `36`, or `37`, the later explicit decision file takes precedence.

---

# 1. OVERLORD CORE

## Minions Remastered

Coverage: REQUIRED CORE CAMPAIGN PROGRESSION.

Minion recovery and the restoration of an active horde are fundamental to OVERLORD REIGN.

Quest logic must acknowledge actual implemented Minion capability unlocks rather than assume gameplay support that does not exist.

The four traditional Brown, Red, Green, and Blue tribes remain canon in-universe. Exact playable-type support remains implementation-dependent until the relevant Minion integrations are finalized.

## TOBI's Minion Enhancements

Coverage: SUPPORTING IMPLEMENTATION.

Use its actual capabilities where useful. It does not require an independent mod-specific questline.

## Overlord Brown Minion and future traditional-type integrations

Coverage: ABSORBED IN MINION / TOWER PROGRESSION.

Any successfully implemented traditional Minion-type unlock belongs to core Minion progression and is acknowledged by the quest system. Do not invent separate Hive-restoration chains for gameplay types that are not implemented.

---

# 2. CIVILIZATION COVERAGE

The following ten civilizations require their established authored civilization arcs and disposition handling:

- Villagers;
- Illagers;
- Dwarves;
- Gnumus;
- Goblins;
- Kobolds;
- Ribbits;
- Sea Dwellers;
- Piglins;
- Umvuthana.

Supporting mods such as VillagersPlus, VillagerTradingPlus, Guard Villagers, It Takes A Pillage, Savage & Ravage, Pillager Caravans, The Conjurer, Better Village, Towns and Towers, Nether Villages, and relevant Mowzie's Mobs content feed those established civilization frameworks rather than becoming independent civilizations merely because they are separate mods.

---

# 3. CORE MAGIC COVERAGE

The following systems require their established dedicated magical progression or authored quest treatment:

- Iron's Spells 'n Spellbooks / spell study and making;
- Farmer's Spell / Gluttony;
- Theurgy;
- Ars Elixirum / alchemy-pharmacology;
- Biomancy;
- Eidolon: Repraised.

Selected physical Tower rooms for these systems are governed by `reference/34_REIGN_TOWER_RESTORATION_DECISIONS.md`. A Tower room does not cause the entire associated magic progression to become Tower Restoration.

---

# 4. CONFIRMED DEDICATED ADVENTURE COVERAGE

The following non-civilization adventure content has been explicitly confirmed for dedicated authored quest treatment:

- The Twilight Forest;
- The Bumblezone;
- L_Ender's Cataclysm;
- The Graveyard;
- Knight Quest;
- The Lost Castle;
- Rats;
- Church of Sin;
- Oddities;
- Immersive Melodies / Quaver's Tower Band, at small Tower-personnel scale.

Important correction from the pre-interview coverage pass: the installed Knight Quest build does not contain a substantial authored native quest campaign. OVERLORD REIGN supplies the authored narrative arc using its essence / Great Chalice progression and Netherman climax as mechanical material.

Exact scale, framing, absorption, and popup rules for all reviewed mods are authoritative in `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md`.

---

# 5. CENTRAL END / WASTELAND COVERAGE

The End / Ender Dragon remains central-campaign material and the Ender Dragon defeat remains the selected final mechanical trigger for the central OVERLORD REIGN campaign.

YUNG's Better End Island, The Outer End, Better End Cities, Enderman Overhaul, and other relevant End extensions are integrated into the End / Wasteland context according to `reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` rather than automatically receiving separate mod questlines.

The same world remains playable after the ending.

---

# 6. REVIEWED CONTENT THAT IS NOT A DEDICATED QUESTLINE

`reference/36_REIGN_MOD_QUESTLINE_ASSIGNMENTS_FINAL.md` is the complete final authority for reviewed mods assigned to any of the following treatments:

- absorbed into another questline;
- conditional or small authored arc;
- popup acknowledgement only;
- introductory popup only;
- provider support;
- quest-location support;
- Tower-restoration substrate;
- systemic / ambient use;
- no quest-facing treatment.

These are intentional outcomes. The Quest Maker must not interpret absence from the quest log as an omission when `36` explicitly assigns a mod to one of these categories.

In particular, the earlier candidate classifications for Rats, Darker Depths, Born in Chaos, Church of Sin, Realm RPG: Imps & Demons, creature/taming systems, Pet Cemetery, Ghosts, equipment systems, and similar entries are resolved by `36` and are no longer open proposals.

---

# 7. PERSONAL BACKPORT SIDEQUEST COVERAGE

The former pending status of Overlord Depths and Overlord NightWalker has been resolved at the quest-treatment level. Exact objectives remain implementation-dependent.

## Overlord Depths / Fathoms adaptation

Coverage: DEDICATED SIDEQUEST ARC IF IMPLEMENTED.

Status: PLANNED / IMPLEMENTATION CONDITIONAL.

If the backport is implemented, Overlord Quests must provide a dedicated sidequest arc rather than leave its content completely uncontextualized.

The preferred principal NPC is the Historian profession if the final NPC and quest mechanics allow it.

The narrative direction may use a Dredge-like discovery/investigation escalation adapted to OVERLORD REIGN and the actual completed Fathoms mechanics. Do not copy Dredge's plot and do not invent unsupported Fathoms mechanics merely to satisfy the concept.

Detailed authority: `reference/37_REIGN_PERSONAL_MOD_SIDEQUEST_DECISIONS.md`.

## Overlord NightWalker / Nycto adaptation

Coverage: DEDICATED VAMPIRE-TRANSITION SIDEQUEST IF IMPLEMENTED.

Status: PLANNED / IMPLEMENTATION CONDITIONAL.

If the backport is implemented, the sidequest activates when the player becomes a vampire through the implemented NightWalker / Nycto system.

A vampire named Lestat joins the Dark Tower and guides the Overlord through the transition. Lestat is to be characterized from the existing Interview with the Vampire television-series transcript research rather than from a generic vampire archetype.

Gnarl and Lestat are intended to have a conflicting but functional relationship. Exact vampire mechanics, tracking hooks, and quest climax must follow the final backport implementation.

Detailed authority: `reference/37_REIGN_PERSONAL_MOD_SIDEQUEST_DECISIONS.md`.

If either personal backport is not implemented in the final pack, its quest must not be fabricated with placeholder mechanics.

---

# 8. EXPLICIT NON-GOAL: QUESTING EVERY MOD

OVERLORD REIGN is not expected to give every installed JAR a questline.

Libraries, optimization mods, UI mods, rendering systems, recipe viewers, building utilities, decorations, storage systems, navigation tools, general equipment frameworks, infrastructure, and content with no meaningful authored progression hook may remain systemic or invisible.

The objective is conscious coverage, not numerical quest-count completeness.

---

# 9. QUEST MAKER COMPLETION RULE

Before Overlord Quests is considered content-complete, the implementation owner must:

1. implement or deliberately account for every dedicated civilization, magic, adventure, Tower, and central-campaign assignment established in `34` and `36`;
2. respect every absorbed, popup-only, systemic, ambient, or no-integration decision in `36` rather than manufacturing extra mod-specific questlines;
3. implement the Overlord Depths dedicated sidequest if that backport is present and sufficiently complete to support it;
4. implement the Lestat-led Overlord NightWalker vampire-transition sidequest if that backport is present and the player becomes a vampire;
5. preserve the campaign spoiler firewall while doing so;
6. record any technically impossible integration as an explicit deferment rather than silently dropping it.

A mod may intentionally receive no questline. It may not be silently forgotten when this ledger, `36`, or `37` says it requires authored treatment.