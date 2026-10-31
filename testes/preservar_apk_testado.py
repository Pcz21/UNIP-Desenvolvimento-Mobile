"""Entrega o APK efetivamente instalado, conferindo o código com o build atual."""
from pathlib import Path
import subprocess as S,hashlib,json
from zipfile import ZipFile
R=Path(__file__).resolve().parents[1];adb=str(R/'.ferramentas/android-sdk/platform-tools/adb')
installed=S.check_output([adb,'shell','pm','path','br.edu.unip.mobile'],timeout=60).decode().strip()
assert installed.startswith('package:') and '\n' not in installed
remote=installed.removeprefix('package:');local=R/'.ferramentas/apk-testado.apk'
S.run([adb,'pull',remote,str(local)],check=True,timeout=60,stdout=S.DEVNULL)
current=R/'android-nativo/app/build/outputs/apk/debug/app-debug.apk'
with ZipFile(local) as a,ZipFile(current) as b:
 for name in ['classes.dex','resources.arsc','AndroidManifest.xml']:
  assert a.read(name)==b.read(name),'Build difere do código testado: '+name
out=R/'artefatos/unip-mobile-debug.apk';out.write_bytes(local.read_bytes());h=hashlib.sha256(out.read_bytes()).hexdigest()
(R/'artefatos/SHA256SUMS').write_text(h+'  '+out.name+'\n')
result={'apk':'artefatos/unip-mobile-debug.apk','sha256':h,'origem':'APK instalado e testado no emulador API 30','comparacao_build_atual':'classes.dex, resources.arsc e AndroidManifest.xml idênticos','observacao':'Chaves locais de depuração podem mudar a assinatura entre máquinas; a cópia entregue é a efetivamente testada.'}
(R/'testes/apk-verificado.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
