from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8-sig');s=s.replace("['S','Crawl shaft ↔'", "['9','Half wall','#8da2b5','▃'],['j','Crawl junction','#7899ac','┼'],['a','Crawl bend N/E','#7899ac','└'],['c','Crawl bend E/S','#7899ac','┌'],['d','Crawl bend S/W','#7899ac','┐'],['e','Crawl bend W/N','#7899ac','┘'],['S','Crawl shaft ↔'",1)
a=s.index('function wall(');s=s[:a]+'''const crawlOpenings={S:[[1,0],[-1,0]],Q:[[0,-1],[0,1]],j:[[1,0],[-1,0],[0,-1],[0,1]],a:[[0,-1],[1,0]],c:[[1,0],[0,1]],d:[[0,1],[-1,0]],e:[[-1,0],[0,-1]]};
function crawlConnects(from,to,dx,dy){let permits=(tile,x,y)=>!crawlOpenings[tile]||crawlOpenings[tile].some(v=>v[0]===x&&v[1]===y);return permits(from,dx,dy)&&permits(to,-dx,-dy)}
function groundHeight(){return world[Math.floor(player.y)]?.[Math.floor(player.x)]==='9'?.65:0}
''' +s[a:]
a=s.index("if(tile==='S')");b=s.index('if(arcadeTiles.includes(tile))',a);s=s[:a]+"if(tile==='9')return true;if(crawlOpenings[tile]){let fx=x-Math.floor(x),fz=y-Math.floor(y);return shaftBoxes(tile,Math.floor(x),Math.floor(y)).slice(1).some(([lo,hi])=>x>=lo[0]&&x<=hi[0]&&y>=lo[2]&&y<=hi[2])}"+s[b:]
s=s.replace("['S','Q'].includes(world[Math.floor(z)]?.[Math.floor(x)])", "!!crawlOpenings[world[Math.floor(z)]?.[Math.floor(x)]]",1)
a=s.index('function shaftBoxes(');b=s.index('function shaftBlocks(',a);s=s[:a]+'''function shaftBoxes(t,x,z){if(t==='9')return [[[x,0,z],[x+1,.65,z+1]]];let boxes=[[[x,.55,z],[x+1,2.5,z+1]]],open=(dx,dy)=>crawlOpenings[t]?.some(v=>v[0]===dx&&v[1]===dy);if(!open(0,-1))boxes.push([[x,0,z],[x+1,.55,z+.08]]);if(!open(0,1))boxes.push([[x,0,z+.92],[x+1,.55,z+1]]);if(!open(-1,0))boxes.push([[x,0,z],[x+.08,.55,z+1]]);if(!open(1,0))boxes.push([[x+.92,0,z],[x+1,.55,z+1]]);return boxes}
''' +s[b:]
s=s.replace("if(['S','Q'].includes(t))", "if(crawlOpenings[t]||t==='9')")
s=s.replace("if(!['S','Q'].includes(t))", "if(!crawlOpenings[t])",1)
s=s.replace('function canMove(x,y,height=1.25){let r=.22;return', "function canMove(x,y,height=1.25,feet=0){let r=.22,blocked=(a,b)=>world[Math.floor(b)]?.[Math.floor(a)]==='9'?feet<.65:wall(a,b);return",1)
s=s.replace('&&!wall(x-r,y-r)&&!wall(x+r,y-r)&&!wall(x-r,y+r)&&!wall(x+r,y+r)', '&&!blocked(x-r,y-r)&&!blocked(x+r,y-r)&&!blocked(x-r,y+r)&&!blocked(x+r,y+r)',1)
s=s.replace('playerBodyHeight()))', 'playerBodyHeight(),player.height||0))')
s=s.replace("(player.height||0)===0){player.velocity=4.1}", "(player.height||0)<=groundHeight()+.001){player.velocity=4.1}",1)
s=s.replace('player.height=Math.max(0,(player.height||0)+player.velocity*dt);if(player.height===0)', 'player.height=Math.max(groundHeight(),(player.height||0)+player.velocity*dt);if(player.height===groundHeight())',1)
s=s.replace("if((t==='S'||here==='S')&&dy!==0||(t==='Q'||here==='Q')&&dx!==0)continue;", "if(!crawlConnects(here,t,dx,dy))continue;",1)
s=s.replace("if(!cell||seen.has(k)||(cell==='S'||t==='S')&&dy!==0||(cell==='Q'||t==='Q')&&dx!==0)continue;", "if(!cell||seen.has(k)||!crawlConnects(t,cell,dx,dy))continue;",1)
s=s.replace("['1','2','C','D','G'", "['1','2','9','C','D','G'")
# Half walls obstruct low sight but do not hide a standing player behind a low barrier.
s=s.replace("if(wall(x+(tx-x)*i/n,y+(ty-y)*i/n))return false", "if(wall(x+(tx-x)*i/n,y+(ty-y)*i/n)&&world[Math.floor(y+(ty-y)*i/n)]?.[Math.floor(x+(tx-x)*i/n)]!=='9')return false",1)
a=s.index("if(['S','Q'].includes(tile)){",s.index('function rebuildGeometry'));b=s.index("if(tile==='Z')",a);s=s[:a]+'''if(tile==='9'){box(v,x+.5,.325,y+.5,1,.65,1,[.3,.4,.5]);box(v,x+.5,.64,y+.5,1.015,.035,1.015,[.6,.7,.77])}if(crawlOpenings[tile]){for(let [lo,hi]of shaftBoxes(tile,x,y)){box(v,(lo[0]+hi[0])/2,(lo[1]+hi[1])/2,(lo[2]+hi[2])/2,hi[0]-lo[0],hi[1]-lo[1],hi[2]-lo[2],[.23,.32,.39]);if(lo[1]===0)box(v,(lo[0]+hi[0])/2,.48,(lo[2]+hi[2])/2,hi[0]-lo[0]+.005,.035,hi[2]-lo[2]+.005,[.25,.85,.8])}}''' +s[b:]
p.write_text(s,encoding='utf-8')
