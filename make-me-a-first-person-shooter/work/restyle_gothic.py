from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
s=s.replace("['w','Gothic ribbed','#79718c','♜'],['z','Cyber cathedral','#b26be2','✧']","['w','Obsidian reliquary','#b79459','♜'],['z','Neon lancet','#65b9d8','✧']",1)
s=s.replace("w:[.16,.14,.21],z:[.105,.065,.17]","w:[.075,.08,.095],z:[.055,.085,.13]",1)
a=s.index("if(t==='w'||t==='z'){let rib=");b=s.index('\n}',a)
s=s[:a]+'''if(t==='w'||t==='z'){
let trim=t==='w'?[.48,.36,.19]:[.23,.34,.43],glow=t==='w'?[.94,.43,.09]:[.12,.73,.88];
// Four solid-faced lancets with a true pointed silhouette and inset panel.
let emit=(points,col,depth)=>{for(let axis of [0,1])for(let side of [-1,1]){let normal=axis===0?[0,0,side]:[side,0,0];for(let i=1;i<points.length-1;i++)for(let p of [points[0],points[i],points[i+1]])v.push(axis===0?x+.5+p[0]:x+.5+side*depth,p[1],axis===0?z+.5+side*depth:z+.5+p[0],...normal,...col)}};
let outer=[[-.34,.39],[.34,.39],[.34,1.65],[0,2.24],[-.34,1.65]],inner=[[-.27,.47],[.27,.47],[.27,1.63],[0,2.11],[-.27,1.63]];
for(let i=0;i<5;i++){let j=(i+1)%5;emit([outer[i],outer[j],inner[j],inner[i]],trim,.522)}
emit(inner,[.025,.033,.05],.504);
for(let a of [-.43,.43])face(a,1.25,.075,2.5,trim,.016);band(.14,.16,trim);band(2.39,.12,trim);
if(t==='w'){for(let y of [.7,1.02,1.34]){face(0,y,.3,.105,[.17,.19,.22],.01);face(0,y,.13,.035,glow,.026)}face(0,1.82,.075,.13,glow,.02)}
else {emit([[-.225,.56],[-.035,.56],[-.035,1.94],[-.225,1.6]],[.08,.49,.61],.509);emit([[.035,.56],[.225,.56],[.225,1.6],[.035,1.94]],[.42,.12,.59],.509);face(0,1.15,.025,1.3,trim,.022);for(let y of [.83,1.19,1.55])face(0,y,.52,.028,trim,.022);face(0,2.04,.035,.075,glow,.025)}
}''' +s[b:]
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s=s.replace('cybergothic ribbed stone and cyber cathedral panels','cybergothic obsidian reliquaries and neon lancet panels');s+='\nCybergothic walls use pointed metal frames: Obsidian reliquary has warm brass trim and amber inset lights; Neon lancet has divided cyan/violet panels. Frame and panel surfaces are separated in depth.\n';p.write_text(s,encoding='utf-8')
