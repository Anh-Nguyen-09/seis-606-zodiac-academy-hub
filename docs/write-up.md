# Astraeum Tower – Project 1 Write-up

**Student**: Anh Nguyen · **Course**: SEIS 606, Fall 2026 · **Repo**: https://github.com/Anh-Nguyen-09/seis-606-zodiac-academy-hub
**Play**: https://anh-nguyen-09.github.io/seis-606-zodiac-academy-hub/dungeon/

Astraeum Tower is a 2D pixel-art action dungeon crawler (a small action RPG with roguelite-style generated floors). The player picks one of 12 zodiac students from my own fantasy world, climbs a 15-floor tower, fights monsters and three bosses with a personal weapon and ice/fire magic, collects gold and items, and returns to a lobby that saves progress.

## 1. Status: what works, what partly works, what doesn't

**Works (the full core loop runs from start to finish):**

- Lobby, new game, choosing any of the 12 characters, Continue from a saved run, and a record board.
- 15 floors: floors 1–2 are hand-built (floor 1 uses my own PixelLab layout), the rest are generated and always checked so the exit can be reached. Bosses on floors 5, 10 and 15, and a win screen after floor 15.
- Combat: 12 different weapons, each with its own effect, ice and fire spells with a Steam Burst combo, dodge, shield and healing herbs.
- Six regular enemy types (slime, bat, spitter, brute, rock golem, jumping mushroom), three bosses, gold, chests, gems, a shrine shop and run upgrades.
- Automatic saving at the start of each floor.

**Partly works:**

- **Character action sprites.** The game direction is still on my original plan. The one part I have not finished is adding action sprites (attack and spell-casting poses) for the characters, because I have not yet been able to make sprites that look the way I want. Right now the characters use their walking sprite while the weapon and spell effects are drawn in code. I tried Virgo's attack animation, but at its original speed it was too slow and did not line up with when the hit lands, so I removed it for now.
- **Balance.** I raised the player's HP to 500, but herbs still heal 30 and the Vitality charm still adds 20, so healing now feels small and the game is easier than intended.
- **Mobile.** It is playable with on-screen buttons, but the buttons are cramped on a phone.

**Doesn't work yet / not built:**

- Cast and attack animations for 11 of the 12 characters (and the 12th was removed).
- Final sprites for monsters and bosses (they are drawn in code as placeholders).
- Progress inside a floor is not saved. Refreshing mid-floor restarts that floor.

## 2. Root causes

| Problem | Root cause |
| --- | --- |
| Missing action sprites | My own decision and an art bottleneck: I make every sprite with PixelLab and want them to match the chibi style of the walking sprites. Getting 12 characters × 4 directions × 2 actions (96 animations) to look right takes many tries. |
| Sprite timing felt wrong | A spec gap: my spec said what each attack should look like but never said how long an attack takes or on which frame the hit happens. The GIF ran at 0.2 s per frame (1.8 s for the whole attack), but the weapon cooldown is 0.37 s. |
| Too many keys | A spec decision: I added features one by one (shield, dodge, element swap, herbs) and each one got its own key. I never stepped back to design the controls as a whole. |
| Save crash found in testing | AI-generated code issue: the first save code trusted whatever was in localStorage. It only handled broken JSON, not valid JSON with the wrong values. The security probe found it and it is now fixed. |
| Healing balance | My own change (HP 100 → 500) without updating the related numbers. |
| Spec written after the code for the dungeon | Process: the walkable hub (feature 001) went through Spec Kit first, but the dungeon grew quickly from prompts and I wrote its spec afterwards to match what was built. |

## 3. Path forward (in priority order)

| # | Step | Effort |
| --- | --- | --- |
| 1 | **Finish the action sprites**: an attack and a cast animation for each of the 12 characters in 4 directions, using a fixed frame size and naming (`<character>_<action>_<direction>.gif`). | Large: about 3–5 weeks, because there are 96 animations and each needs several PixelLab tries |
| 2 | **Adjust the timing so it is smoother**: decide on a target length for each weapon (for example 0.3–0.5 s), cut each animation to the wind-up and strike frames, and make the hit and the slash effect happen on the strike frame. | Medium: about 1 week once the sprites exist (the code already supports per-character attack sprites) |
| 3 | **Rebalance for 500 HP**: scale herb healing, the Vitality charm and enemy damage, then playtest floors 1–5 again. | Small: 1–2 days |
| 4 | **Make the controls easier to learn**: a short tutorial on floor 1, key hints on the HUD and fewer keys. | Small–medium: 2–4 days |
| 5 | **Replace code-drawn monsters and bosses** with PixelLab sprites. | Large: 2–3 weeks |
| 6 | **Release clean-up**: remove the test hook from the public build, and optionally save progress within a floor. | Small: 1 day |

## 4. Reflection: what I would do differently

- **Spec first, every time.** I used Spec Kit for the hub but not for the dungeon. If I had written the dungeon spec first, I would have caught missing details such as attack timing and the full control layout before building.
- **Put numbers and timing in the spec.** Things like "the hit lands on frame 4, the whole attack lasts 0.4 s" or "the player can heal about 20 % of HP with one herb" are easy to write down and save a lot of back-and-forth later.
- **Make the art plan match the code earlier.** I should have decided the sprite size, frame count, speed and file naming before making sprites, so new art can be dropped in without fixing timing afterwards.
- **Smaller prompts and test after each one.** When I asked for many changes in one prompt it was harder to check each one. Smaller steps with a quick test after each worked better.
- **Test earlier with other people.** The usability test showed in a few minutes that there are too many keys. I would run that kind of test after the first playable floor, not at the end.
- **Ask for security and edge-case checks as part of each feature**, not only at the end. The save crash was easy to fix once found, but it existed for a week.

What surprised me most is that the AI could write all the spell, weapon and monster effects in code without any image assets. That let me keep a fully playable game while my own art is still in progress.
