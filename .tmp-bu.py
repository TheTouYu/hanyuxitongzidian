import io,os,re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx"); ps=d.paragraphs
for i,p in enumerate(ps):
    t=(p.text or "").strip()
    if re.match(r"^346[.．]",t):
        print("HEAD",i,t[:40])
        for j in range(i,min(len(ps),i+12)):
            tt=(ps[j].text or "").strip()
            if tt: print(j,"|",tt[:150])
        for j in range(i,min(len(ps),i+15)):
            for b in ps[j]._p.findall('.//'+qn('a:blip')):
                rid=b.get(qn('r:embed')); part=ps[j].part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                im=Image.open(io.BytesIO(part.blob))
                if max(im.size)>=200:
                    os.makedirs(r"D:\系统汉字\web\public\glyphs\photos\𦟀",exist_ok=True)
                    im.convert("RGB").save(r"D:\系统汉字\web\public\glyphs\photos\𦟀\01.jpg","JPEG",quality=90)
                    print("IMG",j,im.size)
        break