# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const lab=(it?it.c:ch)+al;","const lab=(it&&it.h)||((it?it.c:ch)+al);")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"ok")
    else: print(f.split("\\")[-1],"MISS")
b=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(b,encoding="utf-8").read()
if '"h":' not in t:
    t=t.replace('"c":','"h":d.get("head") or "",\n      "c":',1)
    io.open(b,"w",encoding="utf-8",newline="\n").write(t); print("builder h")