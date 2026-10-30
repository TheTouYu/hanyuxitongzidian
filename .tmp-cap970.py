import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尸.json"
try:
    d=json.load(io.open(p,encoding="utf-8"))
    print("keys",list(d.keys()))
    print("sections",[(s.get("key"),s.get("label"),bool(s.get("groups"))) for s in d.get("sections",[])])
    for s in d.get("sections",[]):
        if s.get("groups"):
            for g in s["groups"]: print(" group",g.get("title"),len(g.get("rows") or []))
except Exception as e:
    print("ERR",e)
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
hit=[x for x in idx if x.get("c")=="尸"]
print("index",hit)