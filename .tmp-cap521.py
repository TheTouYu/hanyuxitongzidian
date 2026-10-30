import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\支.json",encoding="utf-8"))
g=[s for s in d["sections"] if s.get("key")=="zizu"][0]["groups"]
rows=[(gi,r) for gi,gg in enumerate(g) for r in gg["rows"]]
for gi,r in rows:
    if r[0] in ("伎","技","妓","䰙"): print(gi,r[0],r[1])
print("伎 count",sum(1 for _,r in rows if r[0]=="伎"),"总行",len(rows))