import br.edu.unip.mobile.Regras;
import java.util.List;
public class TesteRegras {
 static int casos=0;
 static void igual(String real,String esperado) {casos++;if(!real.equals(esperado))throw new AssertionError("Caso "+casos+": resultado inesperado");}
 public static void main(String[] args) {
  igual(Regras.selecoes(List.of()),"Nenhuma tecnologia selecionada.");
  igual(Regras.selecoes(List.of("Java")),"Tecnologias selecionadas: Java");
  igual(Regras.selecoes(List.of("Java","Flutter")),"Tecnologias selecionadas: Java, Flutter");
  igual(Regras.erroEmail(""),"E-mail obrigatório.");
  igual(Regras.erroEmail("   "),"E-mail obrigatório.");
  igual(Regras.erroEmail("aluno"),"E-mail inválido.");
  igual(Regras.erroEmail("a@b"),"E-mail inválido.");
  igual(Regras.erroEmail("aluno@example.com"),"");
  igual(Regras.erroEmail("  aluno@example.com  "),"");
  igual(Regras.erroSenha(""),"Senha obrigatória.");
  igual(Regras.erroSenha("12345"),"Senha deve ter pelo menos 6 caracteres.");
  igual(Regras.erroSenha("123456"),"");
  igual(Regras.erroSenha("😀😀😀"),"Senha deve ter pelo menos 6 caracteres.");
  igual(Regras.validar("aluno@example.com","123456"),"Dados válidos localmente. Sem autenticação em servidor.");
  igual(Regras.validar("",""),"E-mail obrigatório.\nSenha obrigatória.");
  System.out.println(casos+" testes de regras Java aprovados. Não substituem testes da interface Android.");
 }
}
