# Verificação dos documentos

## Aprovado

- Nove DOCX abertos com python-docx; pacotes ZIP íntegros e imagens incorporadas comparadas byte a byte com os PNG originais.
- Nove PDF abertos e renderizados com PyMuPDF; R1 com 2 páginas, R2–R8 com 3 páginas e consolidado com 24 páginas.
- Pixels das 22 imagens incorporadas aos PDF comparados aos PNG originais, incluindo o consolidado.
- Os 16 prints do commit `3988be1` continuam idênticos por SHA-256.

## Tentativa adicional de renderização DOCX

Pacotes oficiais de LibreOffice Writer 25.2 foram baixados com índices Debian assinados e extraídos em `.ferramentas/lo-root`, sem instalação de sistema. A execução local não inicializou o contexto UNO, retornando `DeploymentException` e depois `RuntimeException`, inclusive após correção de caminhos de bootstrap e prioridade das bibliotecas locais. Os logs dessa etapa não representam aprovação de renderização DOCX.

A tentativa foi encerrada sem alterar o sistema ou modificar os documentos para contornar erros. Não se afirma renderização em Microsoft Word/LibreOffice. A aparência e paginação do DOCX devem ser conferidas no editor de entrega; o PDF tem a paginação efetivamente validada. Isso é distinto de uma falha de código dos aplicativos ou de ausência de imagens.
