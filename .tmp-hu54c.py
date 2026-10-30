# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷八  虎.docx").paragraphs]
BEN=ps[121].replace("本義：","",1)
RAD=["言","口","欠","口","疒","女","心","邑","土","缶","水","手","玉","石","竹","血","木"]
rows={}; cur=None
for k in range(122,143):
    t=ps[k]
    if not t: continue
    if t.startswith("字族衍義"): continue
    m=re.match(r"^([①②③])(.+)$",t)
    if m: cur=m.group(1)+m.group(2); rows[cur]=[]; continue
    m=re.match(r"^(\S+?)\s*([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)?)\s*(.*)$",t)
    if m and cur: rows[cur].append((m.group(1),m.group(2),m.group(3)))
idx=0
def build_groups():
    global idx
    out=[]
    for i,(t,rs) in enumerate(rows.items(),1):
        rr=[]
        for name,p,st in rs:
            rr.append([name,p,RAD[idx] if idx<len(RAD) else "",st]); idx+=1
        out.append({"no":"①②③"[i-1],"title":t,"rows":rr})
    return out
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
def card(ch,head,pinyin,level,parent,sections,aliases=None):
    d={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: d["aliases"]=aliases
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
gs=build_groups()
card("虖","虖（雽䖉𧆪𧆜）","hū",2,"虍",[
 {"key":"benyi","label":"本义","text":BEN},
 {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：張口吼叫，聲豁然而大（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":""}],aliases=["雽","䖉","𧆪","𧆜"])
n=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"虖",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":"（按今读音取拟态义一面，推。）"},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）"}])
        n+=1
print("groups",[ (g["title"],len(g["rows"])) for g in gs],"cards",n)