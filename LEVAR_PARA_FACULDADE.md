# Continuidade no laboratório — Desenvolvimento Mobile

## O que levar

Baixe o repositório pelo GitHub como ZIP, ou use `git clone https://github.com/Pcz21/UNIP-Desenvolvimento-Mobile.git` onde Git já estiver disponível. Leve também `artefatos/unip-mobile-debug.apk`, os oito DOCX/PDF em `relatorios/`, o consolidado e os dois PDFs oficiais em `documentos_oficiais/`. Confira `CHECKLIST_GERAL.md` e `PENDENCIAS_REAIS.md`: documentos gerados não significam atividades finalizadas.

Preencha **nome, RA, polo, local e data acadêmica reais**. Não declare que o trabalho remoto ocorreu presencialmente. Combine com o docente a aceitação do Flutter web e da execução por emulador no Cloud. Não é necessário instalar programas no computador da faculdade para ler PDFs ou usar o DartPad.

## Flutter sem instalação: DartPad no navegador

1. Acesse https://dartpad.dev e selecione o modo Flutter.
2. Para a atividade 3, copie **todo** `flutter/relatorio03-login/lib/main.dart`. Execute. Confira e-mail, senha, Login e mensagem de boas-vindas; teste campos vazios e formato inválido. Use `aluno@example.com` e senha fictícia.
3. Capture a interface e o resultado, sem usar credenciais reais. Salve PNG em `evidencias/relatorio03/`.
4. Para a atividade 8, substitua o código integral por `flutter/relatorio08-senhas/lib/main.dart`.
5. Confira os critérios visíveis: Fraca nos demais casos; Média a partir de 8 caracteres e duas classes; Forte a partir de 12 e quatro classes. Teste três entradas **fictícias**, com o campo oculto, e a limpeza do campo. Não use senhas pessoais ou as registre em logs.
6. Salve as três capturas em `evidencias/relatorio08/`. Registre resultados efetivamente observados; não chame a classificação de garantia de segurança.

Se DartPad estiver indisponível no laboratório, use o Cloud após liberar o download oficial do SDK. Não substitua Flutter por uma página HTML parecida.

## Android Studio já disponível no laboratório

1. Abra a pasta **android-nativo**, que contém `settings.gradle`, `app/` e o Gradle Wrapper. Requisitos: JDK 21 (Gradle aceita JDK 17 ou 21), Gradle 8.9, plugin Android 8.7.3 e plataforma Android 35. A IDE pode fornecer JDK e SDK existentes.
2. O arquivo `local.properties` é local, não versionado. Use o SDK que já está no laboratório; **não copie o caminho do Cloud**. Em caso de falta de ferramenta ou restrição, peça ao responsável técnico; não contorne bloqueios do laboratório.
3. Aguarde a sincronização e execute em emulador ou dispositivo autorizado, Android 6/API 23 ou superior. O teste remoto, se aprovado, usa API 30; isso não prova comportamento em todas as versões.
4. A tela inicial é o Relatório 1. Capture a **IDE real** com a árvore de projeto e o aplicativo funcionando. Explique `java`, `res/layout`, `res/values`, Manifest, arquivos Gradle e emulador. Captura do aplicativo sozinha não substitui captura da IDE.
6. Use os botões da tela inicial para abrir as demais Activities. Não é necessário editar código para selecionar exercício.

### Demonstrações Android

|Atividade|Procedimento|Resultado esperado|
|---|---|---|
|1|Abrir aplicação e explorar projeto na IDE|Texto inicial alterado; identificar estrutura real|
|2|Entrar vazio; depois preencher e-mail/senha fictícios|Orientação; saudação local, sem alegar autenticação|
|4|Abrir Cadastro e voltar; Consultar e voltar; Configurações; Sair|Destinos/mensagem distintos; Sair encerra tarefa|
|5|Verificar sem selecionar; marcar Java; depois também Flutter|Nenhuma seleção; uma tecnologia; duas tecnologias|
|6|Salvar um nome fictício; forçar parada pelas configurações do Android; abrir novamente|Nome recuperado do SharedPreferences, sem apagar dados|
|7|Vazios; e-mail inválido; senha de 5; depois 6 caracteres|Mensagens específicas; dados válidos apenas localmente|

