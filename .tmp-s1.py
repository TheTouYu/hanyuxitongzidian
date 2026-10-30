import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\士.json",encoding="utf-8"))
print("士 level",d.get("level"),"bus",d.get("bus"))
for s in d["sections"]:
    g=s.get("groups") or []
    print(s.get("key"),s.get("label"),"组",len(g),"字",sum(len(x.get("rows") or []) for x in g))