from pathlib import Path
root=Path(__file__).resolve().parents[1]/'android-nativo'
def write(name,text):
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
write('settings.gradle',"pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }\ndependencyResolutionManagement { repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS); repositories { google(); mavenCentral() } }\nrootProject.name = 'UNIPMobile'\ninclude ':app'\n")
write('build.gradle',"plugins { id 'com.android.application' version '8.7.3' apply false }\n")
write('gradle.properties','org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8\norg.gradle.workers.max=2\n')
write('app/build.gradle',"plugins { id 'com.android.application' }\nandroid {\n namespace 'br.edu.unip.mobile'\n compileSdk 35\n defaultConfig { applicationId 'br.edu.unip.mobile'; minSdk 23; targetSdk 35; versionCode 1; versionName '1.0' }\n compileOptions { sourceCompatibility JavaVersion.VERSION_17; targetCompatibility JavaVersion.VERSION_17 }\n}\n")
write('app/src/main/AndroidManifest.xml','''<manifest xmlns:android="http://schemas.android.com/apk/res/android">
<application android:theme="@android:style/Theme.Material.Light.NoActionBar" android:label="UNIP Mobile" android:allowBackup="false" android:supportsRtl="true">
<activity android:name=".MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity>
</application></manifest>''')
write('app/src/main/res/layout/activity_main.xml','''<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent" android:fillViewport="true">
<LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="vertical" android:padding="24dp" android:background="#F1F5F9">
<TextView android:layout_width="match_parent" android:layout_height="wrap_content" android:text="Desenvolvimento Mobile — UNIP" android:textSize="26sp" android:textColor="#12304A" android:layout_marginTop="32dp"/>
<TextView android:layout_width="match_parent" android:layout_height="wrap_content" android:text="Olá! Meu primeiro aplicativo Android em Java e XML." android:textSize="18sp" android:paddingTop="20dp"/>
<LinearLayout android:id="@+id/exercicios" android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="vertical" android:paddingTop="24dp"/>
</LinearLayout></ScrollView>''')
write('app/src/main/java/br/edu/unip/mobile/MainActivity.java','''package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
public class MainActivity extends Activity {
 @Override public void onCreate(Bundle state) { super.onCreate(state); setContentView(R.layout.activity_main); }
}
''')
