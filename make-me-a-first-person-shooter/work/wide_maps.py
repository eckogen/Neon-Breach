from pathlib import Path
p=Path('outputs/index.html');s=p.read_text(encoding='utf-8');s=s.replace('<option value="40x40">40 × 40</option>','<option value="40x20">40 × 20</option><option value="40x40">40 × 40</option>',1);s=s.replace('[[20,20],[20,40],[40,40]]','[[20,20],[20,40],[40,20],[40,40]]');s=s.replace('20 × 20, 20 × 40, or 40 × 40 grid','20 × 20, 20 × 40, 40 × 20, or 40 × 40 grid');p.write_text(s,encoding='utf-8')
p=Path('work/check.cjs');s=p.read_text(encoding='utf-8');s=s.replace('[[20,20],[20,40],[40,40]]','[[20,20],[20,40],[40,20],[40,40]]');p.write_text(s,encoding='utf-8')
p=Path('outputs/README.md');s=p.read_text(encoding='utf-8');s=s.replace('20 × 20, 20 × 40, or 40 × 40','20 × 20, 20 × 40, 40 × 20, or 40 × 40');p.write_text(s,encoding='utf-8')
