# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
# 1) 厂 gets 2 photos: keep 古崖居 as 01, move 人字雁阵 to 02
src=os.path.join(P,"鴈","01.jpg"); dst2=os.path.join(P,"厂","02.jpg")
shutil.copyfile(src,dst2)
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def first_img(k,minlen=3000):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob
                if len(b)>=minlen: return b
    return None
b=first_img(244)
d2=os.path.join(P,"鴈"); os.makedirs(d2,exist_ok=True)
for f in os.listdir(d2): os.remove(os.path.join(d2,f))
open(os.path.join(d2,"01.jpg"),"wb").write(b)
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); pm=ix.get("photos") or ix
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cp.get("captions") or cp
pm["厂"]=["01.jpg","02.jpg"]; cm["厂"]=["北京延慶古崖居","「人」字形雁陣"]
pm["鴈"]=["01.jpg"]; cm["鴈"]=["白額雁"]
json.dump({"photos":pm},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 2) rows: 取义落点 以原文训释为准
rows={
 "①指“石”，表示懸崖或懸崖狀":[
  ["厓","yá","厂","《說文》「山邊也」；圭為疊加聲符"],
  ["崖","yá","山","《說文》「高邊也」；應从山厓聲"],
  ["涯","yá","水","《新附》「水邊也」；引申邊際、極限"],
  ["睚","yá","目","《新附》「目際也」；怒視"],
  ["屵","è","山","《說文》「岸高也」；仰也"],
  ["娾","ǎi","女","《玉篇》「喜樂也」；《集韻》「女媿也」"],
  ["厊","yǎ","厂","《集韻》「厏厊，不相合也」；上牙齙出"],
  ["广","yǎn","广","《說文》「因广為屋，象對剌高屋之形」"],
  ["𠆲","yǎn","","《集韻》「髙峻皃」"],
  ["𢇘","yǎn","广","《廣韻》「齊𢇘也」；《玉篇》「卑皃」"],
  ["㚧","yǎn","女","《集韻》「婦人齊整皃」"],
  ["𢇞","hàn","","《廣韻》「𢇞嘾，乳汁狀」"]],
 "②同“丂”，表示大雁":[
  ["㷳","yàn","火","《說文》「火色也」，色如褐雁"],
  ["贗","yàn","貝","《集韻》「偽物」；鵝似雁而味不如"],
  ["鴈","yàn","鳥","《說文》「䳘也」；厂或為丂（人字陣）之誤"]]}
p=os.path.join(C,"厂.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["groups"]=[{"t":k,"rows":v} for k,v in rows.items()]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")