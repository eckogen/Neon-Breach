from pathlib import Path


path = Path(__file__).parents[1] / "outputs" / "index.html"
source = path.read_text(encoding="utf-8")

replacements = {
    '<option value="20x20">20 × 20</option><option value="20x30">20 × 30</option><option value="20x40">20 × 40</option><option value="30x20">30 × 20</option><option value="30x30">30 × 30</option><option value="30x40">30 × 40</option><option value="40x20">40 × 20</option><option value="40x30">40 × 30</option><option value="40x40">40 × 40</option>':
        '<option value="40x40">40 × 40</option><option value="40x60">40 × 60</option><option value="40x80">40 × 80</option><option value="60x40">60 × 40</option><option value="60x60">60 × 60</option><option value="60x80">60 × 80</option><option value="80x40">80 × 40</option><option value="80x60">80 × 60</option><option value="80x80">80 × 80</option>',
    '[[20,20],[20,30],[20,40],[30,20],[30,30],[30,40],[40,20],[40,30],[40,40]].some(([w,h])=>':
        '[20,30,40,60,80].some(h=>[20,30,40,60,80].some(w=>',
    "r.every(t=>palette.some(p=>p[0]===t))))}":
        "r.every(t=>palette.some(p=>p[0]===t)))))}",
    "Map must be a valid grid with width and height of 20, 30, or 40 tiles.":
        "Map must be a valid grid using supported legacy or doubled dimensions.",
    "($('newMapSize').value||'20x20')": "($('newMapSize').value||'40x40')",
}

for old, new in replacements.items():
    count = source.count(old)
    if count == 0 and source.count(new) == 1:
        continue
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:80]}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
path.write_text(source, encoding="utf-8")
