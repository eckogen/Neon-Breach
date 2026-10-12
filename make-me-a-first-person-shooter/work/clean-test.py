from pathlib import Path
p=Path('work/check.cjs');s=p.read_text();needle="initGame();state='playing';mouseLook({target:canvas";a=s.find(needle);b=s.find(needle,a+1);end=s.find("console.log('PASS: default map",b);s=s[:b]+s[end:] if b>=0 else s;p.write_text(s)
