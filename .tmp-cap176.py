import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V=json.load(io.open(r"D:\系统汉字\web\public\cards\variants.json",encoding="utf-8"))
for c in ("龁","齕","讫","訖"):
    print(c, V.get(c), [k for k,v in V.items() if c in (v if isinstance(v,list) else [v])][:3])
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print("龁",[x.get("c") for x in idx if x.get("c")=="龁" or "龁" in (x.get("a") or [])])
print("齕",[x.get("c") for x in idx if x.get("c")=="齕" or "齕" in (x.get("a") or [])])