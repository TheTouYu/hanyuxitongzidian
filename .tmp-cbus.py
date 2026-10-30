# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    t=io.open(p,encoding="utf-8").read()
    n=t.count("(d.bus||[])[0]")+t.count("(p.bus||[])[0]")+t.count("((d.bus||[{}])[0]||{})")
    t=t.replace("(d.bus||[])[0]||{}","(Array.isArray(d.bus)?d.bus[0]:(d.bus||{}))||{}")
    t=t.replace("(p.bus||[])[0]||{}","(Array.isArray(p.bus)?p.bus[0]:(p.bus||{}))||{}")
    t=t.replace("((d.bus||[{}])[0]||{})","(Array.isArray(d.bus)?(d.bus[0]||{}):(d.bus||{}))")
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
    print(p.split(chr(92))[-1],"replaced",n)