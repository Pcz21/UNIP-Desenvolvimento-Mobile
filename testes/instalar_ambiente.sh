#!/usr/bin/env bash
set -euo pipefail
cd /workspace/UNIP-Desenvolvimento-Mobile
python testes/preparar_android.py
source testes/ambiente_android.sh
sdkmanager --sdk_root="$ANDROID_HOME" 'platform-tools' 'platforms;android-35' 'build-tools;35.0.0'
printf 'sdk.dir=%s\n' "$ANDROID_HOME" > android-nativo/local.properties
cd android-nativo
./gradlew --no-daemon assembleDebug lintDebug
# Flutter está validado; preparar o SDK e repetir as verificações se necessário.
cd /workspace/UNIP-Desenvolvimento-Mobile
python testes/preparar_flutter.py
bash testes/flutter_validar.sh
