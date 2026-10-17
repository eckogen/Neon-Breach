from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "</dialog>\n<script>":
        "</dialog>\n<script src=\"assets/office-worker-mesh.js\"></script>\n<script>",
    "['*','City window wall','#55b9d4','▣'],['P'":
        "['*','City window wall','#55b9d4','▣'],['^','Office worker NPC','#d6b08c','♟'],['P'",
    "let chairs=[],debris=[],glassPanes=[];":
        "let chairs=[],debris=[],glassPanes=[],npcs=[];",
    "if(cabinetTiles.includes(tile)){let fx=x-Math.floor(x),fy=y-Math.floor(y);return fx>=.1625&&fx<=.8375&&fy>=.1625&&fy<=.8375}return":
        "if(cabinetTiles.includes(tile)){let fx=x-Math.floor(x),fy=y-Math.floor(y);return fx>=.1625&&fx<=.8375&&fy>=.1625&&fy<=.8375}if(tile==='^')return Math.hypot(x-Math.floor(x)-.5,y-Math.floor(y)-.5)<=.34;return",
    "[...wallTiles,'%','&','C','D','G','I','K','L','M','N','U','W','J','F'].includes(t)":
        "[...wallTiles,'%','&','C','D','G','I','K','L','M','N','U','W','J','F','^'].includes(t)",
    "[...wallTiles,'%','&','C','D','G','I','K','L','M','N','U','W','J','F'].includes(cell)":
        "[...wallTiles,'%','&','C','D','G','I','K','L','M','N','U','W','J','F','^'].includes(cell)",
    "{name:'Props',tiles:['C','K','U']},":
        "{name:'Props',tiles:['C','K','U']},\n{name:'Characters',tiles:['^']},",
    "['C','D','G','I','K','L','M','N','U','W','J','F','9'].includes(t)":
        "['C','D','G','I','K','L','M','N','U','W','J','F','9','^'].includes(t)",
    "doors=[];chairs=[];debris=[];glassPanes=[];":
        "doors=[];chairs=[];debris=[];glassPanes=[];npcs=[];",
    "if(chairTiles.includes(t))chairs.push({x:x+.5,z:y+.5,type:t,hp:60});":
        "if(chairTiles.includes(t))chairs.push({x:x+.5,z:y+.5,type:t,hp:60});if(t==='^')npcs.push({x:x+.5,z:y+.5,name:'Office worker'});",
    "function useDoor(){if(useLogicObject())return;if(useTether())return;":
        "function nearestNpc(){return npcs.map(n=>({n,dist:Math.hypot(n.x-player.x,n.z-player.y)})).filter(o=>o.dist<1.7&&lineClear(player.x,player.y,player.x+(o.n.x-player.x)*Math.max(0,1-.45/o.dist),player.y+(o.n.z-player.y)*Math.max(0,1-.45/o.dist))).sort((a,b)=>a.dist-b.dist)[0]?.n}\nfunction useNpc(){let n=nearestNpc();if(!n)return false;doorMessage=n.name+': The building is in lockdown. Stay alert.';doorMessageTime=4;sound(520,.08,'triangle',.018);return true}\nfunction useDoor(){if(useLogicObject())return;if(useNpc())return;if(useTether())return;",
    "function placeCabinet(out,x,z,tile){let angle=cabinetTiles.indexOf(tile)*Math.PI/2+Math.PI,c=Math.cos(angle),s=Math.sin(angle);for(let i=0;i<cabinetMesh.length;i+=9){let px=cabinetMesh[i]*.75,pz=cabinetMesh[i+2]*.75,nx=cabinetMesh[i+3],nz=cabinetMesh[i+5];out.push(x+px*c-pz*s,cabinetMesh[i+1]*.75,z+px*s+pz*c,nx*c-nz*s,cabinetMesh[i+4],nx*s+nz*c,cabinetMesh[i+6],cabinetMesh[i+7],cabinetMesh[i+8])}}":
        "function placeCabinet(out,x,z,tile){let angle=cabinetTiles.indexOf(tile)*Math.PI/2+Math.PI,c=Math.cos(angle),s=Math.sin(angle);for(let i=0;i<cabinetMesh.length;i+=9){let px=cabinetMesh[i]*.75,pz=cabinetMesh[i+2]*.75,nx=cabinetMesh[i+3],nz=cabinetMesh[i+5];out.push(x+px*c-pz*s,cabinetMesh[i+1]*.75,z+px*s+pz*c,nx*c-nz*s,cabinetMesh[i+4],nx*s+nz*c,cabinetMesh[i+6],cabinetMesh[i+7],cabinetMesh[i+8])}}\nfunction placeOfficeNpc(out,x,z){for(let i=0;i<officeNpcMesh.length;i+=9)out.push(x+officeNpcMesh[i],officeNpcMesh[i+1],z+officeNpcMesh[i+2],officeNpcMesh[i+3],officeNpcMesh[i+4],officeNpcMesh[i+5],officeNpcMesh[i+6],officeNpcMesh[i+7],officeNpcMesh[i+8])}",
    "if(chairTiles.includes(tile))placeChair(v,x+.5,y+.5,tile);if(wallTiles.includes(tile))":
        "if(chairTiles.includes(tile))placeChair(v,x+.5,y+.5,tile);if(tile==='^')placeOfficeNpc(v,x+.5,y+.5);if(wallTiles.includes(tile))",
    "for(let pane of glassPanes){if(pane.broken)continue;":
        "for(let npc of npcs){let d=rayBox(origin,dir,[npc.x-.3,0,npc.z-.3],[npc.x+.3,1.8,npc.z+.3]);if(d<dist){best=npc;kind='npc';dist=d}}for(let pane of glassPanes){if(pane.broken)continue;",
    "if(!(kind==='glass'&&glassTypes[best.type]?.indestructible))best.hp-=weaponStats[activeWeapon].damage;if(kind==='target')":
        "if(kind!=='npc'&&!(kind==='glass'&&glassTypes[best.type]?.indestructible))best.hp-=weaponStats[activeWeapon].damage;if(kind==='npc'){doorMessage=best.name+\": Don't shoot! I'm unarmed!\";doorMessageTime=3;sound(115,.12,'triangle',.025)}else if(kind==='target')",
    "let nearby=nearestDoor(),prompt=doorMessageTime>0?doorMessage:nearby?":
        "let nearby=nearestDoor(),nearbyNpc=nearestNpc(),prompt=doorMessageTime>0?doorMessage:nearby?",
    ":'';if(doorMessageTime===0&&nearestTether())prompt='[E] '":
        ":'';if(!prompt&&nearbyNpc)prompt='[E] Speak to '+nearbyNpc.name;if(!prompt&&doorMessageTime===0&&nearestTether())prompt='[E] '",
}

for old, new in replacements.items():
    count = source.count(old)
    expected = 1
    if count != expected:
        raise RuntimeError(f"Expected {expected} match(es), found {count}: {old[:120]}")
    source = source.replace(old, new)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
