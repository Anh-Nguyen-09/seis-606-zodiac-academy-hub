# Game source

- `game-template.html`: the full game code (HTML, CSS, JavaScript) before the art is embedded. Placeholders `__CHARS__`, `__TEX__`, `__MAPS__` and `__LAYOUT__` are filled in by the build step with base64 PixelLab sprites, tiles and maps, which produces `../index.html`.
- `char_layout.js`: frame sizes and foot anchors for each character's sprites.
- `maps.json`: the hand-built floors (floor 1 from my PixelLab layout, floor 2, and the boss arena).

To read or review the code, use `game-template.html`. It is much smaller than the built `index.html` because it has no embedded images.
