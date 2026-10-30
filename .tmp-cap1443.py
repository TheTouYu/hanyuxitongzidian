# -*- coding: utf-8 -*-
# 审计：每个带图卡，必须在原稿该字条后（下一字头前）确有图片段落
import json,io,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
ph=json.load(io.open(P+r"\index.json",encoding="utf-8")).get("photos") or {}
# 建 字 -> 所在 docx 的段区（图段位置）
def load(f):
    doc=Document(f); ps=doc.paragraphs; parts=doc.part.related_parts
    out=[]
    for k,p in enumerate(ps):
        has=False
        for el in p._p.iter():
            for a,v in el.attrib.items():
                if (a.endswith("}embed") or a.endswith("}id")) and v in parts and len(parts[v].blob)>8000: has=True
        out.append((ps[k].text.strip(),has))
    return out
cache={}
def has_img(f,ch):
    if f not in cache: cache[f]=load(f)
    ps=cache[f]
    pat=re.compile(r"^"+re.escape(ch)+r"([^\u4e00-\u9fff]|$)")
    for i,(t,h) in enumerate(ps):
        if pat.match(t):
            for j in range(i,min(i+4,len(ps))):
                if ps[j][1]: return True
            return False
    return None
miss=[]
for ch in list(ph.keys()):
    found=None
    for f in glob.glob(r"D:\字谱智能体\*.docx"):
        r=has_img(f,ch)
        if r: found=True; break
        if r is False: found=False
    if found is not True: miss.append(ch)
print("可疑误配",len(miss))
print(miss[:25])