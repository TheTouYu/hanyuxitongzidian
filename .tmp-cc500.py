# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs"); P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
def blobs(k):
    o=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: o.append(parts[rid[0]].blob)
                except KeyError: pass
    return o
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
gb=blobs(73); d=os.path.join(G,"乎"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
names=[]
for i,b in enumerate(gb,1):
    fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
e=chars.get("乎") or {"doc":"","variants":[]}; e["files"]=names; chars["乎"]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# inline glyphs in 本義 (p74)
ib=blobs(74); ID=os.path.join(G,"inline","乎","benyi"); os.makedirs(ID,exist_ok=True)
for f in os.listdir(ID): os.remove(os.path.join(ID,f))
inames=[]
for i,b in enumerate(ib,1):
    fn="%02d.%s"%(i,kd(b)); open(os.path.join(ID,fn),"wb").write(b); inames.append(fn)
def photo(par,ch,cap):
    b=blobs(par)
    b=[x for x in b if len(x)>8000]
    if not b: return None
    dd=os.path.join(P,ch); os.makedirs(dd,exist_ok=True)
    for f in os.listdir(dd): os.remove(os.path.join(dd,f))
    fn="01."+kd(b[0]); open(os.path.join(dd,fn),"wb").write(b[0])
    ip=os.path.join(P,"index.json"); i=json.load(io.open(ip,encoding="utf-8")); ph=i.get("photos") or i; ph[ch]=[fn]
    json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
    cm[ch]=[cap]; json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
    return fn
pf=photo(85,"㭔","黃櫨花（不孕花梗久留，如吐氣成霧）"); pg=photo(97,"𩶈","蝠鱝（魔鬼魚）")
rows=[("呼（詨謼謞嚆誟嘮罅）","hū、xiāo、xū、hè、xià、lì","口",ps[79],"h「豁活」取「豁」：張口吐氣豁然而出（推）。"),
("𧦝","hū","言",ps[80],"h「豁活」取「豁」：召喚而豁出（推）。"),
("軤","hū","車",ps[81],"h「豁活」取「豁」：車聲豁然（推）。"),
("𤝘","hú","犬",ps[82],"h「豁活」取「豁」：犬吠豁出（推）。"),
("㭔","lú","木",ps[84],"l「拢离」取「拢」：花梗久聚不落（推）。"),
("烀","hū","火",ps[86],"h「豁活」取「豁」：氣豁而熟（推）。"),
("苸","hū","艸",ps[87],"h「豁活」取「豁」：艸多豁生（推）。"),
("雽","hū、hù","雨",ps[88],"h「豁活」取「豁」：雨氣豁然（推）。"),
("䉿（糊）","hú","米",ps[89],"h「豁活」取「豁」：黏而豁合（推）。"),
("𤇠","hū","火",ps[90],"h「豁活」取「豁」：得而豁然（推）。"),
("泘（滹）","hū","水",ps[92],"h「豁活」取「豁」：水勢豁然（推）。"),
("𡛚（媩）","hú","女",ps[93],"h「豁活」取「豁」：女字（推）。"),
("𪕉（猢）","hú","鼠",ps[94],"h「豁活」取「豁」：猿屬靈活（推）。"),
("𥬏（箶）","hú","竹",ps[95],"h「豁活」取「豁」：箭室中空（推）。"),
("𩶈","hū","魚",ps[96],"h「豁活」取「豁」：巨口豁然（推）。"),
("垀（㙤培㟝附）","hū、fū、pèi、fóu、póu","土",ps[98],"h「豁活」取「豁」：地裂豁然（推）。"),
("䴣（𡦱）","hū","鹿",ps[100],"h「豁活」取「豁」：獸名（推）。"),
("𠓧（𠓢）","jiè","入",ps[101],"j「聚决」取「聚」：草卷聚束（推）。")]
beny=ps[74].replace('从丂上有。“丂”','从丂上有。')
if len(inames)>=1: beny=beny.replace('从丂上有。','从丂上有{{benyi/01.png}}。',1)
head={"char":"乎","head":"乎（𠂞𠂠）","pinyin":"hū","level":2,"parent":"丂","bus":[{"num":34,"name":"丂"}],"aliases":["𠂞","𠂠"],
 "sections":[{"key":"benyi","label":"本义","text":beny,"gdir":"inline/乎","cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[75:77]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：伸頸張口呼叫，聲氣豁然而出（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指呼喚，或表示聲音","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:4]]},
    {"title":"②指呼氣，表示氣息狀","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[4:10]]},
    {"title":"③指張開口，表示縫隙、大口","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[10:16]]},
    {"title":"④形近字「孝、手」之訛","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[16:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"乎.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    bare=re.match(r"^([^\s（(]+)",r[0]).group(1)
    f=os.path.join(C,bare+".json")
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"乎","bus":[{"num":34,"name":"丂"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    if bare=="㭔" and pf: d["photos"]=[pf]; d["captions"]=["黃櫨花（不孕花梗久留，如吐氣成霧）"]
    if bare=="𩶈" and pg: d["photos"]=[pg]; d["captions"]=["蝠鱝（魔鬼魚）"]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",len(rows),len(inames))