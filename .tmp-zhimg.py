import sys,os,json,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx")
ps=d.paragraphs
i=[k for k,p in enumerate(ps) if p.text.strip().startswith("3.旨")][0]
rids=[]
for p in ps[i:i+30]:
    for bl in p._p.iter():
        for a in bl.attrib:
            if a.endswith('}embed'): rids.append(bl.attrib[a])
seen=[]
for r in rids:
    if r in seen: continue
    seen.append(r)
print("imgs",len(seen))
out=r"D:\系统汉字\web\public\glyphs\photos\旨"
os.makedirs(out,exist_ok=True)
k=0
for r in seen:
    try: part=d.part.related_parts[r]
    except: continue
    blob=part.blob
    if len(blob)<8000: continue
    open(os.path.join(out,f"{k+1:02d}.jpg"),"wb").write(blob); k+=1
    if k>=2: break
print("saved",k)
if k:
    p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
    ph=json.load(open(p,encoding="utf-8")); ph=ph.get("photos") if "photos" in ph else ph
    ph["旨"]=[f"{i:02d}.jpg" for i in range(1,k+1)]
    json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")