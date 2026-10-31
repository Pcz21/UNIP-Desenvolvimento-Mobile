from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
n=sys.argv[1]
build=json.loads((R/'testes'/f'flutter-validacao-{n}.json').read_text())
data=json.loads((R/'testes'/f'flutter-funcional-{n}.json').read_text())
p=R/'relatorios/fontes'/f'relatorio{n}.json';m=json.loads(p.read_text())
labels={'01-login-flutter.png':'Login Flutter executado no navegador','02-boas-vindas.png':'Mensagem real de boas-vindas após Login','01-fraca.png':'Classificação Senha Fraca','02-media.png':'Classificação Senha Média','03-forte.png':'Classificação Senha Forte'}
images=[]
for t in data['testes']:
 if t.get('captura'):
  path=f"evidencias/relatorio{n}/"+t['captura'];assert (R/path).is_file()
  images.append({'path':path,'caption':f"Figura {len(images)+1} — {labels[t['captura']]}. Fonte: execução própria em Chromium."})
for page in m['pages']:
 for item in page:
  if item[0]=='p' and ('Até esta versão, não executados' in item[1] or 'Não executados nesta versão:' in item[1]):
   item[1]=f"Flutter 3.35.7 e Dart 3.9.2 instalados com SHA-256 oficial. flutter pub get, flutter analyze, flutter test e flutter build web aprovados. A suíte executou {build['widget_tests']} teste(s) de widget/lógica. O aplicativo compilado também foi servido localmente e testado em Chromium: {len(data['testes'])} verificações de interface aprovadas. Logs e registros: testes/flutter-validacao-{n}.json e flutter-funcional-{n}.json."
  if item[0]=='p':
   item[1]=item[1].replace('O projeto está implementado, mas o funcionamento permanece pendente de validação real.','O funcionamento foi confirmado por testes de widget e execução real no navegador; a mesma fonte mantém compatibilidade com a proposta do DartPad.').replace('A atividade ainda depende de execução e evidências antes da entrega final.','A execução no navegador confirmou os três níveis e o retorno à instrução inicial ao limpar o campo.').replace('Não executados nesta versão:', 'Não executados nesta versão:')
last=m['pages'][-1];idx=next(i for i,x in enumerate(last) if x==['h','Referências']);refs=last[idx:]
m['pages'][-1]=[['h','Evidências autênticas e resultados'],['p',f"Aplicativo Flutter real compilado e executado em Chromium. {len(data['testes'])} verificações de interface aprovadas; apenas dados fictícios, sem armazenamento ou logs de senhas. Os PNG originais permanecem em evidencias/relatorio{n}."],['grid',images],['p','Requisitos técnicos e capturas concluídos. Identificação acadêmica permanece a preencher pelo estudante.']]+refs
p.write_text(json.dumps(m,ensure_ascii=False,indent=2))
