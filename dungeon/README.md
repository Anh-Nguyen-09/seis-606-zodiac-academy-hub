# Astraeum Tower

A 2D pixel-art dungeon crawler set in the world of the Astraeum magic academy. Pick one of 12 zodiac students and climb a 15-floor tower. Each floor is harder than the last, and every fifth floor has a boss.

This is a course project prototype and the first playable slice of a larger personal game.

## Play

Open `index.html` in any modern browser. Everything (sprites, tiles, code) is bundled into that one file, so no install or server is needed. Progress is saved in the browser.

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
| E | Open chests, use the shop, enter portals |
| H | Use a healing herb |
| P / Esc / ⏸ button | Pause menu (resume, restart floor, return to lobby) |

On mobile, use the on-screen buttons below the game.

## The tower

- **15 floors, rising difficulty.** Floors 1–2 are hand-built. The other non-boss floors are generated fresh each time from rooms and corridors, and every layout is checked so the exit can always be reached. Enemy health, damage and speed scale with each floor, maps get bigger, and new enemies appear: bats from floor 3, purple spitter slimes from floor 6, giant brute slimes from floor 11.
- **Bosses every 5 floors.**
  - Floor 5, **Dungeon Slime King**: jump slams with a warning circle, bullet rings, and summoned slimes when enraged.
  - Floor 10, **Bat Lord**: aimed bullet fans, screech rings, and telegraphed swoops across the arena. Summons bats.
  - Floor 15, **Slime Emperor**: a harder Slime King with denser fire rings, an earlier enrage and spitter minions.
- **After a boss** two portals open. The gold one returns you to the lobby with your progress saved, and the purple one continues to the next floor.
- **Gold coins** drop from enemies, chests and bosses.
- **Shrine shop** on floors 4, 9 and 14 (right before each boss). Buy herbs, an elixir, and run upgrades: +max HP, +weapon damage, +spell damage, +stamina. You can also sell minerals and glowcaps for gold.
- **Lobby.** Continue your saved run or start a new one. A 15-floor record board shows which floors you have cleared, your best time on each and which character set it. Records are kept when you start a new game.
- **Saving.** The run saves automatically at the start of every floor. Dying lets you retry the floor or go back to the lobby.

## Combat

- **Magic:** one shared spell set in two elements, swappable at any time with Q. Ice slows enemies; fire burns them over time. Hitting a slowed enemy with fire, or a burning enemy with ice, sets off a **Steam Burst** that damages everything nearby.
- **Weapons:** every character fights with a signature weapon: wide arcs (halberd, greatsword, sword, twin swords, twin axes, scythe), fast thrusts (rapier, spear, twin daggers, trident) or ranged throws (throwing knives, bow). Melee swings soft-aim at the nearest enemy, always connect with enemies right next to you, and cut through enemy bullets.
- **Defense:** a stamina-based dodge (dash through attacks and bullets) and a timed shield with an on-screen countdown.

## Tuning

Balance values (HP, damage, speed, cooldowns, floor scaling, Steam Burst, dodge, shield) live in the `TUNE` object near the top of the script in `index.html`. Per-character weapon stats live in `WEAPONS`, bosses in `BOSSES`, and shop items and prices in `SHOP`.

## Credits

- **Character sprites:** created by Anh Nguyen with PixelLab.
- **Dungeon tiles and props:** [Pixel Art Top Down - Basic](https://docs.cainos.net/pixel-art-top-down-basic) by Cainos.
- **Monsters, bosses, spell and weapon effects:** drawn in code as placeholders until final sprites are made.
- **Code:** built with AI-assisted development (Claude).
