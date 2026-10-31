#!/usr/bin/env bash
set -euo pipefail
PROJETO_MOBILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$PROJETO_MOBILE/testes/ambiente_android.sh"
mkdir -p "$PROJETO_MOBILE/.ferramentas/classes"
javac -d "$PROJETO_MOBILE/.ferramentas/classes" "$PROJETO_MOBILE/android-nativo/app/src/main/java/br/edu/unip/mobile/Regras.java" "$PROJETO_MOBILE/testes/TesteRegras.java"
java -cp "$PROJETO_MOBILE/.ferramentas/classes" TesteRegras
