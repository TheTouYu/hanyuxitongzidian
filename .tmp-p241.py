# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
b=parts["rId133"].blob
open(r"D:\系统汉字\.tmp-p241.jpg","wb").write(b); print(len(b))