from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace('#e5b849','#c77b22').replace('#ffda58','#fff23b').replace('rgb:[.9,.65,.17]','rgb:[.82,.40,.055]').replace('rgb:[1,.8,.12]','rgb:[1,1,.055]')
s=s.replace("['3','Gold door','#c77b22','▥']", "['3','Gold door','#c77b22','Ⅱ']",1).replace("['g','Gold keycard','#c77b22','▰']", "['g','Gold keycard','#c77b22','Ⅱ']",1)
s=s.replace("box(v,d.x,cy,d.y,sx,h,sz,[.13,.19,.27]);", "box(v,d.x,cy,d.y,sx,h,sz,d.type==='3'?[.32,.15,.025]:[.13,.19,.27]);if(d.type==='3'){for(let offset of [-.16,.16])box(v,d.x,cy+offset,d.y,sx+.035,Math.min(.06,h),sz+.035,[1,.73,.29])}",1)
s=s.replace("box(v,o.x,y+.025,o.y,.23,.035,.043,[.95,.95,.86],elapsed*.7);", "if(o.type==='g'){for(let offset of [-.045,.045])box(v,o.x,y+offset,o.y,.25,.025,.048,[.18,.065,.01],elapsed*.7)}else box(v,o.x,y+.025,o.y,.23,.035,.043,[.95,.95,.86],elapsed*.7);",1)
p.write_text(s,encoding='utf-8')
