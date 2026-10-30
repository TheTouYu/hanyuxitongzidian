from docx import Document
from docx.oxml.ns import qn
import io, glob, os
from PIL import Image
for path in glob.glob(r"D:\字谱智能体\卷一*.docx"):
    d=Document(path); print(os.path.basename(path))
    for i,p in enumerate(d.paragraphs):
        if "孵" not in p.text and "伏卵" not in p.text and "抱卵" not in p.text: continue
        print("  para",i,p.text[:60])
        for j in range(max(0,i-2),min(len(d.paragraphs),i+4)):
            for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
                rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                try: im=Image.open(io.BytesIO(part.blob)); wh=im.size
                except Exception: continue
                print("   img p",j,wh)