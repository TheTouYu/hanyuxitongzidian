from docx import Document
from docx.oxml.ns import qn
import io,os
from PIL import Image
d=Document(r"D:\字谱智能体\卷卌二  丵.docx")
for i,p in enumerate(d.paragraphs):
    t=(p.text or "").strip()
    if t.startswith("差") and len(t)>6:
        print("HIT p",i,t[:40])
        for j in range(i,min(len(d.paragraphs),i+10)):
            for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
                rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                im=Image.open(io.BytesIO(part.blob)); 
                if max(im.size)<200: continue
                os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\差",exist_ok=True)
                im.convert("RGB").save(r"D:\系统汉字\web\public\glyphs\photos\差\01.jpg","JPEG",quality=90)
                print("saved p",j,im.size); raise SystemExit
        break