import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\知.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="shengmu": s["text"]="zh「凿总」取「总」：報靶人總合諸箭中否之況，一總而報（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(s["text"])