# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
rid=None
for el in ps[100]._p.iter():
    for a,v in el.attrib.items():
        if (a.endswith("}embed") or a.endswith("}id")) and v in parts:
            rid=v
b=parts[rid].blob
D=r"D:\系统汉字\web\public\glyphs\inline\䵹\shiyi"; os.makedirs(D,exist_ok=True)
ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
p=r"D:\系统汉字\web\public\cards\䵹.json"; d=json.load(io.open(p,encoding="utf-8"))
img=f'<img class="gin" src="glyphs/inline/䵹/shiyi/{fn}" alt="字形">'
for s in d["sections"]:
    if s["key"]=="shiyi":
        s["text"]=s["text"].replace("聲。，或从虫","聲。"+img+"，或从虫")
    if s["key"]=="shengmu":
        s["text"]="zh「凿总」取「总」：蜘蛛坐鎮網中，總羅昆蟲（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("img",fn,len(b),"text ok", img in d["sections"][0]["text"])
# 规模：正文出现「聲。」「。」等丢字痕迹
C=r"D:\系统汉字\web\public\cards"; cnt=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    try: dd=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if not isinstance(dd,dict): continue
    for s in dd.get("sections",[]):
        if isinstance(s,dict) and s.get("key")=="shiyi" and re.search(r"聲。，|。，|，。",s.get("text","")): cnt+=1
print("疑似丢字卡",cnt)