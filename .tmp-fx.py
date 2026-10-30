# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="((t.lv>=2&&t.pr)?t.pr:t.n)"
new="(t.pr||t.n)"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    t=io.open(f,encoding="utf-8").read()
    n=t.count(old)
    if n: io.open(f,"w",encoding="utf-8",newline="\n").write(t.replace(old,new))
    print(f.split("\\")[-1],n)