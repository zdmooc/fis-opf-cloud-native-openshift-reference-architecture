#!/usr/bin/env python3
"""Validate structural references and check for forbidden client identifiers."""
from pathlib import Path
import re, sys
base=Path(__file__).resolve().parents[1]
problems=[];md=list(base.rglob('*.md'))
# Never include original client names, references, or documents.
forbidden=[r'\b'+('C'+'APS')+r'\b', 'Cr[eé]dit '+'Agricole', 'BPM'+'046926', 'Vincent '+'DELAHAYE', 'FCT/TPS/'+'SMT/ARC']
for p in sorted(base.rglob('*')):
    if not p.is_file() or p.suffix not in ('.md','.yaml','.yml','.mmd','.py','.sh'):
        continue
    t=p.read_text(encoding='utf-8')
    for phrase in forbidden:
        if re.search(phrase,t,re.I):problems.append(f'{p.relative_to(base)} includes forbidden marker')
    if p.suffix=='.md':
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',t):
            if target.startswith(('https://','http://','#','mailto:')):continue
            local=(p.parent/target.split('#')[0]).resolve()
            if not local.exists():problems.append(f'{p.relative_to(base)} -> missing {target}')
required=['README.md','SOURCES.md','LICENSE','docs/00-cadrage/exigences-tracabilite.md','docs/03-architecture/hld-cible.md','docs/06-trajectoire/roadmap-migration.md','docs/07-validation/matrice-de-recette.md','diagrams/03-sequences-paiement.mmd','contracts/openapi-payment-facade.yaml','poc/README.md']
for x in required:
    if not (base/x).is_file():problems.append(f'Missing {x}')
print('Files:',sum(1 for p in base.rglob('*') if p.is_file()),'Markdown:',len(md),'Issues:',len(problems))
for x in problems:print('ERROR',x)
sys.exit(bool(problems))
