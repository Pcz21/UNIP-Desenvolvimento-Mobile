# Atividades nativas — Java e XML

Abra esta pasta no Android Studio. Gradle Wrapper 8.9, plugin Android 8.7.3, SDK 35 e Java 17 para o código (JDK 21 usado no build). O `local.properties` é específico da máquina; deixe a IDE configurá-lo.

|Relatório|Activity|Layout|
|---|---|---|
|1|MainActivity|activity_main.xml|
|2|LoginActivity|activity_login.xml|
|4|MenuActivity e DestinoActivity|activity_menu.xml e activity_destino.xml|
|5|CheckboxActivity|activity_checkbox.xml|
|6|PreferenciasActivity|activity_preferencias.xml|
|7|ValidacaoActivity|activity_validacao.xml|

Classes: `app/src/main/java/br/edu/unip/mobile/`; layouts: `app/src/main/res/layout/`; textos: `res/values/strings.xml`; ponto de entrada e Activities: `AndroidManifest.xml`.

Todas as telas são acessíveis a partir da MainActivity. Estão exportadas para permitir a execução independente via ADB nesta demonstração didática, sem dados sensíveis; num aplicativo real, restrinja componentes públicos conforme o modelo de segurança. Não há permissão de Internet ou backend. Validação e saudação não autenticam ninguém.

O armazenamento do relatório 6 usa `getSharedPreferences("perfil", MODE_PRIVATE)`, chave `nome`. Apagar os dados ou desinstalar remove o valor; forçar parada não deve removê-lo. Não armazene senhas nesse arquivo.

Para compilar: `./gradlew assembleDebug lintDebug`. Para testes puros Java no Cloud: `bash ../testes/java_validar.sh`. Testes de interface reais, logs e capturas estão em `../testes/` e `../evidencias/`; confira o status em vez de pressupor aprovação. O teste remoto usa Android API 30, sem afirmar cobertura de todas as versões suportadas.
