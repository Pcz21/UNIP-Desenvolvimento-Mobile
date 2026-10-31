"""DOCX e PDF a partir da mesma estrutura; imagens reais incorporadas em ambos."""
from pathlib import Path
import json, re
from xml.sax.saxutils import escape
from docx import Document
from docx.shared import Inches, Pt, Cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Preformatted, KeepTogether, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
ROOT=Path(__file__).resolve().parents[1]
for style,name in [('','DejaVuSans.ttf'),('-Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont('DejaVu'+style,'/usr/share/fonts/truetype/dejavu/'+name))
pdfmetrics.registerFont(TTFont('Mono','/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))
styles=getSampleStyleSheet()
styles['Normal'].fontName='DejaVu';styles['Normal'].fontSize=10;styles['Normal'].leading=14;styles['Normal'].spaceAfter=7
styles['Heading1'].fontName='DejaVu-Bold';styles['Heading1'].fontSize=15;styles['Heading1'].leading=20
styles['Heading2'].fontName='DejaVu-Bold';styles['Heading2'].fontSize=11;styles['Heading2'].leading=15
styles.add(ParagraphStyle('Codigo',fontName='Mono',fontSize=6.5,leading=8,spaceAfter=8))
styles.add(ParagraphStyle('Legenda',parent=styles['Normal'],fontSize=8,leading=10))
def prepare_doc():
 d=Document();s=d.sections[0];s.page_height=Cm(29.7);s.page_width=Cm(21);s.top_margin=Cm(1.7);s.bottom_margin=Cm(1.7);s.left_margin=Cm(2);s.right_margin=Cm(2)
 n=d.styles['Normal'];n.font.name='Arial';n.font.size=Pt(10);n.paragraph_format.space_after=Pt(7)
 s.header.paragraphs[0].text='UNIP • Instituto de Ciências Exatas e Tecnologia • Desenvolvimento Mobile'
 s.header.paragraphs[0].runs[0].font.size=Pt(8)
 s.footer.paragraphs[0].text='UNIP • Análise e Desenvolvimento de Sistemas • Desenvolvimento Mobile'
 return d
def add(d,story,kind,text):
 if kind=='title':d.add_heading(text,0);story.append(Paragraph(escape(text),styles['Heading1']))
 elif kind=='h':d.add_heading(text,2);story.append(Paragraph(escape(text),styles['Heading2']))
 elif kind=='p':d.add_paragraph(text);story.append(Paragraph(escape(text).replace('\n','<br/>'),styles['Normal']))
 elif kind=='code':
  para=d.add_paragraph();run=para.add_run(text);run.font.name='Consolas';run.font.size=Pt(7)
  story.append(Preformatted(text,styles['Codigo']))
 elif kind=='grid':
  # Mesmos PNG originais, sem fabricar ou alterar pixels. Tabela apenas os dispõe.
  grid=[];dt=d.add_table(rows=0, cols=2)
  for first in range(0,len(text),2):
   row=[];cells=dt.add_row().cells
   for j,item in enumerate(text[first:first+2]):
    path=ROOT/item['path'];w,h=PILImage.open(path).size
    height=250 if len(text)<=2 else 180;width=height*w/h
    if width>200:width=200;height=width*h/w
    row.append([Image(str(path),width=width,height=height),Paragraph(escape(item['caption']),styles['Legenda'])])
    cells[j].paragraphs[0].add_run().add_picture(str(path),height=Inches(height/72))
    cells[j].add_paragraph(item['caption'],style='Caption')
   if len(row)==1:row.append('')
   grid.append(row)
  table=Table(grid,colWidths=[235,235]);table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
  story.append(table)
 elif kind=='image':
  path=ROOT/text['path'];caption=text['caption']
  w,h=PILImage.open(path).size
  width=min(text.get("max_width",440),w);height=width*h/w
  if height>text.get("max_height",420):
   limit=text.get("max_height",420);width*=limit/height;height=limit
  d.add_picture(str(path),width=Inches(width/72));d.add_paragraph(caption,style='Caption')
  story.extend([Image(str(path),width=width,height=height),Paragraph(escape(caption),styles['Legenda'])])
def render_one(meta,d=None,story=None):
 own=d is None
 if own:d=prepare_doc();story=[]
 for i,page in enumerate(meta['pages']):
  if i:d.add_page_break();story.append(PageBreak())
  for kind,text in page:add(d,story,kind,text)
 if own:
  out=f"relatorio{meta['id']}"
  d.save(ROOT/'relatorios/word'/f'{out}.docx')
  SimpleDocTemplate(str(ROOT/'relatorios/pdf'/f'{out}.pdf'),pagesize=(595.28,841.89),leftMargin=55,rightMargin=55,topMargin=45,bottomMargin=45).build(story,onFirstPage=pagina_pdf,onLaterPages=pagina_pdf)
 return d,story
def pagina_pdf(canvas, doc):
 canvas.saveState();canvas.setFont('DejaVu',7);canvas.setFillColor(colors.HexColor('#425466'))
 canvas.drawString(55,823,'UNIP • Instituto de Ciências Exatas e Tecnologia • Desenvolvimento Mobile')
 canvas.drawString(55,23,'Análise e Desenvolvimento de Sistemas • '+str(doc.page))
 canvas.restoreState()
def main():
 metas=[json.loads(p.read_text()) for p in sorted((ROOT/'relatorios/fontes').glob('relatorio*.json'))]
 for meta in metas:render_one(meta)
 if len(metas)==8:
  d=prepare_doc();story=[]
  for kind,text in [('title','UNIVERSIDADE PAULISTA — UNIP'),('h','Análise e Desenvolvimento de Sistemas'),('h','Desenvolvimento Mobile'),('p','Relatórios das oito atividades práticas'),('p','Nome: [PREENCHER]\nRA: [PREENCHER]\nPolo de matrícula: [PREENCHER]\nLocal da realização da aula prática: [PREENCHER]\nData acadêmica: [PREENCHER]'),('p','Compilação documental. Consultar o status de cada atividade; evidências obrigatórias pendentes impedem a conclusão acadêmica.')]:add(d,story,kind,text)
  for m in metas:
   d.add_page_break();story.append(PageBreak());render_one(m,d,story)
  d.save(ROOT/'relatorios/word/consolidado.docx')
  SimpleDocTemplate(str(ROOT/'relatorios/pdf/consolidado.pdf'),pagesize=(595.28,841.89),leftMargin=55,rightMargin=55,topMargin=45,bottomMargin=45).build(story,onFirstPage=pagina_pdf,onLaterPages=pagina_pdf)
if __name__=='__main__':main()
