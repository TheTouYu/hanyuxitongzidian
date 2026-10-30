# -*- coding: utf-8 -*-
import glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.oxml.ns import qn
src=glob.glob(r"D:\字谱智能体\*.docx"); dst=r"D:\字谱智能体\单栏"
os.makedirs(dst,exist_ok=True)
ok=0;bad=[]
for f in src:
    try:
        d=Document(f)
        for sec in d.sections:
            cols=sec._sectPr.find(qn("w:cols"))
            if cols is None:
                cols=sec._sectPr.makeelement(qn("w:cols"),{}); sec._sectPr.append(cols)
            for a in list(cols.attrib):
                if a.endswith("}num") or a.endswith("}space") or a.endswith("}equalWidth") or a.endswith("}sep"):
                    del cols.attrib[a]
            cols.set(qn("w:num"),"1")
        out=os.path.join(dst,os.path.basename(f)); d.save(out); ok+=1
    except Exception as e:
        bad.append((os.path.basename(f),str(e)[:80]))
print("转换",ok,"失败",len(bad),bad[:3])