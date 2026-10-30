import json,io,re
r=json.load(open(r"data\knowledge\registry.json",encoding="utf-8"))
ts=r.get("topics",{})
items=ts.items() if isinstance(ts,dict) else [(t.get("id"),t) for t in ts]
for tid,t in items:
    p=(t.get("path") or "")
    if "38a" in p or "guai" in p: print(tid,"|",p,"|",t.get("title"))
print("--- have 茁?", "茁" in io.open(r"knowledge\hanzi-yinyuan\38a-guai.md",encoding="utf-8").read())