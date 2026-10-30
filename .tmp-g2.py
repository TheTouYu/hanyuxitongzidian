# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
HAN="[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]"
def runs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        t=el.tag.split("}")[-1]
        if t=="t" and (el.text or "").strip(): out.append(("T",el.text.strip()))
        elif t=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(("I",rid[0]))
    return out
def extract(k,first_char):
    seq=runs(k); cur=first_char; idx={}
    for typ,val in seq:
        if typ=="I":
            b=parts[val].blob
            idx.setdefault(cur,[]).append(b)
        else:
            m=re.findall(HAN,val)
            if m and len(val)<=4:
                cand=[c for c in val if re.match(HAN,c)]
                if cand: cur=cand[-1]
    files={}
    for ch,bs in idx.items():
        d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
        for f in os.listdir(d): os.remove(os.path.join(d,f))
        lst=[]
        for i,b in enumerate(bs):
            ext="png" if b[:4]==b"\x89PNG" else "jpg"
            fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b)
            lst.append(ch+"/"+fn)
        files[ch]=lst
    return files
f1=extract(237,"橐"); f2=extract(248,"庶")
print({k:len(v) for k,v in f1.items()},{k:len(v) for k,v in f2.items()})
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8")); ch=g["chars"]
for files in (f1,f2):
    for k,v in files.items():
        e=ch.setdefault(k,{}); e["files"]=v
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)