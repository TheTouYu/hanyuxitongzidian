# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
def small(p):
    out=[]
    for el in p._p.iter():
        for a,v in el.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    pt=parts[v]
                    if hasattr(pt,'blob') and 800<len(pt.blob)<20000: out.append(v)
                except KeyError: pass
    return out
rids=[]
for k in range(629,637):
    rids+=small(ps[k])
print("cand",len(rids))
if rids:
    d=r"D:\系统汉字\web\public\glyphs\𦣞"; os.makedirs(d,exist_ok=True)
    files=[]
    seen=set()
    for i,r in enumerate(rids,1):
        if r in seen: continue
        seen.add(r)
        b=parts[r].blob
        ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
        fn=f"{i:02d}{ext}"; open(os.path.join(d,fn),"wb").write(b); files.append("𦣞/"+fn)
    p=r"D:\系统汉字\web\public\glyphs\index.json"
    x=json.load(io.open(p,encoding="utf-8"))
    x["chars"]["𦣞"]={"doc":"12.𦣞部","desc":"𦣞（𦣝）","variants":["𦣝"],"files":files}
    json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("glyphs",len(files))