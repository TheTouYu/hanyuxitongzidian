# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
def imgs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(parts[rid[0]].blob)
    return out
def save(ch, blobs, start=1):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    fs=[]
    for i,b in enumerate(blobs):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b); fs.append(ch+"/"+fn)
    return fs
b=imgs(393); print("row",len(b))
wo=save("我", b[:13]); e=save("娥", b[13:])
ph=imgs(395); print("photo",len(ph))
os.makedirs(os.path.join(G,"photos","我"),exist_ok=True)
open(os.path.join(G,"photos","我","01.jpg"),"wb").write(ph[0])
# rows
groups=[("①","指鵝的叫，表示乞食、吟哦",range(403,407)),
        ("②","指鵝的翅膀寬大，表示蝴蝶、闊展的樣子",range(408,413)),
        ("③","指鵝的伸長脖子，表示高皃、傾側",range(414,422))]
RX=re.compile(r"^([^\s（(《]+)(?:（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)[、]?[^《]*《")
rows_by=[]; cards=[]
for no,title,rng in groups:
    rows=[]
    for k in rng:
        t=ps[k]
        m=RX.match(t)
        if not m: print("MISS",k,t[:30]); continue
        ch=m.group(1); py=m.group(3)
        rows.append([ch,py,"",t])
        cards.append((ch,py,"",t))
    rows_by.append({"no":no,"title":title,"rows":rows})
print("rows",sum(len(r["rows"]) for r in rows_by), "chars",len(cards))
json.dump({"rows":rows_by,"cards":cards,"wo":wo,"e":e},io.open(r"D:\系统汉字\.tmp-wo.json","w",encoding="utf-8"),ensure_ascii=False)