import glob,io,os,re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
def imgs(ps,j):
    out=[]
    for b in ps[j]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=ps[j].part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        try: out.append(Image.open(io.BytesIO(part.blob)))
        except Exception: pass
    return out
for path in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(path)
    except Exception: continue
    ps=d.paragraphs
    head=None
    for i,p in enumerate(ps):
        t=(p.text or "").strip()
        if re.match(r"^27[0-9][.．]\s*冖部",t) or (t.endswith("冖部") and re.match(r"^\d{1,3}[.．]",t)):
            head=i; print("HEAD",os.path.basename(path),i,t[:30]); break
    if head is None: continue
    for i in range(head,min(len(ps),head+120)):
        t=(ps[i].text or "").strip()
        if t.startswith("宗") and "《" in t:
            print("ENTRY",i,t[:40])
            for j in range(i,min(len(ps),head+140)):
                for im in imgs(ps,j):
                    if max(im.size)<200: continue
                    os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\宗",exist_ok=True)
                    im.convert("RGB").save(r"D:\系统汉字\web\public\glyphs\photos\宗\01.jpg","JPEG",quality=90)
                    print("SAVED",j,im.size); raise SystemExit