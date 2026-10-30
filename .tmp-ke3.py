# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"可.json"),encoding="utf-8"))
G={"g":("隔估","隔"),"k":("口控","口"),"h":("豁活","豁"),"j":("聚决","聚"),"q":("亲缺","缺"),
"x":("续消","续"),"z":("凿总","凿"),"zh":("凿总","凿"),"c":("刺持","刺"),"ch":("刺持","持"),
"s":("失收","收"),"sh":("失收","收"),"b":("闭剥","闭"),"p":("拼辟","辟"),"f":("附分","分"),
"m":("蒙末","末"),"d":("囤动","囤"),"t":("涂突","突"),"n":("纳弄","纳"),"l":("拢离","拢"),"r":("柔锐","锐")}
FACE=["雁叫","雁身","浮水","宛曲","羽白"]
made=0
for gi,g in enumerate([x for x in d["sections"] if x.get("key")=="zizu"][0]["groups"]):
    for row in g["rows"]:
        head=row[0]; py=row[1].split("、")[0].split("，")[0]
        m=re.match(r"^([^\s（(]+)",head); ch=m.group(1)
        init=re.match(r"^(zh|ch|sh|[a-z])",py)
        if not init: continue
        ini=init.group(1); grp,face=G.get(ini,("",""))
        p=os.path.join(C,ch+".json")
        if os.path.exists(p): continue
        secs=[{"key":"shiyi","label":"释义","text":row[3],"cites":[]},
              {"key":"shengmu","label":"声母拟态","text":f"{ini}「{grp}」取「{face}」：从可之{FACE[gi]}义（推）。","cites":[]},
              {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}],"cites":[]}]
        dd={"char":ch,"head":head,"pinyin":row[1],"level":3,"parent":"可","bus":[{"num":34,"name":"丂"}],"aliases":[],"sections":secs}
        json.dump(dd,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("made",made)