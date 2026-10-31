from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'CHECKLIST_GERAL.md';s=p.read_text().split('## Situação verificada')[0]+'## Situação verificada\n\n'
s+='Conclusão técnica não preenche dados pessoais nem declara presença no laboratório. Nome, RA, polo, local e data acadêmica permanecem a preencher.\n\n'
s+='|Relatório|Código desenvolvido|Compilação realizada|Aplicativo executado|Testes realizados|Prints reais|Capturas inseridas|Word gerado|PDF gerado|Pendências|Status|\n|---|---|---|---|---|---|---|---|---|---|---|\n'
for n in ['01','02','03','04','05','06','07','08']:
 native=n not in ['03','08'];kind='android' if native else 'flutter';log=R/'testes'/f'{kind}-funcional-{n}.json';ok=log.exists()
 compiled=native
 if not native:
  v=R/'testes'/f'flutter-validacao-{n}.json'
  if v.exists():
   data=json.loads(v.read_text());folder={'03':'relatorio03-login','08':'relatorio08-senhas'}[n]
   compiled=data.get('build_web')=='aprovado' and data['source_sha256']==hashlib.sha256((R/'flutter'/folder/'lib/main.dart').read_bytes()).hexdigest()
 imgs=list((R/'evidencias'/f'relatorio{n}').glob('*.png'));ct=len(imgs)
 testes=f"{len(json.loads(log.read_text())['testes'])} verificações de interface aprovadas" if ok else 'interface pendente'
 if not native and compiled:testes+='; testes Flutter aprovados'
 pend='Preencher identificação acadêmica'
 studio=(R/'testes/android-studio-evidencia.json').exists()
 complete=ok and compiled and (n!='01' or studio)
 if n=='01' and not studio:pend+='; captura real da IDE Android Studio'
 if not ok:pend+='; concluir execução, testes e capturas reais'
 status='concluído' if complete else 'parcialmente concluído'
 s+=f"|{n}|sim|{'sim' if compiled else 'não'}|{'sim' if ok else 'não'}|{testes}|{ct}|{'sim' if ok and ct else 'não'}|sim|sim|{pend}|{status}|\n"
 if complete:
  pattern=r'(### Relatório '+n+r' — .*?\n\nFonte: .*?\n\n)- \[ \]'
  s=re.sub(pattern,lambda m:m.group(1)+'- [x]',s,flags=re.S)
p.write_text(s)
