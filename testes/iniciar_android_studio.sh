#!/usr/bin/env bash
set -euo pipefail
PROJETO_MOBILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$PROJETO_MOBILE/testes/ambiente_android.sh"
export DISPLAY=:99
export XDG_RUNTIME_DIR="$PROJETO_MOBILE/.ferramentas/xdg-runtime"
mkdir -p "$XDG_RUNTIME_DIR"
chmod 700 "$XDG_RUNTIME_DIR"
export LD_LIBRARY_PATH="$PROJETO_MOBILE/.ferramentas/gui/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
export XDG_CONFIG_HOME="$PROJETO_MOBILE/.ferramentas/config"
export STUDIO_PROPERTIES="$PROJETO_MOBILE/.ferramentas/studio.properties"
export STUDIO_VM_OPTIONS="$PROJETO_MOBILE/.ferramentas/studio.vmoptions"
export STUDIO_JDK="$PROJETO_MOBILE/.ferramentas/android-studio/jbr"
mkdir -p "$PROJETO_MOBILE/.ferramentas/studio-config/options"
if [ ! -e "$STUDIO_PROPERTIES" ]; then
 cat > "$STUDIO_PROPERTIES" <<EOF
idea.config.path=$PROJETO_MOBILE/.ferramentas/studio-config
idea.system.path=$PROJETO_MOBILE/.ferramentas/studio-system
idea.plugins.path=$PROJETO_MOBILE/.ferramentas/studio-plugins
idea.log.path=$PROJETO_MOBILE/.ferramentas/studio-log
disable.android.first.run=true
idea.initially.ask.config=false
EOF
fi
if [ ! -e "$STUDIO_VM_OPTIONS" ]; then
 cp "$PROJETO_MOBILE/.ferramentas/android-studio/bin/studio64.vmoptions" "$STUDIO_VM_OPTIONS"
 cat >> "$STUDIO_VM_OPTIONS" <<EOF
-Dsun.java2d.opengl=false
-Dsun.java2d.uiScale=1.25
-Ddisable.android.first.run=true
-Dide.show.tips.on.startup=false
EOF
fi
exec "$PROJETO_MOBILE/.ferramentas/android-studio/bin/studio.sh" "$PROJETO_MOBILE/android-nativo"
