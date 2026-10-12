from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace('sightTime:0,accuracy:.1','sightTime:0,accuracy:.1,evadeRemaining:0,evadeSwitch:0,evadeDirection:1')
s=s.replace('let ey=1.05+Math.sin(elapsed*3+i)*.06,d=rayBox', 'let ey=droneHeight(e,i),d=rayBox',1)
s=s.replace("best.hit=.12;if(best.hp<=0){kills++;sound(400,.18,'triangle',.03)}", "best.hit=.12;if(best.hp<=0){kills++;shatterDrone(best,dir);sound(400,.18,'triangle',.03)}else{best.evadeRemaining=3;best.evadeSwitch=.65;best.evadeDirection=Math.random()<.5?-1:1}",1)
old="if(d>1.8){let vx=(player.x-e.x)/d*dt*.9,vy=(player.y-e.y)/d*dt*.9;if(canMove(e.x+vx,e.y))e.x+=vx;if(canMove(e.x,e.y+vy))e.y+=vy}"
assert old in s;s=s.replace(old,'',1)
s=s.replace('if(visible){if(d<7', 'moveDrone(e,dt,visible);if(visible){if(d<7',1)
a=s.index('function updateDroneAim(')
s=s[:a]+'''function droneHeight(e,i){return 1.05+Math.sin(elapsed*3+i)*.06+((e.evadeRemaining||0)>0?Math.sin(elapsed*9)*.10:0)}
function moveDrone(e,dt,visible){let evasive=(e.evadeRemaining||0)>0;if(!visible&&!evasive)return;let dx=player.x-e.x,dy=player.y-e.y,d=Math.hypot(dx,dy)||1,ux=dx/d,uy=dy/d,vx=0,vy=0;if(evasive){e.evadeSwitch=(e.evadeSwitch||0)-dt;if(e.evadeSwitch<=0){e.evadeDirection=-(e.evadeDirection||1);e.evadeSwitch=.65}let side=e.evadeDirection||1,retreat=d<2.4?-.65:d>5?.25:0;vx=(-uy*side+ux*retreat)*2.1*dt;vy=(ux*side+uy*retreat)*2.1*dt;e.evadeRemaining=Math.max(0,e.evadeRemaining-dt)}else if(d>1.8){vx=ux*dt*.9;vy=uy*dt*.9}let blocked=false;if(canMove(e.x+vx,e.y))e.x+=vx;else blocked=true;if(canMove(e.x,e.y+vy))e.y+=vy;else blocked=true;if(blocked&&evasive){e.evadeDirection=-(e.evadeDirection||1);e.evadeSwitch=.65}}
function droneParts(e,i){let y=droneHeight(e,i),a=Math.atan2(player.y-e.y,player.x-e.x),c=e.hit?[1,1,1]:(e.evadeRemaining||0)>0?[1,.5,.08]:[.9,.12,.22],parts=[];for(let dx of [-.12,.12])for(let dz of [-.12,.12]){let ca=Math.cos(a),sa=Math.sin(a);parts.push([e.x+dx*ca-dz*sa,y,e.y+dx*sa+dz*ca,.24,.32,.24,[.22,.30,.4],a])}parts.push([e.x,y+.02,e.y,.50,.06,.50,c,a],[e.x,y+.21,e.y,.23,.12,.23,[.12,.17,.23],a]);for(let dx of [-.31,.31])for(let dz of [-.25,.25])parts.push([e.x+dx,y,e.y+dz,.18,.1,.18,[.08,.12,.18],0],[e.x+dx,y+.07,e.y+dz,.23,.035,.23,c,elapsed*9]);return parts}
function shatterDrone(e,dir){let index=enemies.indexOf(e),parts=droneParts({...e,hit:0},Math.max(0,index));for(let [x,y,z,sx,sy,sz,color,angle]of parts){let mesh=[];box(mesh,0,0,0,sx,sy,sz,color);debris.push({mesh,x,y,z,vx:dir[0]*1.6+(Math.random()-.5)*3.8,vy:1.8+Math.random()*2.8,vz:dir[2]*1.6+(Math.random()-.5)*3.8,rx:0,ry:angle,rz:0,wx:(Math.random()-.5)*12,wy:(Math.random()-.5)*12,wz:(Math.random()-.5)*12,radius:Math.max(.045,Math.hypot(sx,sy,sz)/2),age:0,alpha:1})}if(debris.length>180)debris.splice(0,debris.length-180);e.evadeRemaining=0;}
''' +s[a:]
a=s.index('enemies.filter(e=>e.hp>0).forEach((e,i)=>{let y=',s.index('function render3D'));b=s.index('pickups.filter',a)
s=s[:a]+"enemies.forEach((e,i)=>{if(e.hp>0)for(let part of droneParts(e,i))box(v,...part)});\n"+s[b:]
s=s.replace('// Transparent debris retains the original chair mesh fragments and colors.', '// Transparent debris contains chair fragments and shattered drone components.')
p.write_text(s,encoding='utf-8')
