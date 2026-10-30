# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs\inline"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
def build(ch,key,rng):
    dd=os.path.join(G,ch,key); os.makedirs(dd,exist_ok=True)
    for f in os.listdir(dd): os.remove(os.path.join(dd,f))
    out=[];n=0
    for k in rng:
        buf=[]
        for el in doc.paragraphs[k]._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": buf.append(el.text or "")
            elif tag=="blip":
                rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
                if not rid: continue
                b=parts[rid[0]].blob
                if len(b)>50000: continue          # 大图为插图，不入正文
                n+=1; ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
                fn="%02d.%s"%(n,ext); open(os.path.join(dd,fn),"wb").write(b)
                buf.append("{{%s/%s}}"%(key,fn))
        t="".join(buf).strip(); t=re.sub(r'^(本義|轉義)[：:]','',t).strip()
        if t: out.append(t)
    return "\n".join(out),n
p=os.path.join(C,"或.json"); d=json.load(io.open(p,encoding="utf-8"))
b,nb=build("或","benyi",range(262,267)); z,nz=build("或","zhuanyi",range(268,271))
for s in d["sections"]:
    if s["key"]=="benyi": s["text"]=b; s["gdir"]="inline/或"
    if s["key"]=="zhuanyi": s["text"]=z; s["gdir"]="inline/或"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("benyi imgs",nb,"zhuanyi imgs",nz)
print(z[:120])