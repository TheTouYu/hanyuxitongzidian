import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\䵹.json",encoding="utf-8"))
print("head",d.get("head"),"aliases",d.get("aliases"),"trad",d.get("trad"),"char",d["char"])
idx=json.load(io.open(C+r"\index.json",encoding="utf-8"))
for x in idx:
    if x.get("c")=="䵹": print("idx",x)
for q in ("蜘","鼅"):
    print(q,[x.get("c") for x in idx if q in (x.get("a") or []) or x.get("c")==q])