# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const lab=(it&&it.h)||((it?it.c:ch)+al);","const lab=(it?it.c:ch);")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"chips=字头")
    else: print("MISS")