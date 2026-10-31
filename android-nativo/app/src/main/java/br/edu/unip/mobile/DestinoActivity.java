package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
public class DestinoActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b); setContentView(R.layout.activity_destino);
  ((TextView)findViewById(R.id.destino)).setText(getIntent().getStringExtra("titulo") + "\n\n" + getIntent().getStringExtra("mensagem"));
  findViewById(R.id.voltar).setOnClickListener(v -> finish());
 }
}
