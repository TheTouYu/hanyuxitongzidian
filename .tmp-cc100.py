# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs"); P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
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
gb=blobs(28)
plan=[("丂",gb[0:5]),("巧",gb[5:6]),("攷",gb[6:10]),("雁",gb[10:11])]
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
for ch,imgs in plan:
    d=os.path.join(G,ch)
    exist=(chars.get(ch) or {}).get("files") or []
    if exist and ch!="丂": continue
    os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
rows=[("巧","qiǎo、kǎo","工","《說文》：「技也。从工丂聲。苦絞切。」技能；靈巧。《廣韻》：「好也。能也。善也。」kǎo，《釋名》：「考也。考合異類共成一體也。」","q「親缺」取「缺」：彎曲靈活如缺折（推）。"),
("㱙（朽）","xiǔ、guǎ","歹","《說文》：「腐也。从歺丂聲。，㱙或从木。許久切。」腐爛。骨頭（或木頭）本來是硬的，如果象脖子一樣軟的話，當然是已經腐朽了。","x「续消」取「消」：腐爛消敗（推）。"),
("㤍","qiāo、qiǎo","心","《玉篇》：「㤍㤉，伏態。」感情不外露。qiǎo，《集韻》：「巧，偽也。或从心。」","q「親缺」取「缺」：情伏不露如缺（推）。"),
("䲾","qiǎo","鳥","《廣韻》：「䲾婦鳥。案《爾雅注》云：『鷦𪃧，桃雀也。俗呼爲巧婦。』字俗从鳥。」鷦鷯，善築巢。","q「親缺」取「缺」：巧婦鳥善築巢（推）。"),
("㚽","qiǎo","女","《集韻》：「女字。」","q「親缺」取「缺」：女字（推）。"),
("𩈎","chǎo","面","《集韻》：「楚絞切，音炒。𩈏（ǎo）𩈎，面曲。」","ch「刺持」取「刺」：面曲如刺（推）。"),
("䒓（𦫼）","kǎi","艸","《集韻》：「口蠏切。戾也。」曲。乖戾。《字彙補》：「𦫼，同䒓。」","k「口控」取「控」：曲戾失控（推）。"),
("攷（考）","kǎo","攴","《說文》：「敂也。从攴丂聲。苦浩切。」叩擊。《廣韻》：「考，校也。成也。引也。亦瑕釁，《淮南子》云『夏后氏之璜不能無考』是也。攷，古文。」","k「口控」取「口」：叩擊而考（推）。"),
("䛒（辯）","biàn","言","《廣韻》：「辯，別也。理也。慧也。《說文》：『治也。』符蹇切。䛒，俗。」善辯。","b「闭剥」取「閉」：辯別如剖析（推）。")]
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
p1=photo(35,"丂","“丂”字形雁陣")
p2=photo(43,"㱙","")
p3=photo(62,"號","老虎嚎叫")
head={"char":"丂","head":"丂（𠀀）","pinyin":"kǎo、hē","level":1,"bus":[{"num":34,"name":"丂"}],
 "aliases":aliases("丂（𠀀）","丂"),
 "sections":[{"key":"benyi","label":"本义","text":ps[29]+"\n"+ps[30],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[31:35]),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":ps[37]+"\n"+ps[38],"cites":[]},
  {"key":"yinyuan","label":"音源","text":"音源字，源自鴻雁的叫聲。","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"k「口控」取「口」：伸頸張口而號（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指雁脖子，表示柔軟、靈巧","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:7]]},
    {"title":"②指雁啄食，表示稽考","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[7:8]]},
    {"title":"③象意字，含靈巧義","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[8:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
if p1: head["photos"]=[p1]; head["captions"]=["“丂”字形雁陣"]
json.dump(head,io.open(os.path.join(C,"丂.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    if os.path.exists(f) and bare not in ("㱙",): continue
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"丂","bus":[{"num":34,"name":"丂"}],
       "aliases":aliases(r[0],bare),
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    if bare=="㱙" and p2: d["photos"]=[p2]
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")