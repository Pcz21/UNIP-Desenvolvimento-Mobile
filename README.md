# UNIP — Desenvolvimento Mobile

Oito atividades práticas da disciplina **Desenvolvimento Mobile**, com base nos dois documentos oficiais fornecidos. Não inclui disciplinas .NET ou Banco de Dados.

**Estado real da entrega:** consulte [CHECKLIST_GERAL.md](CHECKLIST_GERAL.md), [PENDENCIAS_REAIS.md](PENDENCIAS_REAIS.md) e [testes/RESULTADOS.md](testes/RESULTADOS.md). Código e documento gerados não comprovam execução. Onde não houver captura autêntica, o relatório registra **EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA**.

## Arquivos principais

|Pasta/arquivo|Conteúdo|
|---|---|
|`documentos_oficiais/`|PDFs UNIP originais e extrações integrais de texto|
|`android-nativo/`|Projeto Java + XML, seis atividades nativas e telas independentes|
|`flutter/relatorio03-login/`|Login Flutter/Dart, compatível com DartPad|
|`flutter/relatorio08-senhas/`|Classificador local de senhas Flutter/Dart|
|`artefatos/unip-mobile-debug.apk`|APK de depuração compilado neste ambiente|
|`evidencias/relatorioNN/`|Somente PNG de execução real, quando obtidos|
|`relatorios/word/`|Oito relatórios individuais e consolidado DOCX|
|`relatorios/pdf/`|Oito relatórios individuais e consolidado PDF|
|`relatorios/fontes/`|Conteúdo editável e referências para regenerar os documentos|
|`testes/`|Testes, scripts de reprodução, resultados e logs|
|[LEVAR_PARA_FACULDADE.md](LEVAR_PARA_FACULDADE.md)|Como abrir, executar, demonstrar e completar as evidências|

## Projeto Android

Abra **android-nativo** no Android Studio já instalado, sincronize e execute. Ferramentas fixadas: plugin Android 8.7.3, Gradle 8.9, JDK 21 no Cloud, compile/target SDK 35, mínimo API 23. O Gradle Wrapper inclui o checksum oficial da distribuição. Não use Kotlin/Compose: a lógica está em Java e as interfaces em XML.

A tela inicial corresponde à atividade 1; seus botões abrem Login (2), Menu (4), CheckBox (5), SharedPreferences (6) e Validações (7). O menu usa ícones e ações reais de navegação/mensagem/encerramento. Login e validação são demonstrações **sem autenticação em servidor**.

```bash
# No Cloud, dentro deste repositório, após preparar ferramentas:
source testes/ambiente_android.sh
cd android-nativo
./gradlew --no-daemon assembleDebug lintDebug
```

Compilação e Android Lint aprovados não substituem testes do APK. O Lint tem avisos documentados; não foram suprimidas verificações para obter sucesso. O APK não é uma versão de produção nem foi publicado em loja.

## Projetos Flutter e DartPad

Cada aplicação tem `pubspec.yaml`, `lib/main.dart`, configuração web e testes. Copie integralmente seu `lib/main.dart` para o modo Flutter em https://dartpad.dev ou use um SDK Flutter. Não há pacotes externos de aplicação; `flutter_test` é dependência de desenvolvimento.

- **Login:** MaterialApp, Scaffold, TextField e ElevatedButton, com mensagem de boas-vindas e validação didática.
- **Senhas:** Fraca nos demais casos; Média a partir de 8 pontos de código e duas classes; Forte a partir de 12 e quatro classes. Classes: minúsculas ASCII, maiúsculas ASCII, dígitos e símbolos (exceto espaços). Campo vazio solicita entrada. A heurística não mede entropia ou vazamentos. Senhas não são gravadas nem registradas nos logs.

O script `testes/preparar_flutter.py` prepara Flutter 3.35.7 com SHA-256 do manifesto oficial. Consulte as pendências de rede antes de usá-lo. **Não há afirmação de compilação ou teste Flutter enquanto os logs não comprovarem os comandos.**

## Relatórios e evidências

Os relatórios têm identificação acadêmica a preencher, teoria específica, implementação, resultados reais, conclusão e referências verificadas em formato ABNT. O código integral é entregue como arquivo separado no projeto para respeitar o limite de páginas. O consolidado contém capa e os oito relatórios; não substitui as entregas individuais.

As fontes JSON são a versão editável usada por `python testes/gerar_relatorios.py`. O script sobrescreve DOCX/PDF: preserve alterações manuais feitas no Word antes de regenerar. O verificador compara imagens dos documentos com os PNG originais e confere os limites de páginas dos PDFs. Sem execução aprovada, não cria imagens para preencher espaços.

## Segurança e autoria das evidências

Use entradas fictícias. Não inserir tokens, senhas pessoais, RA fictício, declarações de participação presencial ou imagens de aplicativos alheios. Não há captura gerada por IA. As diferenças entre os pesos do roteiro e do modelo de relatórios estão preservadas no checklist.
