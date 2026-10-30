from docx import Document
from docx.oxml.ns import qn
import io, os
from PIL import Image
os.makedirs(r"D:\系统汉字\.tmp-fu",exist_ok=True)
d=Document(r"D:\字谱智能体\卷廿五  勹.docx")
for i,p in enumerate(d.paragraphs):
    if not (255<=i<=275): continue
    for b in p._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        try: im=Image.open(io.BytesIO(part.blob)); wh=im.size
        except Exception: continue
        ext='png' if part.blob[:4]==b'\x89PNG' else 'jpg'
        fn=rf"D:\系统汉字\.tmp-fu\p{i}.{ext}"
        open(fn,'wb').write(part.blob); print(fn,wh,len(part.blob)//1024,"KB")