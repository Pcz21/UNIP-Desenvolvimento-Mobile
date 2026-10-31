"""Automação preparada, AINDA NÃO EXECUTADA: requer build Flutter web real.
Uso: python testes/flutter_capturas.py 03 (ou 08), após flutter_validar.sh.
Não usa HTML substituto nem gera imagens; captura somente o Flutter renderizado.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
import argparse,json,shutil,subprocess
from playwright.sync_api import sync_playwright,expect
R=Path(__file__).resolve().parents[1]
def main(n):
 name={'03':'relatorio03-login','08':'relatorio08-senhas'}[n]
 build=R/'flutter'/name/'build/web'
 if not (build/'main.dart.js').is_file():raise RuntimeError('Build Flutter web ausente. Execute flutter_validar.sh e confira seus resultados.')
 out=R/'evidencias'/('relatorio'+n);out.mkdir(exist_ok=True);results=[]
 class Handler(SimpleHTTPRequestHandler):
  def log_message(self,*args):pass
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(build)))
 thread=Thread(target=server.serve_forever,daemon=True);thread.start()
 def record(page,text,file):
  expect(page.get_by_text(text,exact=True)).to_be_visible(timeout=30000)
  page.screenshot(path=str(out/file),full_page=True)
  results.append({'esperado':text,'resultado':'aprovado','captura':file})
 try:
  with sync_playwright() as pw:
   browser=pw.chromium.launch(executable_path=shutil.which('chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader'])
   page=browser.new_page(viewport={'width':960,'height':800},locale='pt-BR')
   page.goto(f'http://127.0.0.1:{server.server_port}',wait_until='networkidle',timeout=90000)
   page.locator('flt-semantics-placeholder').first.evaluate('(el) => el.click()',timeout=30000)
   if n=='03':
    expect(page.get_by_role('textbox',name='E-mail',exact=True)).to_be_visible(timeout=30000)
    page.screenshot(path=str(out/'01-login-flutter.png'),full_page=True)
    results.append({'esperado':'Campos E-mail e Senha e botão Login','resultado':'aprovado','captura':'01-login-flutter.png'})
    page.get_by_role('button',name='Login',exact=True).click()
    expect(page.get_by_text('Preencha e-mail e senha.',exact=True)).to_be_visible()
    page.get_by_role('textbox',name='E-mail',exact=True).fill('invalido')
    page.get_by_role('textbox',name='Senha',exact=True).fill('Exemplo123')
    page.get_by_role('button',name='Login',exact=True).click()
    expect(page.get_by_text('Informe um e-mail válido.',exact=True)).to_be_visible()
    page.get_by_role('textbox',name='E-mail',exact=True).fill('aluno@example.com')
    page.get_by_role('button',name='Login',exact=True).click()
    record(page,'Bem-vindo(a), aluno@example.com!','02-boas-vindas.png')
   else:
    field=page.get_by_role('textbox',name='Senha',exact=True)
    for value,label,file in [('abc','Senha Fraca','01-fraca.png'),('Abcdef12','Senha Média','02-media.png'),('Abcdef12345!','Senha Forte','03-forte.png')]:
     field.fill(value);record(page,label,file)
    field.fill('');expect(page.get_by_text('Digite uma senha para analisar.',exact=True)).to_be_visible()
   browser.close()
 finally:server.shutdown();server.server_close()
 (R/'testes'/f'flutter-funcional-{n}.json').write_text(json.dumps({'atividade':n,'plataforma':'Flutter web real em Chromium headless','testes':results},ensure_ascii=False,indent=2))
 print(n,'testes reais de navegador aprovados; inserir as imagens no relatório e revisar fontes JSON.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('atividade',choices=['03','08']);main(p.parse_args().atividade)
