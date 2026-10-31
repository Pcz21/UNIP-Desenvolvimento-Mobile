"""Confere arquivos, páginas e imagens incorporadas, sem substituir testes de apps."""
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
import json,hashlib,fitz
from PIL import Image
from docx import Document
R=Path(__file__).resolve().parents[1]
def pixels(data):
 im=Image.open(BytesIO(data)).convert('RGB');return (im.size,hashlib.sha256(im.tobytes()).hexdigest())
def imgs(meta):
 out=[]
 for page in meta['pages']:
  for kind,value in page:
   if kind=='image':out.append(value['path'])
   if kind=='grid':out.extend(item['path'] for item in value)
 return out
baseline=json.loads((R/'testes/android-original-sha256.json').read_text())
for original,expected_hash in baseline['imagens'].items():
 assert hashlib.sha256((R/original).read_bytes()).hexdigest()==expected_hash,original+' foi alterado'
assert len(baseline['imagens'])==16
results=[];all_images=[]
for n in ['01','02','03','04','05','06','07','08']:
 m=json.loads((R/f'relatorios/fontes/relatorio{n}.json').read_text());paths=imgs(m);all_images+=paths
 assert {str(p.relative_to(R)) for p in (R/'evidencias'/('relatorio'+n)).glob('*.png')}==set(paths),(n,'PNG não incorporado ao relatório')
 expected={hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}
 docx=R/f'relatorios/word/relatorio{n}.docx';pdf=R/f'relatorios/pdf/relatorio{n}.pdf'
 Document(docx)
 with ZipFile(docx) as z:
  assert z.testzip() is None
  actual={hashlib.sha256(z.read(name)).hexdigest() for name in z.namelist() if name.startswith('word/media/')}
 assert actual==expected,(n,'DOCX: imagens diferentes dos PNG originais')
 d=fitz.open(pdf);maxpages=2 if n=='01' else 3;minpages=1 if n=='01' else 2
 assert minpages<=len(d)<=maxpages,(n,'limite de páginas',len(d))
 expectedpixels={pixels((R/p).read_bytes()) for p in paths};actualpixels=set()
 for pg in d:
  for img in pg.get_images(full=True):actualpixels.add(pixels(d.extract_image(img[0])['image']))
 assert actualpixels==expectedpixels,(n,'PDF: pixels incorporados divergentes')
 text=''.join(pg.get_text() for pg in d)
 assert 'Referências' in text
 if not paths:assert 'EVIDÊNCIA PENDENTE' in text
 results.append({'relatorio':n,'paginas_pdf':len(d),'imagens_originais':len(paths),'imagens_docx_e_pdf':'conferidas','docx':'aberto por python-docx; pacote ZIP íntegro','pdf':'aberto por PyMuPDF'})
pdf=fitz.open(R/'relatorios/pdf/consolidado.pdf')
assert len(pdf)==1+sum(x['paginas_pdf'] for x in results)
combined_pixels=set()
for pg in pdf:
 for img in pg.get_images(full=True):combined_pixels.add(pixels(pdf.extract_image(img[0])['image']))
assert combined_pixels=={pixels((R/p).read_bytes()) for p in all_images},'Imagens do PDF consolidado divergentes'
with ZipFile(R/'artefatos/unip-mobile-debug.apk') as apk:
 assert apk.testzip() is None
 assert {'classes.dex','AndroidManifest.xml','resources.arsc'}<=set(apk.namelist())
with ZipFile(R/'relatorios/word/consolidado.docx') as z:
 assert {hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.startswith('word/media/')}=={hashlib.sha256((R/p).read_bytes()).hexdigest() for p in all_images}
for p in ['CHECKLIST_GERAL.md','README.md','PENDENCIAS_REAIS.md','LEVAR_PARA_FACULDADE.md','artefatos/unip-mobile-debug.apk']:
 assert (R/p).is_file(),p
for official,pages in [('Roteiro.dev.mobile.pdf',17),('Relatório.dev.mobile.pdf',13)]:assert len(fitz.open(R/'documentos_oficiais'/official))==pages
output={'documentos':results,'consolidado_paginas':len(pdf),'verificacao':'aprovada','estrutura_docx':'aprovada','renderizacao_docx':'não concluída: falha de bootstrap UNO do LibreOffice local','pdf_renderizado':'aprovado','imagens_totais':len(all_images),'originais_android_preservados':16,'limite':'DOCX aberto estruturalmente e imagens conferidas; renderização adicional por LibreOffice local falhou no contexto UNO. PDF renderizado, com paginação verificada.'}
(R/'testes/entrega-verificacao.json').write_text(json.dumps(output,ensure_ascii=False,indent=2))
print(json.dumps(output,ensure_ascii=False,indent=2))
