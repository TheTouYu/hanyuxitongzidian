# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
def sec(a,b,label):
    t="\n".join(x for x in ps[a:b] if x)
    return re.sub(r"^(本義|轉義|辯證|音源)：","",t,count=1)
benyi=sec(111,112,"本義")
zhuanyi=sec(114,121,"轉義")
yin=sec(121,122,"音源")
groups=[
 ("①指石頭的相關用途",123,129,["祏","宕","鉐","坧","砅"]),
 ("②指用石砍砸、投擲",129,138,["斫","拓","䞠","袥","沰","𡇈","䲽","鼫"]),
 ("③指石頭的硬",138,143,["蹠","柘","妬","炻"]),
 ("④指石之大",143,147,["碩","䄷","𦚈"])]
rows={}
for title,a,b,chars in groups:
    rr=[]
    for k in range(a,b):
        t=ps[k]
        if not t or t.startswith("①") or t.startswith("②") or t.startswith("③") or t.startswith("④"): continue
        m=re.match(r"^([^\s（《]{1,3}(?:（[^）]*）)?)\s*([a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ、，\s]*)[《]",t)
        if not m: continue
        ch=m.group(1); py=m.group(2).strip(" 、，")
        base=ch.split("（")[0]
        rows[base]=(py,t)
        rr.append([ch,py,"",t])
    rows.setdefault("__g",[]).append({"no":"","title":title,"rows":rr})
card={"char":"石","head":"石（䂖𥐘𥐖）","pinyin":"shí","bus":{"num":45,"name":"石"},"level":1,"aliases":["䂖","𥐘","𥐖"],
 "erji":[{"ch":"席","label":"席"},{"ch":"度","label":"度"},{"ch":"叚","label":"叚"},{"ch":"橐","label":"橐"},{"ch":"庶","label":"庶"}],
 "sections":[{"key":"benyi","label":"本义","text":benyi},
  {"key":"zhuanyi","label":"转义","text":zhuanyi},
  {"key":"yinyuan","label":"音源","text":yin},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「收」：石塊收聚崖下，敲之有聲而氣收（推）。"},
  {"key":"zizu","label":"字族衍义","groups":rows["__g"]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"石.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 字形
parts=doc.part.related_parts; d=os.path.join(G,"石"); os.makedirs(d,exist_ok=True)
files=[];i=0
for el in doc.paragraphs[110]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob;i+=1;fn="%02d.%s"%(i,"png" if b[:4]==b"\x89PNG" else "jpg")
            open(os.path.join(d,fn),"wb").write(b);files.append("石/"+fn)
gi=os.path.join(G,"index.json");g=json.load(io.open(gi,encoding="utf-8"))
g["chars"].setdefault("石",{})["files"]=files
# 照片 ▲出土的原始石器
b=None
for el in doc.paragraphs[112]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: b=parts[rid[0]].blob
if b:
    dd=os.path.join(P,"石"); os.makedirs(dd,exist_ok=True)
    ext="png" if b[:4]==b"\x89PNG" else "jpg"
    open(os.path.join(dd,"01."+ext),"wb").write(b)
    g["chars"]["石"]["photos"]=[{"file":"01."+ext,"caption":"出土的原始石器"}]
json.dump({"chars":g["chars"]},io.open(gi,"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(files),"rows",sum(len(x[3]) if isinstance(x,list) else 0 for x in []) )