from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "['z','Neon lancet','#65b9d8','✧'],['P'":
        "['z','Neon lancet','#65b9d8','✧'],['*','City window wall','#55b9d4','▣'],['P'",
    "const wallTiles=['1','2','q','t','u','v','w','z'];":
        "const wallTiles=['1','2','q','t','u','v','w','z','*'];",
    "Borders: walls only": "Borders: walls and city windows only",
    "Border cells accept full-height wall objects only.":
        "Border cells accept full-height walls and sealed city windows only.",
    "function perspective(aspect){let f=1/Math.tan((60-18*weaponMotion.ads)*Math.PI/360),n=.035,far=60;":
        "function perspective(aspect){let f=1/Math.tan((60-18*weaponMotion.ads)*Math.PI/360),n=.035,far=180;",
    "function buildWall(v,x,z,t){let bases={'1':[.29,.38,.49],'2':[.055,.35,.39],q:[.72,.7,.61],t:[.31,.17,.085],u:[.27,.33,.38],v:[.22,.25,.27],w:[.075,.08,.095],z:[.055,.085,.13]};box(v,x+.5,1.25,z+.5,1,2.5,1,bases[t]);":
        "function buildWall(v,x,z,t){let bases={'1':[.29,.38,.49],'2':[.055,.35,.39],q:[.72,.7,.61],t:[.31,.17,.085],u:[.27,.33,.38],v:[.22,.25,.27],w:[.075,.08,.095],z:[.055,.085,.13],'*':[.08,.12,.17]};if(t==='*'){let edgeX=x===0||x===world[0].length-1,sx=edgeX?.2:1,sz=edgeX?1:.2,frame=[.12,.18,.24],trim=[.15,.72,.78];box(v,x+.5,.29,z+.5,sx,.58,sz,frame);box(v,x+.5,2.31,z+.5,sx,.38,sz,frame);for(let side of [-.43,.43])box(v,x+.5+(edgeX?0:side),1.3,z+.5+(edgeX?side:0),edgeX?.2:.14,1.65,edgeX?.14:.2,frame);box(v,x+.5,.62,z+.5,sx+.025,.055,sz+.025,trim);box(v,x+.5,2.08,z+.5,sx+.025,.055,sz+.025,trim);return}box(v,x+.5,1.25,z+.5,1,2.5,1,bases[t]);",
    "function rebuildGeometry(){let v=[];":
        "function buildCityscape(v){let w=world[0].length,h=world.length,cx=w/2,cz=h/2,span=Math.max(w,h)+120,sky=[.012,.022,.06];box(v,cx,24,cz-62,span,48,.5,sky);box(v,cx,24,cz+h+62,span,48,.5,sky);box(v,-62,24,cz,.5,48,span,sky);box(v,w+62,24,cz,.5,48,span,sky);box(v,cx,-.65,cz,w+150,.5,h+150,[.018,.025,.045]);let addBuilding=(x,z,bw,bd,bh,seed)=>{let body=seed%3===0?[.035,.055,.09]:seed%3===1?[.055,.045,.085]:[.035,.075,.085],glow=seed%2?[.12,.7,.82]:[.88,.3,.62];box(v,x,bh/2-.35,z,bw,bh,bd,body);box(v,x,bh-.28,z,bw+.12,.16,bd+.12,[.08,.13,.2]);if(seed%4===0)box(v,x,bh+.7,z,.08,1.8,.08,glow);for(let y=.8;y<bh-.5;y+=1.15){for(let side of [-1,1])box(v,x+side*(bw/2+.006),y,z,.018,.24,bd*.62,glow);box(v,x,y,z+bd/2+.006,bw*.62,.24,.018,glow)}};for(let side=0;side<4;side++)for(let i=0;i<18;i++){let seed=i+side*23,bw=2.2+(seed%4)*.55,bd=2+(seed*3%5)*.4,bh=5+(seed*7%15),u=(i+.5)/18;if(side<2)addBuilding(-8+u*(w+16),side?h+9+(i%3)*4:-9-(i%3)*4,bw,bd,bh,seed);else addBuilding(side===2?-9-(i%3)*4:w+9+(i%3)*4,-8+u*(h+16),bd,bw,bh,seed)}}\nfunction rebuildGeometry(){let v=[];buildCityscape(v);",
    "let transparentPanes=glassPanes.filter(p=>!p.broken).map(p=>{":
        "let boundaryWindows=[];world.forEach((row,z)=>row.forEach((tile,x)=>{if(tile!=='*')return;let edgeX=x===0||x===world[0].length-1,mesh=[];box(mesh,x+.5,1.34,z+.5,edgeX?.035:.86,1.4,edgeX?.86:.035,[.26,.72,.88]);boundaryWindows.push({x:x+.5,y:1.34,z:z+.5,mesh,alpha:.2,pane:true})}));let transparentPanes=glassPanes.filter(p=>!p.broken).map(p=>{",
    "for(let p of [...debris,...transparentPanes].sort":
        "for(let p of [...debris,...transparentPanes,...boundaryWindows].sort",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
