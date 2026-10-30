import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
f=glob.glob(r"D:\字谱智能体\卷六十四*絲*.docx") or glob.glob(r"D:\字谱智能体\卷六十四*.docx")
print(f)
doc=Document(f[0]); ps=doc.paragraphs; parts=doc.part.related_parts
start=None
for k,p in enumerate(ps):
    if re.match(r"^389[.．]\s*己部", p.text.strip()): start=k; break
print("start",start)
cur=None
for k in range(start, min(len(ps), start+120)):
    t=ps[k].text.strip()
    m=re.match(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùü]+", t)
    if m: cur=m.group(1)
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>30000: print(k,cur,len(b),"cap:",t[:16])