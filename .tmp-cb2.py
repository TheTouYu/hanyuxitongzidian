# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"
t=io.open(p,encoding="utf-8").read()
old='if d.get("parent") != bu:'
new='if d.get("parent") and d.get("parent") != bu and not d.get("multi"):'
print("found", old in t)
if old in t:
    t=t.replace(old,new,1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)