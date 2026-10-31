# Checklist geral — Desenvolvimento Mobile

## Fontes e regras

Leitura integral: Roteiro.dev.mobile.pdf (17 páginas) e Relatório.dev.mobile.pdf (13 páginas). Textos extraídos preservados em documentos_oficiais. Os pesos abaixo pertencem a rubricas diferentes; nenhuma foi substituída pela outra. Requisitos adicionais do pedido (testes, complexidade, versões editáveis e continuidade) complementam os PDFs.

- [ ] Identificação: nome, RA, polo e local reais, a preencher; não declarar presença ou datas acadêmicas não informadas.
- [ ] R1: 1–2 páginas; R2–R8: 2–3 páginas; teoria, prática, códigos, referências ABNT e conclusões específicas.
- [ ] Evidências autênticas incorporadas e legendadas imediatamente; sem captura, usar EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA.
- [ ] Oito DOCX/PDF, consolidado com capa, códigos completos separados, testes e guia de laboratório.
- [ ] Conferir páginas/imagens/abertura e salvar no GitHub.

## Requisitos e critérios antes do desenvolvimento

### Relatório 01 — Conhecendo o Android Studio

Fonte: Roteiro pp. 2–4; relatório pp. 2–3.

- [ ] Criar projeto; alterar texto; executar; explicar IDE, Activity, XML, Manifest, Gradle, res e Java; prints reais da IDE e estrutura.

Rubrica do roteiro: Instalação 3; criação 3; execução 2; relatório 2.

Rubrica do relatório: Teoria 2; ambiente 3; criação/execução 3; relatório 2.

### Relatório 02 — Login XML

Fonte: Roteiro pp. 5–7; relatório pp. 4–5.

- [x] TextView, EditText (e-mail e senha), Button Entrar, LinearLayout e título; cores/espaços; interação local; XML, print e explicação.

Rubrica do roteiro: XML 3; visual 3; funcionamento 2; relatório 2.

Rubrica do relatório: Teoria 2; interface 3; funcionamento 3; relatório 2.

### Relatório 03 — Login Flutter

Fonte: Roteiro pp. 8–9; relatório pp. 6–7.

- [x] MaterialApp, Scaffold, TextField, ElevatedButton; e-mail/senha/Login/boas-vindas; código Dart e captura; explicar Flutter, Dart e widgets; comparar nativo/Flutter e vantagens.

Rubrica do roteiro: Estrutura 3; widgets 3; funcionamento 2; relatório 2.

Rubrica do relatório: Clareza 2; conceitos 3; interface 3; criatividade/melhorias 2.

### Relatório 04 — Menu XML

Fonte: Roteiro pp. 10–11; relatório pp. 8–9.

- [x] Cadastro, Consultar, Configurações, Sair; botões, ícones, XML; ações funcionais; XML/print/explicação; teoria de navegação e conclusão sobre experiência do usuário.

Rubrica do roteiro: Organização 3; componentes 3; funcionamento 2; relatório 2.

Rubrica do relatório: Conceitos 2; menu 3; funcionamento 3; relatório 2.

### Relatório 05 — CheckBox

Fonte: Roteiro pp. 12–13; relatório p. 10.

- [x] Pergunta Quais tecnologias você conhece?; Java/Kotlin/Flutter/Python; Verificar Resposta; capturar escolhas; Java e XML completos; prints; usos práticos e formulários; testes nenhuma/uma/múltiplas.

Rubrica do roteiro: CheckBox 4; lógica 3; interface 2; relatório 1.

Rubrica do relatório: Componente 3; lógica 3; visual 2; relatório 2.

### Relatório 06 — SharedPreferences

Fonte: Roteiro p. 14; relatório p. 11.

- [ ] Receber nome; salvar localmente; recuperar na reabertura; código e prints de salvamento/recuperação; teoria armazenamento local/SharedPreferences; distinguir temporário/persistente; testar reinício.

Rubrica do roteiro: Salvar 4; recuperar 3; interface 2; relatório 1.

Rubrica do relatório: Teoria 2; implementação 4; funcionamento 2; relatório 2.

### Relatório 07 — Validações

Fonte: Roteiro p. 15; relatório p. 12.

- [ ] Vazio obrigatório; e-mail inválido; senha menor que seis caracteres; mensagens específicas; código/prints/lógica; teoria segurança, validação, autenticação; casos inválidos/válidos; validação local não autentica.

Rubrica do roteiro: Validações 4; funcionamento 3; interface 2; relatório 1.

Rubrica do relatório: Conceitos 3; validações 3; funcionamento 2; relatório 2.

### Relatório 08 — Senhas Flutter

Fonte: Roteiro pp. 16–17; relatório p. 13.

- [ ] Receber senha; analisar tamanho e complexidade; Fraca/Média/Forte; atualização visual; Dart/captura/lógica; critérios numéricos explícitos; teoria widgets/validação/segurança; conclusão aplicações reais; três níveis testados; sem logs de senhas.

Rubrica do roteiro: Lógica 4; interface 3; funcionamento 2; relatório 1.

Rubrica do relatório: Teoria 3; lógica 3; funcionamento 2; relatório 2.

## Situação verificada

|Relatório|Código desenvolvido|Compilação realizada|Aplicativo executado|Testes realizados|Prints reais|Capturas inseridas|Word gerado|PDF gerado|Pendências|Status|
|---|---|---|---|---|---|---|---|---|---|---|
|01|sim|sim|sim|1 verificações de interface aprovadas|1|sim|sim|sim|Preencher identificação acadêmica; print real da IDE Android Studio e exploração da estrutura|parcialmente concluído|
|02|sim|sim|sim|3 verificações de interface aprovadas|2|sim|sim|sim|Preencher identificação acadêmica|concluído|
|03|sim|não|não|não executados|0|não|sim|sim|Preencher identificação acadêmica; liberar storage.googleapis.com, instalar SDK, compilar, testar e capturar Flutter|parcialmente concluído|
|04|sim|sim|sim|5 verificações de interface aprovadas|4|sim|sim|sim|Preencher identificação acadêmica|concluído|
|05|sim|sim|não|15 testes compartilhados de regras Java (R5/R7); interface não testada|0|não|sim|sim|Preencher identificação acadêmica; executar e capturar emulador|parcialmente concluído|
|06|sim|sim|não|não executados|0|não|sim|sim|Preencher identificação acadêmica; executar e capturar emulador|parcialmente concluído|
|07|sim|sim|não|15 testes compartilhados de regras Java (R5/R7); interface não testada|0|não|sim|sim|Preencher identificação acadêmica; executar e capturar emulador|parcialmente concluído|
|08|sim|não|não|não executados|0|não|sim|sim|Preencher identificação acadêmica; liberar storage.googleapis.com, instalar SDK, compilar, testar e capturar Flutter|parcialmente concluído|
