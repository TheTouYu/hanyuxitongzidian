# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"弋.json"),encoding="utf-8"))
F={"d":("囤动","动"),"t":("涂突","突"),"sh":("失收","失"),"zh":("凿总","凿"),"z":("凿总","凿"),"c":("刺持","持"),"ch":("刺持","持"),
"j":("聚决","聚"),"q":("亲缺","亲"),"x":("续消","续"),"b":("闭剥","闭"),"p":("拼辟","拼"),"m":("蒙末","蒙"),"l":("拢离","拢"),
"g":("隔估","隔"),"k":("口控","口"),"h":("豁活","活"),"f":("附分","分"),"n":("纳弄","纳"),"r":("柔锐","锐")}
n=0
for s in d["sections"]:
    if s["key"]!="zizu": continue
    for gi,g in enumerate(s["groups"]):
        for r in g["rows"]:
            ch,py_,t=r[0],r[1],r[3]
            p=os.path.join(C,ch+".json")
            ini=re.sub(r"[^a-z]","",py_.lower())[:2]
            key=ini if ini in F else ini[:1]
            if gi==4: sm="不取義：形近「戈」之訛，不涉聲旁取義。"
            elif ini in ("y","w",""): sm="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
            elif key in F:
                grp,face=F[key]; sm=f"{key}「{grp}」取「{face}」：{t.split('《')[0][:12]}（推）。"
            else: sm="y「零聲母」不系（照實）。"
            card={"char":ch,"trad":ch,"pinyin":py_,"level":3,"parent":"弋","bus":[{"num":26,"name":"弋"}],
              "sections":[{"key":"shiyi","label":"释义","text":t,"cites":[]},
                          {"key":"shengmu","label":"声母拟态","text":sm,"cites":[]},
                          {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}]}
            json.dump(card,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("弋族卡",n)