Use capturas reais dos estados exigidos, especialmente salvamento/recuperação e cada validação. Para persistência, não desinstale nem limpe os dados entre salvar e reabrir.

## Cloud: ferramentas locais ao projeto

Use o checkout existente: cada tarefa já é isolada, portanto **não crie worktree**. Todas as ferramentas adicionais ficam em `.ferramentas/` (ignorada pelo Git).

```bash
cd /workspace/UNIP-Desenvolvimento-Mobile
python testes/preparar_android.py
source testes/ambiente_android.sh
sdkmanager --sdk_root="$ANDROID_HOME" 'platform-tools' 'platforms;android-35' 'build-tools;35.0.0'
printf 'sdk.dir=%s\n' "$ANDROID_HOME" > android-nativo/local.properties
cd android-nativo
./gradlew --no-daemon assembleDebug lintDebug
```

O script de ambiente configura proxy e certificados **deste Cloud**. Não o carregue no computador da faculdade. Na IDE do laboratório, use a configuração local. O APK pronto pode ser instalado apenas em dispositivo autorizado; é uma compilação de depuração, sem publicação em loja.

Para Flutter no Cloud, após aplicar a política de rede:

```bash
cd /workspace/UNIP-Desenvolvimento-Mobile
python testes/preparar_flutter.py
export PATH="$PWD/.ferramentas/flutter/bin:$PATH"
export PUB_CACHE="$PWD/.ferramentas/pub-cache"
bash testes/flutter_validar.sh
# Para executar manualmente, entrar em um dos projetos:
cd flutter/relatorio03-login
flutter run -d web-server --web-hostname 127.0.0.1 --web-port 8763
```

Após build aprovado, há automação preparada (ainda não executada) em `testes/flutter_capturas.py`: execute `python testes/flutter_capturas.py 03` ou `08`. Ela serve o build Flutter real, testa pelo Chromium e captura apenas após confirmar o resultado. Se a semântica do Flutter mudar, investigue o seletor em vez de simular aprovação. Insira as capturas e os resultados nas fontes JSON e regenere os relatórios.

O SDK está fixado em 3.35.7, verificado pelo SHA-256 do manifesto oficial. A instalação e os testes Flutter só podem ser chamados de aprovados após executar e conferir os logs. Não compartilhe links localhost como prévias; faça validação interna ou use DartPad em seu navegador.

## Atualizar relatórios com novas evidências

Os arquivos editáveis de conteúdo estão em `relatorios/fontes/relatorioNN.json`. A ferramenta `testes/gerar_relatorios.py` gera DOCX/PDF a partir desses arquivos; ela **sobrescreve os documentos gerados**, portanto guarde cópias de edições feitas diretamente no Word antes de executá-la.

- Preserve os PNG originais; inclua caminho, legenda, contexto e resultado observado no JSON. O tipo `grid` dispõe imagens originais sem fabricar pixels.
- Para capturas Android produzidas por `testes/android_funcional.py NN`, execute `python testes/incorporar_evidencias.py NN` e depois `python testes/gerar_relatorios.py`.
- Edite as fontes JSON atuais; não reconstrua rascunhos antigos sobre relatórios revisados.
- No Cloud, use dependências em ambiente virtual dentro do projeto, conforme `testes/requirements.txt` se não estiverem disponíveis. Nunca forneça senhas ou tokens no terminal ou chat.
- Revise páginas, imagens e identificação. Execute `python testes/verificar_entrega.py`. Atualize checklist e pendências com os resultados reais antes de enviar ao professor.
