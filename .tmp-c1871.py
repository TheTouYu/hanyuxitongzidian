import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
b=parts["rId377"].blob
ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
d=os.path.join(P,"邑"); os.makedirs(d,exist_ok=True)
open(os.path.join(d,"01"+ext),"wb").write(b)
ip=os.path.join(P,"index.json"); ph=json.load(io.open(ip,encoding="utf-8"))["photos"]
ph["邑"]=["01"+ext]; json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
c=r"D:\系统汉字\web\public\cards\邑.json"
j=json.load(io.open(c,encoding="utf-8")); j["photos"]=["01"+ext]
json.dump(j,io.open(c,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("邑 插图",ext,len(b))