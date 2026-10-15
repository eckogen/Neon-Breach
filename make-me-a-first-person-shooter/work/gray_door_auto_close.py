from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "d.open=true;world[Math.floor(d.y)][Math.floor(d.x)]='0';doorMessage=c.name":
        "d.open=true;d.closing=false;d.clearTime=0;world[Math.floor(d.y)][Math.floor(d.x)]='0';doorMessage=c.name",
    "function update(dt){updateWeaponMotion(dt);":
        "function updateDoors(dt){doors.forEach(d=>{if(d.type!=='O'){if(d.open)d.slide=Math.min(1,d.slide+dt*2.5);return}let occupied=Math.hypot(d.x-player.x,d.y-player.y)<1.25||enemies.some(e=>e.hp>0&&Math.hypot(d.x-e.x,d.y-e.y)<1);if(d.open){d.slide=Math.min(1,d.slide+dt*2.5);if(d.slide>=1){d.clearTime=occupied?0:(d.clearTime||0)+dt;if(d.clearTime>=.75){d.open=false;d.closing=true;d.clearTime=0}}}if(d.closing){if(occupied){d.open=true;d.closing=false;d.clearTime=0}else{d.slide=Math.max(0,d.slide-dt*2.5);if(d.slide===0){d.closing=false;world[Math.floor(d.y)][Math.floor(d.x)]='O';sound(170,.18,'triangle',.02)}}}})}\nfunction update(dt){updateWeaponMotion(dt);",
    "doorMessageTime=Math.max(0,doorMessageTime-dt);doors.forEach(d=>{if(d.open)d.slide=Math.min(1,d.slide+dt*2.5)});":
        "doorMessageTime=Math.max(0,doorMessageTime-dt);updateDoors(dt);",
    "if(door){door.open=true;world[Math.floor(door.y)][Math.floor(door.x)]='0'}let dx=node.x":
        "if(door){door.open=true;door.closing=false;door.clearTime=0;world[Math.floor(door.y)][Math.floor(door.x)]='0'}let dx=node.x",
    "if(door){door.open=true;world[Math.floor(door.y)][Math.floor(door.x)]='0';sound(200,.15,'triangle',.015)}":
        "if(door){door.open=true;door.closing=false;door.clearTime=0;world[Math.floor(door.y)][Math.floor(door.x)]='0';sound(200,.15,'triangle',.015)}",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
