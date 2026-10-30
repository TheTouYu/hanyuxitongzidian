# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
row=re.compile(r"^([^\s（(（]{1,3})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、]+)\s*[《“]")
groups=[];cur=None
for k in range(30,73):
    t=ps[k]
    if not t: continue
    if re.match(r"^[①②③④⑤]",t):
        cur={"title":t,"note":"","rows":[]}; groups.append(cur); continue
    m=row.match(t)
    if m and cur is not None:
        cur["rows"].append([m.group(1),m.group(4).split("、")[0],"",t])
print([(g["title"],len(g["rows"])) for g in groups])
d={"char":"弋","trad":"弋","pinyin":"yì","level":1,"bus":[{"num":26,"name":"弋"}],
 "sections":[
  {"key":"benyi","label":"本义","text":ps[21].replace("本義：","")+"\n"+ps[22],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[k].replace("轉義：","") for k in (24,25,26,27)),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":ps[28].replace("辯證：",""),"cites":[]},
  {"key":"yinyuan","label":"音源","text":ps[29].replace("音源：",""),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":groups,"cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}],
 "head":"弋（𢍺）","aliases":["𢍺"],
 "photos":["01.jpg"],"captions":["后羿弋射圖（戰國 曾侯乙墓衣箱漆畫）"]}
json.dump(d,io.open(os.path.join(C,"弋.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("弋 部头建成")