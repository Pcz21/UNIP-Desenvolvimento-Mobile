"""Instala ferramentas oficiais localmente; verifica hashes publicados."""
from pathlib import Path
import urllib.request as U, hashlib, tarfile, zipfile, concurrent.futures
root=Path(__file__).resolve().parents[1]/'.ferramentas'; root.mkdir(exist_ok=True)
items=[('jdk.tar.gz','https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.9%2B10/OpenJDK21U-jdk_x64_linux_hotspot_21.0.9_10.tar.gz','sha256',None),('gradle.zip','https://downloads.gradle.org/distributions/gradle-8.9-bin.zip','sha256',None),('android.zip','https://dl.google.com/android/repository/commandlinetools-linux-16111833_latest.zip','sha1','e025545c62a8e64c7559119566a569fb1dec5f60')]
def get(item):
 name,url,alg,expected=item;p=root/name
 if not p.exists(): U.urlretrieve(url,p)
 if expected is None: expected=U.urlopen(url+('.sha256.txt' if name.startswith('jdk') else '.sha256')).read().decode().split()[0]
 actual=hashlib.new(alg,p.read_bytes()).hexdigest()
 if actual!=expected: raise RuntimeError('Checksum inválido: '+name)
 print(name,'checksum OK',flush=True)
 if name=='jdk.tar.gz':
  if not (root/'jdk-21.0.9+10').exists():
   with tarfile.open(p) as f:f.extractall(root,filter='data')
 elif name=='gradle.zip':
  if not (root/'gradle-8.9').exists():
   with zipfile.ZipFile(p) as f:f.extractall(root)
 else:
  dest=root/'android-sdk'/'cmdline-tools'/'latest'
  if not dest.exists():
   with zipfile.ZipFile(p) as f:f.extractall(root/'android-unpack')
   dest.parent.mkdir(parents=True,exist_ok=True);(root/'android-unpack'/'cmdline-tools').rename(dest)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(get,items))
for d in [root/'gradle-8.9'/'bin',root/'android-sdk'/'cmdline-tools'/'latest'/'bin']:
 for p in d.iterdir():p.chmod(0o755)
