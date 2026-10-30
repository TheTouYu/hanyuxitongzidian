import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for x in idx:
    if x.get("c") in ("臺","至"): print(x.get("c"),"pr=",x.get("pr"),"a=",x.get("a"),"h=",x.get("h"))