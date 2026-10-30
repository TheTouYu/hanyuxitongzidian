import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\射.json",encoding="utf-8"))
g=[s for s in d["sections"] if s["key"]=="zizu"][0]
print("title",g["groups"][0].get("title"),"rows",len(g["groups"][0].get("rows",[])))
print(json.dumps(g["groups"][0]["rows"][:2],ensure_ascii=False)[:300])