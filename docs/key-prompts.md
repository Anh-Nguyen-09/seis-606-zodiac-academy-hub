# Key Prompts

The game was built with Claude (Anthropic) as the coding assistant. Most prompts were written in Vietnamese. Below are the key ones, translated to English, in the order they shaped the game. The Spec Kit artifacts are in [`specs/`](../specs/).

## Spec Kit (feature 001, walkable hub)

- `/speckit.specify` "Build a walkable hub screen where the player moves a character with arrow keys or WASD in real time, bounded to the map. Walking near a building shows a popup with its name and a one-line description… The character cannot walk through buildings."
- `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` → `specs/001-walkable-hub/`

## Dungeon (feature 002, Astraeum Tower)

| # | Prompt (translated) | What it led to |
| --- | --- | --- |
| 1 | "Let the character swap spells while playing, and also attack with a weapon." | Q element swap, L weapon attack, `WEAPONS` table |
| 2 | "The weapon often misses and can't hit monsters that are right next to me, fix it. Add a shield with a countdown, and a short sprint with stamina that refills when you stop." | Soft-aim + close-range hit rule, shield (U), stamina |
| 3 | "Remove sprint, replace it with a dodge." / "Put dodge on Space." | Dodge with stamina on Space |
| 4 | "After beating a boss there should be a portal back to the lobby… at least 15 floors… a boss every 5 floors… a shrine to buy items… gold coins." | 15-floor tower, bosses, portals, shop, gold, save/continue |
| 5 | "Add walls, choose which piece goes where." (with my PixelLab wall assets) | Wall rendering with my art |
| 6 | "Use this as the floor 1 map." / "Use the tileset like in that file, drop the old set." | My Damp Corridors layout and wang tileset |
| 7 | "Move the single candles into wall corners as small light sources, alternate with cobwebs, put items or chests in the small wall nooks." | Decoration and alcove placement rules |
| 8 | "Remove mushrooms, make the gems smaller." → "Keep the mushrooms, group all gems under the amethyst slot." | Bag HUD with a combined gem slot |
| 9 | "Add a rock golem and a jumping mushroom to the monster list… I don't have assets. Bats attack with a sonic wave from the mouth." | Code-drawn golem and mushroom, bat sonic attack |
| 10 | "Give Aries a halberd, Taurus a greatsword, Gemini a rapier…" (all 12) | Final weapon lineup |
| 11 | "Adjust the effects for each character to match their weapon type." | Per-weapon attack effects |
| 12 | "Add this for Virgo." (attack GIFs) → "Keep the original speed" → "Only the pull-back and slash" → "2x speed" → "Remove that sprite, no time to fix it." | Attack-sprite support in code; Virgo's sprite removed for now |
| 13 | "Raise character HP to 500." | `TUNE.playerHp = 500` |

## Testing prompts

- "Help me prepare everything this requirements file asks for… test log with all categories…" → test scripts in `dungeon/tests/`, [test-log.md](test-log.md)
- AI review prompt for a second tool: see section 5 of the [test log](test-log.md).
