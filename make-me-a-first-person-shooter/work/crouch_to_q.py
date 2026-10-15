from pathlib import Path


root = Path(__file__).parents[1]
index = root / "outputs" / "index.html"
source = index.read_text(encoding="utf-8")

replacements = {
    "<kbd>Z</kbd> Hold to crouch": "<kbd>Q</kbd> Hold to crouch",
    "keys.KeyZ?'crouch'": "keys.KeyQ?'crouch'",
    "e.code==='KeyZ'": "e.code==='KeyQ'",
}

for old, new in replacements.items():
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old}")
    source = source.replace(old, new, 1)

source = "\n".join(line.rstrip() for line in source.splitlines()) + "\n"
index.write_text(source, encoding="utf-8")
