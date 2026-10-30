# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
T=lambda k: ps[k]
G1=[(475,8),(476,8),(477,8),(478,8),(479,8),(480,8),(481,8)]
PY=r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+"
def split(t):
    m=re.match(r"^(\S{1,10}?)\s*("+PY+r")",t)
    if m: return m.group(1),m.group(2),t[m.end():].lstrip()
    m=re.match(r"^(\S{1,10}?)("+PY+r")",t)
    if m: return m.group(1),m.group(2),t[m.end():].lstrip()
    return t[:1],"",t[1:].lstrip()
def rows(paras):
    out=[]
    for k in paras:
        if not ps[k]: continue
        ch,py,rest=split(ps[k]); out.append([ch,py,rest])
    return out
r1=rows([475,476,477,478,479,480,481])
r2=rows(list(range(483,499)))
r2=[r for r in r2 if r[0] not in ("②","③")]
r3=rows([500,501,502])
SMG="g「隔估」取「隔」：軛加於牲口肩頸，橫隔而前拉（推）。"
SMH="h「豁活」取「豁」：加禮相慶，場面豁然而開（推）。"
SM0="「零聲母」不系：緒論七組未列（照實）。"
def sm(py):
    if py.startswith(("h",)): return SMH
    if py and py[0] in "gjkq": return SMG
    return SM0
def fam(rs,parent):
    for ch,py,rest in rs:
        name=ch.split("（")[0]
        c={"char":name,"head":ch,"pinyin":py,"level":3,"parent":parent,"bus":[{"num":37,"name":"加"}],
           "sections":[{"key":"shiyi","label":"释义","text":rest},{"key":"shengmu","label":"声母拟态","text":sm(py)},
             {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
        json.dump(c,io.open(os.path.join(C,name+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fam(r1,"加"); fam(r2,"加"); fam(r3,"加")
head={"char":"加","head":"加","pinyin":"jiā","level":1,"bus":[{"num":37,"name":"加"}],"aliases":[],
 "sections":[
  {"key":"benyi","label":"本义","text":T(466).split("：",1)[1]+"\n"+T(467).split("：",1)[1]},
  {"key":"zhuanyi","label":"转义","text":T(470).split("：",1)[1]+"\n"+T(471).split("：",1)[1]},
  {"key":"yinyuan","label":"音源","text":T(472).split("：",1)[1]},
  {"key":"shengmu","label":"声母拟态","text":SMG},
  {"key":"zizu","label":"字族衍义","groups":[
    {"no":"①","title":"指戴加，表示駕馭或增加","rows":[[r[0],r[1],"",r[2]] for r in r1]},
    {"no":"②","title":"指加狀，表示樣子如加","rows":[[r[0],r[1],"",r[2]] for r in r2]},
    {"no":"③","title":"音譯字","rows":[[r[0],r[1],"",r[2]] for r in r3]}]},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"加.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# glyphs p465 (+ photo p468)
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def blobs(k):
    o=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: o.append(parts[rid[0]].blob)
    return o
def dump(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    o=[]
    for i,b in enumerate(bs):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(i+1,ext)
        open(os.path.join(d,fn),"wb").write(b); o.append(ch+"/"+fn)
    return o
gb=blobs(465); jia=dump("加",gb[:-1]); jia2=dump("嘉",gb[-1:])
ixp=os.path.join(G,"index.json"); ix=json.load(io.open(ixp,encoding="utf-8")); chs=ix["chars"]
chs["加"]["files"]=jia; chs.setdefault("嘉",{"doc":"","variants":"","files":[]})["files"]=jia2
ph=ix.get("photos") or {}; pb=blobs(468)
if pb:
    d=os.path.join(G,"photos","加"); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    ext="png" if pb[0][:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(pb[0])
    ph["加"]=[{"file":"加/01."+ext,"caption":"魏晉磚畫《牛耕圖》"}]
ix["photos"]=ph
json.dump(ix,io.open(ixp,"w",encoding="utf-8"),ensure_ascii=False)
print("rows",len(r1),len(r2),len(r3),"glyphs",len(jia),len(jia2),"photo",bool(pb))