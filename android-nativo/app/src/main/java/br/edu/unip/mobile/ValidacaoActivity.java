package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
public class ValidacaoActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b);setContentView(R.layout.activity_validacao);
  EditText email=findViewById(R.id.email), senha=findViewById(R.id.senha);
  findViewById(R.id.validar).setOnClickListener(v -> {
   email.setError(null);senha.setError(null);
   String e=email.getText().toString().trim(), s=senha.getText().toString();
   String erroEmail=Regras.erroEmail(e), erroSenha=Regras.erroSenha(s);
   if(!erroEmail.isEmpty())email.setError(erroEmail);
   if(!erroSenha.isEmpty())senha.setError(erroSenha);
   ((TextView)findViewById(R.id.resultado)).setText(Regras.validar(e,s));
  });
 }
}
