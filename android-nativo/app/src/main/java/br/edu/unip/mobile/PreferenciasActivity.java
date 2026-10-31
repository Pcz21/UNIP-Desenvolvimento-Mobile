package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
import android.content.SharedPreferences;
public class PreferenciasActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b); setContentView(R.layout.activity_preferencias);
  SharedPreferences prefs=getSharedPreferences("perfil", MODE_PRIVATE);
  EditText nome=findViewById(R.id.nome); TextView resultado=findViewById(R.id.resultado);
  String salvo=prefs.getString("nome", ""); nome.setText(salvo);
  resultado.setText(salvo.isEmpty()?"Nenhum nome salvo.":"Nome recuperado: " + salvo);
  findViewById(R.id.salvar).setOnClickListener(v -> {
   String valor=nome.getText().toString().trim();
   if(valor.isEmpty()) { nome.setError("Informe o nome."); resultado.setText("Nome obrigatório."); return; }
   // commit síncrono confirma a escrita nesta demonstração com um único valor.
   boolean ok=prefs.edit().putString("nome", valor).commit();
   resultado.setText(ok?"Nome salvo: " + valor:"Não foi possível salvar o nome.");
  });
 }
}
