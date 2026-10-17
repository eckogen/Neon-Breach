from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")
old = "function nearestNpc(){return npcs.map(n=>({n,dist:Math.hypot(n.x-player.x,n.z-player.y)})).filter(o=>o.dist<1.7&&lineClear(player.x,player.y,o.n.x,o.n.z)).sort((a,b)=>a.dist-b.dist)[0]?.n}"
new = "function nearestNpc(){return npcs.map(n=>({n,dist:Math.hypot(n.x-player.x,n.z-player.y)})).filter(o=>o.dist<1.7&&lineClear(player.x,player.y,player.x+(o.n.x-player.x)*Math.max(0,1-.45/o.dist),player.y+(o.n.z-player.y)*Math.max(0,1-.45/o.dist))).sort((a,b)=>a.dist-b.dist)[0]?.n}"
if source.count(old) != 1:
    raise RuntimeError(f"Expected one NPC proximity query, found {source.count(old)}")
source = source.replace(old, new, 1)
source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
