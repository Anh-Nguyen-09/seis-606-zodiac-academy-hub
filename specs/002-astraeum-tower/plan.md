# Implementation Plan: Astraeum Tower

**Branch**: `002-astraeum-tower` | **Date**: 2026-10-14 | **Spec**: [spec.md](spec.md)

## Summary

A single-file HTML5 canvas game. All code, sprites, tiles and maps are bundled into `dungeon/index.html` so it runs by double-clicking the file or from GitHub Pages. A small Python build step embeds the PixelLab art as base64 data URIs into a hand-written template.

## Technical Context

- **Language**: JavaScript (ES2020) in one HTML file; Python 3 for the build script and tests.
- **Rendering**: HTML5 Canvas 2D, 32 px tiles, 60 fps fixed-step update loop, pixel art drawn at 1x with smoothing off.
- **Storage**: browser `localStorage` (`astraeum-tower-save`, `astraeum-tower-records`, `astraeum-dungeon-pick`).
- **Testing**: Playwright (Chromium) scripts in `dungeon/tests/` that drive the game through a small test hook (`window.__dungeon`).
- **Target**: desktop browsers (Chrome, Edge, Firefox, Safari); playable on mobile with on-screen buttons.
- **Constraints**: no server, no external libraries, no network calls except a Google Font.

## Architecture

| Part | What it does |
| --- | --- |
| Lobby / UI (HTML overlays) | New game, Continue, character select, record board, pause, shop, death and win screens |
| Map layer | Floor 1 = author's PixelLab layout, floor 2 handmade, boss floors fixed; others from `genMap` (rooms + MST corridors + nooks), checked with BFS so the exit is reachable |
| Renderer | Wang (dual-grid) tileset for walls/floor, props, darkness overlay with light sources (candles, spells, glows) |
| Player | 4-direction walk sprites, weapon (`WEAPONS` table), spells (`EL` ice/fire), dodge, shield, herbs |
| Enemies | `updateEnemies` state machines per type; bosses in `updateBoss` / `updateBatLord` |
| Loot and shop | pickups, chests, gold, `SHOP` and `SELL` tables |
| Save | `storeJSON` at floor start; `loadSave` validates the save before use |

## Project Structure

```text
dungeon/
├── index.html            # the built game (open this)
├── README.md             # how to play
├── source/
│   ├── game-template.html  # game code before the art is embedded
│   ├── char_layout.js      # sprite frame sizes and anchors
│   └── maps.json           # hand-built floors 1-3
└── tests/                # Playwright test scripts
specs/002-astraeum-tower/ # this spec, plan and tasks
docs/                     # test log, key prompts
```

## Key Decisions

- **One file** so the professor and classmates can run it with no setup.
- **Code-drawn monsters and effects** as placeholders, so the game is fully playable before every sprite is ready.
- **Seeded fixed maps** for floors 1–2 and boss floors so specific art placement stays where the author put it.
- **Data tables** (`TUNE`, `WEAPONS`, `BOSSES`, `SHOP`) so balance can change without touching logic.
