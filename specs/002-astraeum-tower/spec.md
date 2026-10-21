# Feature Specification: Astraeum Tower (dungeon crawler)

**Feature Branch**: `002-astraeum-tower`
**Created**: 2026-10-14
**Status**: Implemented (baseline), action sprites pending
**Input**: User description: "Turn the Astraeum academy world into a playable 2D pixel dungeon crawler. The player picks one of the 12 zodiac students, fights through a tower of at least 15 floors with a boss every 5 floors, collects gold and items, can buy upgrades at a shrine, and returns to a lobby through a portal after each boss. Each character uses their own weapon and can swap between ice and fire magic while playing."

## User Scenarios & Testing

### User Story 1 - Pick a character and play a floor (Priority: P1)

The player opens the game, starts a new run, picks one of the 12 zodiac characters and walks a dungeon floor, fighting monsters with a weapon and magic until they reach the exit.

**Why this priority**: This is the core loop. Without it there is no game.

**Independent Test**: Open `dungeon/index.html`, click New game, pick any character, kill a monster with L/J/K and walk to the exit stairs.

**Acceptance Scenarios**:

1. **Given** the lobby, **When** the player clicks New game and picks a character, **Then** floor 1 loads with that character's sprite, weapon and starting element.
2. **Given** a monster in range, **When** the player presses L, **Then** the character's own weapon hits it (arc, thrust or thrown projectile, depending on the weapon).
3. **Given** the player presses Q, **Then** the magic swaps between ice and fire and the HUD shows the new element.
4. **Given** the player reaches the exit, **When** they press E, **Then** the next floor loads.

### User Story 2 - Climb the tower and beat bosses (Priority: P1)

The player climbs 15 floors that get harder. Every 5th floor is a boss lair. After a boss, two portals appear: one back to the lobby (progress saved) and one to the next floor.

**Independent Test**: Play (or use the test hook) to floor 5, defeat the Slime King, check both portals.

**Acceptance Scenarios**:

1. **Given** floors 3+ (non-boss), **Then** the layout is generated and the exit is always reachable.
2. **Given** floors 5, 10, 15, **Then** a boss appears with telegraphed attacks and enrages below 50% HP.
3. **Given** a boss is defeated, **Then** a lobby portal and a next-floor portal open.
4. **Given** floor 15's boss is defeated, **Then** the win screen appears.

### User Story 3 - Loot, gold and the shrine shop (Priority: P2)

Monsters and chests drop gold, healing herbs, glowcap mushrooms and gems. The shrine shop on floors 4, 9 and 14 sells herbs, an elixir and run upgrades, and buys gems and glowcaps.

**Acceptance Scenarios**:

1. **Given** a monster dies, **Then** it may drop gold and herbs/glowcaps.
2. **Given** a chest, **When** the player presses E, **Then** it opens and drops loot.
3. **Given** the shop, **When** the player buys an upgrade with enough gold, **Then** gold goes down and the upgrade applies.
4. **Given** gems in the bag, **When** the player clicks Sell, **Then** gems are removed and gold goes up by their value.

### User Story 4 - Save, continue and records (Priority: P2)

The run saves automatically at the start of every floor. The lobby offers Continue and shows a 15-floor record board (best time and character per floor).

**Acceptance Scenarios**:

1. **Given** a saved run, **When** the page is reloaded, **Then** Continue resumes at the saved floor with the saved HP, gold and bag.
2. **Given** no save (or an invalid save), **Then** Continue is disabled and the game does not crash.

### User Story 5 - Defensive moves (Priority: P3)

The player can dodge (Space, costs stamina), raise a shield (U, 3 s, 10 s cooldown) and use a healing herb (H).

### Edge Cases

- Rapid key presses must not crash the game or break cooldowns.
- Losing window focus pauses the game.
- Refreshing mid-floor returns to the lobby; Continue restarts that floor (progress inside a floor is not saved, by design).
- A save edited or corrupted in DevTools must not crash the lobby.

## Requirements

### Functional Requirements

- **FR-001**: The game MUST run by opening one HTML file, with no install or server.
- **FR-002**: The player MUST be able to choose any of the 12 zodiac characters, each with their own weapon.
- **FR-003**: Movement MUST use arrow keys or WASD; actions use L (weapon), J (spell), K (burst), Q (swap element), U (shield), Space (dodge), E (interact), H (herb), P/Esc (pause).
- **FR-004**: The tower MUST have 15 floors; floors 1–2 hand-built, other non-boss floors generated; a boss on floors 5, 10 and 15.
- **FR-005**: Generated floors MUST always have a reachable exit.
- **FR-006**: Difficulty (enemy HP, damage, speed, map size, enemy types) MUST scale with the floor.
- **FR-007**: Gold, herbs, glowcaps, gems and chests MUST be collectable; the bag shows herbs, glowcaps and a combined gem count.
- **FR-008**: A shrine shop MUST appear on floors 4, 9 and 14.
- **FR-009**: The run MUST auto-save at each floor start and the lobby MUST offer Continue and a record board.
- **FR-010**: Fire and ice MUST combine into a Steam Burst reaction.
- **FR-011**: Each weapon family MUST have a distinct visual effect (arc slash, thrust, thrown projectile).
- **FR-012** *(pending)*: Each character SHOULD have attack and cast sprite animations in 4 directions.

### Key Entities

- **Run**: character, element, floor, HP, gold, bag, upgrades, kills, time.
- **Floor**: grid map, enemies, pickups, chests, props, shop, exit/portals.
- **Enemy**: type (slime, bat, spitter, brute, golem, jumping mushroom, bosses), HP, damage, behaviour state.
- **Records**: per floor best time and character.

## Success Criteria

- **SC-001**: A new player can start a run and clear floor 1 in under 5 minutes.
- **SC-002**: 100% of generated floors have a reachable exit (checked on 250 generated maps).
- **SC-003**: All 15 floors and 3 bosses can be completed in one run.
- **SC-004**: No JavaScript errors during the automated test runs.

## Assumptions

- Desktop keyboard is the main input; mobile gets on-screen buttons.
- Character, tile, prop and item art is made by the author with PixelLab; monsters, bosses and effects are drawn in code until sprites exist.
