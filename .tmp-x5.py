import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十一  犀.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
hit=None
for i in range(120,150):
    for b in d.paragraphs[i]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)>=300:
            os.makedirs(r"web\public\glyphs\photos\㚇",exist_ok=True)
            im.convert("RGB").save(r"web\public\glyphs\photos\㚇\01.jpg","JPEG",quality=90)
            print("PIC p",i,im.size,ps[i][:40]); hit=i; break
    if hit: break
print("---- 恖 head ----")
for j in range(150,200):
    t=ps[j]
    if t and ("恖" in t or "思" in t) and len(t)<60: print(j,t[:80])