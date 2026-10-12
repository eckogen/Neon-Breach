from pathlib import Path
p=Path('work/check.cjs');s=p.read_text(encoding='utf-8-sig');marker="console.log('PASS: WebGL"
insert="""initGame();state='playing';player={x:3.5,y:1.5,angle:0,pitch:0,hp:100,height:0,velocity:0};enemies=[{x:5.5,y:1.5,hp:60,attack:0,hit:0}];pickups=[];const originalRandom=Math.random;try{Math.random=()=>.699;update(.01);check(player.hp===91,'Turret hits below 70 percent threshold');enemies[0].attack=0;hurt=0;Math.random=()=>.7;update(.01);check(player.hp===91&&hurt===0,'Turret misses at 70 percent threshold');check(enemies[0].attack===1.4,'Miss still consumes firing cooldown')}finally{Math.random=originalRandom}console.log('PASS: turret 70 percent hit threshold and miss cooldown');
"""
assert marker in s;s=s.replace(marker,insert+marker,1);p.write_text(s,encoding='utf-8')
