import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\夷.json",encoding="utf-8"))
chs=[]
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            for r in g["rows"]: chs.append(r[0].split("（")[0])
bad=[]
for ch in chs:
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): bad.append((ch,"no card")); continue
    c=json.load(io.open(p,encoding="utf-8"))
    if c.get("parent")!="夷" or c.get("level")!=3: bad.append((ch,c.get("parent"),c.get("level")))
print(len(chs),"族字，问题",len(bad)); print(bad[:12])