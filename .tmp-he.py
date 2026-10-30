# -*- coding: utf-8 -*-
import sys,os,re,json,io,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
DOC=r"D:\字谱智能体\卷六  鶴.docx"
doc=Document(DOC); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
HAN=r"[\u3400-\u4DBF\u9fff\U00020000-\U0002A6DF]"
ROW=re.compile(r"^("+HAN+r"+)(?:（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹḿ、·]+)?\s*(.*)$")

def blobs(a,b):
    out=[]
    for k in range(a,b+1):
        for el in doc.paragraphs[k]._p.iter():
            if el.tag.split("}")[-1]=="blip":
                rid=[v for a2,v in el.attrib.items() if a2.endswith("}embed") or a2.endswith("}id")]
                if rid:
                    try: out.append(parts[rid[0]].blob)
                    except KeyError: pass
    return out

def save_glyphs(ch,a,b):
    bs=blobs(a,b); d=os.path.join(G,ch)
    if not bs: return 0
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(d,exist_ok=True)
    for i,b in enumerate(bs):
        ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
        if ext=="bin": continue
        open(os.path.join(d,"%02d.%s"%(i+1,ext)),"wb").write(b)
    return len(bs)

def rows(k1,k2):
    r=[]
    for k in range(k1,k2+1):
        t=ps[k]
        if not t or t.startswith("▲"): continue
        m=ROW.match(t); 
        if m: r.append({"ch":m.group(1),"alt":[x for x in (m.group(2) or "").split() if x],"py":(m.group(3) or "").replace("、","／"),"text":t})
    return r

def card(ch,head,py,level,parent,secs,groups,aliases=None):
    d={"char":ch,"head":head,"pinyin":py,"level":level,"parent":parent,
       "bus":[{"num":42,"name":"禾"}],"aliases":aliases or [],"sections":secs,"groups":groups}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)

def sec(key,label,text): return {"key":key,"label":label,"text":text}

# 禾
gh1=save_glyphs("禾",335,341)
card("禾","禾","hé",1,None,[
 sec("benyi","本义",ps[342]),sec("zhuanyi","转义",ps[344]),
 sec("bianzheng","辩证",ps[346]),sec("yinyuan","音源",ps[348]),
 sec("shengmu","声母拟态","g「隔估」取「隔」：禾形似戈，戈之橫刃與柄相闔而橫隔（推）。")],
 [{"no":"①","title":"指禾之用，表示應和、調和、和順","rows":[{"ch":r["ch"],"alt":"／".join(r["alt"]),"py":r["py"],"cat":"口／龠／金／言／心／木／女","text":r["text"]} for r in rows(351,358)]},
  {"no":"②","title":"指盉之狀，表示一頭細長一頭肥大之物","rows":[{"ch":r["ch"],"alt":"／".join(r["alt"]),"py":r["py"],"cat":"皿／艸","text":r["text"]} for r in rows(360,363)]}],
 ["咊"])
# 科
gh2=save_glyphs("科",364,364)
m=ROW.match(ps[364]); kh=m.group(1) if m else "科"
card(kh,kh,"kē",2,"禾",[
 sec("benyi","本义",ps[365]),sec("zhuanyi","转义","\n".join([ps[366],ps[367],ps[368]])),
 sec("shengmu","声母拟态","k「口控」取「口」：斗圓而柄曲，舀酒出入其口（推）。")],
 [{"no":"①","title":"指科的長柄而圓頭形","rows":[{"ch":r["ch"],"alt":"／".join(r["alt"]),"py":r["py"],"cat":"虫／牛／竹／艸","text":r["text"]} for r in rows(372,375)]}])
# 族卡
fams=[r for r in rows(351,358)]+[r for r in rows(360,363)]+[r for r in rows(372,375)]
for r in fams:
    par = kh if r["ch"] in [x["ch"] for x in rows(372,375)] else "禾"
    card(r["ch"],r["ch"],r["py"],3,par,[sec("shiyi","释义",r["text"]),sec("shengmu","声母拟态","（按今讀聲母取擬態義一面，推。）")],[])
print("禾 glyphs",gh1,"科 glyphs",gh2,"fams",len(fams))