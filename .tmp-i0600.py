# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; G=os.path.join(ROOT,"web","public","glyphs")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
def kd(b):
    if b[:4]==b"\x89PNG": return "png"
    if b[:4]==b"\x01\x00\x00\x00": return "emf"
    if b[:2]==b"\xff\xd8": return "jpg"
    return "bin"
pend=[]; groups=[]
for el in doc.paragraphs[264]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            try: pend.append(parts[rid[0]].blob)
            except KeyError: pass
    elif tag=="t" and el.text:
        t=el.text.strip()
        m=re.match(r"^([\u3400-\u9fff]{1,3})(（([^）]*)）)?$",t)
        if m and pend:
            groups.append((m.group(1),m.group(3) or "",pend)); pend=[]
if pend: groups.append(("弔","",pend))
ALIAS={"釣":"鈟"}
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
report={}
for head,var,imgs in groups:
    ch=ALIAS.get(head,head)
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}
    e["files"]=names
    if var: e["variants"]=[var]
    chars[ch]=e; report[ch]=len(names)
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print(report)