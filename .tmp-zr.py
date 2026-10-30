import io,os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷卌八  民.docx"); ps=d.paragraphs
for i in range(215,320):
    t=(ps[i].text or "").strip()
    n=len(ps[i]._p.findall('.//'+qn('a:blip')))
    if t or n: print(i,"|",t[:46],"| imgs",n)