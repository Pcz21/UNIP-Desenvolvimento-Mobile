#!/usr/bin/env bash
# Usar: source testes/ambiente_android.sh, a partir de qualquer diretório.
PROJETO_MOBILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export JAVA_HOME="$PROJETO_MOBILE/.ferramentas/jdk-21.0.9+10"
export ANDROID_HOME="$PROJETO_MOBILE/.ferramentas/android-sdk"
export ANDROID_SDK_ROOT="$ANDROID_HOME"
export GRADLE_USER_HOME="$PROJETO_MOBILE/.ferramentas/gradle-home"
export PATH="$JAVA_HOME/bin:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PROJETO_MOBILE/.ferramentas/gradle-8.9/bin:$PATH"
export JAVA_TOOL_OPTIONS="-Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts -Dhttps.proxyHost=proxy -Dhttps.proxyPort=8080 -Dhttp.proxyHost=proxy -Dhttp.proxyPort=8080 -Dhttp.nonProxyHosts=localhost|127.*"
export ANDROID_USER_HOME="$PROJETO_MOBILE/.ferramentas/android-user"
export ANDROID_EMULATOR_HOME="$ANDROID_USER_HOME"
export ANDROID_AVD_HOME="$ANDROID_USER_HOME/avd"
export JAVA_TOOL_OPTIONS="$JAVA_TOOL_OPTIONS -Djava.util.prefs.userRoot=$PROJETO_MOBILE/.ferramentas/java-prefs"
