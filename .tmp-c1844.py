import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\第八章  子.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
cur=None
for k in range(309,430):
    t=ps[k].text.strip()
    m=re.match(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùü]+",t)
    if m: cur=m.group(1)
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>30000: print(k,cur,len(b),t[:18])