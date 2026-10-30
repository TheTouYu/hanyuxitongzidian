import sys,struct
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
for rid in ("rId156","rId157"):
    b=parts[rid].blob
    if b[:4]==b"\x89PNG":
        w,h=struct.unpack(">II",b[16:24]); print(rid,"png",w,"x",h,len(b))
    else:
        print(rid,b[:4].hex(),len(b))