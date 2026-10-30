# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos"); C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
def grab(k,ch,cap):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")][0]
            b=parts[rid].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
            for f in os.listdir(d): os.remove(os.path.join(d,f))
            open(os.path.join(d,"01."+ext),"wb").write(b)
            ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=ix["photos"]; m[ch]=["01."+ext]
            json.dump({"photos":m},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
            cx=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cx["captions"]; cm[ch]=[cap]
            json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
            gx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); h=gx["chars"].get(ch) or {"doc":"","variants":[],"files":[]}
            h["photos"]=[ch+"/01."+ext]; gx["chars"][ch]=h
            json.dump({"chars":gx["chars"]},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
            return True
    return False
print(grab(266,"或","北京故宮的護城河"),grab(280,"或","紅刺楤"))
# 或 第二张图
print("skip2")
# erji links on 戈
p=os.path.join(C,"戈.json"); d=json.load(io.open(p,encoding="utf-8"))
if not any(s["key"]=="erji" for s in d["sections"]):
    i=[j for j,s in enumerate(d["sections"]) if s["key"]=="zizu"][0]
    d["sections"].insert(i+1,{"key":"erji","label":"本部二级字根","links":[{"ch":"或","label":"或"},{"ch":"國","label":"國"}]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")