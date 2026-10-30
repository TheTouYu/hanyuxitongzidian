import sys,os,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def blobs(k):
    o=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: o.append(parts[rid[0]].blob)
                except KeyError: pass
    return o
b=blobs(55)[0]
d=os.path.join(P,"号"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
open(os.path.join(d,"01."+ext),"wb").write(b)
for name,key,val in (("index.json","photos",["01."+ext]),("captions.json","captions",["雁鵝張口嚎叫（原稿此圖無▲圖注）"])):
    p=os.path.join(P,name); dd=json.load(io.open(p,encoding="utf-8")); m=dd.get(key) or dd
    m["号"]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok",len(b),ext)