# -*- coding: utf-8 -*-
import json,sys,os,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
he=json.load(open(rf"{C}\曷.json",encoding="utf-8"))
MIME={"zh":"凿总：","z":"凿总：","ch":"刺持：","c":"刺持：","sh":"失收：","s":"失收：","h":"豁活：","g":"隔估：","k":"口控：","j":"聚决：","q":"亲缺：","x":"续消：","b":"闭剥：","p":"拼辟：","f":"附分：","m":"蒙末：","d":"囤动：","t":"涂突：","n":"纳弄：","l":"拢离：","r":"柔锐：","y":"","w":""}
n=0; made=[]
for g in he["sections"][-1]["groups"]:
    for r in g["rows"]:
        ch=r[0].split("（")[0]; py=r[1]; lei=r[2]; luo=r[3]
        f=rf"{C}\{ch}.json"
        ini="".join([c for c in py if c.isalpha()])[:2]
        key=ini if ini in MIME else ini[:1]
        sec=[{"key":"shiyi","label":"释义","text":f"从{lei}曷聲：{luo}。","cites":[]},
             {"key":"shengmu","label":"声母拟态","text":f"{key}「{MIME.get(key,'')}」{luo[:18]}（推）。" if MIME.get(key) else "今读零声母，不系（推）。","cites":[]}]
        d={"char":ch,"trad":ch,"simp":"","pinyin":py,"level":3,"parent":"曷","bus":[{"num":4,"name":"匃"}],"sections":sec}
        json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1; made.append(ch)
print("cards",n)
print("".join(made))