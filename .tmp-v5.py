import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
arr=d["cards"] if isinstance(d,dict) else d
hit=[x for x in arr if x.get("c")=="卷一雞"]
print(type(d).__name__, len(arr), hit)
print([x for x in arr if x.get("c")=="旨"][0])