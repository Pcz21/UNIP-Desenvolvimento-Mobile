#!/usr/bin/env bash
set -euo pipefail
PROJETO_MOBILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PATH="$PROJETO_MOBILE/.ferramentas/flutter/bin:$PATH"
export PUB_CACHE="$PROJETO_MOBILE/.ferramentas/pub-cache"
# Somente dados de teste fictícios. Não registrar entradas de senha.
for alvo in relatorio03-login relatorio08-senhas; do
 cd "$PROJETO_MOBILE/flutter/$alvo"
 flutter pub get > "$PROJETO_MOBILE/testes/$alvo-pub.log" 2>&1
 flutter analyze > "$PROJETO_MOBILE/testes/$alvo-analyze.log" 2>&1
 flutter test > "$PROJETO_MOBILE/testes/$alvo-test.log" 2>&1
 flutter build web --no-web-resources-cdn > "$PROJETO_MOBILE/testes/$alvo-build.log" 2>&1
done
