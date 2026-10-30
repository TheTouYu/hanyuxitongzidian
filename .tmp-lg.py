from docx import Document
from docx.oxml.ns import qn
import io,glob,os
from PIL import Image
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    for i,p in enumerate(d.paragraphs):
        t=p.text or ""
        if t.startswith("莨") or t.startswith("莨（"):
            print("HIT",os.path.basename(path),i,t[:60])
            for j in range(i,min(len(d.paragraphs),i+12)):
                for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
                    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                    if part is None or not hasattr(part,'blob'): continue
                    try: im=Image.open(io.BytesIO(part.blob)); wh=im.size
                    except Exception: continue
                    print("   img p",j,wh,len(part.blob)//1024,"KB")
            raise SystemExit