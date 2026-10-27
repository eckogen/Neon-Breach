# Neon Breach

Open index.html in a desktop browser (Chrome, Edge, or Firefox). Everything is contained in that one file; no download, build step, server, or internet connection is required.

## Play

Click Deploy. Clear the six security drones and walk into the green extraction beacon.

- WASD: move. Shift: sprint.
- Mouse: look left/right and up/down. Left click: fire. If mouse capture is unavailable, move the cursor over the game to aim; leave and re-enter to reposition the cursor.
- Arrow left/right: turn. F: fire (also works when mouse capture is unavailable). Space: jump.
- R: reload. Escape: pause and release the mouse.
- Medkits restore 35 health. Ammo crates add 48 rounds.
- The radar shows walls, remaining drones, and the exit.

## Level Lab

Choose a tile and click or drag across the grid. Right-click erases. The perimeter stays enclosed. Placing a spawn or extraction moves the existing one, so there is always at most one of each.

Paint walls, drones, medkits, ammo crates, and an extraction. Name your map and click Play this map. Validation checks the spawn, exit, boundaries, and paths to drones and extraction.

The Load a map dropdown switches between The Relay and any saved maps. Save in browser updates the selected saved map or creates a new entry. Save as new map creates a separate copy. Maps are stored in this browser's local storage; an older single-map save is migrated automatically. Switching with unsaved edits asks before discarding them. Incomplete draft maps can also be saved. Export JSON downloads a portable map. To import, open the JSON file in a text editor, copy its contents, and paste into Import JSON. Use Export for durable backups: browser storage depends on browser settings and the file's location.

Desktop keyboard and mouse are required. This is a single-player WebGL 3D shooter with a tile editor supporting arenas up to 80 by 80 tiles.

## Colored doors and keycards

Collect red, blue, or yellow keycards by walking over them. Press E near a door to open it with its matching card. Cards are reusable for all doors of that color. Locked doors block movement and shots. Cards reset when you restart. The HUD shows collected cards and nearby door prompts.

The editor includes all three door and keycard colors. Validation follows keycard progression and rejects cards or mission targets trapped behind doors that cannot be unlocked. The Relay includes sample doors and cards; restore it in Level Lab to load the updated layout.

Drone accuracy starts at 10% and rises to 70% over six seconds of uninterrupted line of sight. Breaking sight or moving beyond detection range resets tracking. Standing still adds 10 percentage points (up to 80%); sprinting while moving subtracts 10 (down to 0%). Holding sprint against a wall counts as stationary.

## Voxel chair asset

Choose Voxel chair in Level Lab, select its facing direction, and paint tiles. Right-click erases. Chairs use the supplied voxChair.glb mesh and colors, scaled to 1.15 meters tall. Chair tiles block movement and fire and are included in map save, export, and import. Keep walkways clear. The mesh is embedded in index.html for offline use; the original asset is preserved in assets/voxChair.glb.

Chairs are destructible: two rifle hits shatter them into pieces of the original model. Fragments tumble, bounce off floors and walls, remain for 2.5 seconds, then fade out over four seconds. Destroying a chair clears its blocked tile for the current mission; restarting restores the editor layout. Debris is cosmetic and does not block movement.

Drones that survive a rifle hit enter evasive mode for three seconds. They strafe faster, reverse direction, retreat at close range, and bob vertically; their lights turn orange. Another hit refreshes evasive mode. Destroyed drones break into 14 body and rotor components with the same bouncing, tumbling physics and gradual fade as chair debris.

## Glass panes

Level Lab includes Glass pane | and Glass pane — for the two orientations. Panes are transparent, block walking and bullets, and shatter from a single rifle shot or when sprinting through them. Sprinting through each intact pane costs 10 health once. A shot used to shatter glass does not continue into a target behind it. Glass shards tumble, bounce and fade away. Breaking panes affects the current mission only; restarting restores them.

Gray doors can be placed in Level Lab and opened with E. They require no keycard and block movement and shots until activated. They use the same opening animation and reset on mission restart.
After opening, gray doors wait until the doorway is clear, then close automatically behind the player. A closing door reverses if the player or a drone enters its doorway. Keyed doors remain open.

