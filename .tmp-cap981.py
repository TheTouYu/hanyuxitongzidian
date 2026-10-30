import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尸.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            if g["title"].startswith("③"):
                g["rows"]=[r for r in g["rows"] if r[0]=="屍"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]: print(g["title"],[r[0] for r in g["rows"]])