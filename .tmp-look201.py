import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=d.paragraphs; parts=d.part.related_parts
cur=None; import re
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,3})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
for k in range(737,800):
    if k>=len(ps): break
    t=ps[k].text.strip(); m=pat.match(t)
    if m: cur=m.group(1)
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>8000: print(k,cur,v,len(b),t[:14])