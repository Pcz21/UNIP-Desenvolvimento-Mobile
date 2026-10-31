import 'package:flutter/material.dart';
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
