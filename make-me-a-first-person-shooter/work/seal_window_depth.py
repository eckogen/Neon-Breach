from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

old = "let edgeX=x===0||x===world[0].length-1,sx=edgeX?.2:1,sz=edgeX?1:.2,frame=[.12,.18,.24],trim=[.15,.72,.78];box(v,x+.5,.33,z+.5,sx,.66,sz,frame);box(v,x+.5,2.26,z+.5,sx,.48,sz,frame);for(let side of [-.43,.43])box(v,x+.5+(edgeX?0:side),1.3,z+.5+(edgeX?side:0),edgeX?.2:.14,1.65,edgeX?.14:.2,frame);box(v,x+.5,.63,z+.5,sx+.025,.08,sz+.025,trim);box(v,x+.5,2.04,z+.5,sx+.025,.08,sz+.025,trim);"
new = "let edgeX=x===0||x===world[0].length-1,sx=edgeX?.2:1,sz=edgeX?1:.2,frame=[.12,.18,.24],trim=[.15,.72,.78];box(v,x+.5,.33,z+.5,1,.66,1,frame);box(v,x+.5,2.26,z+.5,1,.48,1,frame);for(let side of [-.43,.43])box(v,x+.5+(edgeX?0:side),1.3,z+.5+(edgeX?side:0),edgeX?1:.14,1.65,edgeX?.14:1,frame);box(v,x+.5,.63,z+.5,edgeX?1.025:sx+.025,.08,edgeX?sz+.025:1.025,trim);box(v,x+.5,2.04,z+.5,edgeX?1.025:sx+.025,.08,edgeX?sz+.025:1.025,trim);"

if source.count(old) != 1:
    raise RuntimeError(f"Expected one city-window frame definition, found {source.count(old)}")
source = source.replace(old, new, 1)
source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
