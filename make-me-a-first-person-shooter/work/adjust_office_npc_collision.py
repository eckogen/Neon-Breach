from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")
old = "if(tile==='^')return Math.hypot(x-Math.floor(x)-.5,y-Math.floor(y)-.5)<=.3;"
new = "if(tile==='^')return Math.hypot(x-Math.floor(x)-.5,y-Math.floor(y)-.5)<=.34;"
if source.count(old) != 1:
    raise RuntimeError(f"Expected one NPC collision radius, found {source.count(old)}")
source = source.replace(old, new, 1)
source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
