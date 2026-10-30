from docx import Document
from docx.oxml.ns import qn
from PIL import Image
import io,glob
for f in [glob.glob(r"D:\字谱智能体\卷卌七*.docx")[0], glob.glob(r"D:\字谱智能体\卷卅三*.docx")[0] if glob.glob(r"D:\字谱智能体\卷卅三*.docx") else None]:
    if not f: continue
    d=Document(f); print("FILE",f)
    for i,p in enumerate(d.paragraphs):
        for b in p._p.findall('.//'+qn('a:blip')):
            rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
            if part is None or not hasattr(part,'blob'): continue
            try:
                im=Image.open(io.BytesIO(part.blob)); wh=im.size
            except Exception: continue
            if wh[0]>=400: print(f"  p{i} {wh[0]}x{wh[1]} {len(part.blob)//1024}KB")