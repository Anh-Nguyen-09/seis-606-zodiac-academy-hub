# SEIS 606 · Project 1 · Astraeum Tower

**Anh Nguyen · University of St. Thomas · Fall 2026**

A 2D pixel-art action dungeon crawler set in my own fantasy world, the Astraeum magic academy. Pick one of 12 zodiac students and climb a 15-floor tower with a boss every 5 floors.

## Links

| What | Link |
| --- | --- |
| ▶ **Play the game (live)** | https://anh-nguyen-09.github.io/seis-606-zodiac-academy-hub/dungeon/ |
| Academy town hub (first Spec Kit feature) | https://anh-nguyen-09.github.io/seis-606-zodiac-academy-hub/academy-town.html |
| How to play (controls, floors, bosses) | [dungeon/README.md](dungeon/README.md) |
| Spec Kit: spec, plan, tasks | [specs/002-astraeum-tower/](specs/002-astraeum-tower/) · [specs/001-walkable-hub/](specs/001-walkable-hub/) |
| Test log (all 5 categories) | [docs/test-log.md](docs/test-log.md) |
| Key AI prompts | [docs/key-prompts.md](docs/key-prompts.md) |
| Automated tests | [dungeon/tests/](dungeon/tests/) |
| Game source (code without embedded art) | [dungeon/source/](dungeon/source/) |

## Run it

1. **Online**: open the "Play the game" link above.
2. **From the repo**: download or clone the repo and open `dungeon/index.html` in Chrome, Edge, Firefox or Safari. No install or server needed. Everything is in that one file.

```bash
git clone https://github.com/Anh-Nguyen-09/seis-606-zodiac-academy-hub.git
cd seis-606-zodiac-academy-hub
open dungeon/index.html        # macOS  (Windows: start dungeon\index.html)
```

Quick start: **New game** → pick a character → **Start**. Move with arrows/WASD, **L** weapon, **J** spell, **K** burst, **Q** swap ice/fire, **Space** dodge, **U** shield, **E** interact, **H** herb, **P** pause.

## Run the tests (optional)

```bash
pip install playwright && python -m playwright install chromium
python dungeon/tests/test_floors_and_bosses.py
python dungeon/tests/test_shop_save_bosses.py
python dungeon/tests/test_weapons.py
python dungeon/tests/test_edge_and_security.py
```

## Repo map

```text
dungeon/index.html          the game (built, single file)
dungeon/README.md           how to play
dungeon/source/             game code template, sprite layout, hand-built maps
dungeon/tests/              Playwright test scripts
specs/001-walkable-hub/     Spec Kit artifacts for the academy hub
specs/002-astraeum-tower/   Spec Kit artifacts for the dungeon game
docs/                       test log, key prompts
academy-town.html           walkable academy hub (feature 001)
.specify/                   Spec Kit config, templates and constitution
```

## Known gaps (documented, not hidden)

- Attack and cast animations for the characters are not done yet (walking sprite + code-drawn effects for now).
- Healing (herb 30 HP) has not been rebalanced for the new 500 HP base.
- Progress inside a floor is not saved: refreshing restarts that floor.
- Monsters and bosses are drawn in code as placeholders.


## Credits

Character sprites, tileset, props, items and Floor 1 layout: Anh Nguyen (made with PixelLab). Code written with AI assistance (Claude). Monsters, bosses and effects are drawn in code.
