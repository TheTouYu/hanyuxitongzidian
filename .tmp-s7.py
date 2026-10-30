# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\野.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["text"]="原稿：指郊野，表示野外的物体或状态。"
        for g in (s.get("groups") or []):
            g["title"]="①指郊野，表示野外的物体或状态"
            rows=g.get("rows") or []
            have={r[0] for r in rows}
            add=[["嘢","yě","口","方言，指「東西」；从口野聲"]]
            for a in add:
                if a[0] not in have: rows.insert(len(rows)-1,a)
            g["rows"]=rows
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",[ (g.get("title"),[r[0] for r in g.get("rows") or []]) for s in d["sections"] if s.get("key")=="zizu" for g in s.get("groups") or []])