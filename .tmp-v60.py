# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); ch=False
    for s in d["sections"]:
        if s.get("key")=="js_音系" and s.get("groups"):
            for g in s["groups"]:
                g["header"]=["部目","字根","中心义","字族"]
                if g.get("rows") and len(g["rows"][0])!=4:
                    g["rows"]=[(r+["—"]*4)[:4] for r in g["rows"]]
            ch=True
    if ch: json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改表头",n)
d=json.load(io.open(C+r"\卷八虎.json",encoding="utf-8"))
s=[x for x in d["sections"] if x.get("key")=="js_音系"][0]
print(s["groups"][0]["header"], s["groups"][0]["rows"][0][:3])