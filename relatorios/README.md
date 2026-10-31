# Documentos acadêmicos

- `word/relatorio01.docx` a `relatorio08.docx`: oito entregas individuais editáveis.
- `pdf/relatorio01.pdf` a `relatorio08.pdf`: versões PDF.
- `word/consolidado.docx` e `pdf/consolidado.pdf`: capa e oito relatórios para eventual entrega única.
- `fontes/`: conteúdo que gera os dois formatos. O código integral está nos projetos Android/Flutter, como anexo separado para preservar o limite de páginas.

**Antes de entregar:** preencher identificação real e conferir o status no checklist. Um DOCX/PDF existente pode ser parcial. A ausência de print obrigatório é indicada por “EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA”. Captura do emulador não equivale a captura do Android Studio.

Regeneração: `python testes/gerar_relatorios.py` na raiz. Ela sobrescreve os documentos; preserve edições diretas feitas no Word. Para conferir arquivos, páginas dos PDFs e imagens originais incorporadas: `python testes/verificar_entrega.py`. O verificador não renderiza DOCX no Microsoft Word.
