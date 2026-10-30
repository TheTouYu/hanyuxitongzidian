# -*- coding: utf-8 -*-
import json,io,os,re,sys
from docx import Document
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
BEN=re.sub(r"^本義：","",ps[148])
TR="\n".join(re.sub(r"^轉義：","",ps[k]) for k in (151,152,153))
Z=["①指席或席狀物"]
rows=[]
for k in range(155,159):
    t=ps[k]; m=re.match(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(?:（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ、，\s]*?)(?=《|：|$)",t)
    if not m: print("SKIP",k,t[:20]); continue
    rows.append([m.group(1),(m.group(2) or "").strip(" 、，"),"",t])
LEI={"蓆":"艸","褯":"衣","𥱊":"竹","𣝸":"木"}
for r in rows: r[2]=LEI.get(r[0],"" )
groups=[{"no":"①","title":"指席或席狀物","rows":rows}]
card={"char":"席","head":"席（𠩌𠩛𥔆）","pinyin":"xí","bus":{"num":45,"name":"石"},"parent":"石","level":2,"aliases":["𠩌","𠩛","𥔆"],
 "sections":[
  {"key":"benyi","label":"本义","text":BEN},
  {"key":"zhuanyi","label":"转义","text":TR},
  {"key":"shengmu","label":"声母拟态","text":"x「续消」取「收」：席以收捲鋪展為用，斂物而承之（推）。"},
  {"key":"zizu","label":"字族衍义","groups":groups},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"席.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=1
for r in rows:
    ch=r[0]
    c={"char":ch,"head":ch,"pinyin":r[1],"bus":{"num":45,"name":"石"},"parent":"席","level":3,"aliases":[],
       "sections":[{"key":"shiyi","label":"释义","text":r[3].rstrip("。")+"。"},
        {"key":"shengmu","label":"声母拟态","text":"x「续消」取「收」：席狀而收捲（推）。"},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
    json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# 图：p149
for el in doc.paragraphs[149]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        b=doc.part.related_parts[rid[0]].blob
        d=os.path.join(P,"席"); os.makedirs(d,exist_ok=True)
        for f in os.listdir(d): os.remove(os.path.join(d,f))
        ext="png" if b[:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(b)
        m=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m["photos"]["席"]=["01."+ext]
        json.dump(m,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
        c2=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); c2["captions"]["席"]=["河姆渡文化葦席殘片（7000年前）"]
        json.dump(c2,io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
        break
print("cards",n,"rows",len(rows))