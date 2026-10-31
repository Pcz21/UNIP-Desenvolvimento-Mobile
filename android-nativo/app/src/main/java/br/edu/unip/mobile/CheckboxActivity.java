package br.edu.unip.mobile;
import android.app.Activity;
import android.os.Bundle;
import android.widget.*;
import java.util.ArrayList;
public class CheckboxActivity extends Activity {
 @Override public void onCreate(Bundle b) {
  super.onCreate(b); setContentView(R.layout.activity_checkbox);
  findViewById(R.id.verificar).setOnClickListener(v -> {
   ArrayList<String> escolhas=new ArrayList<>();
   for(int id:new int[]{R.id.tecnologia0,R.id.tecnologia1,R.id.tecnologia2,R.id.tecnologia3}) {
    CheckBox check=findViewById(id); if(check.isChecked()) escolhas.add(check.getText().toString());
   }
   ((TextView)findViewById(R.id.resultado)).setText(Regras.selecoes(escolhas));
  });
 }
}
