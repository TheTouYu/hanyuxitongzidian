# -*- coding: utf-8 -*-
import sys,os,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.oxml.ns import qn
bad=[];ok=0
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    d=Document(f)
    nums={ (s._sectPr.find(qn("w:cols")).get(qn("w:num")) if s._sectPr.find(qn("w:cols")) is not None else None) for s in d.sections }
    if nums<= {"1"} or nums=={None}: ok+=1
    else: bad.append((os.path.basename(f),nums))
print("单栏校验通过",ok,"异常",len(bad),bad[:5])
print("备份数",len(glob.glob(r"D:\字谱智能体\_原始备份\*.docx")))