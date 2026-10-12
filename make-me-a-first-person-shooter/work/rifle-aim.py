from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace('let cameraMotion=', 'let weaponMotion={ads:0,recoil:0,pitchKick:0};\nlet cameraMotion=',1);s=s.replace('function initGame(){cameraMotion=', 'function initGame(){weaponMotion={ads:0,recoil:0,pitchKick:0};cameraMotion=',1)
s=s.replace("canvas.onmousedown=e=>{if(state==='playing'&&e.button===0){keys.Mouse=true;fire()}};window.addEventListener('mouseup',()=>keys.Mouse=false);", "canvas.onmousedown=e=>{if(state!=='playing')return;if(e.button===0){keys.Mouse=true;fire()}if(e.button===2){e.preventDefault();keys.Aim=true}};window.addEventListener('mouseup',e=>{if(e.button===0)keys.Mouse=false;if(e.button===2)keys.Aim=false});",1)
s=s.replace("mousePosition=null;keys.Mouse=false});", "mousePosition=null;if(document.pointerLockElement!==canvas){keys.Mouse=false;keys.Aim=false}});",1)
s=s.replace("state='paused';keys={};mousePosition=null", "state='paused';keys={};weaponMotion.ads=0;mousePosition=null",1)
s=s.replace('player.angle+=dx*.005;', 'player.angle+=dx*.005*(1-.35*weaponMotion.ads);',1).replace('(player.pitch||0)-dy*.005', '(player.pitch||0)-dy*.005*(1-.35*weaponMotion.ads)',1)
s=s.replace('let cp=Math.cos(player.pitch||0),dir=[Math.cos(player.angle)*cp,Math.sin(player.pitch||0)', 'let aimPitch=(player.pitch||0)+weaponMotion.pitchKick,cp=Math.cos(aimPitch),dir=[Math.cos(player.angle)*cp,Math.sin(aimPitch)',1)
a=s.index('function fire()');b=s.index('function finish',a);fire=s[a:b].rstrip();assert fire.endswith('}');fire=fire[:-1]+"weaponMotion.recoil=Math.min(1.5,weaponMotion.recoil+.65);weaponMotion.pitchKick=Math.min(.18,weaponMotion.pitchKick+(weaponMotion.ads>.5?.018:.032));}\n";s=s[:a]+fire+s[b:]
s=s.replace('function update(dt){updateStance(dt);', 'function update(dt){updateWeaponMotion(dt);updateStance(dt);',1)
a=s.index('function perspective(');s=s[:a]+'''function updateWeaponMotion(dt){let target=keys.Aim&&!reload?1:0;weaponMotion.ads+=(target-weaponMotion.ads)*(1-Math.exp(-14*dt));weaponMotion.recoil*=Math.exp(-11*dt);weaponMotion.pitchKick*=Math.exp(-7*dt)}
''' +s[a:]
s=s.replace('let f=1/Math.tan(Math.PI/6),n=', 'let f=1/Math.tan((60-18*weaponMotion.ads)*Math.PI/360),n=',1)
s=s.replace('p=player.pitch||0,ca=', 'p=(player.pitch||0)+weaponMotion.pitchKick,ca=',1)
s=s.replace('cameraMotion.roll),sr=Math.sin(cameraMotion.roll)', 'cameraMotion.roll*(1-.8*weaponMotion.ads)),sr=Math.sin(cameraMotion.roll*(1-.8*weaponMotion.ads))',1)
s=s.replace('right[0]*cameraMotion.side', 'right[0]*cameraMotion.side*(1-.8*weaponMotion.ads)',1).replace('right[2]*cameraMotion.side', 'right[2]*cameraMotion.side*(1-.8*weaponMotion.ads)',1).replace('+cameraMotion.bob,player.y', '+cameraMotion.bob*(1-.8*weaponMotion.ads),player.y',1)
s=s.replace("gx=.23,gy=-.25+bob-lower,gz=-.5+shot*.2", "gx=.23*(1-weaponMotion.ads),gy=-.25+.145*weaponMotion.ads+bob*(1-.85*weaponMotion.ads)-lower+weaponMotion.recoil*.015,gz=-.5+shot*.2+weaponMotion.recoil*.055",1)
s=s.replace("if(flash)box(v,gx", "for(let side of [-1,1])box(v,gx+side*.022,gy+.105,gz+.14,.012,.025,.025,[.08,.11,.14]);box(v,gx,gy+.082,gz+.14,.055,.01,.025,[.08,.11,.14]);if(flash)box(v,gx",1)
s=s.replace("ctx.strokeStyle=shot>0?", "ctx.globalAlpha=1-weaponMotion.ads;ctx.strokeStyle=shot>0?",1).replace("ctx.stroke();\nif(hurt)", "ctx.stroke();ctx.globalAlpha=1;\nif(hurt)",1)
s=s.replace('<span><kbd>Mouse</kbd> Look & shoot</span>', '<span><kbd>Mouse</kbd> Look · Left: fire · Hold right: iron sights</span>',1)
p.write_text(s,encoding='utf-8')
