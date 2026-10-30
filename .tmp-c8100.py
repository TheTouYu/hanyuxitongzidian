# -*- coding: utf-8 -*-
import json,io,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); P=os.path.join(ROOT,"web","public","glyphs","photos")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]
def grab(a,b):
    out=[];cur=None;buf={}
    for k in range(a,b):
        t=ps[k]
        if not t: continue
        if t.startswith("本義"): cur="benyi"; buf[cur]=[t.split("：",1)[-1]]; continue
        if t.startswith("轉義"): cur="zhuanyi"; buf[cur]=[t.split("：",1)[-1]]; continue
        if t.startswith("辯證"): cur="bianzheng"; buf[cur]=[t.split("：",1)[-1]]; continue
        if t.startswith("音源"): cur="yinyuan"; buf[cur]=[re.sub(r"^音源[：:]?","",t)]; continue
        if cur: buf[cur].append(t)
    return {k:"\n".join(v) for k,v in buf.items()}
S=grab(287,295)
rows=[["㰘","yí","木","《說文》：「木也。从木彝聲。羊皮切。」樹名。《正字通·木部》：「或曰古禮器多用木，此木可作彝器，故从木。」","y「零聲母」不系：零聲母，緒論七組未列（照實）。"]]
head={"char":"彝","head":"彝（彜彛彞𢁔𢍵𢑴𦇚𢇏𦄳𦆩𧤋𢑱𢑲）","pinyin":"yí","level":1,"bus":[{"num":30,"name":"彝"}],
 "sections":[{"key":"benyi","label":"本义","text":S.get("benyi",""),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":S.get("zhuanyi",""),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":S.get("bianzheng",""),"cites":[]},
  {"key":"yinyuan","label":"音源","text":S.get("yinyuan",""),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[{"title":"①樹名（古禮器多用木）","note":"","rows":rows}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
# 插图
parts=doc.part.related_parts; fn=None
for k in range(290,293):
    for el in doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>8000:
                    ext=".png" if b[:4]==b"\x89PNG" else (".emf" if b[:4]==b"\x01\x00\x00\x00" else ".jpg"); fn="01"+ext
                    D=os.path.join(P,"彝"); os.makedirs(D,exist_ok=True); open(os.path.join(D,fn),"wb").write(b)
    if fn: break
if fn:
    head["photos"]=[fn]; head["captions"]=["婦好墓出土的偶方彝（商）"]
json.dump(head,io.open(os.path.join(C,"彝.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
d={"char":"㰘","head":"㰘","pinyin":"yí","level":3,"parent":"彝","bus":[{"num":30,"name":"彝"}],
   "sections":[{"key":"shiyi","label":"释义","text":rows[0][3],"cites":[]},
    {"key":"shengmu","label":"声母拟态","text":rows[0][4],"cites":[]},
    {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
json.dump(d,io.open(os.path.join(C,"㰘.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 索引与图注
if fn:
    i=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=i.get("photos") or i; ph["彝"]=[fn]
    json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["彝"]=["婦好墓出土的偶方彝（商）"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("photo",fn,flush=True)