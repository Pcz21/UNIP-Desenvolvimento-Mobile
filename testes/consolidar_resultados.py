"""Resumo derivado dos registros reais; não infere execução de código existente."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
rows=[];checks=0;images=0
for n in ['01','02','03','04','05','06','07','08']:
 p=R/'testes'/f'android-funcional-{n}.json'
 if p.exists():
  d=json.loads(p.read_text());ct=len(d['testes']);im=sum(bool(t['captura']) for t in d['testes']);checks+=ct;images+=im
  rows.append(f'|{n}|Aprovado: {ct} verificações reais|{im}|')
 else:rows.append(f'|{n}|Não executado até este resumo|0|')
text='## Resumo por atividade\n\n|Relatório|Teste de interface|Capturas reais|\n|---|---|---|\n'+'\n'.join(rows)+f'\n\nTotal: **{checks} verificações de interface aprovadas e {images} PNG reais**. As 15 verificações Java de regras são um conjunto separado. Relatório 1 ainda requer print da IDE Android Studio; Flutter 3 e 8 continuam pendentes de SDK e execução.\n'
p=R/'testes/RESULTADOS.md';s=p.read_text().split('## Resumo por atividade')[0];p.write_text(s+'\n'+text)
print(text)
