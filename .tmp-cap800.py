# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
b=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(b,encoding="utf-8").read()
t=t.replace("return sorted(x for x in s if x and (x==c or x not in _OWN))","return sorted(x for x in s if x)",1)
io.open(b,"w",encoding="utf-8",newline="\n").write(t); print("aliases restored")
# 搜索排序：字头精确命中优先
for f in (r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const exact=IDX.filter(x=>x.c===q||x.a===q);","const exact=IDX.filter(x=>x.c===q||x.a===q).sort((a,b)=>(b.c===q)-(a.c===q));")
    h=h.replace("(x.a||[]).includes(q)","(x.a||[]).includes(q)")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"sort")
    else: print("MISS",f)