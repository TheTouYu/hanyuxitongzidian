# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]
rows=[("𨥟","xī","金",ps[120],"x「续消」取「消」：絆而消（推）。"),
("𥍠（𥍟）","xù","矛",ps[121],"x「续消」取「续」：長矛續接（推）。"),
("𧿝","xī","足",ps[122],"x「续消」取「消」：跡消（推）。"),
("肹（肸）","xī","肉",ps[124],"x「续消」取「消」：散布而消（推）。"),
("𪏱（𪏯）","lí","黃",ps[125],"l「拢离」取「拢」：眾聚（推）。"),
("𦖬（𦗃𥈕）","mí","耳",ps[126],"m「蒙末」取「蒙」：汙面蒙（推）。"),
("𨳣（𨳚𨳜䦏𨳿）","fēn","門",ps[127],"f「附分」取「分」：火氣分（推）。")]
import re
for r in rows:
    bare=re.match(r"^([^\s（(]+)",r[0]).group(1)
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"兮","bus":[{"num":34,"name":"丂"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(d,io.open(os.path.join(C,bare+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=os.path.join(C,"兮.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        gs=[g for g in s["groups"] if not g["title"].startswith("③")]
        gs.append({"title":"③形近字「丂、勿、必、分」之訛","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows]})
        s["groups"]=gs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("groups",[ (g["title"][:6],len(g["rows"])) for g in d["sections"][1]["groups"]] if False else [ (g["title"][:8],len(g["rows"])) for s in d["sections"] if s.get("key")=="zizu" for g in s["groups"]])