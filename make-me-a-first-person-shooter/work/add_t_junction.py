from pathlib import Path
p=Path('outputs/index.html')
s=p.read_text(encoding='utf-8')
s=s.replace("['j','Crawl junction','#7899ac','┼'],", "['j','Crawl junction','#7899ac','┼'],['f','Crawl T N/E/W','#7899ac','┴'],['h','Crawl T N/E/S','#7899ac','├'],['i','Crawl T E/S/W','#7899ac','┬'],['k','Crawl T N/S/W','#7899ac','┤'],",1)
s=s.replace('e:[[-1,0],[0,-1]]};','e:[[-1,0],[0,-1]],f:[[0,-1],[1,0],[-1,0]],h:[[0,-1],[1,0],[0,1]],i:[[1,0],[0,1],[-1,0]],k:[[0,-1],[0,1],[-1,0]]};',1)
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s+='\nCrawl T-junctions are available in four orientations: N/E/W, N/E/S, E/S/W, and N/S/W. Each has three open paths and one blocked side, with crawl-only clearance.\n';p.write_text(s,encoding='utf-8')
p=Path('work/check.cjs');s=p.read_text(encoding='utf-8');marker="console.log('PASS: half-wall movement cover and landing, crawl junction, four elbows and directional validation');";extra="""
for(let [tile,closed] of [['f',[0,1]],['h',[-1,0]],['i',[0,-1]],['k',[1,0]]]){world[5][5]=tile;check(crawlOpenings[tile].length===3,'T junction has three openings');check(canMove(5.5,5.5,.38)&&!canMove(5.5,5.5,1.25),'T junction crawl clearance');for(let [dx,dy] of [[0,-1],[1,0],[0,1],[-1,0]])check(crawlConnects(tile,'0',dx,dy)===(dx!==closed[0]||dy!==closed[1]),'T junction respects open and closed paths');check(shaftBoxes(tile,5,5).length===2,'T junction roof and single closed side');bendMap.grid[4][4]=tile;check((validate(bendMap)==='')===(tile==='f'||tile==='h'),'T junction validation follows orientation')}
render();console.log('PASS: four T junction orientations, crawl clearance, geometry and route validation');
""";assert marker in s;s=s.replace(marker,marker+extra,1);p.write_text(s,encoding='utf-8')
