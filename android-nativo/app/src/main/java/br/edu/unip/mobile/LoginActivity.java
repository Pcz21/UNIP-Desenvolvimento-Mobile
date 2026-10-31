package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
public class LoginActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b); setContentView(R.layout.activity_login);
  EditText email=findViewById(R.id.email), senha=findViewById(R.id.senha);
  TextView resultado=findViewById(R.id.resultado);
  findViewById(R.id.entrar).setOnClickListener(v -> {
   if(email.getText().toString().trim().isEmpty() || senha.getText().length()==0)
    resultado.setText("Preencha e-mail e senha.");
   else { resultado.setText("Olá, " + email.getText().toString().trim() + "! Demonstração local, sem autenticação."); senha.setText(""); }
  });
 }
}
