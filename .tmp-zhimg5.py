import sys,os,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
d=Document(r"D:\字谱智能体\卷一  雞.docx")
body=d.element.body
cur=None; out=[]; cap=None
for child in body.iterchildren():
    tag=child.tag.split('}')[-1]
    if tag=='p':
        p=Paragraph(child,d); t=p.text.strip()
        if t.startswith("3.旨"): cur="旨"
        elif cur and t[:1].isdigit() and t[1:2] in ".．": cur=None
        elif t.startswith("▲"): cap=t
        if cur:
            for bl in child.iter():
                for a in bl.attrib:
                    if a.endswith('}embed'): out.append((len(d.part.related_parts[a].blob),a,cap))
    elif tag=='tbl' and cur:
        tb=Table(child,d)
        for row in tb.rows:
            for cell in row.cells:
                for bl in cell._tc.iter():
                    for a in bl.attrib:
                        if a.endswith('}embed'): out.append((len(d.part.related_parts[a].blob),a,"(表)"+((cap or ""))))
big=[x for x in out if x[0]>25000]
print("embed",len(out),"big",len(big))
for s,r,c in big[:6]: print(s,r,c[:40])
if big:
    dst=r"D:\系统汉字\web\public\glyphs\photos\旨"; os.makedirs(dst,exist_ok=True)
    names=[]
    for i,(s,r,c) in enumerate(big[:3],1):
        blob=d.part.related_parts[r].blob
        ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
        fn=f"{i:02d}{ext}"; open(os.path.join(dst,fn),"wb").write(blob); names.append(fn)
    p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
    x=json.load(open(p,encoding="utf-8")); ph=x.get("photos") or x
    ph["旨"]=names
    json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
    print("saved",names)