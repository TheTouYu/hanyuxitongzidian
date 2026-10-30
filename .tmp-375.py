import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i,t in enumerate(ps):
    if i>140 and len(t)<12 and t[:3].isdigit() and "." in t[:5]:
        print("HEAD p%d %s"%(i,t[:40]))
# 席 photo p145
for b in d.paragraphs[145]._p.findall('.//'+qn('a:blip')):
    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
    if part is None or not hasattr(part,'blob'): continue
    im=Image.open(io.BytesIO(part.blob))
    if max(im.size)>=200:
        os.makedirs(r"web\public\glyphs\photos\㐁",exist_ok=True)
        im.convert("RGB").save(r"web\public\glyphs\photos\㐁\01.jpg","JPEG",quality=90)
        print("photo 㐁",im.size)