from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "if((x===0||y===0||x===w-1||y===h-1)&&!wallTiles.includes(t))return;":
        "let boundary=x===0||y===0||x===w-1||y===h-1;if(boundary&&!wallTiles.includes(t)||t==='*'&&!boundary)return;",
    "if(l.grid.some((r,y)=>r.some((t,x)=>(x===0||y===0||x===w-1||y===h-1)&&!wallTiles.includes(t))))return 'The arena must have solid boundary walls.';":
        "if(l.grid.some((r,y)=>r.some((t,x)=>(x===0||y===0||x===w-1||y===h-1)&&!wallTiles.includes(t))))return 'The arena must have solid boundary walls.';if(l.grid.some((r,y)=>r.some((t,x)=>t==='*'&&x>0&&y>0&&x<w-1&&y<h-1)))return 'City windows can only be placed in boundary walls.';",
    "distanceToEye*0.047": "distanceToEye*0.018",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
