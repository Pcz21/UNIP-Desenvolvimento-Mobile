import 'package:flutter/material.dart';
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
