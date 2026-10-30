# -*- coding: utf-8 -*-
import json,io,os,re,sys
from docx import Document
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
BEN=re.sub(r"^本義：","",ps[195])
TR="\n".join(re.sub(r"^轉義：","",ps[k]) for k in range(196,200))
segs=[("①指叚形，表示大、遠、閑、久",204,213),("②指叚質，表示堅硬",214,222),("③指叚色，表示赤、斑駁",226,235)]
LEI={"假":"人","嘏":"古","暇":"日","遐":"辵","徦":"彳","䫗":"頁","蕸":"艸","睱":"目","婽":"女","瘕":"疒","豭":"豕","椵":"木","麚":"鹿","䠍":"足","鍜":"金","䪗":"韋","犌":"牛","碬":"石","騢":"馬","瑕":"玉","葭":"艸","鰕":"魚","赮":"赤","𣮫":"毛","貑":"豸","霞":"雨","蝦":"虫"}
RX=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(?:（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ、，\s]*?)(?=《|：|$)")
groups=[]
for title,a,b in segs:
    rr=[]
    for k in range(a,b):
        t=ps[k]
        if not t: continue
        m=RX.match(t)
        if not m: print("SKIP",k,t[:20]); continue
        ch=m.group(1); py=(m.group(2) or "").strip(" 、，")
        rr.append([ch,py,LEI.get(ch,""),t])
    groups.append({"no":title[0],"title":title[1:],"rows":rr})
card={"char":"叚","head":"叚（𠖊𠭊）","pinyin":"jiǎ","bus":{"num":45,"name":"石"},"parent":"石","level":2,"aliases":["𠖊","𠭊"],
 "sections":[{"key":"benyi","label":"本义","text":BEN},
  {"key":"zhuanyi","label":"转义","text":TR},
  {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：石之輾轉相聚而假借於人（推）。"},
  {"key":"zizu","label":"字族衍义","groups":groups},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"叚.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=1
for g in groups:
    for ch,py,lei,txt in g["rows"]:
        c={"char":ch,"head":ch,"pinyin":py,"bus":{"num":45,"name":"石"},"parent":"叚","level":3,"aliases":[],
           "sections":[{"key":"shiyi","label":"释义","text":txt},
            {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：石之相聚而%s（推）。"%g["title"][1:4]},
            {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
        json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# 图：叚=p200/花崗岩 p201；碬=p223/礪石 p224；蝦=p235/蛤蟆 p236
def grab(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            return doc.part.related_parts[rid[0]].blob
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); cx=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))
for ch,imgk,cap in (("叚",200,"花崗岩"),("碬",223,"良渚文化遺址礪石（5000年前）"),("蝦",235,"蛤蟆")):
    b=grab(imgk)
    if not b: continue
    d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    ext="png" if b[:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(b)
    ix["photos"][ch]=["01."+ext]; cx["captions"][ch]=[cap]
json.dump(ix,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump(cx,io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("cards",n,[(g["title"],len(g["rows"])) for g in groups])