"""Instalador local da IDE oficial; hash publicado por Android Developers."""
from pathlib import Path
import urllib.request as U,hashlib,tarfile,json
R=Path(__file__).resolve().parents[1];tools=R/'.ferramentas'
url='https://dl.google.com/dl/android/studio/ide-zips/2026.2.2.8/android-studio-rabbit2-linux.tar.gz'
expected='b47fdcc0703019618a7afd5ad1822cafc5de66bed984640be2977a0fdb538304'
p=tools/'android-studio.tar.gz'
if not p.exists():U.urlretrieve(url,p)
h=hashlib.sha256()
with p.open('rb') as f:
 for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
assert h.hexdigest()==expected,'Checksum Android Studio divergente'
print('Android Studio SHA-256 oficial confirmado',flush=True)
if not (tools/'android-studio').exists():
 with tarfile.open(p) as f:f.extractall(tools,filter='data')
(R/'testes/android-studio-distribuicao.json').write_text(json.dumps({'versao':'Android Studio Rabbit 2 | 2026.2.2','url':url,'sha256':expected,'fonte_checksum':'https://developer.android.com/studio','integridade':'aprovada'},indent=2))
print('Android Studio extraído no projeto',flush=True)
