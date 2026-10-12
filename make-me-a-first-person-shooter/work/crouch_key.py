from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8').replace("keys.ControlLeft||keys.ControlRight?'crouch'","keys.KeyZ?'crouch'").replace("['ControlLeft','ControlRight'].includes(e.code)","e.code==='KeyZ'").replace('<kbd>Ctrl</kbd> Crouch','<kbd>Z</kbd> Hold to crouch');p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8').replace('Hold Ctrl to crouch.','Hold Z to crouch.');p.write_text(s,encoding='utf-8')
p=Path('work/check.cjs');s=p.read_text(encoding='utf-8').replace('ControlLeft:true','KeyZ:true').replace('Ctrl crouches with lower camera','Z crouches with lower camera');p.write_text(s,encoding='utf-8')
