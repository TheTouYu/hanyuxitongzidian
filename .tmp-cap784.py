import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print("搜臺",[(x.get("c"),x.get("pr")) for x in idx if x.get("c")=="臺" or "臺" in (x.get("a") or [])])
print("台 a",[x.get("a") for x in idx if x.get("c")=="台"])