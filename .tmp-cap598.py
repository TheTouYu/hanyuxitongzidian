# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pair={"失":"收","收":"失","续":"消","消":"续","亲":"缺","缺":"亲","聚":"决","决":"聚","隔":"估","估":"隔","凿":"总","总":"凿","囤":"动","动":"囤","涂":"突","突":"涂","闭":"剥","剥":"闭","豁":"活","活":"豁"}
real=[];ph=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if not isinstance(s,dict) or s.get("key")!="shengmu": continue
        t=s.get("text","")
        m=re.search(r"取「(.)」",t)
        if not m: continue
        o=pair.get(m.group(1))
        if not (o and o in t.split("：",1)[-1]): continue
        (ph if re.search(r"母",t) or len(t)<=20 else real).append((d.get("char"),t))
print("占位",len(ph),"真双面",len(real))
for b in real[:15]: print(b[0],"|",b[1][:50])