import sys,os,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
D=r"D:\系统汉字\web\public\glyphs\inline\弔\benyi"; os.makedirs(D,exist_ok=True)
open(os.path.join(D,"01.png"),"wb").write(parts["rId156"].blob)
open(os.path.join(D,"02.emf"),"wb").write(parts["rId157"].blob)
print("ok")