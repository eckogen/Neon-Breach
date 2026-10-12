from pathlib import Path
p=Path('work/check.cjs');s=p.read_text();s=s.replace('getContext(){return context}', 'addEventListener(){},getContext(){return context}');s=s.replace("console.log('PASS:", """initGame();state='playing';mouseLook({target:canvas,clientX:100,clientY:100});mouseLook({target:canvas,clientX:140,clientY:80});check(Math.abs(player.angle-.1)<.0001&&Math.abs(player.pitch-.05)<.0001,'Unlocked mouse turns and pitches camera');
mouseLook({target:{},clientX:500,clientY:500});const before=player.angle;mouseLook({target:canvas,clientX:500,clientY:500});check(player.angle===before,'Re-entry avoids camera jumps');
document.pointerLockElement=canvas;mouseLook({movementX:20,movementY:10});check(Math.abs(player.angle-.15)<.0001&&Math.abs(player.pitch-.025)<.0001,'Captured mouse controls camera');
mouseLook({movementX:0,movementY:-10000});check(player.pitch===.65,'Pitch stays bounded');render();state='paused';const pausedAngle=player.angle;mouseLook({movementX:100,movementY:100});check(player.angle===pausedAngle,'Paused camera stays still');
console.log('PASS: mouse aiming captured and uncaptured, pitch limits, re-entry, pause');
console.log('PASS:""");p.write_text(s)
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8');s=s.replace('ctx.fillRect(0,half,w,half);','ctx.fillRect(0,half,w,h-half);');s=s.replace("if(Math.abs(a)<Math.atan2(.3,d)&&d<dist&&lineClear", "if(Math.abs((player.pitch||0)*canvas.height*.6)<canvas.width/(2*Math.tan(FOV/2))/d*.32&&Math.abs(a)<Math.atan2(.3,d)&&d<dist&&lineClear");p.write_text(s,encoding='utf-8')

