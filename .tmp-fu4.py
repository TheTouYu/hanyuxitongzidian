from docx import Document
from docx.oxml.ns import qn
import io, glob, os, re
from PIL import Image
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    hit=None
    for i,p in enumerate(d.paragraphs):
        if re.match(r"^\s*141[.．、]", p.text) and "孚" in p.text[:12]:
            hit=i; break
    if hit is None: continue
    print("FILE",os.path.basename(path),"para",hit,p.text[:40])
    for j in range(hit, min(len(d.paragraphs), hit+40)):
        for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
            rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
            if part is None or not hasattr(part,'blob'): continue
            try: im=Image.open(io.BytesIO(part.blob)); wh=im.size
            except Exception: continue
            print("   img p",j,wh,len(part.blob)//1024,"KB")
    break