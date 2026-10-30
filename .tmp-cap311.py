# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const isZX=s=>s.key==='zigen'||s.key==='zixing'||/字形/.test(s.label||'')"
new="const isZX=s=>!(s.text||'').includes('gscroll')&&(s.key==='zigen'||s.key==='zixing'||/字形/.test(s.label||''))"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk33.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print(os.path.basename(f),"rc",r.returncode, new in h)
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zigen": print("帝 zigen:",(s.get("text") or "")[:90])