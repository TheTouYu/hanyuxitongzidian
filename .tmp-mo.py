import os,glob,io,re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
ph=r"web\public\glyphs\photos"
for c in ("某","梅","每"):
    p=os.path.join(ph,c)
    print(c, os.listdir(p) if os.path.isdir(p) else "none")
# search docx for 某 entry
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    for i,p in enumerate(d.paragraphs):
        t=(p.text or "").strip()
        if t.startswith("某") and len(t)>4:
            imgs=[]
            for j in range(i,min(len(d.paragraphs),i+25)):
                for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
                    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                    if part is None or not hasattr(part,'blob'): continue
                    im=Image.open(io.BytesIO(part.blob))
                    if max(im.size)>=200: imgs.append((j,im))
            if imgs:
                print("HIT",os.path.basename(path),i,t[:50],imgs[0][0],imgs[0][1].size)
                os.makedirs(os.path.join(ph,"某"),exist_ok=True)
                imgs[0][1].convert("RGB").save(os.path.join(ph,"某","01.jpg"),"JPEG",quality=90)
                raise SystemExit