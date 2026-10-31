# Iniciar o trabalho no Cloud

Use o checkout existente em `/workspace/UNIP-Desenvolvimento-Mobile`: cada tarefa já é isolada; não crie worktree. Leia README.md, CHECKLIST_GERAL.md, PENDENCIAS_REAIS.md e testes/RESULTADOS.md antes de atribuir sucesso a alguma atividade. Todas as ferramentas adicionais ficam em `.ferramentas/`; preserve alterações do usuário.

## Android — compilação e testes

1. `cd /workspace/UNIP-Desenvolvimento-Mobile` e `source testes/ambiente_android.sh`.
2. Execute `cd android-nativo && ./gradlew --no-daemon assembleDebug lintDebug`; volte ao diretório raiz e execute `bash testes/java_validar.sh`. Sucesso deve ser observado, não inferido dos logs antigos.
3. APK em `android-nativo/app/build/outputs/apk/debug/app-debug.apk`. A cópia entregue fica em `artefatos/`.
4. Para execução, verifique `adb devices` e reutilize apenas o emulador deste projeto ou dispositivo autorizado. Os processos não sobrevivem necessariamente à restauração da máquina.
5. Se precisar iniciar o emulador, instale `sdkmanager --sdk_root="$ANDROID_HOME" 'emulator' 'system-images;android-30;default;x86_64'`. A imagem atual fica no SDK local. Crie AVD somente se não existir: `printf 'no\n' | "$ANDROID_HOME/cmdline-tools/16.0/bin/avdmanager" create avd -n unip_api30 -k 'system-images;android-30;default;x86_64' -p "$ANDROID_AVD_HOME/unip_api30.avd"`. O avdmanager 16 pode ser preparado por `python testes/instalar_android_fixo.py`.
6. Inicie `"$ANDROID_HOME/emulator/emulator" -avd unip_api30 -no-window -no-audio -no-boot-anim -accel off -gpu swiftshader -memory 2048 -cores 2 -no-snapshot -no-metrics`, com log no projeto. Não dependa de `/dev/kvm`. Limite a tentativa de boot a 10 minutos; confira `adb shell getprop sys.boot_completed` = `1` e disponibilidade dos serviços. O primeiro boot real levou cerca de 402 segundos. Um aviso System UI isn't responding já ocorreu; não conte isso como sucesso.
7. Instale com `adb install -r android-nativo/app/build/outputs/apk/debug/app-debug.apk`. Execute `python testes/android_funcional.py NN` para 01, 02, 04, 05, 06 ou 07, uma atividade por vez. Cada JSON comprova resultados daquele teste; screenshots só são aceitos após confirmar a interface.
8. Após cada atividade aprovada: `python testes/incorporar_evidencias.py NN`, `python testes/gerar_relatorios.py`, `python testes/atualizar_status.py` e `python testes/verificar_entrega.py`. Não apague preferências entre salvar e reabrir no teste 6. Não declare print da IDE a partir do emulador.

## Flutter — SDK e execução concluídos

Flutter 3.35.7 / Dart 3.9.2 estão em `.ferramentas/flutter`; os dois projetos têm pubspec.lock e validação aprovada. Se faltar o SDK numa nova máquina, execute `python testes/preparar_flutter.py`, que verifica SHA-256 oficial. Configure `PATH`, `PUB_CACHE` e `XDG_CONFIG_HOME` conforme `testes/flutter_validar.sh`. Não contorne proxy ou verificação TLS.

Para repetir somente a validação Flutter: `bash testes/flutter_validar.sh`; registre cada alvo com `python testes/registrar_flutter.py 03` e `08`. Para execução e captura reais: `python testes/flutter_capturas.py 03` ou `08`; a automação serve o build web e usa teclado real no Chromium. Em seguida execute `python testes/incorporar_flutter.py NN`, regenere os documentos e valide-os. Não interprete código de teste existente como aprovação de uma nova rodada.

## Android Studio em display virtual

A IDE foi executada de verdade e a captura já está incorporada ao Relatório 1. Distribuição: `testes/preparar_android_studio.py`, com hash oficial. O Xvfb e xdotool ficam em `.ferramentas/gui`, extraídos de pacotes Debian assinados. O script `testes/preparar_display_local.py` prepara uma configuração APT inteiramente local; consulte os logs de download e o guia no repositório.

Inicie o display :99 somente se não estiver ativo e, depois, use `bash testes/iniciar_android_studio.sh`. O script aponta configurações/cache para `.ferramentas/`, desativa Java2D OpenGL e abre o projeto existente. Não crie projeto novo nem atualize AGP/Gradle para repetir a captura. Dispense login Google opcional; não é preciso inserir credenciais. A sincronização foi concluída sem alterar fontes Android.

## Documentos

`python testes/gerar_relatorios.py` sobrescreve DOCX/PDF a partir de `relatorios/fontes/`; preserve edições manuais antes de regenerar. `python testes/verificar_entrega.py` confere páginas PDF, abertura estrutural dos DOCX e imagens originais. A tentativa adicional de renderização DOCX com LibreOffice local falhou no bootstrap UNO; veja `testes/documentos-renderizacao.md`. Não declare essa etapa aprovada.
