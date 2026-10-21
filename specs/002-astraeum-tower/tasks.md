# Tasks: Astraeum Tower

**Input**: [spec.md](spec.md), [plan.md](plan.md)
**Legend**: `[X]` done · `[ ]` not done yet · `[P]` can run in parallel

## Phase 1: Setup

- [X] T001 Create single-file canvas game shell with fixed 60 fps loop in `dungeon/index.html`
- [X] T002 Build script that embeds PixelLab sprites, tiles and maps as data URIs
- [X] T003 [P] Import 12 character walk sprites (4 directions) and idle portraits

## Phase 2: User Story 1 – Pick a character and play a floor (P1)

- [X] T010 Character select screen with 12 cards, weapon name and starting element
- [X] T011 Movement (arrows / WASD) with wall collision and wall-face band
- [X] T012 Per-character weapons table (`WEAPONS`): arc, thrust and throw types
- [X] T013 Spells: J bolt, K burst, Q swap ice/fire, Steam Burst reaction
- [X] T014 Melee soft-aim and close-range hits (fix for missed swings)
- [X] T015 Floor 1 from the author's Damp Corridors layout, wang tileset rendering
- [X] T016 Exit stairs and floor transition

## Phase 3: User Story 2 – Tower and bosses (P1)

- [X] T020 15-floor structure, three tiers of darkness/tint
- [X] T021 Map generator (rooms + MST corridors + nooks) with BFS reachability check
- [X] T022 Floor scaling of enemy HP / damage / speed and map size
- [X] T023 Enemies: slime, bat (sonic wave), spitter, brute, rock golem (ground slam), jumping mushroom
- [X] T024 Bosses: Slime King (F5), Bat Lord (F10), Slime Emperor (F15) with enrage phases
- [X] T025 Lobby portal + next-floor portal after each boss; win screen on F15

## Phase 4: User Story 3 – Loot and shop (P2)

- [X] T030 Gold coins, herbs, glowcaps, five gem types, chests (normal and rune)
- [X] T031 Props (barrels, crates, pots, pillars, rubble), candles, cobwebs, items placed in alcoves
- [X] T032 Shrine shop on F4/F9/F14: herbs, elixir, upgrades, sell gems and glowcaps
- [X] T033 Bag HUD: herb, glowcap, combined gem slot

## Phase 5: User Story 4 – Save and records (P2)

- [X] T040 Auto-save at floor start, Continue from lobby
- [X] T041 Record board (best time + character per floor)
- [X] T042 Validate saved data before using it (found by security probing, see test log)

## Phase 6: User Story 5 – Defence (P3)

- [X] T050 Dodge with stamina (Space)
- [X] T051 Shield with countdown (U)
- [X] T052 Healing herb (H)

## Phase 7: Polish

- [X] T060 Per-weapon attack effects (halberd thrust + sweep, greatsword slam, rapier double thrust, spear lunge, twin swords X, daggers, axes, scythe crescent, trident prongs)
- [X] T061 Pause menu, death screen, blur-to-pause
- [X] T062 Mobile on-screen buttons
- [ ] T063 Attack sprite animation for all 12 characters × 4 directions (attempted for Virgo, removed: timing did not match)
- [ ] T064 Cast sprite animation for all 12 characters × 4 directions
- [ ] T065 Sync hit timing and effects with the attack animation frames
- [ ] T066 Rebalance herb heal / Vitality charm for the new 500 HP base
- [ ] T067 In-game control hints to reduce the number of keys to remember
- [ ] T068 Final monster and boss sprites to replace code-drawn placeholders
