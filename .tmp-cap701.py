# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const it=IDX.find(x=>x.c===ch||((x.a||[]).includes(ch)));"
new="const it=IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)));"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=h.count(old)
    h=h.replace(old,new)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)