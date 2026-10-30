# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
# 㳄：显式声源链（原文音源为「欠」，附于《次部》）
p = os.path.join(C, "㳄.json")
d = json.load(io.open(p, encoding="utf-8"))
d["rootChain"] = ["欠", "次", "㳄"]
json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# 索引构建器加 rc 字段
p = r"D:\系统汉字\.tmp-rel2.py"
t = io.open(p, encoding="utf-8").read()
if '"rc"' not in t:
    t = t.replace('"pr":(d.get("char") if d.get("level")==2 else d.get("parent",""))',
                  '"pr":(d.get("char") if d.get("level")==2 else d.get("parent","")),"rc":d.get("rootChain",[]),', 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("builder rc")
# 页面：优先用 rc；其次就近声根链；防自环
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h = io.open(f, encoding="utf-8").read(); o = h
    h = h.replace("const chain=[];let p=(t.lv===2)?t.c:((t.lv>2&&t.pr)?t.pr:t.n);let guard=0;",
                  "const chain=[];let p=(t.rc&&t.rc.length)?t.rc[t.rc.length-1]:((t.lv===2)?t.pr:((t.lv>2&&t.pr)?t.pr:t.n));let guard=0;")
    h = h.replace("while(p&&guard++<5){chain.push(p);const pc=byChar(p);p=pc?pc.pr:'';}",
                  "while(p&&guard++<5){chain.push(p);const pc=byChar(p);const nx=pc?pc.pr:'';if(nx===p)break;p=nx;}if(t.rc&&t.rc.length)chain.length=0,(t.rc).forEach(x=>chain.push(x));")
    if h != o:
        io.open(f, "w", encoding="utf-8", newline="\n").write(h)
        print(f.split("\\")[-1], "patched")
