from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    ".editorcanvas{display:flex;flex-direction:column;align-items:center;gap:12px;padding:20px;background:#0b1420;border:1px solid #26364c;border-radius:10px}#map{max-width:100%;width:640px;touch-action:none;cursor:crosshair}":
        ".editorcanvas{display:flex;flex-direction:column;align-items:center;gap:12px;padding:20px;background:#0b1420;border:1px solid #26364c;border-radius:10px;min-width:0}.map-zoom{display:flex;align-items:center;justify-content:center;gap:8px;width:100%}.map-zoom button{padding:7px 12px}.map-zoom output{min-width:52px;text-align:center;color:var(--cyan);font-size:12px}.map-viewport{width:100%;max-height:72vh;overflow:auto;text-align:center;border:1px solid #203044;border-radius:7px;background:#07101a;padding:8px}#map{max-width:none;width:640px;height:auto;touch-action:none;cursor:crosshair;image-rendering:pixelated}",
    "<div class=\"editorcanvas\"><canvas id=\"map\" width=\"640\" height=\"640\" aria-label=\"Level editor grid\"></canvas><span class=\"legend\" id=\"mapLegend\"></span></div>":
        "<div class=\"editorcanvas\"><div class=\"map-zoom\" aria-label=\"Map zoom controls\"><button id=\"zoomOut\" type=\"button\" aria-label=\"Zoom out\">−</button><button id=\"zoomReset\" type=\"button\">Reset zoom</button><button id=\"zoomIn\" type=\"button\" aria-label=\"Zoom in\">+</button><output id=\"zoomLevel\" aria-live=\"polite\">100%</output></div><div id=\"mapViewport\" class=\"map-viewport\"><canvas id=\"map\" width=\"640\" height=\"640\" aria-label=\"Level editor grid\"></canvas></div><span class=\"legend\" id=\"mapLegend\"></span></div>",
    "function drawMap(){let w=level.grid[0].length,h=level.grid.length,cell=640/Math.max(w,h);map.width=w*cell;map.height=h*cell;map.style.width=map.width+'px';":
        "let editorZoom=1;function setEditorZoom(value){editorZoom=Math.max(.5,Math.min(3,Math.round(value*4)/4));map.style.width=map.width*editorZoom+'px';$('zoomLevel').textContent=Math.round(editorZoom*100)+'%'}function drawMap(){let w=level.grid[0].length,h=level.grid.length,cell=640/Math.max(w,h);map.width=w*cell;map.height=h*cell;map.style.width=map.width*editorZoom+'px';",
    "map.oncontextmenu=e=>e.preventDefault();":
        "map.oncontextmenu=e=>e.preventDefault();$('zoomOut').onclick=()=>setEditorZoom(editorZoom-.25);$('zoomReset').onclick=()=>setEditorZoom(1);$('zoomIn').onclick=()=>setEditorZoom(editorZoom+.25);$('mapViewport').addEventListener('wheel',e=>{if(!e.ctrlKey&&!e.metaKey)return;e.preventDefault();setEditorZoom(editorZoom+(e.deltaY<0?.25:-.25))},{passive:false});",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
