package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
import android.content.Intent;
public class MainActivity extends Activity {
 @Override public void onCreate(Bundle state) {
  super.onCreate(state);setContentView(R.layout.activity_main);
  LinearLayout lista=findViewById(R.id.exercicios);
  String[] titulos={"2 — Login XML","4 — Menu","5 — CheckBox","6 — SharedPreferences","7 — Validações"};
  Class<?>[] telas={LoginActivity.class,MenuActivity.class,CheckboxActivity.class,PreferenciasActivity.class,ValidacaoActivity.class};
  for(int i=0;i<titulos.length;i++) { final Class<?> tela=telas[i]; Button b=new Button(this);b.setText(titulos[i]);
   b.setOnClickListener(v -> startActivity(new Intent(this,tela)));lista.addView(b); }
 }
}
