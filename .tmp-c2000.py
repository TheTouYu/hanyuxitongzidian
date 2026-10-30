# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
row=re.compile(r"^([^\s（(（]{1,3})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、]+)\s*[《“]")
groups=[];cur=None
for k in range(746,792):
    t=ps[k]
    if not t: continue
    if re.match(r"^[①②③④⑤⑥]",t):
        cur={"title":t,"note":"","rows":[]}; groups.append(cur); continue
    m=row.match(t)
    if m and cur is not None:
        cur["rows"].append([m.group(1),(m.group(4) or "").split("、")[0],"",t])
groups[-1]["note"]="原文未列字，仅标组名"   # ④ 讹字组
# ④ 组同行保留
d={"char":"睪","trad":"睪","pinyin":"yì","level":1,
   "bus":[{"num":25,"name":"睪"}],
   "sections":[
    {"key":"benyi","label":"本义","text":ps[740].replace("本義：",""),"cites":[]},
    {"key":"zhuanyi","label":"转义","text":ps[741].replace("轉義：","")+"\n"+ps[742],"cites":[]},
    {"key":"bianzheng","label":"辩证","text":ps[743].replace("辯證：","")+"\n"+ps[744],"cites":[]},
    {"key":"yinyuan","label":"音源","text":ps[745].replace("音源：",""),"cites":[]},
    {"key":"shengmu","label":"声母拟态","text":"y「零声母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
    {"key":"zizu","label":"字族衍义","text":"","groups":groups,"cites":[]},
    {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷三矢","label":"卷三 矢"}],"cites":[]}]}
json.dump(d,io.open(os.path.join(C,"睪.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("groups",[len(g["rows"]) for g in groups])
# 全库删空栏
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); x=json.load(io.open(p,encoding="utf-8"))
    secs=x.get("sections") or []
    keep=[s for s in secs if (s.get("text") or "").strip() or s.get("groups") or s.get("links")]
    if len(keep)!=len(secs):
        x["sections"]=keep; json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("清空栏卡数",n)