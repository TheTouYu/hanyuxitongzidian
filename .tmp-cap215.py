# -*- coding: utf-8 -*-
import json,io,glob,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
G={"b":("闭剥","闭"),"p":("拼辟","拼"),"f":("附分","附"),"m":("蒙末","蒙"),
"d":("囤动","囤"),"t":("涂突","突"),"n":("纳弄","弄"),"l":("拢离","拢"),
"g":("隔估","隔"),"k":("口控","口"),"h":("豁活","豁"),"j":("聚决","聚"),
"q":("亲缺","亲"),"x":("续消","续"),"zh":("凿总","凿"),"z":("凿总","凿"),
"ch":("刺持","刺"),"c":("刺持","刺"),"sh":("失收","失"),"s":("失收","收"),
"r":("柔锐","柔"),"y":("",""),"w":("",""),"":("","")}
n=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm or not sm[0]["text"].startswith("聲旁只記音"): continue
    py_=re.sub(r"[^a-zA-Z]","",d.get("pinyin") or "")[:2].lower()
    ini=py_ if py_ in ("zh","ch","sh") else py_[:1]
    pair,face=G.get(ini,("",""))
    g=""
    for k in ("benyi","shiyi"):
        s0=[x for x in d["sections"] if x["key"]==k]
        if s0: g=(s0[0].get("text") or "")[:22]; break
    if not pair:
        sm[0]["text"]="零聲母，緒論七組未列，不系（照實）。"
    else:
        sm[0]["text"]=f"{ini}「{pair}」取「{face}」：{g}——借聲之字，聲母亦摹其音（推）。"
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)