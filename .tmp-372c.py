import glob,os,re
from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
have={os.path.splitext(f)[0] for f in os.listdir(r"web\public\cards")}
fam=ps[59]
chars=[]
for c in fam[2:]:
    if "\u3400"<=c<="\u9fff" or "\U00020000"<=c<="\U0002a6df":
        if c not in chars: chars.append(c)
miss=[c for c in chars if c not in have]
print("family",len(chars),"missing",len(miss), "".join(miss[:12]))
for ch in miss[:10]:
    found=None
    for i in range(60,150):
        t=ps[i] if i<len(ps) else ""
        if t.startswith(ch) and len(t)>30: found=(i,t); break
    print("==",ch,"p",found[0] if found else "-")
    print((found[1][:130] if found else "no entry"))