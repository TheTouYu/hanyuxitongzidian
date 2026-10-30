# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="(d.simp&&!d.cname)?`（${esc(d.simp)}）`:''"
new="(d.simp&&!d.cname&&!(d.head||'').includes('（'))?`（${esc(d.simp)}）`:''"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    else: print(os.path.basename(f),"no-match")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk20.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print("rc",r.returncode)