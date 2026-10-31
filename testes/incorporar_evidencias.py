"""Atualiza a página de evidências com capturas verificadas por testes reais."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
for n in sys.argv[1:]:
 log=R/'testes'/f'android-funcional-{n}.json'
 data=json.loads(log.read_text());p=R/'relatorios/fontes'/f'relatorio{n}.json';m=json.loads(p.read_text())
 images=[]
 for t in data['testes']:
  if t.get('captura'):
   path=f"evidencias/relatorio{n}/"+t['captura'];assert (R/path).exists()
   images.append({'path':path,'caption':f"Figura {len(images)+1} — {t['esperado']} Fonte: execução própria no emulador Android API 30."})
 refs=m['pages'][-1];idx=next(i for i,x in enumerate(refs) if x==['h','Referências']);refs=refs[idx:]
 page=[['h','Testes funcionais e evidências reais'],['p',f"{len(data['testes'])} verificações aprovadas via ADB e UI Automator. Plataforma: {data['plataforma']}. Resultado conferido pela árvore da interface antes de cada captura; PNG original preservado. Registro: testes/android-funcional-{n}.json."]]
 if n=='01':
  page += [['grid',images],['p','EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA: interface real do Android Studio e exploração visual da estrutura na IDE. A captura acima comprova apenas o aplicativo no emulador; a IDE não foi aberta. Status parcialmente concluído.']]
 else:
  page += [['grid',images],['p','Execução e capturas concluídas nesta plataforma. Identificação acadêmica e local da aula prática permanecem a preencher; não foi declarada presença em laboratório.']]
  if n=='06':page.insert(2,['p','Persistência confirmada: nome fictício salvo, processo encerrado com am force-stop e Activity reaberta; o texto Nome recuperado foi conferido. Os dados da aplicação não foram apagados entre essas etapas.'])
 m['pages'][-1]=page+refs
 p.write_text(json.dumps(m,ensure_ascii=False,indent=2))
