# OVERLORD REIGN Questline Coverage Ledger

Status: PROJECT COVERAGE LEDGER

Date: 2026-09-13

Authority: this file exists to prevent the Overlord Quests implementation from overlooking major installed or planned content. It does not replace the detailed canon files for lore, civilization states, magic, chronology, or campaign structure.

## Purpose

The OVERLORD REIGN modpack contains far more content than the subjects explicitly covered during the lore interview.

The Quest implementation must therefore use this ledger as a minimum coverage checklist before declaring the quest mod content-complete.

A mod appearing here does not mean its native mechanics must be rewritten inside Overlord Quests.

Established campaign policy remains authoritative:

- preserve meaningful native progression wherever practical;
- frame it through Gnarl and OVERLORD REIGN context;
- track important native milestones and outcomes;
- react to sequence breaking instead of invalidating it;
- do not create a questline merely to make every installed JAR appear in the quest log;
- do not replace good native progression with an inferior duplicate.

## Coverage classes

### CLASS A - REQUIRED MAJOR AUTHORED COVERAGE

A substantial authored questline, civilization arc, magic arc, or central-campaign role is required.

### CLASS B - REQUIRED NATIVE-PROGRESSION INTEGRATION

The mod already supplies substantial progression, bosses, structures, advancements, or a native quest path. Overlord Quests should frame, point toward, track, and react to that progression rather than replace it.

### CLASS C - REQUIRED SIDEQUEST / REGIONAL INTEGRATION

The mod supplies content strong enough to deserve authored sidequests, a compact regional arc, provider hooks, or recurring callbacks, but not necessarily a full independent questline.

### CLASS D - CONTEXTUAL / AMBIENT USE

The mod is useful as quest material, world texture, equipment, transport, structures, enemies, rewards, or implementation support, but does not require a dedicated questline.

### CLASS X - PENDING IMPLEMENTATION DECISION

The component is planned or still under development. Quest architecture must leave room for it, but its exact integration cannot yet be frozen.

---

# 1. OVERLORD CORE

## Minions Remastered

Coverage: CLASS A

Status: REQUIRED CORE PROGRESSION

Minion recovery and the restoration of an active horde are fundamental to the OVERLORD campaign.

The exact playable Minion-type scope remains IMPLEMENTATION UNKNOWN while the Overlord investigates whether the traditional Brown, Red, Green, and Blue types can be imported or extended into Minions Remastered.

Quest implementation must therefore isolate Minion capability checks rather than hard-code the current single-gameplay-type limitation.

## TOBI's Minion Enhancements

Coverage: CLASS D

Status: SUPPORTING IMPLEMENTATION

This addon extends Minions Remastered functionality. It does not require an independent questline, but quests may use its actual capabilities when useful.

---

# 2. CIVILIZATION QUESTLINES

The ten generalized disposition civilizations already have authored political baselines elsewhere in the repository. Those decisions remain authoritative.

## Villager civilization cluster

Coverage: CLASS A

Primary gameplay sources include vanilla Villagers plus compatible settlement/profession/defense content such as:

- VillagersPlus;
- Guard Villagers;
- Better Village;
- Towns and Towers where relevant to generated settlements.

These mods do not each receive separate political states. They contribute to the single authored Villager civilization framework.

## Illager civilization cluster

Coverage: CLASS A

Primary sources include:

- It Takes A Pillage;
- Savage & Ravage;
- Pillager Caravans;
- The Conjurer;
- vanilla Illagers and raids;
- compatible mansion/outpost structure replacements where useful.

These feed the established Illager warband/Bastille political arc rather than becoming disconnected mini-factions.

## The Dwarven Forge

Coverage: CLASS A

Status: REQUIRED DWARVEN CIVILIZATION ARC

Its Dwarf race, professions, runes, equipment, structures, and Forge-Thane framework are part of the established REIGN Dwarven quest design.

## Gnumus Settlement

Coverage: CLASS A

Status: REQUIRED GNUMUS CIVILIZATION ARC

Its settlements, mobs, hunters, Shaman role, and regional culture are the gameplay basis for the established Gnumus civilization arc.

## Goblin's Tyranny

Coverage: CLASS A

Status: REQUIRED GOBLIN CIVILIZATION ARC

Its major Camp, leader Goblin, professions, structures, and native content are the gameplay basis for the established Goblin civilization arc.

## Kobolds

Coverage: CLASS A

Status: REQUIRED KOBOLD CIVILIZATION ARC

The Kobold Den, Captain, specialist roles, and native Kobold content are the gameplay basis for the established Kobold civilization arc.

## Ribbits

Coverage: CLASS A

Status: REQUIRED RIBBIT CIVILIZATION ARC

Ribbit Village, native social roles, music, trade, gardening, fishing, and Sorcerer content are the gameplay basis for the established Ribbit civilization arc.

## Realm RPG: Sea Dwellers

Coverage: CLASS A + CLASS B

Status: REQUIRED SEA DWELLER CIVILIZATION ARC WITH NATIVE PROGRESSION HANDOFF

The underwater village/trader civilization requires its authored political arc.

Its existing Ocean Dragon progression should remain native and be framed, tracked, and reacted to rather than replaced.

## Nether Villages + vanilla Piglins

Coverage: CLASS A

Status: REQUIRED PIGLIN CIVILIZATION ARC

The canonical Nether Piglin Village/anchor and vanilla Piglin/Brute behavior provide the basis for the established Piglin civilization arc.

Wild Piglins outside the enrolled anchor remain governed by their native behavior unless a specific authored quest says otherwise.

## Mowzie's Mobs - Umvuthi / Umvuthana content

Coverage: CLASS A

Status: REQUIRED UMVUTHANA CIVILIZATION ARC

The Umvuthi Grove, Abavuthana/Umvuthana followers, masks, trade, Sun Blessing, Heliomancy, and Umvuthi creator-god relationship form the basis of the established Umvuthana civilization arc.

Other Mowzie's Mobs content may be used separately where appropriate.

---

# 3. CORE MAGIC QUESTLINES

These systems have established canonical identities in `05_MAGIC.md` and the Core System Unification work. Their quest treatment must preserve those distinctions.

## Iron's Spells 'n Spellbooks

Coverage: CLASS A

Role: active spellcasting and major magical progression.

The questline should introduce and contextualize spellcasting without requiring Overlord Quests to replace Iron's native mechanics.

## Farmer's Spell

Coverage: CLASS A

Role: Gluttony magic and magical cuisine.

This should receive authored treatment as its own thematic magical path, while preserving its relationship to Iron's and Farmer's Delight.

## Theurgy

Coverage: CLASS A

Role: material transmutation, replication, occult material law, alchemical matter processing.

Its meaningful native progression should be preserved and framed rather than bypassed.

## Ars Elixirum

Coverage: CLASS A

Role: magical pharmacology, essences, extracts, effect composition, mastery.

Its native mastery/progression structure deserves dedicated integration rather than being treated as generic potion crafting.

## Biomancy

Coverage: CLASS A

Role: Evil-Mana flesh magic developed by Gnarl during the Silence, inspired by Solarius.

Biomancy is especially important to REIGN because its in-universe interpretation is directly tied to Gnarl and the Silence. It requires substantial authored quest treatment.

## Eidolon: Repraised

Coverage: CLASS A

Role: rites, souls, ritual necromancy, occult binding, transformation, and opposing light elements.

It requires dedicated integration while preserving the established distinction between ritual occultism, ordinary spellcasting, Biomancy, ghosts, Lifeforce, and true resurrection.

---

# 4. MAJOR ADVENTURE, DIMENSION, AND BOSS PROGRESSION

These mods are too substantial to be silently ignored by the final questmod even when they do not belong to a civilization.

## The Twilight Forest

Coverage: CLASS B

Status: REQUIRED NATIVE-PROGRESSION INTEGRATION

The dimension has a large established native progression path. Overlord Quests should provide REIGN framing, relevant entry hooks, milestone recognition, and callbacks while preserving the native progression structure.

## The Bumblezone

Coverage: CLASS B

Status: REQUIRED NATIVE-PROGRESSION INTEGRATION

The dimension is explicitly built around exploration/adventure and advancement-guided progression. It should receive contextual integration and milestone tracking rather than a duplicate quest tree.

## L_Ender's Cataclysm

Coverage: CLASS B

Status: REQUIRED BOSS/STRUCTURE PROGRESSION INTEGRATION

Cataclysm contains major bosses, structures, equipment, and progression-significant encounters. Important encounters should be recognized by the quest system and may feed the central campaign or substantial optional arcs where lore fit warrants it.

Associated content such as Cataclysm: Spellbooks and L_Ender's Delight should normally support the Cataclysm integration rather than each requiring a separate independent questline.

## The Graveyard

Coverage: CLASS B

Status: REQUIRED BOSS/STRUCTURE INTEGRATION

Its bosses, graveyard structures, undead content, and death themes are substantial enough to deserve a coherent REIGN framing and progression arc.

This must respect the project's established soul, ghost, death, undeath, and resurrection distinctions.

## Knight Quest

Coverage: CLASS B

Status: REQUIRED NATIVE QUESTLINE HANDOFF

The mod already advertises a native questline, enemies, rare materials, and equipment progression.

Overlord Quests should frame and track its progression rather than replace the native questline.

## The End / Ender Dragon / YUNG's Better End Island

Coverage: CLASS A CENTRAL CAMPAIGN

Status: REQUIRED CENTRAL ENDGAME

The Ender Dragon defeat is the selected final mechanical trigger for the central OVERLORD REIGN campaign.

The End is tied in REIGN lore to the Great Cataclysm and dimensional Wasteland rupture.

The native/end-island combat remains mechanically valid, while the ordinary Minecraft end presentation is intended to be replaced or overlaid by an OVERLORD REIGN ending presentation.

The same world continues afterward.

## The Outer End and Better End Cities

Coverage: CLASS B / CLASS C

Status: REQUIRED END CONTEXT INTEGRATION

These extend the End as an explorable place. They do not independently define the central ending, but the Quest implementation should account for their structures, biomes, and exploration when developing the End/Wasteland campaign material.

## The Lost Castle

Coverage: CLASS C

Status: REQUIRED REGIONAL/OPTIONAL ARC

Its enormous authored castle and map-based discovery are strong enough to justify a compact quest arc or major optional expedition rather than being left as uncontextualized structure loot.

---

# 5. STRONG OPTIONAL QUESTLINE CANDIDATES

The following content should not be skipped during quest planning, but current lore decisions do not yet require each to become a full major questline.

Their classification is therefore PROPOSAL / MUST REVIEW rather than CANON QUEST REQUIREMENT.

## Rats

Coverage: PROPOSAL - CLASS B or CLASS C

Reason: unusually deep native advancement, crafting, creature, and progression footprint. The Quest Maker must inspect the actual installed progression before deciding whether it warrants a dedicated arc or substantial sidequest chain.

## Darker Depths

Coverage: PROPOSAL - CLASS C

Reason: substantial underground biomes, structures, and progression material. Best suited to underground regional quests unless deeper installed mechanics justify more.

## Born in Chaos

Coverage: PROPOSAL - CLASS C

Reason: broad hostile-mob and encounter roster. Better suited to monster/problem arcs, bounty-style sidequests, or regional threats than a forced standalone main questline unless a coherent native progression is found.

## Church of Sin

Coverage: PROPOSAL - CLASS C

Reason: strong thematic fit for localized cult/religious side content. Exact installed mechanics must be inspected before committing to scope.

## Realm RPG: Imps & Demons

Coverage: CLASS C

Status: SMALL NETHERWORLD/DEMONIC SIDE CONTENT

Demons are explicitly outside the generalized civilization disposition framework. They may still receive lore, encounters, cult hooks, Netherworld context, and localized sidequests.

## The Conjurer

Coverage: CLASS C WITHIN ILLAGER ARC

The Conjurer should normally be consumed by the Illager quest architecture rather than receiving an unrelated standalone political questline.

## Mythic Mounts / Companions! / Tameable Beasts / Domestication Innovation

Coverage: PROPOSAL - CLASS C / CLASS D

