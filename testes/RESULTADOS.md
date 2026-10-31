# Resultados reais

## Ambiente e compilação

- PDFs oficiais lidos integralmente: roteiro, 17 páginas; modelo de relatórios, 13 páginas. Textos preservados em `documentos_oficiais/`.
- Downloads de JDK 21.0.9+10, Gradle 8.9 e ferramentas Android verificados por checksum publicado. TLS permaneceu habilitado.
- Base Android: `assembleDebug` **aprovado**; log `android-base-build.log`.
- Projeto Android com as seis telas: `assembleDebug` e `lintDebug` **aprovados**; log `android-final-build.log`.
- Android Lint: **0 erros, 10 avisos** (6 SetTextI18n, 2 HardcodedText, 1 DataExtractionRules, 1 MissingApplicationIcon). Arquivo `android-lint.xml`; não foram desativadas regras para passar.
- Testes puros de regras Java: **15 aprovados**, código `TesteRegras.java`, log `java-regras.log`. Cobrem nenhuma/uma/múltiplas tecnologias, e-mail vazio/inválido/válido, espaços laterais, senha vazia, limites 5/6, pontos de código e combinação de erros. Não substituem testes de Activity ou persistência.
- APK de depuração: `artefatos/unip-mobile-debug.apk`, instalado com `Success` no emulador API 30.

## Execução Android

O emulador API 30 x86_64 executa por software, sem `/dev/kvm`. O boot levou aproximadamente 402 segundos. Houve uma primeira falha por aviso de lentidão do System UI; ela não foi contada como sucesso. Após escolher aguardar e estabilizar, o teste da tela inicial passou e produziu um PNG real. Consulte `android-funcional-tentativas.md`.

Cada teste funcional concluído gera `android-funcional-NN.json` com os resultados conferidos via UI Automator. Os PNG só são gravados após a presença do texto esperado na árvore da tela. Os arquivos JSON e `CHECKLIST_GERAL.md` são a fonte para as quantidades finais de testes e capturas. A presença apenas de um arquivo de teste não representa aprovação.

## Flutter

**Não compilado, não executado, sem captura real nesta versão.** O download do SDK de `storage.googleapis.com` recebeu HTTP 403 do proxy de rede. A configuração adicional está salva no rascunho do ambiente, mas não foi aplicada/publicada pelo usuário. Os testes de widget e de lógica estão escritos, não executados. Nenhuma implementação HTML foi usada para simular Flutter.

## Documentos

Oito DOCX/PDF individuais e um consolidado de cada formato são gerados de fontes comuns em `relatorios/fontes/`. O verificador `verificar_entrega.py` abre os arquivos, confere limites de páginas dos PDFs e compara as imagens incorporadas com os PNG de origem. O DOCX é conferido estruturalmente; não foi renderizado no Microsoft Word. O resultado final desse verificador está em `entrega-verificacao.json` quando aprovado.

As referências externas registradas em `referencias-verificadas.json` responderam HTTP 200. Foram consultados Dart, código e documentação de API do Flutter e Android Open Source Project e orientações OWASP, além dos materiais UNIP. O registro preserva a data real da consulta, sem inventar data acadêmica.
