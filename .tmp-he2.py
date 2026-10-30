# -*- coding: utf-8 -*-
import sys,os,re,json,io,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
def rows(a,b):
    out=[]
    for k in range(a,b+1):
        t=ps[k]
        if not t or t.startswith("▲"): continue
        m=re.match(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(（[^）]*）)?([^《]*)?(.*)$",t)
        if not m: continue
        ch=m.group(1); alt=(m.group(2) or "").strip("（）"); py=(m.group(3) or "").strip(" 、，")
        out.append({"ch":ch,"alt":alt,"py":py,"text":t})
    return out
print(len(rows(351,358)),len(rows(360,363)),len(rows(372,375)))
r1=rows(351,358); r2=rows(360,363); r3=rows(372,375)
kh=rows(364,364)
def card(ch,head,py,level,parent,secs,groups,aliases=None):
    json.dump({"char":ch,"head":head,"pinyin":py,"level":level,"parent":parent,
      "bus":[{"num":42,"name":"禾"}],"aliases":aliases or [],"sections":secs,"groups":groups},
      io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def sec(k,l,t): return {"key":k,"label":l,"text":t}
card("禾","禾","hé",1,None,[sec("benyi","本义",ps[342]),sec("zhuanyi","转义",ps[344]),sec("bianzheng","辩证",ps[346]),sec("yinyuan","音源",ps[348]),sec("shengmu","声母拟态","g「隔估」取「隔」：禾形似戈，戈之橫刃與柄相闔而橫隔（推）。")],
 [{"no":"①","title":"指禾之用，表示應和、調和、和順","rows":[{"ch":r["ch"],"alt":r["alt"],"py":r["py"],"cat":"口／龠／金／言／心／木／女","text":r["text"]} for r in r1]},
  {"no":"②","title":"指盉之狀，表示一頭細長一頭肥大之物","rows":[{"ch":r["ch"],"alt":r["alt"],"py":r["py"],"cat":"皿／艸","text":r["text"]} for r in r2]}],["咊"])
khc=kh[0]["ch"] if kh else "科"
card(khc,khc,"kē",2,"禾",[sec("benyi","本义",ps[365]),sec("zhuanyi","转义","\n".join([ps[366],ps[367],ps[368]])),sec("shengmu","声母拟态","k「口控」取「口」：斗圓而柄曲，舀酒出入其口（推）。")],
 [{"no":"①","title":"指科的長柄而圓頭形","rows":[{"ch":r["ch"],"alt":r["alt"],"py":r["py"],"cat":"虫／牛／竹／艸","text":r["text"]} for r in r3]}])
for r in r1+r2+r3:
    par = khc if r in r3 else "禾"
    card(r["ch"],r["ch"],r["py"],3,par,[sec("shiyi","释义",r["text"]),sec("shengmu","声母拟态","（按今讀聲母取擬態義一面，推。）")],[])
print("cards", 2+len(r1+r2+r3), "科头", khc)