import sys,os,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
d=Document(r"D:\字谱智能体\卷一  雞.docx")
def rid_of(el):
    for bl in el.iter():
        for a in bl.attrib:
            if a.endswith('}embed'):
                try:
                    _=d.part.related_parts[a]; return a
                except KeyError: return None
    return None
cur=None; big=[]; cap=None
for child in d.element.body.iterchildren():
    tag=child.tag.split('}')[-1]
    if tag=='p':
        p=Paragraph(child,d); t=p.text.strip()
        if t.startswith("3.旨"): cur="旨"
        elif cur and t[:1].isdigit() and t[1:2] in ".．": cur=None
        elif t.startswith("▲"): cap=t
        if cur:
            r=rid_of(child)
            if r and len(d.part.related_parts[r].blob)>25000: big.append((r,cap))
    elif tag=='tbl' and cur:
        for row in Table(child,d).rows:
            for cell in row.cells:
                r=rid_of(cell._tc)
                if r and len(d.part.related_parts[r].blob)>25000: big.append((r,cap))
print("big",len(big),[c[:20] for _,c in big])
dst=r"D:\系统汉字\web\public\glyphs\photos\旨"
if big:
    os.makedirs(dst,exist_ok=True); names=[]
    for i,(r,c) in enumerate(big[:4],1):
        blob=d.part.related_parts[r].blob
        ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
        fn=f"{i:02d}{ext}"; open(os.path.join(dst,fn),"wb").write(blob); names.append(fn)
    p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
    x=json.load(open(p,encoding="utf-8")); ph=x.get("photos") or x
    ph["旨"]=names; json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
    print("saved",names)