# -*- coding: utf-8 -*-
import json,io,os,re,sys
from docx import Document
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
BEN=re.sub(r"^本義：","",ps[160])
TR="\n".join(re.sub(r"^轉義：","",ps[k]) for k in range(161,168))
segs=[("①指通過",170,176),("②指堵塞",177,180),("③指揣度",181,185),("④指刻畫、裁割",186,191),("⑤指硬如石頭",192,194)]
LEI={"渡":"水","踱":"足","𨍏":"車","䩲":"革","艔":"舟","𪃒":"鳥","𢾅":"攴","𥯖":"竹","𡍨":"土","𢜬":"心","庹":"广","喥":"口","𧶴":"貝","鍍":"金","𣨲":"歹","𦂀":"糸","𧩧":"言","剫":"刀","𦳔":"艸","𩩮":"骨"}
RX=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(?:（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ、，\s]*?)(?=《|：|$)")
groups=[]; rows_all=[]
for title,a,b in segs:
    rr=[]
    for k in range(a,b):
        t=ps[k]
        if not t: continue
        m=RX.match(t)
        if not m: print("SKIP",k,t[:20]); continue
        ch=m.group(1); py=(m.group(2) or "").strip(" 、，")
        rr.append([ch,py,LEI.get(ch,""),t]); rows_all.append(ch)
    groups.append({"no":title[0],"title":title[1:],"rows":rr})
card={"char":"度","head":"度（㡯𤸿𡧪）","pinyin":"dù","bus":{"num":45,"name":"石"},"parent":"石","level":2,"aliases":["㡯","𤸿","𡧪"],
 "sections":[{"key":"benyi","label":"本义","text":BEN},
  {"key":"zhuanyi","label":"转义","text":TR},
  {"key":"shengmu","label":"声母拟态","text":"d「囤动」取「动」：持石而動作，動而有度（推）。"},
  {"key":"zizu","label":"字族衍义","groups":groups},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"度.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=1
for g in groups:
    for ch,py,lei,txt in g["rows"]:
        c={"char":ch,"head":ch,"pinyin":py,"bus":{"num":45,"name":"石"},"parent":"度","level":3,"aliases":[],
           "sections":[{"key":"shiyi","label":"释义","text":txt},
            {"key":"shengmu","label":"声母拟态","text":"d「囤动」取「动」：石之動用，「%s」（推）。"%g["title"][:2]},
            {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
        json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards",n,[(g["title"],len(g["rows"])) for g in groups])