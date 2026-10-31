import 'package:flutter/material.dart';
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
      } else if (!RegExp(r'^[^\s@]+@[^\s@]+\.[^\s@]+$').hasMatch(endereco)) {
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
