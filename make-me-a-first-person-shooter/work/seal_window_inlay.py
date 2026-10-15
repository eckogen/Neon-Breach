from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "box(v,x+.5,.29,z+.5,sx,.58,sz,frame);box(v,x+.5,2.31,z+.5,sx,.38,sz,frame);":
        "box(v,x+.5,.33,z+.5,sx,.66,sz,frame);box(v,x+.5,2.26,z+.5,sx,.48,sz,frame);",
    "box(v,x+.5,.62,z+.5,sx+.025,.055,sz+.025,trim);box(v,x+.5,2.08,z+.5,sx+.025,.055,sz+.025,trim);":
        "box(v,x+.5,.63,z+.5,sx+.025,.08,sz+.025,trim);box(v,x+.5,2.04,z+.5,sx+.025,.08,sz+.025,trim);",
    "box(mesh,x+.5,1.34,z+.5,edgeX?.035:.86,1.4,edgeX?.86:.035,[.26,.72,.88]);":
        "box(mesh,x+.5,1.34,z+.5,edgeX?.045:.88,1.52,edgeX?.88:.045,[.26,.72,.88]);",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
