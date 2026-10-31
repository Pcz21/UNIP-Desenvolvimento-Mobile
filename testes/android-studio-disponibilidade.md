# Android Studio — situação atual

A limitação inicial foi superada nesta retomada. Android Studio Rabbit 2 | 2026.2.2 foi verificado por SHA-256 oficial e executado em Xvfb :99, com Java2D OpenGL desativado. O projeto existente foi aberto e sincronizado; Manifest, Java, layouts, valores e Gradle foram expostos na árvore, ao lado de MainActivity.java.

Captura autêntica: `evidencias/relatorio01/02-android-studio-estrutura.png`. Registro: `android-studio-evidencia.json`. A imagem foi incorporada ao Relatório 1 e ao consolidado. Os 16 prints Android anteriores e os arquivos versionados do projeto nativo foram preservados.

Os pacotes Debian foram apenas baixados/verificados e extraídos em `.ferramentas/`. Não foram instalados pacotes de sistema. Login Google, telemetria e atualizações do projeto não foram necessários.
