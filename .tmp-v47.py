# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    key="b.num===0?(function(){"
    for _ in range(5):
        i=h.find(key)
        if i<0: break
        j=h.find("}()):",i)
        if j<0: break
        h=h[:i]+"d.chapterCard?'':"+h[j+len("}()):"):]
        n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"replaced",n)