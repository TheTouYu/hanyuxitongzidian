from docx import Document
from docx.oxml.ns import qn
import io,os
from PIL import Image
d=Document(r"D:\字谱智能体\卷八十六  良.docx")
for b in d.paragraphs[89]._p.findall('.//'+qn('a:blip')):
    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
    if part is None or not hasattr(part,'blob'): continue
    im=Image.open(io.BytesIO(part.blob)).convert("RGB")
    os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\莨",exist_ok=True)
    im.save(r"D:\系统汉字\web\public\glyphs\photos\莨\01.jpg","JPEG",quality=90)
    print("saved",im.size)