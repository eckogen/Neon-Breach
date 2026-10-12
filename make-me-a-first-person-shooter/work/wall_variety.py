from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
entries="['q','Office plaster','#d5d1bb','▤'],['t','Office walnut','#956844','▥'],['u','Industrial steel','#71808b','▦'],['v','Hazard bulkhead','#d4aa38','⚠'],['w','Gothic ribbed','#79718c','♜'],['z','Cyber cathedral','#b26be2','✧'],"
s=s.replace("['P','Player spawn'",entries+"['P','Player spawn'",1)
pos=s.index('\nconst crawlOpenings=');s=s[:pos]+"\nconst wallTiles=['1','2','q','t','u','v','w','z'];"+s[pos:]
s=s.replace("['1','2',", "[...wallTiles,")
# restore declaration after replacement
s=s.replace("const wallTiles=[...wallTiles,'q','t','u','v','w','z'];","const wallTiles=['1','2','q','t','u','v','w','z'];")
s=s.replace("['1','2'].includes", "wallTiles.includes")
s=s.replace("['0','1','2'].includes(t)","(t==='0'||wallTiles.includes(t))")
s=s.replace("{name:'Structure',tiles:['0','1','2','9','V','T']}","{name:'Structure',tiles:['0','9','V','T']},\n{name:'Walls',tiles:wallTiles}")
old="if(wallTiles.includes(tile)){box(v,x+.5,1.25,y+.5,1,2.5,1,tile==='2'?[.055,.35,.39]:[.29,.38,.49]);box(v,x+.5,1.82,y+.5,1.008,.055,1.008,tile==='2'?[.15,.95,.77]:[.14,.19,.25]);box(v,x+.5,.15,y+.5,1.006,.15,1.006,[.12,.18,.24]);}"
assert old in s
s=s.replace(old,"if(wallTiles.includes(tile)){buildWall(v,x,y,tile);}",1)
helper='''
function buildWall(v,x,z,t){let bases={'1':[.29,.38,.49],'2':[.055,.35,.39],q:[.72,.7,.61],t:[.31,.17,.085],u:[.27,.33,.38],v:[.22,.25,.27],w:[.16,.14,.21],z:[.105,.065,.17]};box(v,x+.5,1.25,z+.5,1,2.5,1,bases[t]);let band=(y,h,c)=>box(v,x+.5,y,z+.5,1.012,h,1.012,c);let face=(offset,y,width,height,c)=>{for(let side of [-1,1]){box(v,x+.5+offset,y,z+.5+side*.503,width,height,.012,c);box(v,x+.5+side*.503,y,z+.5+offset,.012,height,width,c)}};
if(t==='1'||t==='2'){band(1.82,.055,t==='2'?[.15,.95,.77]:[.14,.19,.25]);band(.15,.15,[.12,.18,.24])}
if(t==='q'){band(.1,.2,[.29,.31,.31]);band(.95,.035,[.52,.51,.44]);band(2.36,.08,[.87,.85,.76]);face(0,1.7,.015,1.23,[.58,.57,.5])}
if(t==='t'){band(.12,.24,[.16,.09,.045]);band(.88,.09,[.53,.32,.14]);for(let a of [-.38,-.13,.13,.38])face(a,1.27,.026,2.35,[.52,.32,.17]);band(2.35,.11,[.52,.32,.17])}
if(t==='u'){for(let y of [.13,1.25,2.37])band(y,.075,[.45,.51,.55]);for(let a of [-.43,.43]){face(a,1.25,.045,2.5,[.13,.17,.21]);for(let y of [.3,1.1,1.4,2.2])face(a,y,.065,.065,[.64,.69,.71])}for(let y of [1.58,1.7,1.82,1.94])face(0,y,.54,.045,[.08,.12,.15])}
if(t==='v'){for(let a of [-.4,.4])face(a,1.25,.13,2.5,[.49,.52,.52]);for(let y of [.18,2.3]){band(y,.23,[.92,.66,.08]);for(let a of [-.39,-.13,.13,.39])face(a,y,.12,.235,[.065,.075,.085])}face(0,1.3,.58,.9,[.12,.16,.19]);face(0,1.72,.35,.045,[1,.35,.06]);for(let a of [-.19,.19])face(a,1.2,.045,.55,[.55,.6,.61])}
if(t==='w'||t==='z'){let rib=t==='w'?[.4,.36,.49]:[.33,.21,.43],glow=t==='w'?[.56,.19,.18]:[.73,.14,.95];for(let a of [-.43,.43])face(a,1.25,.095,2.5,rib);band(.16,.19,rib);band(2.38,.13,rib);for(let [a,y] of [[.32,1.8],[.23,1.98],[.13,2.13],[0,2.24],[-.13,2.13],[-.23,1.98],[-.32,1.8]])face(a,y,.13,.15,rib);face(0,1.17,.04,1.5,glow);face(0,1.45,.42,.055,glow);if(t==='z'){for(let a of [-.28,.28])face(a,1.08,.025,1.2,[.06,.85,.87]);face(0,.47,.31,.035,[.06,.85,.87])}}
}
'''
s=s.replace('function rebuildGeometry()',helper+'\nfunction rebuildGeometry()',1)
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s+='\nThe Walls tab includes office plaster and walnut panels, industrial steel and hazard bulkheads, and cybergothic ribbed stone and cyber cathedral panels. Each is solid full-height cover and supports automatic door orientation.\n';p.write_text(s,encoding='utf-8')
