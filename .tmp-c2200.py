# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
d=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=d.part.related_parts
def put(ch,rid,cap):
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,ch); os.makedirs(D,exist_ok=True)
    for f in os.listdir(D): os.remove(os.path.join(D,f))
    fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8"))["photos"]; idx[ch]=[fn]
    json.dump({"photos":idx},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cj=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))["captions"]
    if cap: cj[ch]=[cap]
    else: cj.pop(ch,None)
    json.dump({"captions":cj},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
    p=os.path.join(C,ch+".json"); x=json.load(io.open(p,encoding="utf-8"))
    x["photos"]=[fn]
    if cap: x["captions"]=[cap]
    else: x.pop("captions",None)
    json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,fn,len(b))
put("式","rId44","")
put("栻","rId45","太乙九宫占盘（西漢）")