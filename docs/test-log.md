# Test Log – Astraeum Tower

**App**: `dungeon/index.html` (live: https://anh-nguyen-09.github.io/seis-606-zodiac-academy-hub/dungeon/)
**Tester**: Anh Nguyen (unless noted) · **Dates**: Oct 14 – Oct 21, 2026
**Environment**: Chrome (desktop) for manual play; Playwright + Chromium for automated runs (`dungeon/tests/`).
**Severity**: High = crash or blocks progress · Medium = wrong behaviour, workaround exists · Low = cosmetic or minor.

---

## 1. Functional testing

Does each feature in the spec ([specs/002-astraeum-tower/spec.md](../specs/002-astraeum-tower/spec.md)) behave as intended?

| ID | Feature tested | How | Result | Action |
| --- | --- | --- | --- | --- |
| F-01 | New game + character select (FR-002) | Clicked New game, picked each of the 12 cards, started | Correct sprite, weapon name and element for all 12 | Pass |
| F-02 | Weapons hit for all 12 characters (FR-002, FR-011) | `test_weapons.py`: spawn 3 dummies in a row, press L once per character | All 12 deal damage. Spear, rapier, halberd, scythe and trident reach the 2nd dummy | Pass |
| F-03 | Melee swings missed enemies standing close to the player | Manual play, enemy pressed against the character | **Fail** at first: arc check ignored very close enemies | Fixed: soft-aim + "always hit when adjacent" rule. Retested: pass |
| F-04 | Spells J / K and swap Q (FR-010) | Manual; cast fire on a frozen enemy | Bolt, burst, element swap and Steam Burst all trigger | Pass |
| F-05 | Generated floors always reachable (FR-005) | `test_floors_and_bosses.py`: 250 generated maps on floors 3–14, BFS from start to exit, every chest and enemy | 0 unreachable exits, 0 unreachable chests/enemies | Pass |
| F-06 | All 15 floors load (FR-004, FR-006) | Same script steps through floors 1–15 | Each floor loads; enemy HP and map size grow; new enemy types appear on schedule | Pass |
| F-07 | Bosses on F5 / F10 / F15 | Script wakes each boss, records attacks, damages it below 50 % | Slime King: jump + volley, enrages. Bat Lord: fan, ring, swoop, dash, summon. Slime Emperor: bullet rings | Pass |
| F-08 | Portals after a boss | Kill boss, check portals, enter lobby portal | Lobby + next-floor portals open; lobby portal saves at floor 6 and records floors 4–5 | Pass |
| F-09 | Win screen | Kill the F15 boss | Mode = `win` | Pass |
| F-10 | Shop buy / sell (FR-008) | `test_shop_save_bosses.py`: F4 shop, 300 gold, buy whetstone + vitality, sell gems | Gold 300 → 180, upgrades applied, max HP 500 → 520, gems sold | Pass |
| F-11 | Save and Continue (FR-009) | Reload page after reaching F6, press Continue | Resumes on F6 with the same gold, upgrades, HP and character | Pass |
| F-12 | Chests and loot (FR-007) | Manual: open chests, kill enemies | Gold, herbs, glowcaps and gems drop; bag counts update; gems combine into one slot | Pass |
| F-13 | Dodge, shield, herb | Manual | Dodge avoids damage and costs stamina; shield blocks bullets for 3 s; herb heals 30 HP | Pass |
| F-14 | New enemies (rock golem, jumping mushroom, bat sonic wave) | Spawned next to the player in a test | Golem telegraphs then slams; mushroom wakes and jumps; bats fire sonic waves; no errors | Pass |
| F-15 | Attack sprite animation (FR-012) | Added Virgo's PixelLab attack GIFs (4 directions), compared with the slash effect | Works, but the pose was too slow at the GIF's speed and did not line up with the hit | **Deferred**: sprite removed until the action sprites and timing are redone (task T063, T065) |

## 2. Edge cases and negative testing

| ID | What I tried | How | Result | Action |
| --- | --- | --- | --- | --- |
| E-01 | Empty state: no save | Cleared localStorage, opened lobby | "No saved run yet", Continue disabled | Pass |
| E-02 | Rapid key mashing | `test_edge_and_security.py` presses L, J, K, Q, U, Space, E, H 200 times as fast as possible | No errors, cooldowns hold, game stays in `play` | Pass |
| E-03 | Refresh in the middle of a floor | Reload mid-floor after picking up gold | Back to lobby; Continue restarts the floor from its saved start, so gold picked up on that floor is lost | Won't fix (by design: save at floor start). Documented in README |
| E-04 | Losing focus (alt-tab) | Fired `blur` | Game pauses | Pass |
| E-05 | Small screen | Resized to 420 px wide | Canvas scales to 382 px, no horizontal scroll, touch buttons shown | Pass (Low: buttons are cramped) |
| E-06 | Walking into walls / corners | Manual, every wall type | Player stops; earlier the head went into the wall top | Fixed with a 12 px wall-face collision band |
| E-07 | Item stuck in a wall nook | Manual on generated floors | Earlier some chests sat in unreachable nooks | Fixed: reachability check for chests and enemies (F-05) |
| E-08 | Dying | Took damage until HP 0 | Death screen: retry floor or go to lobby | Pass |
| E-09 | Opening the shop with 0 gold | Manual | Buy buttons are greyed out and cannot be clicked; Sell is disabled when the bag has no gems | Pass |
| E-10 | Bat sonic wave never fired | Spawned a bat next to the player | **Fail**: bats only fired when farther than 50 px, but bats always fly close | Fixed: removed the minimum distance. Retested: pass |
| E-11 | Loot flying out of a chest in a wall nook | Opened chests on floors 3–9 and launched 8 items in every direction from each chest (script) | **Fail**: 57 of 105 items landed inside the wall and could not be picked up (also seen in manual play) | Fixed: items bounce off walls while flying, and any item that still ends up in a wall is moved to the nearest floor tile. Retested: 0 of 102 stuck |

## 3. Usability testing

**Tester 1**: a classmate, first time playing, no help given.
**Task**: start a new game, clear floor 1, try the weapon and both magic types.

| Observation | Where they struggled | Severity | Action |
| --- | --- | --- | --- |
| Hard to remember all the function keys. There are 10 different keys (L, J, K, Q, U, Space, E, H, P, arrows) | Kept checking which key was the weapon and which was the spell; forgot the shield (U) and the herb (H) | Medium | Deferred: show a small key-hint bar on the HUD, and group keys (J/K/L for attacks next to each other) |

**Possible fix ideas**: a first-floor tutorial with prompts, key hints next to each HUD skill icon (already partly there: J, K, L, U letters on the icons), and fewer keys by merging the burst into a long-press of the spell key.

## 4. Security probing

All probes on my own app only. Script: `dungeon/tests/test_edge_and_security.py`.

| ID | Probe | How | Result | Severity | Action |
| --- | --- | --- | --- | --- | --- |
| S-01 | View page source for keys or secrets | Searched the built HTML for `key`, `token`, `secret`, `password`, and every URL | No keys or secrets. Only external URL is Google Fonts. All game data (maps, stats) is visible, which is normal for a client-side game | – | No action |
| S-02 | Edit saved state in DevTools | Changed `astraeum-tower-save` in localStorage to `gold: 99999, floor: 14` | Continue loads floor 14 with 99,999 gold. The save is trusted | Low (single-player, no server or leaderboard) | Won't fix for now. A future online leaderboard would need a server check |
| S-03 | Corrupt the save with bad JSON | Set the save to `{not json` and records to `<script>alert(1)</script>` | Lobby still loads; bad JSON is ignored | – | Pass |
| S-04 | **Valid JSON with wrong types** | Save = `{floor:'<img src=x onerror=alert(1)>', char:'<b>x</b>', hp:'abc', gold:-50}` | **Lobby crashed** (`Cannot read properties of undefined (reading 'idle')`); no script ran, but the game was stuck | **High** | **Fixed**: new `loadSave()` checks every field (known character, element, whole-number floor 1–15, numbers in range). Bad saves are ignored and Continue is disabled. Retested: no errors |
| S-05 | Change values in the DevTools console | Used the test hook `window.__dungeon` to set HP to 1e9 and jump to floor 15 | Works: the hook gives full control | Low | Deferred: remove or hide the test hook in a release build |
| S-06 | Script injection through names or text | Character names, weapon names and the save card only come from the game's own tables; the save card now only renders validated data | No user-typed text is shown anywhere | – | No action |

## 5. AI-assisted review

**Tool**: Google Gemini (different from Claude, which I used to build the game)
**Code reviewed**: `dungeon/source/game-template.html` (the game code without embedded art)

**Prompt used**:

> You are a QA and security tester. Review the code of this single-player browser game (HTML5 canvas + JavaScript, progress saved in localStorage, no server). Give me exactly 5 findings, most important first. For each finding: Finding, Where, How to reproduce, Severity. Focus on: saved data handling (localStorage), anything that could crash the game, cheating through DevTools, rapid key input, and performance in the game loop.

I re-ran every reproduction step Gemini gave (manually and with a Playwright script) before deciding.

| # | Finding from Gemini | Severity (Gemini) | Verified? | How I checked | Decision and why |
| --- | --- | --- | --- | --- | --- |
| 1 | Edited `astraeum-tower-records` (record with no `char`) is not validated and crashes the lobby | High | **Rejected** | Ran Gemini's exact command (`floors: {1: {clears:1, best:100}}`) and reloaded | No crash and no console error. The lobby loads and shows the record. The records are already checked when they load (added after probe S-04) |
| 2 | Debug hook `window.__dungeon` is exposed, allowing god mode and floor skips | Medium | **Verified** | Same as probe S-05: set HP and skipped floors from the console | Deferred. It is only a single-player game with no server, and the hook is what my automated tests use. Remove it from a release build |
| 3 | Pressing P / Esc rapidly together with action keys causes overlapping pause states | Medium | **Rejected** | Pressed P/Esc 40 times mixed with the attack key | Game ends in a correct state, no errors, no double menus |
| 4 | Bullets, rings and scorch marks pile up on a long boss fight (memory leak) | Medium | **Rejected** | Stayed on the floor-10 boss for 12 s with the boss attacking, counted the arrays every 2 s | Arrays stay small (bullets/rings/scorches go back to 0, particles 3–6) because every array is cleaned each frame |
| 5 | Tapping the on-screen H button uses two herbs | Low | **Rejected** | Tapped the H button once with 5 herbs | Herbs 5 → 4 and HP +30: only one herb is used |

**Takeaway**: 1 of 5 findings was real (the debug hook, which I had already found in my own probing). The other 4 sounded convincing and pointed at real function names, but did not happen when I ran them. Checking each finding by hand mattered.

---

## Automated test runs (latest)

| Script | What it covers | Latest result |
| --- | --- | --- |
| `test_floors_and_bosses.py` | 250 generated maps, floors 1–15, all bosses, portals | 0 bad maps, all floors and bosses OK, no JS errors* |
| `test_shop_save_bosses.py` | Shop, save/continue, lobby portal, Bat Lord, win | All checks pass, no JS errors |
| `test_weapons.py` | One attack per character against 3 dummies | All 12 weapons deal damage |
| `test_edge_and_security.py` | Empty state, key mashing, reload, edited/corrupt saves, blur, small screen | All pass after the S-04 fix |

\*The only console message is the Google Font failing to load inside the offline test sandbox, not a game error.

Run them with: `pip install playwright && python dungeon/tests/<script>.py`
