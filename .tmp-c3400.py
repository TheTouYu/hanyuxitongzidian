import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\曳.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]!="zizu": continue
    print("text:",(s.get("text") or "")[:50])
    for g in s.get("groups",[]) or []:
        print("组:",g.get("title"))
        for r in g.get("rows",[]) or []:
            if len(r)>=3 and r[2].strip(): print(" 有类属:",r[0],"|",r[2])