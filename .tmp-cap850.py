# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const byChar=ch=>IDX.find(x=>x.c===ch||((x.a||[]).includes(ch)));"
new="const byChar=ch=>IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)));"
for f in (r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=h.count(old)
    if n==0:
        h2=h.replace("IDX.find(x=>x.c===ch||((x.a||[]).includes(ch)))","IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)))")
        io.open(f,"w",encoding="utf-8",newline="\n").write(h2); print(f.split("\\")[-1],"alt")
    else:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h.replace(old,new)); print(f.split("\\")[-1],n)