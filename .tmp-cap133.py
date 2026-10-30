import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print([x["c"] for x in idx if x["c"] in ("谿","溪") or "溪" in (x.get("a") or [])])