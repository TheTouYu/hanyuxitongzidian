# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const exact=IDX.filter(x=>x.c===q||((x.a||[]).includes(q)));"
new="const exact=IDX.filter(x=>x.c===q||((x.a||[]).includes(q))).sort((a,b)=>(b.c===q)-(a.c===q));"
for f in (r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=h.count(old)
    h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)