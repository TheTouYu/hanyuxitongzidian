# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("${esc(s.text)}","${s.text&&s.text.includes('gscroll')?s.text:esc(s.text)}")
    h=h.replace("<p>${esc(s.text)}</p>","<p>${s.text&&s.text.includes('gscroll')?s.text:esc(s.text)}</p>")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk36.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print(os.path.basename(f),"patched",h!=o,"rc",r.returncode)