These are possible provider, taming, acquisition, or creature-focused sidequest sources. They do not require independent campaign arcs by default.

## Artifacts / Relics

Coverage: CLASS D

Use as exploration rewards, unique quest rewards, treasure targets, or authored objects where suitable. Their existence does not justify separate generic fetch questlines.

## Pet Cemetery / Ghosts

Coverage: CLASS C / CLASS D

Ghosts is already an implementation substrate for selected authored dead-NPC continuations, not a universal afterlife system.

Pet Cemetery may support localized death/pet-related stories if thematically useful.

Neither requires a mandatory independent main questline solely because it is installed.

## Farmer's Delight / Dungeon's Delight / L_Ender's Delight

Coverage: CLASS C / CLASS D

Food and cooking systems may support Gluttony quests, civilization requests, tavern/provider content, dungeon loot, or Cataclysm integration.

Farmer's Delight itself should not receive a generic cookbook-completion questline unless an authored story actually needs one.

## Hot Iron / Shield Expansion / Fantasy Weapons / Fantasy Armor

Coverage: CLASS C / CLASS D

These systems are legitimate sources for smithing, equipment, reward, or specialist-provider quests. They do not require separate lore civilizations or mandatory progression arcs by default.

---

# 6. WORLDGEN AND STRUCTURE MODS

Worldgen replacements and structure overhauls should generally be used as places where quests happen, not as subjects that demand their own questline.

Examples include:

- YUNG's Better Dungeons;
- YUNG's Better Mineshafts;
- YUNG's Better Nether Fortresses;
- YUNG's Better Ocean Monuments;
- Luki's Strongholds;
- Luki's Woodland Mansions;
- Towns and Towers;
- Better Village;
- Amplified Nether;
- Nether Depths Upgrade;
- Pale Garden Backport;
- Better End Cities;
- The Outer End where not being used for the dedicated End context above.

Coverage: CLASS D unless a specific authored quest promotes one to CLASS C or higher.

The Quest Maker may use these locations freely, but should not create artificial questlines whose only premise is that a worldgen mod exists.

---

# 7. PLANNED PERSONAL MOD INTEGRATIONS

These components are being developed in parallel and are expected to become important quest sources.

## Overlord Depths / Fathoms adaptation

Coverage: CLASS X, intended CLASS A or CLASS B depending final native progression

Status: PLANNED

The Quest architecture must leave integration room for its final gameplay loop, bosses, structures, items, and progression once the implementation stabilizes.

Do not invent final quest requirements before reading the completed mod and its handoff/source documentation.

## Overlord NightWalker / Nycto adaptation

Coverage: CLASS X, intended CLASS A or CLASS B depending final native progression

Status: PLANNED

The Quest architecture must leave integration room for its final progression and encounter systems once the implementation stabilizes.

Do not freeze assumptions from an unfinished backport.

---

# 8. EXPLICIT NON-GOAL: QUESTING EVERY MOD

The final Questmod is not expected to give every installed mod a questline.

Libraries, optimization mods, UI mods, resource/display mods, storage utilities, recipe viewers, rendering systems, building tools, purely decorative packs, and similar infrastructure should normally have no quest presence.

Likewise, a content mod with no meaningful narrative or progression hook may remain ordinary sandbox content.

The coverage objective is not numerical completeness. It is to prevent omission of content whose scale, progression, lore value, civilization role, boss structure, magical identity, or native quest design makes it meaningfully deserving of authored integration.

---

# 9. QUEST MAKER COMPLETION RULE

Before Overlord Quests is considered content-complete, the implementation owner must review every CLASS A, CLASS B, CLASS C, CLASS X, and PROPOSAL/MUST REVIEW entry in this ledger and record one of the following outcomes:

- integrated as major authored questline;
- integrated through native progression framing/tracking;
- integrated as sidequest/regional content;
- intentionally left ambient, with reason;
- deferred because the dependent mod is unfinished or technically unavailable.

A listed mod may therefore be intentionally excluded from quests, but it must not be silently forgotten.

This review is subordinate to the spoiler firewall. The Quest Maker does not need to expose detailed campaign plots to the Overlord merely to prove coverage.
