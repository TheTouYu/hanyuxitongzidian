import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\弋.json",encoding="utf-8"))
g=[s for s in d["sections"] if s["key"]=="zizu"][0]["groups"][0]["rows"]
for r in g[:5]: print(r[0],"|",r[1])