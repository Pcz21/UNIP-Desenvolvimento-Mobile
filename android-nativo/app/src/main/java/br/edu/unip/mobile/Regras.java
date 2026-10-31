package br.edu.unip.mobile;
import java.util.List;
public final class Regras {
 private Regras() {}
 public static String selecoes(List<String> itens) {
  return itens.isEmpty()?"Nenhuma tecnologia selecionada.":"Tecnologias selecionadas: " + String.join(", ",itens);
 }
 public static String erroEmail(String email) {
  if(email.trim().isEmpty())return "E-mail obrigatório.";
  return email.trim().matches("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$")?"":"E-mail inválido.";
 }
 public static String erroSenha(String senha) {
  if(senha.isEmpty())return "Senha obrigatória.";
  return senha.codePointCount(0,senha.length())<6?"Senha deve ter pelo menos 6 caracteres.":"";
 }
 public static String validar(String email,String senha) {
  String e=erroEmail(email),s=erroSenha(senha);
  if(e.isEmpty()&&s.isEmpty())return "Dados válidos localmente. Sem autenticação em servidor.";
  return e+(e.isEmpty()||s.isEmpty()?"":"\n")+s;
 }
}
