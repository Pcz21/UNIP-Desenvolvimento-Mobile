"""Testes reais via ADB/UI Automator; só captura após confirmar a tela esperada."""
from pathlib import Path
import subprocess as S,xml.etree.ElementTree as E,re,time,json,argparse
ROOT=Path(__file__).resolve().parents[1]
ADB=str(ROOT/'.ferramentas/android-sdk/platform-tools/adb')
PKG='br.edu.unip.mobile'
class Android:
 def __init__(self,n):self.n=n;self.resultados=[];self.d=ROOT/'evidencias'/('relatorio'+n);self.d.mkdir(exist_ok=True)
 def cmd(self,*a,timeout=60):return S.check_output([ADB,*a],timeout=timeout).decode(errors='replace')
 def dump(self):
  self.cmd('shell','uiautomator','dump','/sdcard/unip-window.xml')
  return E.fromstring(self.cmd('shell','cat','/sdcard/unip-window.xml'))
 def espera(self,texto):
  ultimo=''
  for _ in range(5):
   root=self.dump();ultimo='\n'.join(x.attrib.get('text','') for x in root.iter('node'))
   if texto in ultimo:return root
   time.sleep(1)
  raise AssertionError('Tela esperada não encontrada: '+texto+'\n'+ultimo)
 def item(self,id=None,texto=None):
  for node in self.dump().iter('node'):
   if (id and node.attrib.get('resource-id')==PKG+':id/'+id) or (texto and node.attrib.get('text')==texto):return node
  raise AssertionError('Componente não encontrado: '+str(id or texto))
 def clicar(self,id=None,texto=None):
  node=self.item(id,texto);b=list(map(int,re.findall(r'\d+',node.attrib['bounds'])))
  self.cmd('shell','input','tap',str((b[0]+b[2])//2),str((b[1]+b[3])//2))
 def preencher(self,id,texto):
  self.clicar(id=id);self.cmd('shell','input','keyevent','KEYCODE_MOVE_END');self.cmd('shell','input','keyevent','--longpress','KEYCODE_DEL')
  # Os testes começam com campos vazios; limpeza adicional para eventuais valores restaurados.
  self.cmd('shell','input','text',texto.replace(' ','%s'));self.cmd('shell','input','keyevent','KEYCODE_BACK')
 def abrir(self,cls):
  self.cmd('shell','am','force-stop',PKG)
  out=self.cmd('shell','am','start','-W','-n',PKG+'/.'+cls)
  if 'Error' in out:raise RuntimeError(out)
 def verificar(self,texto,arquivo=None):
  self.espera(texto)
  if arquivo:
   png=S.check_output([ADB,'exec-out','screencap','-p'],timeout=60)
   assert png.startswith(b'\x89PNG\r\n\x1a\n')
   (self.d/arquivo).write_bytes(png)
  self.resultados.append({'esperado':texto,'resultado':'aprovado','captura':arquivo})
  (ROOT/'testes'/f'android-parcial-{self.n}.json').write_text(json.dumps({'atividade':self.n,'plataforma':'Emulador Android API 30 x86_64, TCG sem KVM','testes':self.resultados,'status':'parcial'},ensure_ascii=False,indent=2))
  if arquivo:
   S.run(['python',str(ROOT/'testes/incorporar_evidencias.py'),self.n,'--parcial'],check=True)
   S.run(['python',str(ROOT/'testes/gerar_relatorios.py')],check=True)
 def rodar(self):
  n=self.n
  if n=='01':
   self.abrir('MainActivity');self.verificar('Olá! Meu primeiro aplicativo Android em Java e XML.','01-aplicativo.png')
  elif n=='02':
   self.abrir('LoginActivity');self.verificar('Portal UNIP — Login','01-login.png');self.clicar('entrar');self.verificar('Preencha e-mail e senha.')
   self.preencher('email','aluno@example.com');self.preencher('senha','Exemplo123');self.clicar('entrar');self.verificar('Demonstração local, sem autenticação.','02-interacao.png')
  elif n=='04':
   self.abrir('MenuActivity');self.verificar('Menu de atividades','01-menu.png');self.clicar('cadastro');self.verificar('Tela demonstrativa de cadastro.','02-cadastro.png');self.clicar('voltar')
   self.clicar('consultar');self.verificar('Consulta demonstrativa:','03-consultar.png');self.clicar('voltar');self.clicar('configuracoes');self.verificar('Modo didático local.','04-configuracoes.png');self.clicar(texto='OK');self.clicar('sair')
   out=self.cmd('shell','dumpsys','activity','activities')
   if re.search(r'mResumedActivity.*br\.edu\.unip\.mobile',out):raise AssertionError('Sair não encerrou a tarefa')
   self.resultados.append({'esperado':'Sair encerra tarefa','resultado':'aprovado','captura':None})
  elif n=='05':
   self.abrir('CheckboxActivity');self.clicar('verificar');self.verificar('Nenhuma tecnologia selecionada.','01-nenhuma.png')
   self.clicar('tecnologia0');self.clicar('verificar');self.verificar('Tecnologias selecionadas: Java','02-uma.png')
   self.clicar('tecnologia2');self.clicar('verificar');self.verificar('Tecnologias selecionadas: Java, Flutter','03-multiplas.png')
  elif n=='06':
   self.abrir('PreferenciasActivity');self.verificar('Meu nome — armazenamento local')
   # Limpa apenas o campo, preservando o arquivo de preferências para a prova de reinício.
   self.clicar('nome');self.cmd('shell','input','keyevent','KEYCODE_MOVE_END')
   self.cmd('shell','input','keyevent',*(['KEYCODE_DEL']*30))
   self.cmd('shell','input','text','Aluno%sUNIP');self.cmd('shell','input','keyevent','KEYCODE_BACK');self.clicar('salvar');self.verificar('Nome salvo: Aluno UNIP','01-salvo.png')
   self.abrir('PreferenciasActivity');self.verificar('Nome recuperado: Aluno UNIP','02-recuperado.png')
  elif n=='07':
   self.abrir('ValidacaoActivity');self.clicar('validar');self.verificar('E-mail obrigatório.','01-obrigatorios.png')
   self.abrir('ValidacaoActivity');self.preencher('email','invalido');self.preencher('senha','123456');self.clicar('validar');self.verificar('E-mail inválido.','02-email-invalido.png')
   self.abrir('ValidacaoActivity');self.preencher('email','aluno@example.com');self.preencher('senha','12345');self.clicar('validar');self.verificar('Senha deve ter pelo menos 6 caracteres.','03-senha-curta.png')
   self.abrir('ValidacaoActivity');self.preencher('email','aluno@example.com');self.preencher('senha','123456');self.clicar('validar');self.verificar('Dados válidos localmente.','04-valido.png')
  else:raise ValueError(n)
  (ROOT/'testes'/f'android-funcional-{n}.json').write_text(json.dumps({'atividade':n,'plataforma':'Emulador Android API 30 x86_64, TCG sem KVM','testes':self.resultados},ensure_ascii=False,indent=2))
  print(n,len(self.resultados),'verificações funcionais aprovadas',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('atividade',choices=['01','02','04','05','06','07']);args=p.parse_args();Android(args.atividade).rodar()
