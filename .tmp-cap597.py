# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch,t in {"矢":"sh「失收」取「失」：箭離弦則一去不返（推）。",
             "鉃":"sh「失收」取「失」：箭鏃一發即失，銳鋒盡付於空（推）。"}.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
pair={"失":"收","收":"失","续":"消","消":"续","亲":"缺","缺":"亲","聚":"决","决":"聚","隔":"估","估":"隔","凿":"总","总":"凿","拢":"离","离":"拢","纳":"弄","弄":"纳","蒙":"末","末":"蒙","囤":"动","动":"囤","涂":"突","突":"涂","拼":"辟","辟":"拼","附":"分","分":"附","闭":"剥","剥":"闭","豁":"活","活":"豁","柔":"锐","锐":"柔"}
bad=[]; n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if not isinstance(s,dict) or s.get("key")!="shengmu": continue
        t=s.get("text",""); n+=1
        m=re.search(r"取「(.)」",t)
        if not m: continue
        other=pair.get(m.group(1))
        if other and other in t.split("：",1)[-1]:
            bad.append((d.get("char"),t))
print("有声母栏",n,"可疑",len(bad))
for b in bad[:10]: print(b[0],"|",b[1][:56])