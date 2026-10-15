from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    "#map{max-width:none;width:640px;height:auto;touch-action:none;cursor:crosshair;image-rendering:pixelated}":
        "#map{max-width:none;width:640px;height:auto;touch-action:none;cursor:crosshair;image-rendering:auto}",
    "let editorZoom=1;function setEditorZoom(value){editorZoom=Math.max(.5,Math.min(3,Math.round(value*4)/4));map.style.width=map.width*editorZoom+'px';$('zoomLevel').textContent=Math.round(editorZoom*100)+'%'}function drawMap(){let w=level.grid[0].length,h=level.grid.length,cell=640/Math.max(w,h);map.width=w*cell;map.height=h*cell;map.style.width=map.width*editorZoom+'px';":
        "let editorZoom=1;function setEditorZoom(value){editorZoom=Math.max(.5,Math.min(3,Math.round(value*4)/4));$('zoomLevel').textContent=Math.round(editorZoom*100)+'%';drawMap()}function drawMap(){let w=level.grid[0].length,h=level.grid.length,cell=640/Math.max(w,h)*editorZoom;map.width=Math.round(w*cell);map.height=Math.round(h*cell);map.style.width=map.width+'px';",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
