# -*- coding: utf-8 -*-
import io,re,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in ("index.html","app.html","test.html"):
    p=os.path.join(r"D:\系统汉字\web\public",f)
    if not os.path.exists(p): continue
    t=io.open(p,encoding="utf-8").read(); o=t
    t=re.sub(r"captions\.js(\?v=[^\"']*)?","captions.js?v=20261029b",t)
    t=re.sub(r"photos\.js(\?v=[^\"']*)?","photos.js?v=20261029b",t)
    if t!=o:
        io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("patched",f)