from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
old="let face=(offset,y,width,height,c)=>{for(let side of [-1,1]){box(v,x+.5+offset,y,z+.5+side*.503,width,height,.012,c);box(v,x+.5+side*.503,y,z+.5+offset,.012,height,width,c)}};"
new="let face=(offset,y,width,height,c,lift=0)=>{for(let side of [-1,1]){box(v,x+.5+offset,y,z+.5+side*(.503+lift),width,height,.012,c);box(v,x+.5+side*(.503+lift),y,z+.5+offset,.012,height,width,c)}};"
assert old in s;s=s.replace(old,new,1)
old="if(t==='u'){for(let y of [.13,1.25,2.37])band(y,.075,[.45,.51,.55]);for(let a of [-.43,.43]){face(a,1.25,.045,2.5,[.13,.17,.21]);for(let y of [.3,1.1,1.4,2.2])face(a,y,.065,.065,[.64,.69,.71])}for(let y of [1.58,1.7,1.82,1.94])face(0,y,.54,.045,[.08,.12,.15])}"
new="if(t==='u'){for(let y of [.13,1.25,2.37])band(y,.075,[.45,.51,.55]);for(let a of [-.43,.43]){face(a,1.25,.045,2.5,[.13,.17,.21],.008);for(let y of [.3,1.1,1.4,2.2])face(a,y,.065,.065,[.64,.69,.71],.022)}for(let y of [1.58,1.7,1.82,1.94])face(0,y,.54,.045,[.08,.12,.15],.008)}"
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf-8')
