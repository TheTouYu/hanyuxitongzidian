# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
def child_rows(chars):
    rows=[]
    for c in chars:
        d=json.load(io.open(os.path.join(C,c+".json"),encoding="utf-8"))
        sh=[s["text"] for s in d["sections"] if s["key"]=="shiyi"][0]
        rows.append([c,d.get("pinyin",""),"",sh])
    return rows
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
ER={"key":"erji","label":"本部二级字根","text":"","cites":[],"links":[{"ch":n,"label":n} for n in ("知","智","疾","医","至","到","臺","彘")]}
z={"char":"智","head":"智（𥏼𥏾𢜔）","pinyin":"zhì","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],
 "sections":[{"key":"benyi","label":"本义","text":strip(ps[110]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"由報靶之知，引申指智慧、智謀（原稿以「知」之轉義相通，見知部）。","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「总」：智總合所知而斷，一總而定（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義分兩組：","cites":[],
   "groups":[{"title":"①指看靶，表示遠看","note":"","rows":child_rows(["䚐"])},
             {"title":"②指報靶，表示往復","note":"","rows":child_rows(["𤁰","䠦","𨼓"])},
             {"title":"③形近字之訛（原稿未列具體字）","note":"","rows":[]}]},ER,VOL]}
json.dump(z,io.open(os.path.join(C,"智.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
b="".join(strip(ps[k]) for k in (119,120) if ps[k])
t="".join(strip(ps[k]) for k in (121,122,123,124) if ps[k])
j={"char":"疾","head":"疾（𤕬𤕼𤖏𥏂𥏦𥏴𤶅𤶥𠥻𤕺𤻣𥐃）","pinyin":"jí","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],
 "sections":[{"key":"benyi","label":"本义","text":b,"cites":[]},
  {"key":"zhuanyi","label":"转义","text":t,"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：箭傷聚痛於一處（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義分兩組：","cites":[],
   "groups":[{"title":"①指箭矢，表示尖刺之物","note":"","rows":child_rows(["㑵","蒺","槉","螏","𨪏"])},
             {"title":"②指矢傷，表示急速、劇烈","note":"","rows":child_rows(["𠹋","𧪠","𧽑"])}]},ER,VOL]}
json.dump(j,io.open(os.path.join(C,"疾.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 修子卡 parent 分别归位
for c in ["䚐","𤁰","䠦","𨼓"]:
    p=os.path.join(C,c+".json"); d=json.load(io.open(p,encoding="utf-8")); d["parent"]="智"; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("智/疾 建卡完成")