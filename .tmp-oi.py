# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs\inline"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
ch="或"; key="benyi"
dd=os.path.join(G,ch,key); os.makedirs(dd,exist_ok=True)
for f in os.listdir(dd): os.remove(os.path.join(dd,f))
out=[];n=0
for k in range(262,267):
    buf=[]
    for el in doc.paragraphs[k]._p.iter():
        tag=el.tag.split("}")[-1]
        if tag=="t": buf.append(el.text or "")
        elif tag=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; n+=1
                ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
                fn="%02d.%s"%(n,ext); open(os.path.join(dd,fn),"wb").write(b)
                buf.append("{{%s/%s}}"%(key,fn))
    t="".join(buf).strip(); t=re.sub(r'^本義[：:]','',t).strip()
    if t: out.append(t)
p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]==key: s["text"]="\n".join(out); s["gdir"]="inline/"+ch
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("imgs",n)