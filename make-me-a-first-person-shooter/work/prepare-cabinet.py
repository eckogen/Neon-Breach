from pathlib import Path
s=Path('work/import-chair.py').read_text();s=s.replace("'D:/voxChair.glb'", "'C:/Users/Owner/Downloads/FileCabinet.glb'").replace('c*1.15/1.8','c').replace('chair-mesh.json','cabinet-mesh.json').replace('voxChair.glb','FileCabinet.glb').replace('height 1.15 meters','height 1.8 meters');Path('work/import-cabinet.py').write_text(s)
