# -*- coding: utf-8 -*-
import os,json,io,sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
ORDER=["benyi","bengen","zhuanyi","bianzheng","yinyuan","shengmu","zixing","zizu","suoshujuan","suoshu","shiyi"]
LBL={"benyi":"本义","bengen":"本义","zhuanyi":"转义","bianzheng":"辩证","yinyuan":"音源","shengmu":"声母拟态","zixing":"字形","zizu":"字族衍义","suoshujuan":"所属卷","suoshu":"所属卷","shiyi":"释义"}
def rank(k): 
    return ORDER.index(k) if k in ORDER else 99
fix=0; addzx=0; pruned=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    lv=d.get("level",3)
    secs=d.get("sections") or []
    if lv>=3:
        keep=[s for s in secs if s.get("key") in ("shiyi","shengmu","suoshujuan","suoshu")]
        if len(keep)!=len(secs): pruned+=1
        secs=keep
    else:
        keys={s.get("key") for s in secs}
        if "zixing" not in keys:
            gd=os.path.join(G,ch); n=len([f for f in os.listdir(gd) if f.endswith(".png")]) if os.path.isdir(gd) else 0
            if n:
                secs.append({"key":"zixing","label":"字形","text":f"共 {n} 形，见卡头字形带。","cites":[]}); addzx+=1
        if not any(k in keys for k in ("suoshujuan","suoshu")):
            secs.append({"key":"suoshujuan","label":"所属卷","text":"","cites":[]})
    secs.sort(key=lambda s: rank(s.get("key","")))
    for s in secs:
        if not s.get("label"): s["label"]=LBL.get(s.get("key",""),s.get("key",""))
    if secs!=d.get("sections"):
        d["sections"]=secs; fix+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("排序/修结构",fix,"补字形栏",addzx,"谐声字精简",pruned)