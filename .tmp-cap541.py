import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\支.json"; d=json.load(io.open(p,encoding="utf-8"))
g=[s for s in d["sections"] if s.get("key")=="zizu"][0]["groups"]
g[1]["rows"]=[r for r in g[1]["rows"] if r[0]!="𢺵"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([r[0] for r in g[1]["rows"]], len(g[1]["rows"]))