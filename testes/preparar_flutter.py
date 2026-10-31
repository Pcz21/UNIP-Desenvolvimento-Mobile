"""Instala Flutter 3.35.7 com hash do manifesto oficial, sem desativar TLS."""
from pathlib import Path
import json,hashlib,tarfile,urllib.request as U
root=Path(__file__).resolve().parents[1]/'.ferramentas';root.mkdir(exist_ok=True)
url='https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json'
data=json.load(U.urlopen(url,timeout=40))
release=next(r for r in data['releases'] if r['version']=='3.35.7' and r['channel']=='stable' and r.get('dart_sdk_arch','x64')=='x64')
archive=root/'flutter.tar.xz'
if not archive.exists():U.urlretrieve(data['base_url']+'/'+release['archive'],archive)
h=hashlib.sha256()
with archive.open('rb') as f:
 for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
if h.hexdigest()!=release['sha256']:raise RuntimeError('Checksum Flutter inválido')
if not (root/'flutter').exists():
 with tarfile.open(archive) as t:t.extractall(root,filter='data')
(root/'flutter-release.json').write_text(json.dumps(release,indent=2))
print('Flutter '+release['version']+' verificado por SHA-256')