## File cabinet asset

Choose File cabinet in Level Lab and select a direction under Prop Facing. The supplied FileCabinet.glb mesh and colors are embedded in the game at its 1.35-meter height (75% scale). Cabinets provide solid cover, block movement, and are included in saved and exported maps. Right-click to erase. The original GLB is preserved in assets/FileCabinet.glb.

## World Lab and level tethers

1. Place purple Level tether tiles in Level Lab. Save each level in the map library.
2. Open World Lab. Choose a saved level and click an empty board cell to place a copy. Select neighboring pieces to connect.
3. Select a piece, choose one of its tether coordinates, choose a neighboring piece's tether, and click Connect tethers. Connections work in both directions, and each tether has one partner.
4. Set a starting piece and click Play world. Press E near a purple tether to travel to its paired level.

Health, ammunition, gold/silver/platinum keycards, cleared drones, opened doors, broken glass and destroyed chairs persist across visits during that run. Debris is cleared during transfers. Clear all drones across every piece, then use any extraction beacon. Restarting the world resets the run.

The board is an 8 × 8 layout of level pieces. Travel occurs through tethers between discrete 3D regions. Pieces must share a board edge to connect, and the whole world must be connected before it can be played.

Save world in browser keeps the layout, connections and embedded level snapshots, including incomplete drafts. Export world JSON produces a portable file; paste it into Import world JSON to load it. Saved maps are copied when placed, so editing the library does not silently change world pieces. Select a piece and use Replace with chosen saved level to update its map snapshot. Edit piece in Level Lab opens a copy for editing; save it in the map library and then replace the piece. Load two-piece demo provides a ready-to-play example.

## Crouching, crawling and crawl shafts

Hold Q to crouch. Press C to toggle crawling. Crouching lowers the camera and moves at 1.5 meters/second; crawling lowers it further and moves at 0.85 meters/second. Standing moves at 2.7, or 4.1 while sprinting. Jumping and sprinting require standing.

Level Lab includes Crawl shaft ↔ and Crawl shaft ↕ tiles. Paint aligned runs to build low tunnels. Their 0.55-meter clearance requires crawling; standing players, crouching players and drones cannot enter. Sidewalls prevent lateral entry, and the roof provides cover. Releasing crawl inside a shaft keeps you low until you exit, then you stand automatically. Shafts persist in saved maps and world pieces.

Levels require exactly one player spawn and at least one tether or extraction point. Tether-only levels can be used as intermediate regions in World Lab. Every placed tether and extraction must be reachable.

Hold the right mouse button to aim down the rifle's iron sights. The rifle centers, the field of view narrows, mouse sensitivity and sway decrease, and the crosshair fades. Release to return to normal aiming. Shots kick the weapon backward and lift the camera; recoil recovers smoothly and is reduced while aiming. Reloading lowers the sights.

## Arcade cabinet

Choose Arcade cabinet in Level Lab and select a direction under Prop Facing. The supplied mesh and colors are embedded for offline play, scaled to 85% to fit one editor tile (1.53 meters tall). Arcade cabinets block movement and shots and persist in saved maps and world pieces. The original asset is preserved in assets/ArcadeCabinet.glb.

Door orientation considers neighboring walls, glass panes, and all door colors. Doors span the direction with more supporting neighbors, so mixed partitions and rows of doors align automatically. With equal support, they keep the default orientation.

Gold, silver and platinum doors have matching metallic keys. These three keys persist when traveling between levels in a world. Red, blue and yellow keys are cleared on each transfer; their pickups become collectible again when returning to that level. Previously opened doors stay open. All keys reset on mission/world restart. World validation follows metallic-key progression across linked levels, so a key in one region can unlock a door in another.

## Pistol pickup

Place Pistol pickup in Level Lab. Walk over it to collect and equip the pistol. Press 1 for the rifle or 2 for the pistol. The pistol has a 12-round magazine, 36 starting reserve rounds, 20 damage per shot and a slower firing cadence. R reloads, and holding right mouse aims down the sights. Weapons have separate ammunition and carry across level tethers. Duplicate pistol pickups add 24 pistol reserve rounds. Restarting resets ownership.

