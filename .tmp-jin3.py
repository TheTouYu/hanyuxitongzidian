# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"斲":"斤","斮":"斤","匠":"匚","𪀘":"鳥","庍":"广","斱":"斤","赾":"走","䞪":"走","劤":"力",
   "妡":"女","䓄":"艸","旂":"㫃","𧞐":"衣","馸":"馬","䖐":"虎",
   "𪛊":"竹","盺":"目","炘":"火","峾":"山",
   "垽":"土","伒":"人","𪏴":"黍","邤":"邑","菦":"艸"}
p=os.path.join(C,"斤.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            for r in g["rows"]:
                b=r["字"].split("（")[0]
                if b in M: r["类属"]=M[b]
        print([[r["字"],r["类属"]] for g in s["groups"] for r in g["rows"]])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)