# Astraeum Dungeon

A 2D pixel-art dungeon prototype set in the world of the Astraeum magic academy. Pick one of 12 zodiac students, choose ice or fire magic, and fight through three floors to defeat the Dungeon Slime King.

This is a course project prototype and the first playable slice of a larger personal game.

## Play

Open `index.html` in any modern browser. Everything (sprites, tiles, code) is bundled into that one file, so no install or server is needed.

## Controls

| Key | Action |
| --- | --- |
| Arrows / WASD | Move (4 directions) |
| Space | Dodge: a quick dash with no damage taken. Costs stamina, which refills shortly after |
| L | Weapon attack (each character has their own weapon) |
| J | Cast spell |
| K | Burst (area attack, has a cooldown) |
| Q | Swap between ice and fire magic |
| U | Raise a shield that blocks all damage and bullets for 3 seconds (10 second cooldown) |
| E | Open chests, enter portals |
| H | Use a healing herb |
| P / Esc | Pause |

On mobile, use the on-screen buttons below the game.

## What's in the prototype

- **Characters:** 12 playable zodiac students (Aries to Pisces), each with 4-direction walking sprites and an idle pose.
- **Magic:** one shared spell set in two elements, swappable at any time with Q. Ice slows enemies; fire burns them over time. Hitting a slowed enemy with fire, or a burning enemy with ice, sets off a **Steam Burst** that damages everything nearby.
- **Weapons:** every character fights with a signature weapon: wide arcs (halberd, greatsword, sword, twin swords, twin axes, scythe), fast thrusts (rapier, spear, twin daggers, trident) or ranged throws (throwing knives, bow). Melee swings soft-aim at the nearest enemy, always connect with enemies right next to you, and cut through the boss's bullets.
- **Movement and defense:** a stamina-based dodge (dash through attacks and bullets) and a timed shield with an on-screen countdown.
- **Floors:** Floor 1 has slimes, Floor 2 adds bats, Floor 3 is the boss arena.
- **Boss:** the Dungeon Slime King jumps and slams with a warning circle, fires bullet rings, and enrages below half HP (denser volleys, summons slimes).
- **Loot:** chests and monster drops give minerals (Amethyst, Sapphire) and herbs (Healing Herb, Glowcap). A summary screen shows time, kills and items found.

## Tuning

Balance values (HP, damage, speed, cooldowns, Steam Burst) live in the `TUNE` object, and per-character weapon stats live in `WEAPONS`, near the top of the script in `index.html`.

## Credits

- **Character sprites:** created by Anh Nguyen with PixelLab.
- **Dungeon tiles and props:** [Pixel Art Top Down - Basic](https://docs.cainos.net/pixel-art-top-down-basic) by Cainos.
- **Monsters, boss, spell and weapon effects:** drawn in code as placeholders until final sprites are made.
- **Code:** built with AI-assisted development (Claude).
