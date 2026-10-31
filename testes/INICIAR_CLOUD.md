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

## Flutter — pendência externa explícita

O download oficial recebeu 403 de `storage.googleapis.com`. Há domínios adicionais no rascunho para revisão; a política atual não foi alterada por esse salvamento. Não tente contornar o proxy. Depois de a configuração ser aplicada, teste o acesso novamente; então execute `python testes/preparar_flutter.py` e `bash testes/flutter_validar.sh`. O script fixa Flutter 3.35.7 e verifica SHA-256 oficial. Preserve TLS e checksums.

Para iniciar um app: exporte `PATH="$PWD/.ferramentas/flutter/bin:$PATH"` e `PUB_CACHE="$PWD/.ferramentas/pub-cache"`, entre em `flutter/relatorio03-login` ou `flutter/relatorio08-senhas` e use `flutter run -d web-server --web-hostname 127.0.0.1 --web-port 8763`. Alternativamente, sirva `build/web` após build aprovado. Use Chromium para testes e PNG reais; não apresente links localhost como prévias públicas. DartPad no navegador pessoal é a alternativa sem instalação.

Não declare testes Flutter aprovados só porque o código existe. Incorpore PNG autêntico e legenda nas fontes JSON de cada relatório, regenere e confira DOCX/PDF. Use apenas dados fictícios. Nenhum segredo ou senha pessoal deve ser gravado.
