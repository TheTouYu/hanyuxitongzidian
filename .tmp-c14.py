# -*- coding: utf-8 -*-
import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
pairs=[('<span style="margin-left:14px">字根　${rl}${fam}','<span style="margin-left:14px">${rl}${fam}'),
       ("sp.innerHTML='　<label>字族</label>　'","sp.innerHTML='　'")]
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=0
    for a,b in pairs:
        if a in h: h=h.replace(a,b); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk7.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode)