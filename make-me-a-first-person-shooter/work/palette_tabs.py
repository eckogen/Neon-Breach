from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
s=s.replace('<div class="tools" id="tools"></div>', '<div class="palette-tabs" id="paletteTabs" role="tablist" aria-label="Object categories"></div><p id="selectedTool" class="selected-tool"></p><div class="tools" id="tools" role="tabpanel" aria-label="Build objects"></div>',1)
s=s.replace('.tools{display:grid;gap:8px}', '.palette-tabs{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-bottom:12px}.palette-tabs button{padding:8px 5px;font-size:11px}.selected-tool{font-size:12px;margin-bottom:12px;color:var(--cyan)}.tools{display:grid;gap:8px}',1)
start=s.index('palette.forEach(([id,name,color,icon])=>');end=s.index('\nfunction paintAt',start)
s=s[:start]+'''const paletteGroups=[
{name:'Structure',tiles:['0','1','2','9','V','T']},
{name:'Crawl shafts',tiles:['S','Q','j','f','h','i','k','a','c','d','e']},
{name:'Doors & keys',tiles:['O','R','r','B','b','Y','y','3','g','4','s','5','p']},
{name:'Props',tiles:['C','K','U']},
{name:'Enemies',tiles:['E','7','8']},
{name:'Mission & gear',tiles:['P','Z','X','6','H','A']}
];
let paletteCategory=0;const paletteTabButtons=[];
function selectPaletteCategory(index){paletteCategory=index;let group=paletteGroups[index];if(!group.tiles.includes(brush))brush=group.tiles[0];paletteTabButtons.forEach((b,i)=>{b.className=i===index?'active':'';b.setAttribute('aria-selected',String(i===index));b.tabIndex=i===index?0:-1});$('tools').innerHTML='';for(let id of group.tiles){let [,name,color,icon]=palette.find(p=>p[0]===id),b=document.createElement('button');b.className='tool'+(id===brush?' active':'');b.innerHTML='<span class="swatch" style="background:'+color+';color:#071522">'+icon+'</span>'+name;b.onclick=()=>{brush=id;selectPaletteCategory(index)};$('tools').append(b)}$('selectedTool').textContent='Selected: '+palette.find(p=>p[0]===brush)[1];$('tools').setAttribute('aria-labelledby','paletteTab'+index)}
paletteGroups.forEach((group,index)=>{let b=document.createElement('button');b.id='paletteTab'+index;b.textContent=group.name;b.setAttribute('role','tab');b.setAttribute('aria-controls','tools');b.onclick=()=>selectPaletteCategory(index);b.onkeydown=e=>{let next=e.key==='ArrowRight'?(index+1)%paletteGroups.length:e.key==='ArrowLeft'?(index+paletteGroups.length-1)%paletteGroups.length:e.key==='Home'?0:e.key==='End'?paletteGroups.length-1:null;if(next!==null){e.preventDefault();selectPaletteCategory(next);paletteTabButtons[next].focus()}};paletteTabButtons.push(b);$('paletteTabs').append(b)});
selectPaletteCategory(0);
''' +s[end:]
p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s+='\nThe build palette is organized into Structure, Crawl shafts, Doors & keys, Props, Enemies, and Mission & gear tabs. Switching categories selects the first object in that category; the selected brush is shown above the object list.\n';p.write_text(s,encoding='utf-8')
