"""Registra apenas validação com logs de sucesso e bundle efetivo."""
from pathlib import Path
import json,hashlib,sys
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
n=sys.argv[1];name={'03':'relatorio03-login','08':'relatorio08-senhas'}[n]
logs={k:(R/'testes'/f'{name}-{k}.log').read_text() for k in ['analyze','test','build']}
assert 'No issues found!' in logs['analyze']
assert 'All tests passed!' in logs['test']
assert 'Built build/web' in logs['build']
bundle=R/'flutter'/name/'build/web/main.dart.js';assert bundle.is_file()
source=R/'flutter'/name/'lib/main.dart'
result={'atividade':n,'sdk':'Flutter 3.35.7 / Dart 3.9.2','analyze':'aprovado','test':'aprovado','build_web':'aprovado','widget_tests':1 if n=='03' else 2,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'bundle_sha256':hashlib.sha256(bundle.read_bytes()).hexdigest(),'registro_utc':datetime.now(timezone.utc).isoformat(),'logs':{k:f'testes/{name}-{k}.log' for k in logs}}
(R/'testes'/f'flutter-validacao-{n}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
