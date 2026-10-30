import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尸.json"
d=json.load(io.open(p,encoding="utf-8"))
print("before trad",d.get("trad"),"char",d.get("char"))
d.pop("trad",None)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed")