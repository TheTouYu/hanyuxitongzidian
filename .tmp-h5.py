from docx import Document
from docx.oxml.ns import qn
import os,glob
os.makedirs(r"D:\系统汉字\.tmp-sea",exist_ok=True)
f=glob.glob(r"D:\字谱智能体\卷卌七*.docx")[0]
d=Document(f)
for i in (93,112):
    p=d.paragraphs[i]
    for n,b in enumerate(p._p.findall('.//'+qn('a:blip'))):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        ext='png' if part.blob[:4]==b'\x89PNG' else 'jpg'
        fn=rf"D:\系统汉字\.tmp-sea\p{i}_{n}.{ext}"
        open(fn,'wb').write(part.blob); print(fn)