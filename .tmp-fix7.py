# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
reps=[
 ('norm(x.a)!==q','!((x.a||[]).includes(q))'),
 ("norm(x.a||'').includes(q)","((x.a||[]).some(t=>norm(t).includes(q)))"),
 ('x.c===ch||x.a===ch','x.c===ch||((x.a||[]).includes(ch))'),
]
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=0
    for a,b in reps:
        if a in h: h=h.replace(a,b); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"reps",n)