from pathlib import Path
import urllib.request as U,json,concurrent.futures
sources={
'flutter_widgets':'https://raw.githubusercontent.com/flutter/flutter/stable/packages/flutter/lib/src/widgets/framework.dart',
'dart_overview':'https://raw.githubusercontent.com/dart-lang/site-www/main/src/content/overview.md',
'android_activity':'https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/master/core/java/android/app/Activity.java',
'android_checkbox':'https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/master/core/java/android/widget/CheckBox.java',
'android_prefs':'https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/master/core/java/android/content/SharedPreferences.java',
'owasp_auth':'https://raw.githubusercontent.com/OWASP/CheatSheetSeries/master/cheatsheets/Authentication_Cheat_Sheet.md',
'android_edittext':'https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/master/core/java/android/widget/EditText.java'}
R=Path(__file__).resolve().parents[1]
def run(item):
 key,url=item
 try:
  with U.urlopen(url,timeout=30) as f:data=f.read();status=f.status
  p=R/'.ferramentas/referencias';p.mkdir(exist_ok=True);(p/(key+'.txt')).write_bytes(data)
  return key,{'url':url,'http':status,'bytes':len(data),'consulta':'2026-10-31'}
 except Exception as e:return key,{'url':url,'erro':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=dict(ex.map(run,sources.items()))
(R/'testes/referencias-verificadas.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
print(json.dumps(r,ensure_ascii=False,indent=2))
