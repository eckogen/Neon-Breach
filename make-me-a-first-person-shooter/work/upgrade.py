from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');start=s.index('function cast(angle)');end=s.index('function loop(t)',start);hud=s[s.index("ctx.strokeStyle=shot>0?",start):end];s=s[:start]+Path('work/renderer3d.txt').read_text(encoding='utf-8')+hud+s[end:]
s=s.replace("pitch:0,hp:100", "pitch:0,height:0,velocity:0,hp:100")
s=s.replace("Math.max(-.65,Math.min(.65,", "Math.max(-1.4,Math.min(1.4,")
s=s.replace("if(keys.Space||keys.Mouse)fire();", "if(keys.KeyF||keys.Mouse)fire();if(keys.Space&&(player.height||0)===0){player.velocity=4.1}player.velocity=(player.velocity||0)-10*dt;player.height=Math.max(0,(player.height||0)+player.velocity*dt);if(player.height===0)player.velocity=0;")
s=s.replace('<kbd>Space</kbd> Fire', '<kbd>F</kbd> Fire · <kbd>Space</kbd> Jump')
a=s.index('function fire()');b=s.index('function finish(',a)
s=s[:a]+'''function fire(){if(shot>0||reload||state!=='playing')return;if(ammo<=0){doReload();return}ammo--;shot=.16;flash=.075;sound(140,.11,'sawtooth',.065);let best=null,dist=Infinity;let cp=Math.cos(player.pitch||0),dir=[Math.cos(player.angle)*cp,Math.sin(player.pitch||0),Math.sin(player.angle)*cp],origin=[player.x,1.05+(player.height||0),player.y];enemies.forEach(e=>{if(e.hp<=0)return;let ey=1.05+Math.sin(elapsed*3+enemies.indexOf(e))*.06,lo=[e.x-.42,ey-.22,e.y-.42],hi=[e.x+.42,ey+.28,e.y+.42],near=0,far=50;for(let i=0;i<3;i++){if(Math.abs(dir[i])<.000001){if(origin[i]<lo[i]||origin[i]>hi[i])return}else{let a=(lo[i]-origin[i])/dir[i],b=(hi[i]-origin[i])/dir[i];near=Math.max(near,Math.min(a,b));far=Math.min(far,Math.max(a,b))}}if(near<=far&&near<dist&&lineClear(player.x,player.y,e.x,e.y)){best=e;dist=near}});if(best){best.hp-=30;best.hit=.12;if(best.hp<=0){kills++;sound(400,.18,'triangle',.03)}}}
''' +s[b:]
s=s.replace('SOLO / ARENA FPS','WEBGL / TRUE 3D FPS');p.write_text(s,encoding='utf-8')
