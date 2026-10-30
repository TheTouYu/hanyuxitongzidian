# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards")
INL=os.path.join(ROOT,"web","public","glyphs","inline","弔"); P=os.path.join(ROOT,"web","public","glyphs","photos")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
def kind(b):
    if b[:4]==b"\x89PNG": return "png"
    if b[:4]==b"\x01\x00\x00\x00": return "emf"
    if b[:2]==b"\xff\xd8": return "jpg"
    return "bin"
sec=None; out={}; counts={}
for k in range(265,274):
    p=doc.paragraphs[k]; t=p.text.strip()
    if not t: continue
    if t.startswith("本義"): sec="benyi"
    elif t.startswith("轉義"): sec="zhuanyi"
    elif t.startswith("辯證"): sec="bianzheng"
    elif t.startswith("音源"): sec="yinyuan"
    if sec is None: continue
    buf=[]
    for r in p.runs:
        enc=None
        for a,v in r._r.attrib.items():
            pass
        for el in r._r.iter():
            for a,v in el.attrib.items():
                if a.endswith("}embed") or a.endswith("}id"):
                    enc=v
        if enc:
            try: b=parts[enc].blob
            except KeyError:
                buf.append(r.text); continue
            kd=kind(b)
            if kd=="png" and len(b)<400:  # spacer
                buf.append(r.text); continue
            d=os.path.join(INL,sec); os.makedirs(d,exist_ok=True)
            n=counts.get(sec,0)+1; counts[sec]=n; fn="%02d.%s"%(n,kd)
            open(os.path.join(d,fn),"wb").write(b)
            buf.append('<img class="gin" src="glyphs/inline/弔/%s/%s" alt="字形">'%(sec,fn))
        else:
            buf.append(r.text)
    out.setdefault(sec,[]).append("".join(buf))
txt={k:"\n".join(v) for k,v in out.items()}
d=json.load(io.open(os.path.join(C,"弔.json"),encoding="utf-8"))
for s in d["sections"]:
    if s["key"] in txt: s["text"]=txt[s["key"]]
photo=None
for el in doc.paragraphs[266]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            b=parts[v].blob
            if len(b)>50000 and kind(b)=="png":
                photo="01.png"; os.makedirs(os.path.join(P,"弔"),exist_ok=True); open(os.path.join(P,"弔","01.png"),"wb").write(b)
if photo:
    d["photos"]=[photo]; d["captions"]=["青海宗日遺址的骨制魚鉤（5000年前）"]
json.dump(d,io.open(os.path.join(C,"弔.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in counts.items()}, "photo",photo)