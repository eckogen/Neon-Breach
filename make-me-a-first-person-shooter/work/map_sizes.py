from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
s=s.replace(' N=20,',' ')
s=s.replace('<button id="newMap">New empty map</button>','<label for="newMapSize">New map size (width × height)</label><select id="newMapSize" style="width:100%;padding:10px;background:#0a1421;color:white"><option value="20x20">20 × 20</option><option value="20x40">20 × 40</option><option value="40x40">40 × 40</option></select><button id="newMap">New empty map</button>',1)
s=s.replace('<span class="legend">Click or drag to paint · Right-click to erase · 20 × 20 tiles</span>','<span class="legend" id="mapLegend"></span>',1).replace('Boundary walls stay locked.','Border cells accept full-height wall objects only.')
a=s.index('function mapShape(');b=s.index('\n',a)
s=s[:a]+"function mapShape(l){return !!l&&Array.isArray(l.grid)&&[[20,20],[20,40],[40,40]].some(([w,h])=>l.grid.length===h&&l.grid.every(r=>Array.isArray(r)&&r.length===w&&r.every(t=>palette.some(p=>p[0]===t))))}\nfunction emptyLevel(w,h){return {version:1,name:'Untitled arena',grid:Array.from({length:h},(_,y)=>Array.from({length:w},(_,x)=>x===0||y===0||x===w-1||y===h-1?'1':x===1&&y===1?'P':x===w-2&&y===h-2?'X':'0'))}}"+s[b:]
a=s.index('function validate(');b=s.index('\nfunction drawMap',a);part=s[a:b]
c=part.index('let cells=');part=part[:part.index('{')+1]+"if(!mapShape(l))return 'Map must be a valid 20 × 20, 20 × 40, or 40 × 40 grid.';let h=l.grid.length,w=l.grid[0].length;"+part[c:]
a1=part.index('for(let i=0;i<N;i++)');b1=part.index('let start;',a1)
part=part[:a1]+"if(l.grid.some((r,y)=>r.some((t,x)=>(x===0||y===0||x===w-1||y===h-1)&&!wallTiles.includes(t))))return 'The arena must have solid boundary walls.';"+part[b1:]
part=part.replace('a>=N||b>=N','a>=w||b>=h').replace('y<N','y<h').replace('x<N','x<w');s=s[:a]+part+s[b:]
# world loops use actual world; validator final region loop uses region dimensions
s=s.replace('for(let y=0;y<N;y++)for(let x=0;x<N;x++){let t=slot.map.grid[y][x];','for(let y=0;y<slot.map.grid.length;y++)for(let x=0;x<slot.map.grid[0].length;x++){let t=slot.map.grid[y][x];')
s=s.replace('y<N','y<world.length').replace('x<N','x<world[0].length')
s=s.replace('a>=N-1||b>=N-1','a>=world[0].length-1||b>=world.length-1')
a=s.index('function paintAt(');b=s.index('\n',a);part=s[a:b]
part=part.replace('let rect=', 'let w=level.grid[0].length,h=level.grid.length,rect=').replace('rect.width*N','rect.width*w').replace('rect.height*N','rect.height*h')
part=part.replace('if(x<1||y<1||x>=N-1||y>=N-1)return;', 'if(x<0||y<0||x>=w||y>=h)return;')
part=part.replace("if(t==='C')", "if((x===0||y===0||x===w-1||y===h-1)&&!wallTiles.includes(t))return;if(t==='C')",1);s=s[:a]+part+s[b:]
a=s.index("$('newMap').onclick=");b=s.index(";$('resetMap')",a)
s=s[:a]+"$('newMap').onclick=()=>{let [w,h]=($('newMapSize').value||'20x20').split('x').map(Number);setLevel(emptyLevel(w,h));toast('Fresh '+w+' × '+h+' arena ready.')}"+s[b:]
# editor scaling
s=s.replace("function drawMap(){mctx.fillStyle", "function drawMap(){let w=level.grid[0].length,h=level.grid.length,cell=640/Math.max(w,h);map.width=w*cell;map.height=h*cell;map.style.width=map.width+'px';$('mapLegend').textContent='Click or drag to paint · Right-click to erase · '+w+' × '+h+' tiles · Borders: walls only';mctx.fillStyle",1)
a=s.index('function drawMap()');b=s.index('\nconst paletteGroups',a);part=s[a:b].replace('0,0,640,640','0,0,map.width,map.height').replace('x*32','x*cell').replace('y*32','y*cell').replace('30,30','cell-2,cell-2').replace("'bold 23px system-ui'","'bold '+Math.round(cell*.7)+'px system-ui'").replace('+16,y*cell+24','+cell/2,y*cell+cell*.75').replace('24,3','cell-8,3');s=s[:a]+part+s[b:]
s=s.replace('let scale=4,ox=22,oy=22','let scale=80/Math.max(world.length,world[0].length),ox=22,oy=22',1)
s=s.replace("s.map.grid.forEach((r,y)=>r.forEach((t,x)=>{let p=palette.find", "let tileScale=60/Math.max(s.map.grid.length,s.map.grid[0].length);s.map.grid.forEach((r,y)=>r.forEach((t,x)=>{let p=palette.find",1).replace('x*3,s.y*80+9+y*3,2.5,2.5','x*tileScale,s.y*80+9+y*tileScale,tileScale*.85,tileScale*.85',1)
p.write_text(s,encoding='utf-8')
