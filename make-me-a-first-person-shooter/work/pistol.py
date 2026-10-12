from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace("['H','Medkit'", "['6','Pistol pickup','#b3deff','⌐'],['H','Medkit'",1);s=s.replace('let weaponMotion=', "const weaponStats={rifle:{name:'PULSE RIFLE',capacity:24,delay:.16,reload:1.35,damage:30},pistol:{name:'PISTOL',capacity:12,delay:.3,reload:1,damage:20}};let activeWeapon='rifle',weaponInventory={rifle:{owned:true,ammo:24,reserve:96},pistol:{owned:false,ammo:12,reserve:36}};\nlet weaponMotion=",1)
s=s.replace('function initGame(){weaponMotion=', "function initGame(){activeWeapon='rifle';weaponInventory={rifle:{owned:true,ammo:24,reserve:96},pistol:{owned:false,ammo:12,reserve:36}};weaponMotion=",1)
s=s.replace("['H','A','X'].includes(t)", "['H','A','X','6'].includes(t)",1)
s=s.replace("if(state==='playing'&&e.code==='KeyR')", "if(state==='playing'&&e.code==='Digit1')switchWeapon('rifle');if(state==='playing'&&e.code==='Digit2')switchWeapon('pistol');if(state==='playing'&&e.code==='KeyR')",1)
a=s.index('function doReload()');b=s.index('function paneBounds(',a)
s=s[:a]+'''function syncWeapon(){weaponInventory[activeWeapon].ammo=ammo;weaponInventory[activeWeapon].reserve=reserve}
function switchWeapon(name){if(!weaponInventory[name]?.owned)return false;syncWeapon();activeWeapon=name;ammo=weaponInventory[name].ammo;reserve=weaponInventory[name].reserve;reload=0;shot=0;weaponMotion.recoil=0;weaponMotion.pitchKick=0;return true}
function collectPistol(){let gun=weaponInventory.pistol;if(!gun.owned){gun.owned=true;switchWeapon('pistol');doorMessage='Pistol acquired · 1 rifle / 2 pistol'}else if(activeWeapon==='pistol'){reserve=Math.min(192,reserve+24);syncWeapon();doorMessage='Pistol ammunition +24'}else{gun.reserve=Math.min(192,gun.reserve+24);doorMessage='Pistol ammunition +24'}doorMessageTime=3;sound(500,.15,'triangle',.03)}
function doReload(){let stats=weaponStats[activeWeapon];if(reload||ammo===stats.capacity||reserve<=0)return;reload=stats.reload;sound(170,.08,'triangle',.03)}
''' +s[b:]
s=s.replace('ammo--;shot=.16;', 'ammo--;shot=weaponStats[activeWeapon].delay;',1).replace('best.hp-=30;', 'best.hp-=weaponStats[activeWeapon].damage;',1)
s=s.replace('let n=Math.min(24-ammo,reserve);','let n=Math.min(weaponStats[activeWeapon].capacity-ammo,reserve);',1)
s=s.replace("if(p.type==='H'&&player.hp<100)", "if(p.type==='6'){collectPistol();p.used=true}if(p.type==='H'&&player.hp<100)",1)
s=s.replace("}else if(keyTiles.includes(o.type))", "}else if(o.type==='6'){let y=.48+Math.sin(elapsed*2)*.04;pistolMesh(v,o.x,y,o.y,elapsed*.5,1.4);box(v,o.x,.035,o.y,.45,.045,.45,[.18,.38,.5])}else if(keyTiles.includes(o.type))",1)
a=s.index('box(v,gx,gy,gz,.15');b=s.index('if(flash)box(v,gx',a);s=s[:a]+"if(activeWeapon==='pistol'){pistolMesh(v,gx,gy+.05,gz,0,1)}else{"+s[a:b]+"}"+s[b:]
a=s.index('function placeArcade(');s=s[:a]+'''function pistolMesh(v,x,y,z,angle=0,scale=1){let c=Math.cos(angle),s=Math.sin(angle),part=(dx,dy,dz,sx,sy,sz,color)=>box(v,x+(dx*c-dz*s)*scale,y+dy*scale,z+(dx*s+dz*c)*scale,sx*scale,sy*scale,sz*scale,color,angle);part(0,0,0,.09,.065,.23,[.35,.42,.5]);part(0,-.075,.065,.065,.13,.085,[.09,.13,.17]);part(0,.041,-.085,.014,.018,.02,[.6,1,.85]);for(let side of [-1,1])part(side*.022,.041,.075,.01,.018,.018,[.1,.15,.19]);}
''' +s[a:]
s=s.replace("ctx.fillText('PULSE RIFLE',", "ctx.fillText(weaponStats[activeWeapon].name,",1)
s=s.replace("let hp=player?.hp??100,bullets=ammo", "syncWeapon();let carriedWeapons=clone(weaponInventory),carriedActive=activeWeapon;let hp=player?.hp??100,bullets=ammo",1)
s=s.replace('player.hp=hp;ammo=bullets;', 'weaponInventory=carriedWeapons;activeWeapon=carriedActive;player.hp=hp;ammo=bullets;',1)
s=s.replace('<span><kbd>R</kbd> Reload</span>', '<span><kbd>R</kbd> Reload · <kbd>1 / 2</kbd> Rifle / pistol</span>',1)
p.write_text(s,encoding='utf-8')

