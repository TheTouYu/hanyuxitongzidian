import sys,os,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx")
blob=d.part.related_parts["rId109"].blob
ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
dst=r"D:\系统汉字\web\public\glyphs\photos\旨"; os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
fn="01"+ext; open(os.path.join(dst,fn),"wb").write(blob)
p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
x=json.load(open(p,encoding="utf-8")); ph=x.get("photos") or x
ph["旨"]=[fn]; json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
print(fn,len(blob))