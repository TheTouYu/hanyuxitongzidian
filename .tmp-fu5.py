from docx import Document
from docx.oxml.ns import qn
import os
d=Document(r"D:\字谱智能体\卷廿五  勹.docx")
os.makedirs(r"D:\系统汉字\.tmp-fu",exist_ok=True)
for j in (251,282):
    for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        ext='png' if part.blob[:4]==b'\x89PNG' else 'jpg'
        fn=rf"D:\系统汉字\.tmp-fu\p{j}.{ext}"
        open(fn,'wb').write(part.blob); print(fn); break