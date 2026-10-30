import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十一  犀.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i in (217,216,218):
    for b in d.paragraphs[i]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)>=200:
            os.makedirs(r"web\public\glyphs\photos\囪",exist_ok=True)
            im.convert("RGB").save(r"web\public\glyphs\photos\囪\01.jpg","JPEG",quality=90)
            print("PIC",i,im.size); break
print("----")
for j in range(220,246):
    if ps[j]: print(j, ps[j][:110])