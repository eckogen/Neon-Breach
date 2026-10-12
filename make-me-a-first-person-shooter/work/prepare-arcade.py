from pathlib import Path
s=Path('work/import-cabinet.py').read_text();s=s.replace('FileCabinet.glb','ArcadeCabinet.glb').replace('cabinet-mesh.json','arcade-mesh.json');Path('work/import-arcade.py').write_text(s)
