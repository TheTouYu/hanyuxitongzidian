# -*- coding: utf-8 -*-
import json,io,os,re,sys,struct
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
# 字形行：14 戚 + 1 摵(𡠽)
gb=blobs(324); idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
for ch,imgs in (("戚",gb[:14]),("摵",gb[14:])):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 照片
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
rows=[("槭","qì、sè","木","《說文》：「木。可作大車輮。从木戚聲。子六切。」落葉小喬木，花黃綠色，葉子掌狀分裂，秋季變成紅色或黃色。葉沿呈齒狀，故从「戚」。sè，《集韻》：「木枝空皃。」樹枝光禿，葉凋落貌。","q「親缺」取「缺」：葉沿如齒缺（推）。"),
("慽","qī","心","《說文》：「憂也。从心戚聲。倉曆切。」指憂愁而皺眉、苦臉，使臉部皮膚皺縮。","q「親缺」取「缺」：心缺而憂（推）。"),
("顣","cù","頁","《廣韻》：「顣頞，鼻頤促皃。」皺眉。《字彙》：「與蹙同。」皺縮。","c「刺持」取「刺」：眉蹙如刺聚（推）。"),
("𦟠（𦢑）","cù","肉","《集韻》：「䐚𦟠，膏澤也。或从心。」脂肪表面的皺紋。","c「刺持」取「刺」：脂紋細刺（推）。"),
("摵（𡠽）","shè、sù、mí、cé","手","《新附》：「捎也。从手戚聲。沙劃切。」捎帶。《廣韻》：「隕落皃。」sù，《方言》：「到也。」《集韻》：「至也。」mí，《集韻》：「𡠽，批也。或从手。」cé，《唐韻》：「揩齒也。」","sh「失收」取「收」：捎帶而收（推）。"),
("蹙（蹴踓）","cù","足","《說文》：「迫也。从足戚聲。子六切。」《廣韻》：「促也。近也。急也。」《廣雅》：「辠也。」《集韻》：「蹴，《說文》：『躡也。』或作蹙、踓。」","c「刺持」取「刺」：迫近如刺（推）。"),
("嘁（㗤）","zā、cù、qī","口","《廣韻》：「歍嘁。」歎息。cù，《集韻》：「嘁諮，忸怩，慚也。」《正字通》：「同㗤。本作戚。俗作蹙。」「㗤，愁貌。」qī，象聲詞。形容低語聲。多疊用。","z「凿总」取「总」：歎息聲總聚（推）。"),
("磩（礎）","qì、zhú","石","《廣韻》：「碝磩，石次玉。」象玉的石。zhú，《集韻》：「礎謂之磩。」柱下石墩。","q「親缺」取「缺」：石次玉而有缺（推）。"),
("傶","zú、qī","人","《玉篇》：「邑名。亦姓。」qī，《廣雅》：「近也。」親近。《漢典》：腠理。","q「親缺」取「親」：邑近而相依（推）。"),
("鏚","qī","金","《廣韻》：「干鏚，斧鉞。本亦作戚。」","q「親缺」取「缺」：斧鉞兩側有齒缺（推）。"),
("縬（𦂎縐）","cù","糸","《廣韻》：「縮也。又縬文也。」《集韻》：「繒文。」「聚文也。或作𦂎、縐。」","c「刺持」取「刺」：繒紋蹙縮如刺（推）。"),
("䙘","chǔ、zú","衣","《廣韻》：「《埤蒼》云：『鮮也。一曰美好皃』。」zú，《廣韻》：「好衣皃。」《集韻》：「衣鮮明皃。」《篇海類編》：「鮮白也。」指新衣服的皺褶分明。","ch「刺持」取「持」：新衣皺褶持聚（推）。")]
p1=photo(327,"戚","玉鉞（商）")
head={"char":"戚","head":"戚（𠋰𠎰𡫁𢦫𢧯𩒛）","pinyin":"qī","level":1,"bus":[{"num":32,"name":"戚"}],
 "aliases":aliases("戚（𠋰𠎰𡫁𢦫𢧯𩒛）","戚"),
 "sections":[{"key":"benyi","label":"本义","text":ps[325]+"\n"+ps[326],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":ps[329],"cites":[]},
  {"key":"yinyuan","label":"音源","text":ps[330],"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"q「親缺」取「親」：戚齒排列相親近（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":ps[331],"groups":[{"title":"多取戚齒狀，指蹙縮","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
head["photos"]=["01.png"] if p1 else []; head["captions"]=["玉鉞（商）"] if p1 else []
json.dump(head,io.open(os.path.join(C,"戚.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"戚","bus":[{"num":32,"name":"戚"}],
       "aliases":aliases(r[0],bare),
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
photo(333,"槭","")
print("head photo",p1,"family",len(rows))