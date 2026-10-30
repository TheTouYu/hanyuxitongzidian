from docx import Document
import re,glob,json
mp={}
for p in glob.glob(r"D:\字谱智能体\*.docx"):
    try: d=Document(p)
    except Exception: continue
    for q in d.paragraphs:
        t=q.text.strip()
        if len(t)>40: continue
        m=re.match(r"(\d{3})\s*[\.．、]?\s*(\S+?)部$",t)
        if m and 1<=int(m.group(1))<=609: mp[int(m.group(1))]=m.group(2)
json.dump({str(k):v for k,v in sorted(mp.items())},open(r".tmp-bu.json","w",encoding="utf-8"),ensure_ascii=False)
miss=[i for i in range(1,610) if i not in mp]
print("have",len(mp),"missing",len(miss))
print("gap ranges sample:",miss[:40])