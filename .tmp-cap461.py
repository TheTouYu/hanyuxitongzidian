import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
cur=None
for k in range(700,760):
    t=ps[k].text.strip(); m=pat.match(t)
    if m: cur=m.group(1)
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try: pt=parts[v]; b=pt.blob
                except KeyError: continue
                if len(b)>2000: print(k,cur,v,len(b),t[:18])