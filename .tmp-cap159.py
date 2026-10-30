# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PAIR={"续":"消","消":"续","亲":"缺","缺":"亲","聚":"决","决":"聚","隔":"估","估":"隔",
"口":"控","控":"口","豁":"活","活":"豁","凿":"总","总":"凿","拢":"离","离":"拢","附":"分","分":"附",
"闭":"剥","剥":"闭","拼":"辟","辟":"拼","蒙":"末","末":"蒙","囤":"动","动":"囤","涂":"突","突":"涂",
"纳":"弄","弄":"纳","柔":"锐","锐":"柔","刺":"持","持":"刺","失":"收","收":"失"}
bad=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm: continue
    t=sm[0].get("text") or ""
    m=re.search(r"取「(.)」",t)
    if not m: continue
    x=m.group(1); y=PAIR.get(x)
    if not y: continue
    tail=t.split("」",1)[-1]  # after 取「X」
    if y in tail: bad.append((d["char"],x,y,t))
print("真违规",len(bad))
for c,x,y,t in bad: print(c,"|取",x,"|解释含",y,"|",t[:70])