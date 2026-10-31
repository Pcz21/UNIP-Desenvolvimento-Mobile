# Resultados reais

## Ambiente e compilação

- PDFs oficiais lidos integralmente: roteiro, 17 páginas; modelo de relatórios, 13 páginas. Textos preservados em `documentos_oficiais/`.
- Downloads de JDK 21.0.9+10, Gradle 8.9 e ferramentas Android verificados por checksum publicado. TLS permaneceu habilitado.
- Base Android: `assembleDebug` **aprovado**; log `android-base-build.log`.
- Gradle Wrapper entregue: compilação `./gradlew assembleDebug` **aprovada**; log `android-wrapper-build.log`.
- Projeto Android com as seis telas: `assembleDebug` e `lintDebug` **aprovados**; log `android-final-build.log`.
- Android Lint: **0 erros, 10 avisos** (6 SetTextI18n, 2 HardcodedText, 1 DataExtractionRules, 1 MissingApplicationIcon). Arquivo `android-lint.xml`; não foram desativadas regras para passar.
- Testes puros de regras Java: **15 aprovados**, código `TesteRegras.java`, log `java-regras.log`. Cobrem nenhuma/uma/múltiplas tecnologias, e-mail vazio/inválido/válido, espaços laterais, senha vazia, limites 5/6, pontos de código e combinação de erros. Não substituem testes de Activity ou persistência.
- APK de depuração: `artefatos/unip-mobile-debug.apk`, instalado com `Success` no emulador API 30.

## Execução Android

O emulador API 30 x86_64 executa por software, sem `/dev/kvm`. O boot levou aproximadamente 402 segundos. Houve uma primeira falha por aviso de lentidão do System UI; ela não foi contada como sucesso. Após escolher aguardar e estabilizar, passaram a tela inicial, o login XML, a navegação do menu, os três casos de CheckBox e a persistência real após forçar parada. As capturas estão incorporadas nos documentos de cada atividade. As cinco verificações da tela de validação também foram aprovadas: e-mail obrigatório, senha obrigatória, e-mail inválido, senha curta e dados válidos. Consulte `android-funcional-tentativas.md`.

Cada teste funcional concluído gera `android-funcional-NN.json` com os resultados conferidos via UI Automator. Os PNG só são gravados após a presença do texto esperado na árvore da tela. Os arquivos JSON e `CHECKLIST_GERAL.md` são a fonte para as quantidades finais de testes e capturas. A presença apenas de um arquivo de teste não representa aprovação.

## Flutter — retomada concluída

SDK Flutter 3.35.7 / Dart 3.9.2 baixado do Google e verificado pelo SHA-256 oficial. O bloqueio anterior foi superado após publicação do ambiente; também foi corrigido um segmento extra no URL antigo do manifesto.

- Relatório 3: `pub get`, `analyze`, 1 teste de widget e `build web` aprovados. No Chromium, 5 verificações funcionais passaram: tela inicial, campos vazios, e-mail inválido, boas-vindas e limpeza da senha. Duas capturas reais incorporadas.
- Relatório 8: `pub get`, `analyze`, 2 testes de lógica/widget e `build web` aprovados. No Chromium, Fraca, Média, Forte e limpeza do campo passaram. Três capturas reais incorporadas; valores de teste fictícios e campo oculto.
- A automação do login teve falhas iniciais de seleção/sincronização do input semântico. Foram diagnosticadas e corrigidas com eventos reais de teclado, sem alterar o aplicativo ou desativar assertivas. Os logs de tentativa e o resultado final permanecem separados.
- O build emitiu um aviso de fonte Cupertino opcional, não utilizada nas telas; análise, testes e build terminaram aprovados e os ícones Material foram conferidos nas capturas reais. Não foram adicionadas dependências externas de aplicação.

## Android Studio — nova evidência da IDE

Android Studio Rabbit 2 | 2026.2.2 baixado do Google com SHA-256 publicado em Android Developers. Pacotes Xvfb/xdotool assinados do Debian foram extraídos em `.ferramentas/`, sem instalação de sistema. O projeto existente abriu e sincronizou; a árvore foi expandida e MainActivity.java exibida. A captura real X11 está no Relatório 1. Fontes Android e os 16 PNG de `3988be1` foram preservados; não se repetiram atividades nativas. Os 15 testes puros Java disponíveis passaram novamente, em `java-regras-retomada.log`.

## Documentos

Oito DOCX/PDF individuais e um consolidado de cada formato são gerados de fontes comuns em `relatorios/fontes/`. O verificador `verificar_entrega.py` abre os arquivos, confere limites de páginas dos PDFs e compara as imagens incorporadas com os PNG de origem. O DOCX foi aberto por python-docx e conferido estruturalmente. A tentativa adicional de renderizar com LibreOffice local falhou no bootstrap UNO; não foi declarada aprovação dessa etapa. A paginação dos PDFs e as imagens foram verificadas. O resultado final desse verificador está em `entrega-verificacao.json` quando aprovado.

As referências externas registradas em `referencias-verificadas.json` responderam HTTP 200. Foram consultados Dart, código e documentação de API do Flutter e Android Open Source Project e orientações OWASP, além dos materiais UNIP. O registro preserva a data real da consulta, sem inventar data acadêmica.









## Resumo por atividade

|Relatório|Teste de interface|Capturas reais|
|---|---|---|
|01|Aprovado: 1 verificações reais (android)|2|
|02|Aprovado: 3 verificações reais (android)|2|
|03|Aprovado: 5 verificações reais (flutter)|2|
|04|Aprovado: 5 verificações reais (android)|4|
|05|Aprovado: 3 verificações reais (android)|3|
|06|Aprovado: 3 verificações reais (android)|2|
|07|Aprovado: 5 verificações reais (android)|4|
|08|Aprovado: 4 verificações reais (flutter)|3|

Total: **29 verificações de interface aprovadas e 22 PNG reais**. As 15 verificações Java de regras e os testes Flutter são conjuntos separados. Consulte o checklist para pendências particulares.
