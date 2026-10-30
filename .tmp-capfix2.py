# -*- coding: utf-8 -*-
import io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in ("index.html","test.html","app.html"):
    p=os.path.join(r"D:\系统汉字\web\public",f)
    if not os.path.exists(p): continue
    s=io.open(p,encoding="utf-8").read(); o=s
    s=s.replace("captions.jsonon?v=20261030a","captions.json?v=20261030a")
    if s!=o: io.open(p,"w",encoding="utf-8",newline="\n").write(s); print("fixed",f)