# Pendências reais — Desenvolvimento Mobile

## Situação técnica

As oito implementações e os oito relatórios possuem as evidências obrigatórias de execução. Os relatórios 3 e 8 foram compilados, testados e executados como Flutter web real; o Relatório 1 recebeu uma captura autêntica do Android Studio com o projeto existente. Não há pendência de código, execução ou captura exigida nos roteiros.

Há **22 PNG reais incorporados em DOCX/PDF**, incluindo os 16 PNG Android do commit `3988be1`, preservados byte a byte. Os arquivos Android versionados não foram alterados; suas atividades concluídas não foram refeitas.

## Antes da entrega acadêmica

1. **Identificação pessoal:** preencher nome, RA, polo, local e data acadêmica reais. Esses dados não foram fornecidos e permanecem como `[PREENCHER]`. O trabalho remoto não comprova participação presencial.
2. **DOCX no editor final:** os nove arquivos foram abertos estruturalmente por python-docx, tiveram ZIP e imagens incorporadas conferidos. A tentativa adicional de renderização com LibreOffice extraído no Cloud falhou no bootstrap UNO (`DeploymentException`/`RuntimeException`), sem instalação de sistema. Portanto, não se afirma que houve renderização no Microsoft Word ou LibreOffice. Confira a aparência e a paginação ao abrir no editor de entrega. Os **PDFs foram renderizados e verificados**, com R1 em 2 páginas, R2–R8 em 3 páginas e consolidado em 24 páginas.
3. **Forma de entrega e prazo:** confirmar com o docente a entrega individual ou consolidada, o prazo não informado e a adequação da execução Flutter web/DartPad. Os dois PDFs oficiais têm rubricas distintas, preservadas no checklist.

## Limites documentados, sem exigir novos testes para estes roteiros

Os testes nativos anteriores usam Android API 30; não se afirma cobertura de todos os dispositivos e versões. Os novos testes Flutter usam Chromium, além das suítes de widget/lógica. O classificador de senhas é uma heurística didática e o login não autentica em servidor.

Nenhuma imagem foi fabricada e nenhuma senha pessoal foi utilizada. O ambiente não foi republicado pelo agente; a entrega está preservada em commits na branch `main`.
