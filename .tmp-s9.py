# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\野.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in (s.get("groups") or []):
            rows=g.get("rows") or []
            have={r[0] for r in rows}
            add=[["𤍓","shù","火","《字彙》：「音豎。野火。」野火；从火野聲"],
                 ["𧐓","yě","虫","《玉篇》：「音野。蟲也。」蟲名；从虫野聲"]]
            for a in add:
                if a[0] not in have: rows.append(a)
            g["rows"]=rows
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([[r[0] for r in g["rows"]] for s in d["sections"] if s.get("key")=="zizu" for g in s.get("groups",[])])