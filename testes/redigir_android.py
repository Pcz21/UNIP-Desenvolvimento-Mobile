from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
ident='Nome: [PREENCHER] | RA: [PREENCHER]\nPolo: [PREENCHER] | Local da aula prática: [PREENCHER]\nData acadêmica: [PREENCHER]. Trabalho remoto no Codex Cloud; participação presencial não declarada.'
info={
'01':('Conhecendo a ferramenta Android Studio',
'Criar um projeto Android básico, alterar seu texto inicial e reconhecer os arquivos usados no desenvolvimento. Android Studio é a IDE oficial para Android, reunindo editor, gerenciamento de SDK, sincronização Gradle, ferramentas de depuração e integração com dispositivos virtuais. A IDE facilita o fluxo editar, compilar, instalar, executar e inspecionar.',
'A Activity é o ponto de interação e recebe eventos do ciclo de vida, como onCreate. O layout XML descreve a interface de modo declarativo e é carregado com setContentView. AndroidManifest.xml declara a aplicação, as Activities e o ponto de entrada. Gradle configura plugins, versões do SDK e tarefas de compilação; o Gradle Wrapper padroniza a versão utilizada.',
'android-nativo/app/src/main/java contém classes Java; res/layout contém as telas XML; res/values guarda textos e recursos compartilhados; AndroidManifest.xml fica em app/src/main. app/build.gradle configura o módulo; settings.gradle registra o projeto. O emulador executa uma imagem Android isolada para testar o APK. A pasta build contém saídas geradas e não substitui o código-fonte.',
'MainActivity.java','activity_main.xml',
'@Override public void onCreate(Bundle state) {\n super.onCreate(state);\n setContentView(R.layout.activity_main);\n}',
'O texto inicial foi alterado para “Olá! Meu primeiro aplicativo Android em Java e XML.” A mesma aplicação oferece acesso às outras telas nativas, cada uma em sua Activity. Não se usa Kotlin ou Compose.',
'O conhecimento da estrutura torna possível localizar a interface, a lógica e a configuração. A compilação por linha de comando não demonstra a interface do Android Studio. O print da IDE continua obrigatório e pendente para conclusão acadêmica.'),
'02':('Tela de login em XML',
'Construir uma tela com título, e-mail, senha e botão Entrar. XML é uma linguagem de marcação usada para declarar componentes e atributos. Separar interface e lógica permite ajustar tamanhos, espaçamentos e textos sem misturar essas decisões com o tratamento do clique.',
'TextView apresenta o título e o resultado; EditText coleta e-mail e senha, usando tipos de entrada adequados; Button dispara uma ação; LinearLayout dispõe os filhos verticalmente. Um ScrollView externo mantém acesso em telas menores. Os textos de interface do layout estão em res/values/strings.xml, com margens e áreas de toque mínimas.',
'A Activity carrega activity_login.xml, obtém as referências com findViewById e registra um OnClickListener. Campos vazios geram orientação. Quando preenchidos, o resultado mostra uma saudação e identifica a demonstração como local. A senha é limpa após o clique bem-sucedido. Não existe servidor, sessão ou autenticação.',
'LoginActivity.java','activity_login.xml',
'<LinearLayout android:orientation="vertical" ...>\n <TextView android:text="@string/texto_1" ... />\n <EditText android:id="@+id/email"\n   android:inputType="textEmailAddress" ... />\n <EditText android:id="@+id/senha"\n   android:inputType="textPassword" ... />\n <Button android:id="@+id/entrar" ... />\n</LinearLayout>',
'As reticências identificam um recorte explicativo, não um XML executável. O arquivo integral anexo contém os atributos de tamanho, espaçamento e recursos e é a fonte usada na compilação.',
'A separação entre XML e Java facilita a manutenção. Uma interface de login é apenas a apresentação: a validação visual e a saudação não comprovam identidade. Autenticação de produção exigiria serviço confiável, proteção de comunicação e gerenciamento de sessão.'),
'04':('Menu simples em XML',
'Criar um menu com Cadastro, Consultar, Configurações e Sair. Navegação representa os caminhos entre telas e deve manter rótulos claros, retorno previsível e ações coerentes. Um menu inicial organiza destinos frequentes e reduz a necessidade de descobrir funções por tentativa.',
'O menu é um LinearLayout vertical com Button e ícones nativos drawableStart. Ícones acompanham palavras, preservando o significado mesmo quando o desenho não é reconhecido. Espaçamentos e áreas mínimas de toque tornam a seleção mais previsível.',
'Cadastro e Consultar abrem DestinoActivity por Intent explícita, com título e mensagem próprios, e o botão Voltar encerra apenas o destino. Configurações abre um diálogo que descreve o modo local. Sair executa finishAffinity para encerrar as Activities da tarefa. As telas são demonstrações; não há cadastro ou consulta em banco de dados.',
'MenuActivity.java','activity_menu.xml',
'<Button android:id="@+id/cadastro"\n android:drawableStart="@android:drawable/ic_menu_add" ... />\n<Button android:id="@+id/consultar" ... />\n<Button android:id="@+id/configuracoes" ... />\n<Button android:id="@+id/sair" ... />',
'O XML completo está no arquivo indicado. Cada opção possui um listener; DestinoActivity.java e activity_destino.xml implementam o retorno. Nenhum botão é meramente decorativo.',
'A navegação consistente ajuda o usuário a compreender onde está e como retornar. Nesta solução, os destinos e mensagens são simples, porém cada opção tem efeito verificável. Sair encerra a tarefa em vez de simular um logout de servidor.'),
'05':('Aplicativo utilizando CheckBox',
'Capturar opções independentes para a pergunta “Quais tecnologias você conhece?”. CheckBox representa uma escolha booleana e permite múltiplas seleções, ao contrário de um conjunto de RadioButtons para escolha única. É aplicável a preferências, interesses e itens de formulários.',
'A tela apresenta Java, Kotlin, Flutter e Python, seguidos do botão Verificar Resposta. Os componentes ficam alinhados em uma coluna e cada opção tem área de toque de pelo menos 48 dp. A seleção só é avaliada no clique, tornando o fluxo explícito para o usuário.',
'O listener percorre os quatro IDs e consulta isChecked. Para cada opção marcada, adiciona getText à lista. Regras.selecoes produz uma mensagem específica para lista vazia ou concatena os nomes selecionados em ordem. Um TextView apresenta o resultado de forma persistente na tela.',
'CheckboxActivity.java','activity_checkbox.xml',
'ArrayList<String> escolhas = new ArrayList<>();\n// Para cada CheckBox do layout:\nif (check.isChecked())\n escolhas.add(check.getText().toString());\nresultado.setText(Regras.selecoes(escolhas));',
'O código Java integral inclui a associação dos IDs e o listener. O XML integral contém quatro CheckBoxes e o botão, preservados como arquivos separados para leitura e reprodução.',
'CheckBox permite formulários com escolhas simultâneas sem obrigar o usuário a selecionar um item. Tratar explicitamente a lista vazia evita mensagem ambígua. A lista produzida pode ser utilizada em outras etapas de um formulário, com validações próprias do domínio.'),
'06':('Armazenamento com SharedPreferences',
'Salvar e recuperar o nome do usuário no armazenamento local. Dados mantidos apenas em variáveis desaparecem quando o processo termina; dados persistidos podem sobreviver a esse encerramento. SharedPreferences armazena pares chave-valor simples em um arquivo privado da aplicação.',
'getSharedPreferences("perfil", MODE_PRIVATE) seleciona o arquivo; getString("nome", "") lê o valor anterior ou um padrão. Um Editor recebe putString e commit confirma a escrita. Foi escolhido commit para verificar o retorno booleano nesta demonstração com um único valor pequeno. Em fluxos maiores, escrita síncrona na thread da interface deve ser evitada.',
'PreferenciasActivity recupera o nome em onCreate, preenche o EditText e informa “Nome recuperado”. O botão Salvar nome rejeita entrada vazia e informa sucesso ou falha. Encerrar a Activity sem matar o processo não é prova suficiente de persistência: o teste previsto força o encerramento do aplicativo e o reabre.',
'PreferenciasActivity.java','activity_preferencias.xml',
'SharedPreferences prefs = getSharedPreferences("perfil", MODE_PRIVATE);\nString salvo = prefs.getString("nome", "");\nboolean ok = prefs.edit().putString("nome", valor).commit();',
'O arquivo não contém senhas. MODE_PRIVATE restringe o acesso normal ao sandbox do aplicativo, mas não representa criptografia. Limpar os dados ou desinstalar o app remove esse armazenamento; fechar o processo normalmente não o remove.',
'O armazenamento local melhora a continuidade da experiência ao recuperar preferências sem exigir redigitação. SharedPreferences atende valores simples desta atividade. Dados sensíveis exigem análise adicional e os mecanismos de armazenamento devem ser escolhidos conforme o caso, sem confundir persistência com segurança.'),
'07':('Validações e conceitos de segurança',
'Validar campos obrigatórios, formato de e-mail e senha com menos de seis caracteres. Validação de entrada verifica conformidade com regras; autenticação estabelece a identidade de quem solicita acesso. Segurança também envolve confidencialidade, integridade, disponibilidade e controle de acesso.',
'A tela usa EditText com rótulos, senha oculta, botão Validar e resultado textual. A regra de e-mail verifica formato básico, sem garantir que a caixa postal exista. A regra de senha adota o limite mínimo de seis caracteres do roteiro, contado por pontos de código; esse mínimo acadêmico não é uma política recomendada para produção.',
'Regras.erroEmail distingue obrigatório e formato inválido. Regras.erroSenha distingue vazio e menos de seis caracteres. A Activity limpa erros anteriores, aplica setError em cada campo e exibe mensagens específicas no resultado. Com entradas válidas, informa apenas que os dados passaram pelas regras locais, sem autenticação em servidor.',
'ValidacaoActivity.java','activity_validacao.xml',
'if (email.trim().isEmpty()) return "E-mail obrigatório.";\nif (senha.isEmpty()) return "Senha obrigatória.";\nif (senha.codePointCount(0, senha.length()) < 6)\n return "Senha deve ter pelo menos 6 caracteres.";',
'A lógica compartilhada completa está em Regras.java. Não há gravação nem logs de senha. Testes devem usar apenas exemplos fictícios. Sistemas reais precisam repetir validações no servidor e proteger credenciais, comunicação e sessão; a validação local pode ser contornada.',
'A validação fornece retorno imediato e reduz erros de preenchimento. Ela complementa, mas não substitui, autenticação e autorização. As mensagens específicas tornam o comportamento verificável; o sucesso local não é anunciado como acesso seguro ou identidade comprovada.')}
for n in sys.argv[1:] or info:
 title,objetivo,teoria,pratica,java,xml,codigo,explicacao,conclusao=info[n]
 pagina1=[['title',f'Relatório {int(n)} — {title}'],['p',ident],['h','Objetivo e resumo teórico'],['p',objetivo],['p',teoria],['h','Atividade prática'],['p',pratica]]
 pagina2=[['h','Implementação e códigos'],['code',codigo],['p',explicacao],['p',f'Fontes integrais: android-nativo/app/src/main/java/br/edu/unip/mobile/{java} e android-nativo/app/src/main/res/layout/{xml}. Regras adicionais: Regras.java. Todos os arquivos são anexos de código no repositório.'],['h','Testes e resultados reais'],['p','Compilação da base aprovada (testes/android-base-build.log); compilação das seis telas e Android Lint aprovados (testes/android-final-build.log). Quinze verificações de lógica Java passaram (testes/java-regras.log). Esses resultados não substituem a execução e os testes de interface. A situação específica da execução está registrada na seção de evidências.'],['h','Conclusão'],['p',conclusao]]
 refs=[['h','Referências'],['p',f'UNIVERSIDADE PAULISTA. Roteiros: Desenvolvimento Mobile. [S. l.]: UNIP, [s. d.]. Roteiro {int(n)}. Material didático fornecido.'],['p',f'UNIVERSIDADE PAULISTA. Desenvolvimento Mobile: relatório de aulas práticas. [S. l.]: UNIP, [s. d.]. Relatório {int(n)}. Material didático fornecido.'],['p','ANDROID DEVELOPERS. Documentação para desenvolvedores Android. [S. l.], [s. d.]. Disponível em: https://developer.android.com/. Consulta on-line pendente de liberação de rede.']]
 p3=[['h','Evidências e teste de interface'],['p','EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA'],['p','O emulador está em avaliação. Não foram utilizados prints artificiais. A compilação comprovada não equivale à execução da tela. Status parcial até os testes e as capturas reais.']]+refs
 if n=='01':
  # Relatório 1: limite 1–2 páginas.
  pagina1 += [['h','Implementação'],['code',codigo],['p','Texto inicial alterado e navegação para as atividades independentes. Fontes: MainActivity.java e res/layout/activity_main.xml.']]
  pagina2=[['h','Testes, evidências e conclusão'],['p','A base e o projeto final compilaram; Android Lint não apontou erros. Os logs estão em testes/. EVIDÊNCIA PENDENTE — EXECUÇÃO NECESSÁRIA: aplicativo e interface real do Android Studio. A IDE não foi instalada ou aberta neste ambiente.'],['p',conclusao]]+refs
  pages=[pagina1,pagina2]
 else:pages=[pagina1,pagina2,p3]
 (R/'relatorios/fontes'/f'relatorio{n}.json').write_text(json.dumps({'id':n,'pages':pages},ensure_ascii=False,indent=2))
