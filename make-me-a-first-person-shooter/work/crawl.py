from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace("['Z','Level tether'", "['S','Crawl shaft ↔','#7899ac','↔'],['Q','Crawl shaft ↕','#7899ac','↕'],['Z','Level tether'",1)
s=s.replace('velocity:0,hp:100','velocity:0,hp:100,stance:\'stand\',crawlRequested:false,eyeHeight:1.05',1)
a=s.index('function canMove(');b=s.index('function lineClear',a)
s=s[:a]+'''function clearanceAt(x,z){return ['S','Q'].includes(world[Math.floor(z)]?.[Math.floor(x)])?.55:2.5}
function playerBodyHeight(){return Math.max(player.stance==='crawl'?.38:player.stance==='crouch'?.85:1.25,(player.eyeHeight??1.05)+.12)+(player.height||0)}
function fitsHeight(x,z,height){let r=.22;return [[x-r,z-r],[x+r,z-r],[x-r,z+r],[x+r,z+r]].every(([a,b])=>clearanceAt(a,b)>=height)}
function canMove(x,y,height=1.25){let r=.22;return fitsHeight(x,y,height)&&!wall(x-r,y-r)&&!wall(x+r,y-r)&&!wall(x-r,y+r)&&!wall(x+r,y+r)&&!glassPanes.some(p=>!p.broken&&paneOverlap(p,x,y,r))}
function updateStance(dt){let requested=player.crawlRequested?'crawl':keys.ControlLeft||keys.ControlRight?'crouch':'stand',height=requested==='stand'?1.25:requested==='crouch'?.85:.38;if(!fitsHeight(player.x,player.y,height))requested='crawl';player.stance=requested;let target=requested==='stand'?1.05:requested==='crouch'?.65:.27;player.eyeHeight=(player.eyeHeight??1.05)+(target-(player.eyeHeight??1.05))*(1-Math.exp(-14*dt));if(requested==='crawl'&&!fitsHeight(player.x,player.y,player.eyeHeight+.12))player.eyeHeight=Math.min(player.eyeHeight,.37)}
''' +s[b:]
s=s.replace("if(!tile)return true;if(cabinetTiles", "if(!tile)return true;if(tile==='S'){let z=y-Math.floor(y);return z<.08||z>.92}if(tile==='Q'){let a=x-Math.floor(x);return a<.08||a>.92}if(cabinetTiles",1)
s=s.replace("let t=l.grid[b][a];if(['1'", "let t=l.grid[b][a],here=l.grid[y][x];if((t==='S'||here==='S')&&dy!==0||(t==='Q'||here==='Q')&&dx!==0)continue;if(['1'",1)
s=s.replace("if(state==='playing'&&e.code==='KeyR')", "if(state==='playing'&&e.code==='KeyC'&&!e.repeat)player.crawlRequested=!player.crawlRequested;if(state==='playing'&&['ControlLeft','ControlRight'].includes(e.code))e.preventDefault();if(state==='playing'&&e.code==='KeyR')",1)
s=s.replace('function update(dt){elapsed+=dt;', 'function update(dt){updateStance(dt);elapsed+=dt;',1)
s=s.replace("v=(keys.ShiftLeft||keys.ShiftRight?4.1:2.7)*dt", "v=(player.stance==='crawl'?.85:player.stance==='crouch'?1.5:keys.ShiftLeft||keys.ShiftRight?4.1:2.7)*dt",1)
s=s.replace('if(canMove(player.x+dx,player.y))','if(canMove(player.x+dx,player.y,playerBodyHeight()))',1).replace('if(canMove(player.x,player.y+dy))','if(canMove(player.x,player.y+dy,playerBodyHeight()))',1)
s=s.replace('if(keys.Space&&(player.height||0)===0)', "if(keys.Space&&player.stance==='stand'&&(player.height||0)===0)",1)
s=s.replace('playerSprinting=playerMoving&&!!', "playerSprinting=playerMoving&&player.stance==='stand'&&!!",1)
s=s.replace("if(!(keys.ShiftLeft||keys.ShiftRight)||Math.hypot(dx,dz)<1e-6)", "if(player.stance!=='stand'||!(keys.ShiftLeft||keys.ShiftRight)||Math.hypot(dx,dz)<1e-6)",1)
s=s.replace('1.05+(player.height||0)+cameraMotion.bob', '(player.eyeHeight??1.05)+(player.height||0)+cameraMotion.bob',1)
s=s.replace("sprinting=keys.ShiftLeft||keys.ShiftRight,target=moving?(sprinting?1.5:1):0", "sprinting=player.stance==='stand'&&(keys.ShiftLeft||keys.ShiftRight),target=moving?(player.stance==='crawl'?.25:player.stance==='crouch'?.5:sprinting?1.5:1):0",1)
s=s.replace("if(['1','2','O','R','B','Y'].includes(t))dist=", "if(['S','Q'].includes(t))dist=Math.min(dist,rayBox(origin,dir,[x,.55,y],[x+1,2.5,y+1]));if(['1','2','O','R','B','Y'].includes(t))dist=",1)
s=s.replace("let tile=world[y][x];if(tile==='Z')", "let tile=world[y][x];if(['S','Q'].includes(tile)){let alongX=tile==='S';box(v,x+.5,1.525,y+.5,1,1.95,1,[.20,.28,.34]);for(let side of [-.46,.46]){box(v,x+.5+(alongX?0:side),.275,y+.5+(alongX?side:0),alongX?1:.08,.55,alongX?.08:1,[.25,.36,.42]);box(v,x+.5+(alongX?0:side),.48,y+.5+(alongX?side:0),alongX?1:.085,.035,alongX?.085:1,[.25,.85,.8])}}if(tile==='Z')",1)
s=s.replace("let nearby=nearestDoor(),prompt=", "ctx.font='bold 12px system-ui';ctx.fillStyle='#b8d7e9';ctx.fillText(player.stance==='crawl'?'CRAWLING · C to stand':player.stance==='crouch'?'CROUCHED':'STANDING',22,h-90);let nearby=nearestDoor(),prompt=",1)
s=s.replace('<span><kbd>Shift</kbd> Sprint</span>', '<span><kbd>Shift</kbd> Sprint</span><span><kbd>Ctrl</kbd> Crouch · <kbd>C</kbd> Toggle crawl</span>',1)
p.write_text(s,encoding='utf-8')
