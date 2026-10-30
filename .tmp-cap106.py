import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
e=[x for x in idx if x.get("c")=="祟"][0]
print("祟 aliases:",e.get("a"))
print("搜 𥜱 ->",[x["c"] for x in idx if "𥜱" in (x.get("a") or [])])