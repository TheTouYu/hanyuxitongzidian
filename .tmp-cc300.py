# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
PRE=["本義：","轉義：","辯證：","音源：","釋義："]
n=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); chg=False
    for s in d.get("sections",[]):
        t=(s.get("text") or "").lstrip()
        for pre in PRE:
            if t.startswith(pre): s["text"]=t[len(pre):].lstrip(); chg=True; break
    if chg: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("strip",n)
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
gb=blobs(102)
for ch,bl in (("兮",gb[0:4]),("𠣬",gb[4:7]),("幵",gb[7:11])):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(bl,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
rows=[("𧟯（虧）","kuī","亏","《字彙補》：「同虧。」《集韻》：「虧，《說文》：『氣損也。』《博雅》：『小也。』或从兮。」","k「口控」取「控」：氣損而虛（推）。"),
("𠆵","ní","人","《集韻》：「硏奚切，音倪。𠆵㑮，佯不知皃。」","n「纳弄」取「纳」：佯不知而含纳（推）。"),
("䚷（欵）","yī、yǐ、xì","言","《集韻》：「𧫦，《方言》：『欵、𧫦，然也。』或作䚷。」「誠言也。」yǐ，《玉篇》：「應聲。」應答聲。xì，《廣雅》：「謷也。」調戲、倨傲。","y「零聲母」不系：零聲母，緒論七組未列（照實）。"),
("𠯋","yǐ","口","《廣韻》：「可也。爾也。」《集韻》：「然也。」","y「零聲母」不系：零聲母，緒論七組未列（照實）。"),
("䒊（𦫬）","xī","色","《集韻》：「𦫬，黃病色。或从兮。」《廣韻》：「痛聲。」","x「续消」取「消」：病色消敗（推）。"),
("㿽","xī","皿","《五音集韻》：「胡雞切，音兮。小盆也。」","x「续消」取「消」：小盆受水（推）。"),
("盻","xì、pǎn","目","《說文》：「恨視也。从目兮聲。胡計切。」怒視。《類篇》：「盻盻，勤苦不休息皃。」pǎn，《集韻》：「動目也。」「美目皃。」","x「续消」取「消」：怒視而消（推）。"),
("諡","shì","言","《說文》：「行之跡也。从言、兮、皿。闕。神至切。徐鍇曰：兮，聲也。」《正字通》：「卒而易名也。」人生言行的蹤跡。指死後所稱呼的名字。","sh「失收」取「收」：言行收而後定（推）。"),
("枍","yí","木","《玉篇》：「枍栺，宮名。」《集韻》：「枍栺，木名。」此義同「枅（jī）」。","y「零聲母」不系：零聲母，緒論七組未列（照實）。"),
("𣕆（榽）","xī","木","《玉篇》：「榽，遐雞切。榽橀，木細葉似檀。今江東有之。𣕆，同上。俗。」","x「续消」取「消」：細葉如消（推）。"),
("𪐭（黟）","yī","黑","《玉龍龕》：「𪐭、黟，二俗。《玉篇》：『黟，黑木也。』黑也。」烏木，即「陰沉木」。","y「零聲母」不系：零聲母，緒論七組未列（照實）。")]
head={"char":"兮","head":"兮（𠔃）","pinyin":"xī","level":2,"parent":"丂","bus":[{"num":34,"name":"丂"}],"aliases":["𠔃"],
 "sections":[{"key":"benyi","label":"本义","text":ps[103],"cites":[]},
  {"key":"bianzheng","label":"辩证","text":ps[104]+"\n"+ps[105],"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"x「续消」取「消」：呼氣續出而消（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指「兮」，表示張口、出聲、氣息","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:8]]},
    {"title":"②應指「幵」，表示細而堅挺","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[8:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"兮.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"兮","bus":[{"num":34,"name":"丂"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")