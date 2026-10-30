import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for x in idx:
    if x.get("c")=="㳄": print(x.get("c"),x.get("pr"),x.get("rc"))