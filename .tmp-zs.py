import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷卌八  民.docx"); ps=d.paragraphs
last=None
for i in range(210,len(ps)):
    t=(ps[i].text or "").strip()
    if t.startswith("宗") and len(t)<12: last=i
    if last is not None and t.startswith("本義"):
        print("宗 head",last,"本義 at",i,t[:40])
        for j in range(i,min(len(ps),i+8)):
            for b in ps[j]._p.findall('.//'+qn('a:blip')):
                rid=b.get(qn('r:embed')); part=ps[j].part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                im=Image.open(io.BytesIO(part.blob))
                if max(im.size)<200: continue
                os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\宗",exist_ok=True)
                im.convert("RGB").save(r"D:\系统汉字\web\public\glyphs\photos\宗\01.jpg","JPEG",quality=90)
                print("SAVED",j,im.size); raise SystemExit
        break
print("done")