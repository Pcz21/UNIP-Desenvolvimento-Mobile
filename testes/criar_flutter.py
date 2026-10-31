from pathlib import Path
root=Path(__file__).resolve().parents[1]
login='''import 'package:flutter/material.dart';
void main() => runApp(const LoginApp());
class LoginApp extends StatelessWidget {
  const LoginApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    debugShowCheckedModeBanner: false,
    title: 'UNIP • Login',
    theme: ThemeData(colorSchemeSeed: const Color(0xFF145E75), useMaterial3: true),
    home: const LoginPage(),
  );
}
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPageState();
}
class _LoginPageState extends State<LoginPage> {
  final email = TextEditingController();
  final senha = TextEditingController();
  String mensagem = '';
  void entrar() {
    final endereco = email.text.trim();
    setState(() {
      if (endereco.isEmpty || senha.text.isEmpty) {
        mensagem = 'Preencha e-mail e senha.';
      } else if (!RegExp(r'^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$').hasMatch(endereco)) {
        mensagem = 'Informe um e-mail válido.';
      } else {
        mensagem = 'Bem-vindo(a), $endereco!';
        senha.clear();
      }
    });
  }
  @override
  void dispose() { email.dispose(); senha.dispose(); super.dispose(); }
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('UNIP | Desenvolvimento Mobile')),
    body: Center(child: SingleChildScrollView(padding: const EdgeInsets.all(24),
      child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 420),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          const Icon(Icons.school_outlined, size: 64, color: Color(0xFF145E75)),
          const SizedBox(height: 16),
          Text('Acesse seu espaço', style: Theme.of(context).textTheme.headlineMedium),
          const SizedBox(height: 8),
          const Text('Atividade 3 • Login local demonstrativo'),
          const SizedBox(height: 24),
          TextField(key: const Key('email'), controller: email,
            keyboardType: TextInputType.emailAddress,
            decoration: const InputDecoration(labelText: 'E-mail', border: OutlineInputBorder())),
          const SizedBox(height: 16),
          TextField(key: const Key('senha'), controller: senha, obscureText: true,
            enableSuggestions: false, autocorrect: false,
            onSubmitted: (_) => entrar(),
            decoration: const InputDecoration(labelText: 'Senha', border: OutlineInputBorder())),
          const SizedBox(height: 20),
          ElevatedButton(key: const Key('login'), onPressed: entrar, child: const Text('Login')),
          const SizedBox(height: 20),
          Semantics(liveRegion: true, child: Text(mensagem, key: const Key('resultado'))),
          const SizedBox(height: 16),
          const Text('Demonstração didática: não há autenticação em servidor.'),
        ]),
      ),
    )),
  );
}
'''
senha='''import 'package:flutter/material.dart';
void main() => runApp(const SenhasApp());
// Heurística didática, não mede entropia nem consulta vazamentos.
String classificarSenha(String senha) {
  final tamanho = senha.runes.length;
  final classes = [RegExp(r'[a-z]'), RegExp(r'[A-Z]'), RegExp(r'[0-9]'),
    RegExp(r'[^a-zA-Z0-9\\s]')].where((regra) => regra.hasMatch(senha)).length;
  if (tamanho >= 12 && classes == 4) return 'Senha Forte';
  if (tamanho >= 8 && classes >= 2) return 'Senha Média';
  return 'Senha Fraca';
}
class SenhasApp extends StatelessWidget {
  const SenhasApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    debugShowCheckedModeBanner: false, title: 'UNIP • Verificador de senhas',
    theme: ThemeData(colorSchemeSeed: const Color(0xFF145E75), useMaterial3: true),
    home: const SenhasPage(),
  );
}
class SenhasPage extends StatefulWidget {
  const SenhasPage({super.key});
  @override
  State<SenhasPage> createState() => _SenhasPageState();
}
class _SenhasPageState extends State<SenhasPage> {
  String resultado = 'Digite uma senha para analisar.';
  @override
  Widget build(BuildContext context) {
    final cor = resultado == 'Senha Forte' ? Colors.green.shade800
      : resultado == 'Senha Média' ? Colors.brown.shade700 : Colors.red.shade800;
    return Scaffold(appBar: AppBar(title: const Text('UNIP | Desenvolvimento Mobile')),
      body: Center(child: SingleChildScrollView(padding: const EdgeInsets.all(24),
        child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 460),
          child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
            const Icon(Icons.lock_outline, size: 64, color: Color(0xFF145E75)),
            const SizedBox(height: 16),
            Text('Verificador de senhas', style: Theme.of(context).textTheme.headlineMedium),
            const SizedBox(height: 8), const Text('Atividade 8 • Análise local, sem armazenamento'),
            const SizedBox(height: 24),
            TextField(key: const Key('senha'), obscureText: true, autocorrect: false,
              enableSuggestions: false,
              decoration: const InputDecoration(labelText: 'Senha', border: OutlineInputBorder()),
              onChanged: (valor) => setState(() { resultado = valor.isEmpty
                ? 'Digite uma senha para analisar.' : classificarSenha(valor); })),
            const SizedBox(height: 24),
            Semantics(liveRegion: true, child: Text(resultado, key: const Key('resultado'),
              style: TextStyle(fontSize: 24, color: cor, fontWeight: FontWeight.bold))),
            const SizedBox(height: 24),
            const Text('Critérios didáticos', style: TextStyle(fontWeight: FontWeight.bold)),
            const Text('Forte: 12 ou mais caracteres e quatro classes.\\n'
              'Média: 8 ou mais caracteres e pelo menos duas classes.\\n'
              'Fraca: demais casos.\\n'
              'Classes: minúsculas, maiúsculas, números e símbolos; espaços não contam como símbolo.'),
            const SizedBox(height: 16),
            const Text('Classificação indicativa. Use senhas únicas e longas e autenticação multifator. '
              'Não digite uma senha real nesta demonstração.'),
          ]),
        ),
      )),
    );
  }
}
'''
for name,code in [('relatorio03-login',login),('relatorio08-senhas',senha)]:
 p=root/'flutter'/name;(p/'lib').mkdir(parents=True,exist_ok=True);(p/'web').mkdir(exist_ok=True);(p/'test').mkdir(exist_ok=True)
 (p/'lib/main.dart').write_text(code)
 package=name.replace('-','_')
 (p/'pubspec.yaml').write_text(f'name: {package}\ndescription: Atividade prática de Desenvolvimento Mobile UNIP.\npublish_to: none\nversion: 1.0.0+1\nenvironment:\n  sdk: ">=3.4.0 <4.0.0"\ndependencies:\n  flutter:\n    sdk: flutter\ndev_dependencies:\n  flutter_test:\n    sdk: flutter\nflutter:\n  uses-material-design: true\n')
 (p/'web/index.html').write_text('''<!DOCTYPE html><html lang="pt-BR"><head><base href="$FLUTTER_BASE_HREF"><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>UNIP Mobile</title></head><body><script src="flutter_bootstrap.js" async></script></body></html>''')
 (p/'web/flutter_bootstrap.js').write_text('''{{flutter_js}}
{{flutter_build_config}}
_flutter.loader.load({config: {canvasKitBaseUrl: "canvaskit/"}});
''')
 (p/'README.md').write_text(f'''# {name}\n\nCódigo sem dependências de aplicação externas. Copie integralmente `lib/main.dart` para o modo Flutter do DartPad ou, com Flutter estável instalado, execute nesta pasta:\n\n```sh\nflutter pub get\nflutter analyze\nflutter test\nflutter build web --no-web-resources-cdn\nflutter run -d chrome\n```\n\nA avaliação é local e didática. Não usar credenciais reais. Testes executados, quando disponíveis, estão em `../../testes/RESULTADOS.md`; a presença de testes não significa que passaram.\n''')
 if name.startswith('relatorio03'):
  test='''import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../lib/main.dart';
void main() {
 testWidgets('login: vazio, formato inválido e boas-vindas', (tester) async {
  await tester.pumpWidget(const LoginApp());
  await tester.tap(find.byKey(const Key('login'))); await tester.pump();
  expect(find.text('Preencha e-mail e senha.'), findsOneWidget);
  await tester.enterText(find.byKey(const Key('email')), 'invalido');
  await tester.enterText(find.byKey(const Key('senha')), 'exemplo123');
  await tester.tap(find.byKey(const Key('login'))); await tester.pump();
  expect(find.text('Informe um e-mail válido.'), findsOneWidget);
  await tester.enterText(find.byKey(const Key('email')), 'aluno@example.com');
  await tester.tap(find.byKey(const Key('login'))); await tester.pump();
  expect(find.text('Bem-vindo(a), aluno@example.com!'), findsOneWidget);
  expect(tester.widget<TextField>(find.byKey(const Key('senha'))).controller!.text, isEmpty);
 });
}
'''
 else:
  test='''import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../lib/main.dart';
void main() {
 test('limites e complexidade da classificação', () {
  expect(classificarSenha('abc'), 'Senha Fraca');
  expect(classificarSenha('abcDE12'), 'Senha Fraca');
  expect(classificarSenha('abcdefgh'), 'Senha Fraca');
  expect(classificarSenha('Abcdef12'), 'Senha Média');
  expect(classificarSenha('Abcdef12345!'), 'Senha Forte');
  expect(classificarSenha('Abcdef12345 '), 'Senha Média');
  expect(classificarSenha('Abcde12345!'), 'Senha Média');
 });
 testWidgets('atualiza os três níveis e limpa resultado', (tester) async {
  await tester.pumpWidget(const SenhasApp());
  for (final item in {'abc':'Senha Fraca','Abcdef12':'Senha Média','Abcdef12345!':'Senha Forte'}.entries) {
   await tester.enterText(find.byKey(const Key('senha')), item.key);await tester.pump();
   expect(find.text(item.value), findsOneWidget);
  }
  await tester.enterText(find.byKey(const Key('senha')), '');await tester.pump();
  expect(find.text('Digite uma senha para analisar.'), findsOneWidget);
 });
}
'''
 (p/'test/app_test.dart').write_text(test)
