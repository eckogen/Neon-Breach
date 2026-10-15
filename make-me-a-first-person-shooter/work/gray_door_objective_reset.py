from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")
old = "if(d){d.open=true;world[y][x]='0'}"
new = "if(d){d.open=true;d.closing=false;d.clearTime=0;world[y][x]='0'}"
if source.count(old) != 1:
    raise RuntimeError(f"Expected one objective door action, found {source.count(old)}")
source = source.replace(old, new, 1)
source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
