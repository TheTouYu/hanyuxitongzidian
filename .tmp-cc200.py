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
for ch,bl in (("号",blobs(53)[0:4]),("號",blobs(53)[4:6])):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(bl,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
def photo(par,ch,cap):
    b=[x for x in blobs(par) if len(x)>20000]
    if not b: return
    d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fn="01."+kd(b[0]); open(os.path.join(d,fn),"wb").write(b[0])
    ip=os.path.join(P,"index.json"); i=json.load(io.open(ip,encoding="utf-8")); ph=i.get("photos") or i; ph[ch]=[fn]
    json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    if cap:
        cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
        cm[ch]=[cap]; json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
photo(62,"號","老虎嚎叫")
rows=[("號","háo、hào","虍","《說文》：「呼也。从号从虎。乎刀切。」《廣韻》：「大呼也。又哭也。」本義當指老虎吼叫。hào，《集韻》：「此令也。一曰名號。」","h「豁活」取「豁」：張口大呼如豁開（推）。"),
("鴞","xiāo","鳥","《說文》：「鴟鴞，寧鴂也。从鳥号聲。於嬌切。」《正字通》：「山鴞。卽土梟。狀如母雞有斑，頭如鴝鵒，目如貓，好食桑椹，一名鵩。」","x「续消」取「消」：夜鳴淒厲而消（推）。"),
("呺","xiāo、háo","口","《廣韻》：「呺然，大皃。」《集韻》：「呺然，虛大皃。李軌說。或作𧦢、号。」大而中空皃。háo，《集韻》：「風聲。」《字彙》：「叫呼怒聲。」","x「续消」取「消」：中空而聲消（推）。"),
("𧇼","hào","䖒","《說文》：「土鍪也。从䖒号聲。讀若鎬。胡到切。」《玉篇》：「土釜也。」敞口陶鍋。","h「豁活」取「豁」：敞口如豁（推）。"),
("㙱","hào","土","《廣韻》：「土釡也。《説文》作𧇼，土堥也。」","h「豁活」取「豁」：土釜敞口（推）。"),
("𨚙","háo","邑","《說文》：「南陽淯陽鄉。从邑号聲。乎刀切。」","h「豁活」取「豁」：地名从号（推）。"),
("𤩭","hào","玉","《說文》：「石之似玉者。从玉號聲，讀若鎬。乎到切。」疑指玉扳指之類筒形玉。","h「豁活」取「豁」：筒形中空（推）。"),
("饕","tào","食","《說文》：「貪也。从食號聲。，饕或从口刀聲。，籀文饕从號省。土刀切。」貪食。吞食。《玉篇》：「貪財也。」","t「涂突」取「突」：貪食突入（推）。"),
("枵","xiāo","木","《說文》：「木根也。从木号聲。《春秋傳》曰：『歲在玄枵』。玄枵，虛也。許嬌切。」大木而中空皃。《字彙》：「𢪶，玄𢪶，星名。正从木。」中國古代十二星次之一，位列第二，含女、虛、危三宿。","x「续消」取「消」：中空而消（推）。")]
head={"char":"号","head":"号（號）","pinyin":"háo、hào","level":2,"parent":"丂","bus":[{"num":34,"name":"丂"}],"aliases":["號"],
 "sections":[{"key":"benyi","label":"本义","text":ps[54],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[56:59]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：張口長號，聲氣豁然而出（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指嚎叫","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:2]]},
    {"title":"②指大而中空","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[2:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"号.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"号","bus":[{"num":34,"name":"丂"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    if bare=="號": d["photos"]=["01."+("png" if os.path.exists(os.path.join(P,"號","01.png")) else "jpg")]; d["captions"]=["老虎嚎叫"]; d["aliases"]=[]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")