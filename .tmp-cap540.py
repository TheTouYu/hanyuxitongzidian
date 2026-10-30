# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\支.json"; d=json.load(io.open(p,encoding="utf-8"))
g=[s for s in d["sections"] if s.get("key")=="zizu"][0]["groups"]
rows=[r for r in g[0]["rows"] if r[0]!="伎"]   # ①组不应有伎
g[0]["rows"]=rows
second=[r for r in g[1]["rows"] if r[0]=="伎"][0]
rest=[r for r in g[1]["rows"] if r[0]!="伎"]
dedupe=[];seen=set()
for r in rest:
    if r[0] not in seen: seen.add(r[0]); dedupe.append(r)
# 按原文：②组以伎开头，䞚之后再来一次伎
out=[second]+dedupe
idx=[i for i,r in enumerate(out) if r[0]=="䞚"][0]
out.insert(idx+1, second)
g[1]["rows"]=out
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("组行",[len(x["rows"]) for x in g])
print([r[0] for r in g[1]["rows"]])