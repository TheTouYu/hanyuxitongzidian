import glob,io,os,re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=d.paragraphs
    for i,p in enumerate(ps):
        t=(p.text or "").strip()
        if re.match(r"^宗[（(]?",t) and len(t)>3:
            for j in range(i,min(len(ps),i+40)):
                for b in ps[j]._p.findall('.//'+qn('a:blip')):
                    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                    if part is None or not hasattr(part,'blob'): continue
                    im=Image.open(io.BytesIO(part.blob))
                    if max(im.size)<200: continue
                    os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\宗",exist_ok=True)
                    im.convert("RGB").save(r"D:\系统汉字\web\public\glyphs\photos\宗\01.jpg","JPEG",quality=90)
                    print("HIT",os.path.basename(path),i,j,im.size,t[:50]); raise SystemExit
print("none")