# -*- coding: utf-8 -*-
import os,json,io,sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
CM=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
ORDER=["benyi","bengen","zhuanyi","bianzheng","yinyuan","shengmu","zixing","zizu","suoshujuan","suoshu","shiyi"]
LBL={"benyi":"本义","bengen":"本义","zhuanyi":"转义","bianzheng":"辩证","yinyuan":"音源","shengmu":"声母拟态","zixing":"字形","zizu":"字族衍义","suoshujuan":"所属卷","suoshu":"所属卷","shiyi":"释义"}
CONTENT={"benyi","bengen","shiyi","zhuanyi","bianzheng","yinyuan"}
fixed=0; filled=0; zx=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    lv=d.get("level",3); secs=d.get("sections") or []
    has=[s for s in secs if s.get("key") in CONTENT and (s.get("text") or s.get("groups"))]
    if not has:
        txt=((CM.get(ch) or {}).get("txt") or "").strip()
        if not txt: txt="（原稿未收释义）"
        key="shiyi" if lv>=3 else "benyi"
        secs.insert(0,{"key":key,"label":LBL[key],"text":txt,"cites":[]})
        filled+=1
    if lv<=2:
        if not any(s.get("key")=="zixing" for s in secs):
            gd=os.path.join(G,ch); n=len([f for f in os.listdir(gd) if f.endswith(".png")]) if os.path.isdir(gd) else 0
            if n: secs.append({"key":"zixing","label":"字形","text":f"共 {n} 形，见卡头字形带。","cites":[]}); zx+=1
    secs.sort(key=lambda s: ORDER.index(s["key"]) if s["key"] in ORDER else 99)
    if secs!=d.get("sections"):
        d["sections"]=secs; fixed+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("补内容",filled,"补字形",zx,"重排",fixed)