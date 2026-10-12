from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8')
old="if(t==='v'){for(let a of [-.4,.4])face(a,1.25,.13,2.5,[.49,.52,.52]);for(let y of [.18,2.3]){band(y,.23,[.92,.66,.08]);for(let a of [-.39,-.13,.13,.39])face(a,y,.12,.235,[.065,.075,.085])}face(0,1.3,.58,.9,[.12,.16,.19]);face(0,1.72,.35,.045,[1,.35,.06]);for(let a of [-.19,.19])face(a,1.2,.045,.55,[.55,.6,.61])}"
new="if(t==='v'){for(let a of [-.4,.4])face(a,1.25,.13,2.5,[.49,.52,.52],.018);for(let y of [.18,2.3]){band(y,.23,[.92,.66,.08]);for(let a of [-.39,-.13,.13,.39])face(a,y,.12,.235,[.065,.075,.085],.034)}face(0,1.3,.58,.9,[.12,.16,.19],.008);face(0,1.72,.35,.045,[1,.35,.06],.024);for(let a of [-.19,.19])face(a,1.2,.045,.55,[.55,.6,.61],.024)}"
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf-8')
