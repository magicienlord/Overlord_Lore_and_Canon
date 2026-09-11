# Overlord II Branch-Specific Quest Outcome Ledger

Status: PRIMARY-TEXT EXTRACTION

Date: 2026-09-11

Source: `Resources/System_Quests.8ld`

This file records every quest ID in the supplied English quest workbook that has an explicit branch-specific completion text using `DESC_DONE_DES`, `DESC_DONE_DOM`, or `DESC_DONE_EVIL`.

These are implementation IDs and source quest strings. They are not automatically OVERLORD REIGN quest IDs.

## Summary

- 13 quest IDs have branch-specific completion records.
- 11 use paired Destruction and Domination completion strings.
- 2 use an `EVIL`-specific completion string rather than the paired `DES` / `DOM` form.

## Ledger

| Quest ID | Objective | Destruction / Evil completion | Domination completion |
| --- | --- | --- | --- |
| `LM0_MM1_2` | Decide what to do with the villagers; use them or punish them | `DESC_DONE_EVIL`: You have killed the villagers | No dedicated `DOM` string in this source row set |
| `LM3C_MM9_TYRANNY` | Decide to keep Fay as mistress or drain her to the death | `DESC_DONE_EVIL`: You killed Fay, her power is yours | No dedicated `DOM` string in this source row set |
| `Q16_TASK_01` | Tear the Commune apart | `DESC_DONE_DES`: You've destroyed the Commune through death and mayhem | `DESC_DONE_DOM`: You've controlled the Commune by turning the residents into slaves |
| `Q18_TASK_03` | Kill or Subdue the Everlight Governess | `DESC_DONE_DES`: You have killed the Governess of Everlight | `DESC_DONE_DOM`: You have subdued the Governess of Everlight |
| `Q19_TASK_09` | Destroy the Villa and take down Senator Drearius | `DESC_DONE_DES`: You've destroyed the Villa and killed Senator Drearius | `DESC_DONE_DOM`: You've destroyed the Villa and turned Senator Drearius into your slave |
| `Q24_TASK_03` | Kill or Enslave the Yeti | `DESC_DONE_DES`: You've killed your old friend, the Yeti | `DESC_DONE_DOM`: You've subdued your old friend, the Yeti |
| `Q28_TASK_05` | Overcharge Dark Fay or take her as your Mistress | `DESC_DONE_DES`: You've overcharged Dark Fay and killed her | `DESC_DONE_DOM`: You've taken Dark Fay as your Mistress |
| `Q30_TASK_03` | Decide the fate of the last rebel | `DESC_DONE_DES`: You have punished the elves with death and destruction | `DESC_DONE_DOM`: You have again taught the elves that you are their master |
| `Q4_TASK_15` | Kill or Enslave Borius | `DESC_DONE_DES`: You've killed Governor Borius | `DESC_DONE_DOM`: Governor Borius is your groveling slave |
| `Q8_TASK_04` | Set fire to the giant tar pit or subdue 10 villagers to remove the ice for you | `DESC_DONE_DES`: You've set fire to a giant tarpit and melted the ice | `DESC_DONE_DOM`: You've subdued 10 villagers into melting the ice for you |
| `TCT_EVERLIGHT_QUEST` | Control Everlight Town | `DESC_DONE_DES`: You've destroyed Everlight Town | `DESC_DONE_DOM`: You've dominated Everlight Town |
| `TCT_FAIRYLAND_QUEST` | Control Sanctuary Town | `DESC_DONE_DES`: You've controlled Sanctuary Town through Destruction | `DESC_DONE_DOM`: You've controlled Sanctuary Town through Domination |
| `TCT_NORDBERG_QUEST` | Control Nordberg Town | `DESC_DONE_DES`: You've destroyed Nordberg Town | `DESC_DONE_DOM`: You've dominated Nordberg Town |

## Source conclusions

### 1. Branch state is explicit data

The completion record itself can encode how the objective was resolved. The games do not need to reconstruct tyranny style from a hidden morality number after the fact.

### 2. Domination is not synonymous with mercy

The source uses Domination outcomes including slavery, forced labor, subjugation, and keeping useful targets alive under control.

### 3. Destruction is not always the same physical action

Destruction outcomes include killing a target, annihilating a population, using death/mayhem, or choosing a destructive environmental solution such as the tar pit.

### 4. The same objective can lead to a shared world-state goal through different means

Town-control quest records demonstrate that both branches can satisfy `control` while preserving a different authored completion state.

## Relevance to OVERLORD REIGN

This is direct structural precedent for REIGN's planned civilization-disposition and branching quest model.

A REIGN quest can therefore store:

```text
objective_id
completion_state
resolution_method
civilization_state_change
world_state_change
```

rather than collapsing the outcome into a generic reputation delta.

This is a design inference from primary source structure, not an instruction to copy these specific quest IDs or outcomes.
