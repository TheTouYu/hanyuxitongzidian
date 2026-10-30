# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
HAN="[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]"
def strip(t):
    return re.sub(r"^(本義|轉義|辯證|音源|字族衍義)[：:]","",t).strip()
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(parts[rid[0]].blob)
    return out
def save(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    lst=[]
    for i,b in enumerate(bs):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(i+1,ext)
        open(os.path.join(d,fn),"wb").write(b); lst.append(ch+"/"+fn)
    return lst
# 橐：p237 行，前段归橐、遇「囊」「㯱」切换
seq=[]; cur="橐"; groups={}
for el in doc.paragraphs[237]._p.iter():
    t=el.tag.split("}")[-1]
    if t=="t" and (el.text or "").strip():
        v=el.text.strip()
        if "囊" in v: cur="囊"
        elif "㯱" in v: cur="㯱"
    elif t=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: groups.setdefault(cur,[]).append(parts[rid[0]].blob)
gfiles={k:save(k,v) for k,v in groups.items()}
sfiles={"庶":save("庶",blobs(248))}
print({k:len(v) for k,v in gfiles.items()},{k:len(v) for k,v in sfiles.items()})
json.dump({"橐":gfiles,"庶":sfiles},io.open(r"D:\系统汉字\.tmp-gf.json","w",encoding="utf-8"),ensure_ascii=False)
json.dump({"ps":ps},io.open(r"D:\系统汉字\.tmp-ps.json","w",encoding="utf-8"),ensure_ascii=False)