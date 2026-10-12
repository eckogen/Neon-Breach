from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace('let cameraMotion=', 'let chairs=[],debris=[];\nlet cameraMotion=',1);s=s.replace('enemies=[];pickups=[];doors=[];', 'enemies=[];pickups=[];doors=[];chairs=[];debris=[];',1);s=s.replace("if(doorColors[t])doors.push", "if(chairTiles.includes(t))chairs.push({x:x+.5,z:y+.5,type:t,hp:60});if(doorColors[t])doors.push",1)
a=s.index('function fire()');b=s.index('function finish(',a)
s=s[:a]+Path('work/destruction.txt').read_text(encoding='utf-8')+s[b:] if Path('work/destruction.txt').exists() else s
p.write_text(s,encoding='utf-8')
