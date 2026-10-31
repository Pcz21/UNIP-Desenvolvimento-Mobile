package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
import android.app.AlertDialog;
import android.content.Intent;
public class MenuActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b); setContentView(R.layout.activity_menu);
  findViewById(R.id.cadastro).setOnClickListener(v -> abrir("Cadastro", "Tela demonstrativa de cadastro. Nenhum dado enviado."));
  findViewById(R.id.consultar).setOnClickListener(v -> abrir("Consultar", "Consulta demonstrativa: nenhum registro cadastrado."));
  findViewById(R.id.configuracoes).setOnClickListener(v -> new AlertDialog.Builder(this)
   .setTitle("Configurações").setMessage("Modo didático local. Não há conexão com servidor.").setPositiveButton("OK", null).show());
  findViewById(R.id.sair).setOnClickListener(v -> finishAffinity());
 }
 private void abrir(String titulo, String mensagem) {
  startActivity(new Intent(this, DestinoActivity.class).putExtra("titulo",titulo).putExtra("mensagem",mensagem));
 }
}
