from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'CHECKLIST_GERAL.md';s=p.read_text().split('## Situação verificada')[0]+'## Situação verificada\n\n'
s+='|Relatório|Código desenvolvido|Compilação realizada|Aplicativo executado|Testes realizados|Prints reais|Capturas inseridas|Word gerado|PDF gerado|Pendências|Status|\n|---|---|---|---|---|---|---|---|---|---|---|\n'
for n in ['01','02','03','04','05','06','07','08']:
 native=n not in ['03','08'];log=R/'testes'/f'android-funcional-{n}.json';ok=log.exists();imgs=list((R/'evidencias'/f'relatorio{n}').glob('*.png'));ct=len(imgs)
 testes=f"{len(json.loads(log.read_text())['testes'])} verificações de interface aprovadas" if ok else ('15 testes compartilhados de regras Java (R5/R7); interface não testada' if n in ['05','07'] else 'não executados')
 pend='Preencher identificação acadêmica'
 if n=='01':pend+='; print real da IDE Android Studio e exploração da estrutura'
 if not ok:pend+=('; executar e capturar emulador' if native else '; liberar storage.googleapis.com, instalar SDK, compilar, testar e capturar Flutter')
 status='concluído' if ok and n!='01' else 'parcialmente concluído'
 s+=f"|{n}|sim|{'sim' if native else 'não'}|{'sim' if ok else 'não'}|{testes}|{ct}|{'sim' if ok and ct else 'não'}|sim|sim|{pend}|{status}|\n"
import re
for n in ['02','04','05','06','07']:
 if (R/'testes'/f'android-funcional-{n}.json').exists():
  pattern=r'(### Relatório '+n+r' — .*?\n\nFonte: .*?\n\n)- \[ \]'
  s=re.sub(pattern,lambda m:m.group(1)+'- [x]',s,flags=re.S)
p.write_text(s)
