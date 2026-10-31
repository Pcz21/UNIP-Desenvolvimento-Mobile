import 'package:flutter/material.dart';
void main() => runApp(const SenhasApp());
// Heurística didática, não mede entropia nem consulta vazamentos.
String classificarSenha(String senha) {
  final tamanho = senha.runes.length;
  final classes = [RegExp(r'[a-z]'), RegExp(r'[A-Z]'), RegExp(r'[0-9]'),
    RegExp(r'[^a-zA-Z0-9\s]')].where((regra) => regra.hasMatch(senha)).length;
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
            const Text('Forte: 12 ou mais caracteres e quatro classes.\n'
              'Média: 8 ou mais caracteres e pelo menos duas classes.\n'
              'Fraca: demais casos.\n'
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
