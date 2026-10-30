# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs"); P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: out.append(parts[rid[0]].blob)
                except KeyError: pass
    return out
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
def aliases(head,ch):
    m=re.search(r"（([^）]+)）",head); return sorted({x for x in HAN.findall(m.group(1)) if x!=ch}) if m else []
gb=blobs(347)
plan=[("異",gb[:28]),("翼",gb[28:36]),("冀",gb[36:40]),("戴",gb[40:41])]
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
for ch,imgs in plan:
    d=os.path.join(G,ch)
    exist=(chars.get(ch) or {}).get("files") or []
    if exist and ch!="異": continue   # 已有字形者（翼/冀/戴属他部）不覆盖
    os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
rows=[("廙","yì","广","《說文》：「行屋也。从广異聲。與職切。」可以移動的住房，即帳篷之類。《廣韻》：「恭也，敬也。」","y「零聲母」不系（照實）。"),
("潩","yì","水","《說文》：「水。出河南密縣大隗山，南入潁。从水異聲。與職切。」即今清異河，潁水支流。","y「零聲母」不系（照實）。"),
("㔴（𠥦）","yì","匚","《說文》：「田器也。从匚異聲。與職切。」《玉篇》：「大鼎也。」《集韻》：「或从翼。」","y「零聲母」不系（照實）。"),
("趩","chì","走","《說文》：「行聲也。一曰不行皃。从走異聲。讀若敕。醜亦切。」疑本指不走而行，意即飛行，或被負載而行。《玉篇》：「走皃。」","ch「刺持」取「刺」：行而有聲如刺（推）。"),
("𠪙","xǐ","厂","《說文》：「石利也。从厂異聲。讀若枲。胥裡切。」石頭銳利，大約指礪而使石利。","x「续消」取「消」：礪石而消（推）。"),
("霬","yì","雨","《字彙補》：「人名。」人名用字。","y「零聲母」不系（照實）。"),
("穓","yì","禾","《正字通》：「伊昔切，音亦。耕也。」","y「零聲母」不系（照實）。"),
("熼","yì","火","《廣韻》：「火光。」《集韻》：「火皃。」火焰往上皃。當物體燃燒時，會釋放出大量熱量，這些熱量使得周圍的空氣受熱膨脹，密度變小，因此會向上運動。","y「零聲母」不系（照實）。"),
("𩙺（翼）","yì","飛","《說文》：「翄也。从飛異聲。，篆文𩙺从羽。與職切。」翅膀。《玉篇》：「翹也。又輔也、敬也、助也。」《集韻》：「盛也。」","y「零聲母」不系（照實）。"),
("𧾰","yì","走","《說文》：「趨進𧾰如也。从走翼聲。與職切。」走路如飛。《玉篇》：「趨進皃。」","y「零聲母」不系（照實）。"),
("瀷","yì","水","《說文》：「水。出河南密縣，東入潁。从水翼聲。與職切。」《段注》以為「此潩字的異體」。《廣韻》：「水潦積聚。」雨後地面積聚的水。","y「零聲母」不系（照實）。"),
("冀","jì","北","《說文》：「北方州也。从北異聲。幾利切。」《集韻》：「一曰欲也。」北方州名。希望。本義也應是指翅膀，「北」本指翅膀。","j「聚决」取「聚」：聚翅而望（推）。"),
("驥","jì","馬","《說文》：「千里馬也，孫陽所相者。从馬冀聲。天水有驥縣。幾利切。」","j「聚决」取「聚」：聚力而馳（推）。")]
def photo(par,ch,cap):
    b=[x for x in blobs(par) if len(x)>20000]
    if not b: return None
    d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fn="01."+kd(b[0]); open(os.path.join(d,fn),"wb").write(b[0])
    ip=os.path.join(P,"index.json"); i=json.load(io.open(ip,encoding="utf-8")); ph=i.get("photos") or i; ph[ch]=[fn]
    json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    if cap:
        cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
        cm[ch]=[cap]; json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
    return fn
p1=photo(350,"異","")
p2=photo(364,"熼","火焰燃燒示意圖")
head={"char":"異","head":"異（异𠔱𢄖）","pinyin":"yì","level":1,"bus":[{"num":33,"name":"異"}],
 "aliases":aliases("異（异𠔱𢄖）","異"),
 "sections":[{"key":"benyi","label":"本义","text":ps[348]+"\n"+ps[349],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":ps[351],"cites":[]},
  {"key":"bianzheng","label":"辩证","text":ps[352],"cites":[]},
  {"key":"yinyuan","label":"音源","text":ps[353],"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指佩戴，表示往上、表層發生的行為","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:8]]},
    {"title":"②指翅膀，表示飛速","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[8:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
head["photos"]=[p1] if p1 else []
json.dump(head,io.open(os.path.join(C,"異.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    if os.path.exists(f) and bare!="熼": continue
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"異","bus":[{"num":33,"name":"異"}],
       "aliases":aliases(r[0],bare),
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    if bare=="熼" and p2: d["photos"]=[p2]; d["captions"]=["火焰燃燒示意圖"]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("p1",p1,"p2",p2)