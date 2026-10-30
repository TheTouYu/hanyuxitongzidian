# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
# 找 18 部起点
end=next((k for k in range(300,400) if re.match(r"^18[.．]",ps[k])),360)
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóòūúǔùǖǘǚǜü]+)")
groups=[]; cur=None
for k in range(285,end):
    t=ps[k]
    if not t: continue
    m1=re.match(r"^([①②③④])(.*)",t)
    if m1: cur={"title":t,"note":"","rows":[]}; groups.append(cur); continue
    if t.startswith("▲") or t.startswith("18"): continue
    m=pat.match(t)
    if m and cur is not None:
        cur["rows"].append([m.group(1),m.group(4),("" if not re.search(r"从([一-龥])",t) else re.search(r"从([一-龥])",t).group(1)),t])
print([ (g["title"][:12],len(g["rows"])) for g in groups])
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
z={"char":"尸","head":"尸（𠃜𡰣）","pinyin":"shī","level":1,"bus":[{"num":17,"name":"尸"}],
 "sections":[{"key":"benyi","label":"本义","text":strip(ps[276]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":strip(ps[279])+strip(ps[280])+strip(ps[281]),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":strip(ps[282]),"cites":[]},
  {"key":"yinyuan","label":"音源","text":strip(ps[283]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「收」：尸祭者蹲踞不動，收其動而受祭（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文分組：","cites":[],"groups":groups},VOL]}
json.dump(z,io.open(os.path.join(C,"尸.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 插图 p277
rid=None
for k in range(276,280):
    for el in doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try:
                    if len(parts[v].blob)>30000: rid=v
                except KeyError: pass
if rid:
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,"尸"); os.makedirs(D,exist_ok=True); fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx; ph["尸"]=[fn]
    json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["尸"]=["廣西全州遺存的戴面具“尸祭”祖宗儀式"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("尸卡建，图",bool(rid))