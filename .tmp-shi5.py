# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"石.json"),encoding="utf-8"))
SHOU={"祏":"收","宕":"失","鉐":"收","坧":"收","砅":"失","斫":"收","拓":"收","䞠":"失","袥":"失","沰":"失","𡇈":"失","䲽":"收","鼫":"收","蹠":"收","柘":"收","妬":"收","炻":"收","碩":"失","䄷":"收","𦚈":"失"}
n=0
for g in d["sections"][4]["groups"]:
    for ch,py,_ ,txt in g["rows"]:
        p=os.path.join(C,ch+".json")
        if os.path.exists(p): continue
        face=SHOU.get(ch,"收")
        c={"char":ch,"head":ch,"pinyin":py,"bus":{"num":45,"name":"石"},"parent":"石","level":3,"aliases":[],
           "sections":[{"key":"shiyi","label":"释义","text":txt},
            {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「%s」：%s（推）。"%(face,"石質收聚而堅" if face=="收" else "石散而遠大")},
            {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
        json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("made",n)