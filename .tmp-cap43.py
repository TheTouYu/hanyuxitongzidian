import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print([(x.get("c"),x.get("p"),x.get("lv")) for x in idx if x.get("c") in ("貍","狸")])