# -*- coding: utf-8 -*-
import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read()
h2=re.sub(r"const fam=kids\.length\?`　<label>字族</label>　\$\{kids\.map\(ln\)\.join\(''\)\}`:'';",
          "const fam='';",h,count=1)
if h2==h: print("fam line MISS")
h2=h2.replace("if(sp&&names.length){","if(!names.length){kh=IDX.filter(x=>x.pr===ch).map(x=>x.c);kh.forEach(c=>names.push(c));}\nif(sp&&names.length){",1)
io.open(f,"w",encoding="utf-8",newline="\n").write(h2)
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h2,re.S))
p=os.path.join(tempfile.gettempdir(),"chk3.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("check rc",r.returncode,(r.stderr or "")[:150])