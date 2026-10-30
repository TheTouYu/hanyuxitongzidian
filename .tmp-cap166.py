# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="      if(t.lv===3&&t.pr){const sibs=IDX.filter(x=>x.pr===t.pr&&x.c!==t.c).map(x=>x.c);"
new=("      if(t.lv===3&&t.pr){const seenS=new Set([t.c]);const sibs=[];"
     "\n        IDX.filter(x=>x.pr===t.pr).forEach(x=>{const it=byChar(x.c)||x;const key=it.c;if(seenS.has(key))return;seenS.add(key);sibs.push(key);});")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    else: print("MISS",os.path.basename(f))
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk31.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print("rc",r.returncode)