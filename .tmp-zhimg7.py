import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx")
parts=d.part.related_parts
imgs=[(len(p.blob),rid) for rid,p in parts.items() if hasattr(p,"blob") and len(p.blob)>40000]
print("imgs>40k",len(imgs))
# 按文档顺序列段落，标出图片段与其后最近▲
last=None
for i,p in enumerate(d.paragraphs):
    r=None
    for bl in p._p.iter():
        for a in bl.attrib:
            if a.endswith('}embed'):
                try: _=parts[a]; r=a
                except KeyError: pass
    if r: last=(i,len(parts[r].blob))
    if p.text.strip().startswith("▲"):
        print("cap",i,p.text.strip()[:30],"| prev img",last)