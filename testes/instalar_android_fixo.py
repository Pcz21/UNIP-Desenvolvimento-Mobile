from pathlib import Path
import urllib.request,hashlib,zipfile
p=Path('.ferramentas/android16.zip')
if not p.exists():urllib.request.urlretrieve('https://dl.google.com/android/repository/commandlinetools-linux-12266719_latest.zip',p)
assert hashlib.sha1(p.read_bytes()).hexdigest()=='47e61d3bb57b5e907a74f225a767a767a8b4d7a5'
d=Path('.ferramentas/android-sdk/cmdline-tools/16.0')
if not d.exists():
 with zipfile.ZipFile(p) as z:z.extractall('.ferramentas/android16-unpack')
 Path('.ferramentas/android16-unpack/cmdline-tools').rename(d)
for p in (d/'bin').iterdir():p.chmod(0o755)
print('Android CLI 16.0 checksum OK')
