from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace("states:{}};$('levelHeading')", "states:Object.create(null)};$('levelHeading')",1)
s=s.replace("if(!w||!Array.isArray(w.slots)||!Array.isArray(w.links)||w.slots.length===0)", "if(!w||!Array.isArray(w.slots)||!Array.isArray(w.links)||w.slots.length===0)",1)
# Draft worlds may be saved before their connections are complete.
idx=s.index('function refreshWorldLab()');s=s[:idx]+'''function worldDraftValid(w){if(!w||!Array.isArray(w.slots)||!Array.isArray(w.links)||w.slots.length>64)return false;let ids=new Set(),cells=new Set();for(let s of w.slots){if(!s||typeof s.id!=='string'||ids.has(s.id)||!Number.isInteger(s.x)||!Number.isInteger(s.y)||s.x<0||s.y<0||s.x>7||s.y>7||cells.has(s.x+','+s.y)||!mapShape(s.map))return false;ids.add(s.id);cells.add(s.x+','+s.y)}return w.links.every(l=>l&&[l.a,l.b].every(e=>e&&ids.has(e.slot)&&Number.isInteger(e.x)&&Number.isInteger(e.y)&&w.slots.find(s=>s.id===e.slot).map.grid[e.y]?.[e.x]==='Z'))}
''' +s[idx:]
s=s.replace("let w=JSON.parse(raw),err=worldValidation(w);if(err)return toast(err);worldDesign=w;", "let w=JSON.parse(raw);if(!worldDraftValid(w))return toast('Invalid world data.');worldDesign=w;",1)
s=s.replace("let w=JSON.parse($('worldJSON').value),err=worldValidation(w);if(err)return toast(err);worldDesign=w;", "let w=JSON.parse($('worldJSON').value);if(!worldDraftValid(w))return toast('Invalid world data.');worldDesign=w;",1)
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s+='''
## World Lab and level tethers

1. Place purple Level tether tiles in Level Lab. Save each level in the map library.
2. Open World Lab. Choose a saved level and click an empty board cell to place a copy. Select neighboring pieces to connect.
3. Select a piece, choose one of its tether coordinates, choose a neighboring piece's tether, and click Connect tethers. Connections work in both directions, and each tether has one partner.
4. Set a starting piece and click Play world. Press E near a purple tether to travel to its paired level.

Health, ammunition, keycards, cleared drones, opened doors, broken glass and destroyed chairs persist across visits during that run. Debris is cleared during transfers. Clear all drones across every piece, then use any extraction beacon. Restarting the world resets the run.

The board is an 8 × 8 layout of level pieces. Travel occurs through tethers between discrete 3D regions. Pieces must share a board edge to connect, and the whole world must be connected before it can be played.

Save world in browser keeps the layout, connections and embedded level snapshots, including incomplete drafts. Export world JSON produces a portable file; paste it into Import world JSON to load it. Saved maps are copied when placed, so editing the library does not silently change world pieces. Select a piece and use Replace with chosen saved level to update its map snapshot. Edit piece in Level Lab opens a copy for editing; save it in the map library and then replace the piece. Load two-piece demo provides a ready-to-play example.
''';p.write_text(s,encoding='utf-8')
