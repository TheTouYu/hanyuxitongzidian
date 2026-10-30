# -*- coding: utf-8 -*-
import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
css="\n.ct td:first-child,.ct th:first-child{white-space:nowrap;width:1%}\n"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    if css.strip() in h: print(f.split("\\")[-1],"already"); continue
    i=h.find("</style>")
    h=h[:i]+css+h[i:]
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"css added")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk6.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode)