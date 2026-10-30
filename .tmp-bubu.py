from docx import Document
import re,glob,json
mp={}
for p in glob.glob(r"D:\字谱智能体\*.docx"):
    try: d=Document(p)
    except Exception: continue
    for q in d.paragraphs:
        m=re.match(r"(\d{3})\.(\S+?)部$",q.text.strip())
        if m: mp.setdefault(m.group(1),m.group(2))
json.dump(mp,open(r".tmp-bu.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(mp)); print(" ".join(f"{k}{v}" for k,v in sorted(mp.items()) if 418<=int(k)<=445))