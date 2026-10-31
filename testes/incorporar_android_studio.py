from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
e=json.loads((R/'testes/android-studio-evidencia.json').read_text());assert hashlib.sha256((R/e['captura']).read_bytes()).hexdigest()==e['sha256']
p=R/'relatorios/fontes/relatorio01.json';m=json.loads(p.read_text())
last=m['pages'][-1];i=next(i for i,item in enumerate(last) if item==['h','Referências']);refs=last[i:]
ref=['p','ANDROID DEVELOPERS. Download Android Studio. [S. l.], [s. d.]. Disponível em: https://developer.android.com/studio. Acesso em: 31 out. 2026.']
if ref not in refs:refs.append(ref)
first=[item for item in m['pages'][0] if item[0]!='image' and item!=['h','Aplicativo executado — evidência preservada']]
first += [['h','Aplicativo executado — evidência preservada'],['image',{'path':'evidencias/relatorio01/01-aplicativo.png','caption':'Figura 1 — Aplicativo executado em Android API 30. Fonte: execução própria anterior, PNG original preservado.','max_width':80,'max_height':160}]]
second=[['h','Android Studio real: interface e estrutura'],['p','O projeto existente foi aberto no Android Studio Rabbit 2 em Xvfb, com renderização por software. A sincronização Gradle terminou. A árvore expõe Manifest, Java, res/layout, res/values e Gradle; o editor mostra MainActivity.java. Não foi recriado o projeto nem refeita a atividade Android.'],['image',{'path':e['captura'],'caption':'Figura 2 — Interface autêntica do Android Studio com o projeto existente, sua estrutura e código Java. Fonte: captura própria do display virtual X11.','max_width':440,'max_height':310}],['h','Resultados e conclusão'],['p','A compilação e a execução anteriores permanecem válidas e documentadas nos logs e no print original. A nova captura complementa a evidência da IDE e relaciona a estrutura descrita à ferramenta real. A configuração e as capturas foram realizadas remotamente no Codex Cloud, sem declaração de participação presencial.']]+refs
m['pages']=[first,second];p.write_text(json.dumps(m,ensure_ascii=False,indent=2))
