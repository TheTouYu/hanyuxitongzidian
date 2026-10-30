import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image, ImageDraw, ImageFont
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx"); ps=d.paragraphs
ims=[]
for b in ps[20]._p.findall('.//'+qn('a:blip')):
    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
    if part is None or not hasattr(part,'blob'): continue
    try:
        im=Image.open(io.BytesIO(part.blob)).convert("RGB")
    except Exception: continue
    ims.append(im)
print("glyphs",len(ims))
H=170; GAP=18; COLS=8
cards=[im.resize((int(im.width*H/im.height),H),Image.LANCZOS) for im in ims]
rows=[cards[i:i+COLS] for i in range(0,len(cards),COLS)]
f=ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc",26)
W=int(max(sum(c.width for c in r)+GAP*(len(r)-1) for r in rows))+80
Ht=40+len(rows)*(H+GAP)+30
img=Image.new("RGB",(W,Ht),"white"); dr=ImageDraw.Draw(img)
dr.text((36,10),"𦟀（騾之初文，第 346 部部首字·一级字根）——象两耳长长的騾子形",font=f,fill=(25,25,25))
y=46
for r in rows:
    x=36
    for c in r: img.paste(c,(x,y)); x+=c.width+GAP
    y+=H+GAP
img.save(r"D:\系统汉字\intake\20261022-释蠃-字形.png"); print("saved",img.size)