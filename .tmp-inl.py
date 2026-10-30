# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs\inline"
char="蒦"; docp=r"D:\字谱智能体\卷六  鶴.docx"
doc=Document(docp); parts=doc.part.related_parts
def build(paras,key):
    d=os.path.join(G,char,key); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    n=0; out=[]
    for k in paras:
        buf=[]
        for el in doc.paragraphs[k]._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": buf.append(el.text or "")
            elif tag=="blip":
                rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
                if rid:
                    b=parts[rid[0]].blob; n+=1
                    ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
                    fn="%02d.%s"%(n,ext); open(os.path.join(d,fn),"wb").write(b)
                    buf.append("{{%s/%s}}"%(key,fn))
        t="".join(buf).strip()
        t=re.sub(r'^(本義|轉義|辯證|音源)[：:]','',t).strip()
        if t: out.append(t)
    return "\n".join(out), n
p=os.path.join(C,char+".json"); d=json.load(io.open(p,encoding="utf-8"))
for key,paras in (("benyi",(142,143)),("zhuanyi",(146,147))):
    txt,n=build(paras,key)
    for s in d["sections"]:
        if s["key"]==key:
            s["text"]=txt; s["gdir"]="inline/"+char
    print(key,"imgs",n)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)