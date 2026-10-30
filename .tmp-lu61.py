# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
# 字形 p144
d=os.path.join(G,"虜"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[144]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1; fn="%02d.png"%n
            open(os.path.join(d,fn),"wb").write(b); fs.append("虜/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["虜"]={"doc":"卷八 虎","files":fs}
json.dump(idx,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 解析字族
RAD=["手","广","魚","金","心","口","木","疒","髟"]
rows={}; cur=None
for k in range(149,161):
    t=ps[k]
    if not t: continue
    if t.startswith("字族衍義"): continue
    m=re.match(r"^([①②③])(.+)$",t)
    if m: cur=m.group(2); rows[cur]=[]; continue
    m=re.match(r"^(\S+?)\s*([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)?)\s*(.*)$",t)
    if m and cur: rows[cur].append((m.group(1),m.group(2),m.group(3)))
gs=[];i=0
for no,(t,rs) in zip("①②③",rows.items()):
    rr=[]
    for name,p,st in rs:
        rr.append([name,p,RAD[i] if i<len(RAD) else "",st]); i+=1
    gs.append({"no":no,"title":t,"rows":rr})
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
SH={"擄":"l「拢离」取「拢」：以爪攏住獵物而掠取（推）。","㢚":"l「拢离」取「拢」：堂下周屋四圍攏合（推）。",
"䲐":"l「拢离」取「拢」：魚名，照實記音（推）。","鐪":"l「拢离」取「拢」：煎膠之器，收攏膠液（推）。",
"𢢛":"l「拢离」取「离」：心惑而散離不定（推）。","𠿛":"l「拢离」取「拢」：喚豬之聲，攏聚之（推）。",
"㯭":"l「拢离」取「拢」：雙手攏櫓而進船（推）。","𤺿":"l「拢离」取「离」：痞結而氣離（推）。",
"𩯜":"l「拢离」取「拢」：鬣髮攏聚（推）。"}
def card(ch,head,pinyin,level,parent,sections,aliases=None):
    dd={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},
        "suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: dd["aliases"]=aliases
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("虜","虜（虏虜）","lǔ",2,"虍",[
 {"key":"benyi","label":"本义","text":ps[145].replace("本義：","",1)},
 {"key":"zhuanyi","label":"转义","text":ps[147].replace("轉義：","",1)},
 {"key":"bianzheng","label":"辩证","text":ps[148].replace("辯證：","",1)},
 {"key":"shengmu","label":"声母拟态","text":"l「拢离」取「拢」：虎爪攏住獵物而掠取（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}],aliases=["虏","虜"])
m=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"虜",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":SH.get(base,"（按今读音取拟态义一面，推。）")},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}])
        m+=1
print("glyphs",len(fs),"groups",[(g["title"],len(g["rows"])) for g in gs],"cards",m)