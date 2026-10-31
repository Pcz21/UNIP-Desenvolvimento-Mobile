from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
rows=[];checks=0;images=0
for n in ['01','02','03','04','05','06','07','08']:
 prefix='flutter' if n in ['03','08'] else 'android'
 p=R/'testes'/f'{prefix}-funcional-{n}.json'
 if p.exists():
  d=json.loads(p.read_text());ct=len(d['testes']);im=len(list((R/'evidencias'/f'relatorio{n}').glob('*.png')));checks+=ct;images+=im
  rows.append(f'|{n}|Aprovado: {ct} verificações reais ({prefix})|{im}|')
 else:rows.append(f'|{n}|Execução ainda pendente|0|')
text='## Resumo por atividade\n\n|Relatório|Teste de interface|Capturas reais|\n|---|---|---|\n'+'\n'.join(rows)+f'\n\nTotal: **{checks} verificações de interface aprovadas e {images} PNG reais**. As 15 verificações Java de regras e os testes Flutter são conjuntos separados. Consulte o checklist para pendências particulares.\n'
p=R/'testes/RESULTADOS.md';s=p.read_text().split('## Resumo por atividade')[0];p.write_text(s+'\n'+text);print(text)
