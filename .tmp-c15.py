# -*- coding: utf-8 -*-
import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read()
h=h.replace('<span style="margin-left:14px">${rl}${fam}','<span style="margin-left:14px">字根　${rl}${fam}',1)
h=h.replace("<span id=\"famspan\"></span></span>`;","<span id=\"famspan\"></span></span>`;",1)
h=h.replace("sp.innerHTML='　'","sp.innerHTML='　<label>字族</label>　'",1)
i=h.find('rel=`<span style="margin-left:14px">字根　')
if i<0: print("anchor missing")
else:
    h=h[:i]+'rel=d.chapter?\' \':`'+h[i+len('rel=`'):]
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("rel gated")
h=io.open(f,encoding="utf-8").read()
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk8.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode,(r.stderr or "")[:200])
print([l for l in h.split("\n") if "famspan" in l][:1])