from docx import Document
from docx.oxml.ns import qn
import io
from PIL import Image
d=Document(r"D:\字谱智能体\卷廿五  勹.docx")
for i in range(240,252):
    p=d.paragraphs[i]; t=(p.text or "").strip()
    imgs=[]
    for b in p._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        try: imgs.append(Image.open(io.BytesIO(part.blob)).size)
        except Exception: pass
    if t or imgs: print(i,"|",t[:30],"|",imgs)