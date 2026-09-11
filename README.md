# Overlord Lore and Canon

Private working repository for OVERLORD REIGN franchise-source research, lore reconciliation, quest-source reconstruction, and Gnarl dialogue analysis.

## Authority boundary

This repository is a reference and research workspace. Original Overlord franchise evidence does not automatically become OVERLORD REIGN canon.

OVERLORD REIGN canon remains governed by the canonical project files and the Overlord's explicit decisions.

## Repository layout

```text
reference/
  pass01/
  pass02/
source_raw/
  overlord1/
  companion/
tools/
  8ld/
corpus/
  quests/
  gnarl/
  lore/
notes/
```

`source_raw/` should contain only the active non-audio research subset: `.8ld`, `.omp`, official manuals, and small supporting metadata. Original game ZIP archives and MP3 payloads are intentionally excluded.

## Current technical objective

Develop a transparent, reproducible decoder for Triumph Studios' `M8LD` localization format. First validation fixture: `Tower_Awakening.8ld`, correlated against direct `ShowMinionMasterText(...)` references in the Overlord I Tower map.

## Source discipline

Internal quest IDs, debug labels, aliases, and map comments are `PRIMARY-IMPLEMENTATION` evidence, not automatically player-facing franchise terminology.
