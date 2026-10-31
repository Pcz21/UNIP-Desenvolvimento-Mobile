"""Atualiza a página de evidências com capturas verificadas por testes reais."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
legendas={
'01-aplicativo.png':'Tela inicial com texto alterado',
'01-login.png':'Login XML com título, e-mail, senha e botão',
'02-interacao.png':'Saudação da interação demonstrativa',
'01-menu.png':'Menu com quatro opções e ícones',
'02-cadastro.png':'Destino Cadastro',
'03-consultar.png':'Destino Consultar',
'04-configuracoes.png':'Diálogo Configurações',
'01-nenhuma.png':'Resultado sem selecionar tecnologias',
'02-uma.png':'Resultado com uma tecnologia selecionada',
'03-multiplas.png':'Resultado com múltiplas tecnologias',
'01-salvo.png':'Nome salvo no armazenamento local',
'02-recuperado.png':'Nome recuperado após forçar parada e reabrir',
'01-obrigatorios.png':'Erros dos campos obrigatórios',
'02-email-invalido.png':'Erro de e-mail inválido',
'03-senha-curta.png':'Erro de senha inferior a seis caracteres',
'04-valido.png':'Entradas aceitas pela validação local'}

partial='--parcial' in sys.argv
for n in [x for x in sys.argv[1:] if x!='--parcial']:
 log=R/'testes'/(f'android-parcial-{n}.json' if partial else f'android-funcional-{n}.json')
 data=json.loads(log.read_text());p=R/'relatorios/fontes'/f'relatorio{n}.json';m=json.loads(p.read_text())
 images=[]
 for t in data['testes']:
  if t.get('captura'):
   path=f"evidencias/relatorio{n}/"+t['captura'];assert (R/path).exists()
   images.append({'path':path,'caption':f"Figura {len(images)+1} — {legendas.get(t['captura'],t['esperado'])}. Fonte: execução própria."})
 refs=m['pages'][-1];idx=next(i for i,x in enumerate(refs) if x==['h','Referências']);refs=refs[idx:]
 page=[['h','Testes funcionais e evidências reais'],['p',f"{len(data['testes'])} verificações aprovadas via ADB e UI Automator. Plataforma: {data['plataforma']}. Resultado conferido pela árvore da interface antes de cada captura; PNG original preservado. Registro: testes/android-funcional-{n}.json."]]
 if partial:
  page += [['grid',images],['p','TESTE EM ANDAMENTO — estas capturas são reais; a atividade permanece parcial até concluir os demais cenários. EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA para os estados ainda não testados.']]
 elif n=='01':
  page += [['grid',images],['p','EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA: interface real do Android Studio e exploração visual da estrutura na IDE. A captura acima comprova apenas o aplicativo no emulador; a IDE não foi aberta. Status parcialmente concluído.']]
 else:
  page += [['grid',images],['p','Execução e capturas concluídas nesta plataforma. Identificação acadêmica e local da aula prática permanecem a preencher; não foi declarada presença em laboratório.']]
  if n=='06':page.insert(2,['p','Persistência confirmada: nome fictício salvo, processo encerrado com am force-stop e Activity reaberta; o texto Nome recuperado foi conferido. Os dados da aplicação não foram apagados entre essas etapas.'])
 m['pages'][-1]=page+refs
 p.write_text(json.dumps(m,ensure_ascii=False,indent=2))
