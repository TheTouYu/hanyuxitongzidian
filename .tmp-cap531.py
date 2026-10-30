# -*- coding: utf-8 -*-
import json,io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\支.json"; d=json.load(io.open(p,encoding="utf-8"))
g=[s for s in d["sections"] if s.get("key")=="zizu"][0]["groups"]
row=None
for gg in g:
    for r in gg["rows"]:
        if r[0]=="伎": row=list(r)
print("原行",row)
if row:
    g[0]["rows"].append(row)   # 原文①组末尾亦列伎（𢺵）
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("组行数",[len(x["rows"]) for x in g],"伎数",sum(1 for gg in g for r in gg["rows"] if r[0]=="伎"))