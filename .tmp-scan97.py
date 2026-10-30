import glob,re,os
from docx import Document
fs=[f for f in glob.glob(r"D:\字谱智能体\*.docx") if "卷九十七" in f or "卷九十八" in f]
for f in fs: print(os.path.basename(f))
f=fs[0]
d=Document(f); ps=[p.text.strip() for p in d.paragraphs]
print("paras",len(ps))
for i,t in enumerate(ps):
    if re.match(r"^\d{3}\.[^\d]",t): print(i,t[:40])
print("----head----")
for k in range(0,90):
    if ps[k]: print(k,ps[k][:100])