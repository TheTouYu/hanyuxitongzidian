import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
rids=[]
for el in doc.paragraphs[542]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try: b=parts[v].blob
            except KeyError: continue
            if len(b)>800: rids.append((v,b))
seen=[];
for v,b in rids:
    if v not in [x[0] for x in seen]: seen.append((v,b))
d=os.path.join(G,"意"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
for i,(v,b) in enumerate(seen):
    ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    open(os.path.join(d,f"{i+1:02d}{ext}"),"wb").write(b)
p=os.path.join(G,"index.json"); j=json.load(io.open(p,encoding="utf-8"))
chars=j.get("chars") or j
chars["意"]={"doc":"卷三 矢","files":[f"意/{f}" for f in sorted(os.listdir(d))]}
json.dump({"chars":chars},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(seen))