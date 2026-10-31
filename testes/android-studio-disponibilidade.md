# Android Studio — verificação de disponibilidade

- Não há executável Android Studio instalado no ambiente inspecionado.
- Não há `DISPLAY` configurado, `Xvfb`, `xvfb-run` ou `xdotool` disponíveis.
- Pillow tem suporte XCB, mas isso não fornece um servidor gráfico.
- `/var/lib/apt/lists` está vazio. A consulta `apt-cache policy xvfb` não identificou pacote preparado e reportou arquivo de configuração de APT sem permissão de leitura. Nenhum pacote de sistema foi instalado e não houve alterações de configuração fora do projeto.
- Os metadados públicos de atualização em `dl.google.com/android/studio/patches/updates.xml` responderam HTTP 200, mas remetem ao site `developer.android.com` para o instalador. Esse domínio consta do rascunho de rede e ainda não integra a política aplicada.

**Conclusão limitada:** a IDE gráfica não foi preparada nem executada nesta sessão. Não se afirma que seja impossível configurá-la futuramente. A execução real do aplicativo por emulador foi obtida e documentada separadamente. Falta o print obrigatório da IDE e da estrutura explorada nela; coletar em um Android Studio disponível no laboratório, ou após preparar uma sessão gráfica autorizada no Cloud. Não usar captura de código, de build ou do emulador como se fosse a IDE.
