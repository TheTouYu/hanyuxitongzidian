import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
items=idx if isinstance(idx,list) else idx.get("items",[])
print(type(idx).__name__, len(items))
for x in items:
    if x.get("c") in ("鴈","雁","厓"):
        print(x.get("c"),"h=",x.get("h"),"a=",x.get("a"),"lv=",x.get("lv"),"pr=",x.get("pr"))