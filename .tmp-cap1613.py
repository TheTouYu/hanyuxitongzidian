# -*- coding: utf-8 -*-
import io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h = io.open(f, encoding="utf-8").read(); o = h
    h = h.replace("const chain=[];let p=(t.lv>1&&t.pr)?t.pr:t.n;let guard=0;",
                  "const chain=[];let p=(t.lv===2)?t.c:((t.lv>2&&t.pr)?t.pr:t.n);let guard=0;")
    if h != o:
        io.open(f, "w", encoding="utf-8", newline="\n").write(h)
        print(f.split("\\")[-1], "patched")
# 索引 pr：二级字根自身即声根
p = r"D:\系统汉字\.tmp-rel2.py"
t = io.open(p, encoding="utf-8").read()
old = '"pr":d.get("parent","")'
new = '"pr":(d.get("char") if d.get("level")==2 else d.get("parent",""))'
if old in t:
    io.open(p, "w", encoding="utf-8", newline="\n").write(t.replace(old, new, 1))
    print("builder patched")