## Assault drone

Place Assault drone in Level Lab for a tougher encounter. It has 90 health, moves at 2 meters/second, detects players within 14 meters, and fires every 0.6 seconds for 12 damage on a hit. It closes to 1.1 meters, dodges faster after being hit, and breaks into 16 physics pieces when destroyed. It follows the same visibility-based accuracy rules as the security drone.

## Tactical drone

Place Tactical drone in Level Lab for a smarter opponent. Its blue sensor mast distinguishes it from other drones. It has 75 health, follows routes around obstacles, picks lateral firing positions, seeks cover when wounded or hit, and can open gray doors on its route. It cannot unlock keyed doors or enter crawl shafts. It remembers your last observed position for six seconds after losing sight, then stops searching until it sees you or is hit again. It uses the existing visibility-based accuracy rules, fires every 0.9 seconds, and deals 10 damage per hit. Destruction produces fading physics debris.

Level Lab includes a 0.65-meter Half wall for low cover, a four-way Crawl junction, and four Crawl bend orientations (N/E, E/S, S/W, W/N). Half walls block walking and low shots but can be jumped over and stood on. Junctions and bends have the same crawl-only clearance as straight shafts. Map and world validation follows each piece's open edges.

Crawl T-junctions are available in four orientations: N/E/W, N/E/S, E/S/W, and N/S/W. Each has three open paths and one blocked side, with crawl-only clearance.

The build palette is organized into Structure, Crawl shafts, Doors & keys, Props, Enemies, and Mission & gear tabs. Switching categories selects the first object in that category; the selected brush is shown above the object list.

The Walls tab includes office plaster and walnut panels, industrial steel and hazard bulkheads, and cybergothic obsidian reliquaries and neon lancet panels. Each is solid full-height cover and supports automatic door orientation.

Cybergothic walls use pointed metal frames: Obsidian reliquary has warm brass trim and amber inset lights; Neon lancet has divided cyan/violet panels. Frame and panel surfaces are separated in depth.

Choose any width/height combination of 40, 60, and 80 tiles in the New map size selector, then click New empty map. Existing 20/30/40-tile maps remain compatible and retain their dimensions. Rectangular and large maps work with save/load, JSON and World Lab. Border cells can be repainted using any full-height wall in the Walls tab, but cannot be erased or replaced with half walls, doors, glass, or props.

Use the −, Reset zoom, and + controls above the Level Lab grid to zoom from 50% to 300% in 25% steps. You can also hold Ctrl (or Command on macOS) while using the mouse wheel over the map. Enlarged maps remain inside a scrollable editor viewport. Each zoom step redraws the grid and object icons at the new resolution so labels and symbols stay sharp.

Hazards tab: Sweeping laser ↔ spans east/west walls and slides north/south; Sweeping laser ↕ spans north/south walls and slides east/west. Place in a clear corridor with full-height walls on both beam ends. Emitters sweep the continuous matching corridor at 1.2 m/s, reversing at its ends, at 0.95 m height. Contact deals 15 damage with a 0.75-second cooldown. Crouch/crawl underneath or jump over. Obstructed placements without two wall anchors do not activate. Laser motion persists when revisiting a World Lab region.

New map sizes support every width/height combination of 40, 60, and 80 tiles: nine presets from 40 × 40 through 80 × 80.

## Cityscape and boundary windows

Every level is surrounded by a procedural nighttime city with lit 3D skyscrapers against a deep-blue cityscape skybox. The skyline sits outside the playable grid and is visual only.

Choose City window wall from the Walls tab and paint it over a perimeter wall. These sealed floor-to-ceiling windows expose the skyline while continuing to block movement, bullets, and enemy sight. City windows are restricted to the outer boundary and cannot be placed inside the level.

## Office worker NPC

