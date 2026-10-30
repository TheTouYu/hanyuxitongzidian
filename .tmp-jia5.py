# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
J="j「聚决」取「聚」：軛聚加於牲口肩頸，聚攏而前拉（推）。"
G="g「隔估」取「隔」：軛加於牲口肩頸，橫隔而前拉（推）。"
Q="q「亲缺」取「亲」：加著於物，貼近而相合（推）。"
H="h「豁活」取「豁」：加禮相慶，場面豁然而開（推）。"
E="e「零聲母」不系：零聲母，緒論七組未列（照實）。"
names=["加","駕","嘉","枷","痂","𦙺","賀","妿","珈","鴐","跏","笳","㵑","𧝂","茄","䴥","𨔣","迦","泇","𢉤","架","𧉪","袈","伽","鉫"]
n=0
for name in names:
    p=os.path.join(C,name+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8")); py=(d.get("pinyin") or "")[:1]
    if py=="g": t=G
    elif py=="h": t=H
    elif py in ("q","j") : t=(Q if py=="q" else J)
    elif py=="e": t=E
    elif py in ("j","q"): t=J
    else: t=J if name not in ("賀","㵑","𧝂","妿") else H
    if name in ("賀","㵑","𧝂"): t=H
    if name=="妿": t=E
    if name=="鴐": t=G
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("updated",n)