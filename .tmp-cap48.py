# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("esc(d.head||d.cname||ch)","esc(d.head||d.cname||ch)")
    # title line: skip auto (simp) when head already carries parentheses
    h=h.replace("(d.simp?`（${esc(d.simp)}）`:'')","(d.simp&&!(d.head||'').includes('（')?`（${esc(d.simp)}）`:'')")
    h=h.replace("(d.simp?'（'+esc(d.simp)+'）':'')","((d.simp&&!(d.head||'').indexOf('（')>=0)?'（'+esc(d.simp)+'）':'')")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk19.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print(os.path.basename(f),"rc",r.returncode)