Choose Office worker NPC from the Characters tab in Level Lab and paint a civilian into the level. The supplied 1.8-meter character mesh and texture are converted into the native WebGL renderer while the original GLB and animation bundle remain under `outputs/assets/male-office-worker`. Office workers block movement, are non-combatants, and stop bullets without taking damage. Press E nearby to speak with them.


## Objectives and enemy patrols

Open the separate **Objectives** and **Patrol routes** collapsible sections in the right Level Lab panel. Place Objective switches, Data terminals, and Sabotage targets from Mission & gear. Select an object and rename its ID (letters/numbers/hyphens); press E near switches/terminals, and shoot sabotage targets. Coordinates in rules are zero-based editor cells, X,Y. Enemy spawns can also be named.

Create an objective with a title, AND/OR/ordered conditions, and actions, one per line. Conditions: `activate:power`, `kill:core`, `key:g`, `flag:powered`, `allDrones`, `timer:30`, `reach:8,5`. Actions: `open:10,5`, `disableLasers`, `extraction`, `flag:powered`, `route:8,8:route-ID`, or `alarm:route-ID` to redirect all enemies. Route IDs appear as the value in exported JSON. Ordered activation/destruction conditions must occur in the specified order. Optional objectives do not block extraction. Maps with objectives require all mandatory objectives rather than all drone kills; an extraction action, when present, must also fire. Maps without rules retain the original drone-clearing objective.

To patrol: choose a route or enter a new route name, select Loop, Back and forth, or Guard, and click Place nodes on map. Click floor cells to append nodes with the chosen wait duration. Click Finish nodes, then select an enemy and Assign selected route. Enemies follow walkable paths between nodes, wait and rotate at stops, interrupt patrols to engage, investigate nearby gunfire for four seconds, and return after losing the player (tactical drones first finish their last-seen search). Guard routes hold their first node. Gray doors can be opened during patrols; locked doors remain barriers. Objective actions can change routes or rally enemies to a route.

Rules, names, nodes and assignments are included in map saves/exports and World Lab snapshots. Mission flags persist between linked regions; each region remembers its completed objectives, used interactions and patrol state. Restart clears mission progress.

Patrol nodes default to a 0.25-second wait. Existing nodes retain their authored waits. Drones finish the approach inside the goal cell, discard stale paths at node changes, and skip unreachable nodes on looping/reversing routes. Guard routes hold position when blocked.

Objective switches and sabotage targets can use any current prop mesh: Voxel chair, File cabinet, or Arcade cabinet. Select the named object in Objectives, choose its appearance and facing, then Apply appearance. Switches still activate with E; targets still take damage and satisfy their named destruction rules. Appearance settings persist in map JSON and linked-region snapshots.

Glass tab: yellow Reinforced panes have 120 health (four rifle hits), orange Ballistic panes have 300 (ten rifle hits), and gray Titan panes cannot be destroyed. All come in two orientations. These upgraded panes resist sprinting; only ordinary glass can be rammed through. Intact panes block bullets and drones flank around them. Titan panes are permanent barriers in map/world route validation.

The city-window background uses three supplied GLB building meshes with their base-color textures. Browser-ready geometry and 512px textures are bundled in assets/skyline-meshes.js; mesh buffers are uploaded once and reused around all four sides of each map. Source node orientation is preserved and building heights vary across the skyline.

The skyline and exterior ground sit 24 meters below the level. The exterior remains below the level; doubled skyscrapers can extend above the standing eye line.

A 128-segment panoramic cylinder surrounds each level behind the 3D skyline, using the supplied skyline-panorama.png texture. The cylinder scales with map dimensions and repeats the texture six times around its circumference. It is visual scenery only.

A second skyline cylinder sits 60 meters inside the outer panorama. It uses skyline-inner.png with source alpha transparency, five texture repetitions, and a staggered seam for layered depth. Both layers render behind the 3D city and game geometry.

Skyline cylinder radii use the map half-diagonal plus 85m for the outer layer and 25m for the inner layer.

The three skyline meshes use twice their original scale in all dimensions (24–48m tall), with bases anchored at -24m. Panorama cylinders retain their current size.
