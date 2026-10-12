from pathlib import Path
p=Path('outputs/index.html')
s=p.read_text(encoding='utf-8-sig')
s=s.replace("soundContext=null,audioEnabled=true;", "soundContext=null,audioEnabled=true, mousePosition=null, hadPointerLock=false;")
s=s.replace("angle:0,hp:100", "angle:0,pitch:0,hp:100")
s=s.replace("state='playing';keys={};$('overlay')", "state='playing';keys={};mousePosition=null;$('overlay')")
s=s.replace("Mouse capture unavailable. Use arrow keys and Space.", "Move the mouse over the game to aim. Click to fire.")
s=s.replace("Use arrow keys to turn and Space to fire.", "Move the mouse over the game to aim. Click to fire.")
s=s.replace("state='paused';keys={};document", "state='paused';keys={};mousePosition=null;document")
old="document.addEventListener('pointerlockchange',()=>{if(document.pointerLockElement!==canvas&&state==='playing')pause()});document.addEventListener('mousemove',e=>{if(state==='playing'&&document.pointerLockElement===canvas)player.angle+=e.movementX*.0025});"
new="""document.addEventListener('pointerlockchange',()=>{let locked=document.pointerLockElement===canvas;mousePosition=null;canvas.style.cursor=locked?'none':'crosshair';if(hadPointerLock&&!locked&&state==='playing')pause();hadPointerLock=locked});
function mouseLook(e){if(state!=='playing'){mousePosition=null;return}let dx=0,dy=0;if(document.pointerLockElement===canvas){dx=e.movementX||0;dy=e.movementY||0}else{if(e.target!==canvas){mousePosition=null;return}if(mousePosition){dx=e.clientX-mousePosition.x;dy=e.clientY-mousePosition.y}mousePosition={x:e.clientX,y:e.clientY}}player.angle+=dx*.0025;player.pitch=Math.max(-.65,Math.min(.65,(player.pitch||0)-dy*.0025));}
document.addEventListener('mousemove',mouseLook);canvas.addEventListener('mouseleave',()=>{mousePosition=null;keys.Mouse=false});"""
assert old in s
s=s.replace(old,new)
s=s.replace("half=h/2;let ceiling", "centerY=h/2,half=centerY+(player.pitch||0)*h*.6;let ceiling")
# Keep the aiming reticle centered while pitching the scene.
start=s.index("ctx.strokeStyle=shot>0?")
end=s.index("if(hurt)",start)
s=s[:start]+s[start:end].replace('half','centerY')+s[end:]
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8-sig').replace('Mouse: look. Left click: fire.', 'Mouse: look left/right and up/down. Left click: fire. If mouse capture is unavailable, move the cursor over the game to aim; leave and re-enter to reposition the cursor.');p.write_text(s,encoding='utf-8')
