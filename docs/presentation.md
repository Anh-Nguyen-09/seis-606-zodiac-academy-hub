# Astraeum Tower – Presentation (5–7 min)

Slides and speaker notes. Total ≈ 6 minutes + questions.

---

## Slide 1 · What it is and who it's for (≈ 1 min)

**Astraeum Tower**
A 2D pixel-art **action dungeon crawler** (action RPG with roguelite-style floors)

- Pick 1 of 12 zodiac students, each with their own weapon
- Climb a 15-floor tower: generated floors, a boss every 5 floors
- Ice and fire magic, gold, shop, upgrades, save and continue
- Runs in any browser: one HTML file, no install

**Speaker notes**

- This game is a project I have wanted to make for a long time. The 12 zodiac characters and the Astraeum academy come from a fantasy story I have been building for years, and this class finally gave me the chance to start making it into a real game.
- It is for players who like short, replayable action games like *Soul Knight* or *Enter the Gungeon*, and for people who like collecting and switching between characters.
- All the characters, tiles and items are my own art, made with PixelLab.

---

## Slide 2 · Live demo (≈ 2–3 min)

**Live demo**
*(Backup: recorded run + screenshots in case the live demo fails)*

---

## Slide 3 · Most interesting testing finding (≈ 2 min)

**One saved file could break the whole game**

- Security probe: I edited the save in DevTools (localStorage)
- Broken JSON → the game ignored it. ✅
- Valid JSON with the wrong types (`floor: "<img…>"`, unknown character) → **lobby crashed** ❌
- Fix: a `loadSave()` check, which only accepts a known character, a floor from 1 to 15 and numbers in range
- Retested with the same probe: no crash, Continue is disabled

**Also surprising:** every spell, weapon slash and monster is drawn in code. No image assets needed.

**Speaker notes**

- The AI-written save code only protected against broken JSON. It trusted anything else. That is a good example of AI code that looks safe but only covers the obvious case.
- Changing gold to 99,999 still works. I kept that on purpose because it is a single-player game with no server. If I add an online leaderboard, that would need a server check.
- The other thing that surprised me: I expected to need sprite sheets for every effect, but the AI could write the ice bolts, fire bursts, sonic waves, ground slams and all 12 weapon effects in code. That kept the game fully playable while my own art is still in progress.
- Usability: my tester found it hard to remember all the keys (there are about 10). That is on my fix list.

---

## Slide 4 · Gaps and next steps (≈ 1 min)

**What's missing**

- Action sprites (attack and cast) for the 12 characters × 4 directions. I tried Virgo's, but the timing did not fit, so I removed it for now
- Healing balance after raising HP to 500
- Too many keys to remember
- Monsters and bosses are still drawn in code

**Next steps (in order)**

1. Finish the action sprites (largest job: 96 animations)
2. Adjust the timing so the hit lands on the strike frame: smoother and more responsive
3. Rebalance healing, add a floor-1 tutorial and key hints
4. Final monster and boss sprites

**Speaker notes**

- The direction of the game is still exactly on my plan. The only part not done is the action sprites, because I have not been able to make them look the way I want yet. That will take a good amount of time because there are so many characters.
- Lesson: put timing and numbers in the spec, for example how long an attack lasts and which frame hits.

---

## Question to ask a classmate

*"What was the hardest bug you found in your own testing, and was it in code the AI wrote or in your spec?"*
