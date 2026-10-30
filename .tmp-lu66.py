# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
d=os.path.join(G,"虛"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[242]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1; fn="%02d.png"%n
            open(os.path.join(d,fn),"wb").write(b); fs.append("虛/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["虛"]={"doc":"卷八 虎","files":fs}
json.dump(idx,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 本義行内字形
IB=os.path.join(G,"inline","虛","benyi"); os.makedirs(IB,exist_ok=True)
for f in os.listdir(IB): os.remove(os.path.join(IB,f))
buf=[];k=0
for el in doc.paragraphs[243]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t" and el.text: buf.append(el.text)
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; k+=1; fn="%02d.png"%k
            open(os.path.join(IB,fn),"wb").write(b); buf.append("{{benyi/%s}}"%fn)
BEN="".join(buf).replace("本義：","",1).strip()
RAD={"墟":"土","噓":"口","魖":"鬼","歔":"欠","譃":"言","憈":"心","𡃧":"言","𤮆":"瓦","𧇺":"火","驉":"馬","㠊":"山","鱋":"魚","覷":"見","𥕰":"石","戱":"戈","𤂴":"水","㩬":"手","𢴮":"手","𣚛":"虍","𧝔":"衣"}
rows={}; cur=None
for kk in range(245,269):
    t=ps[kk]
    if not t: continue
    if t.startswith("▲") or t.startswith("字族衍義"): continue
    m=re.match(r"^([①②③④])(.+)$",t)
    if m: cur=m.group(2); rows[cur]=[]; continue
    m=re.match(r"^(\S+?)\s*([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)?)\s*(.*)$",t)
    if m and cur: rows[cur].append((m.group(1),m.group(2),m.group(3)))
gs=[]
for no,(t,rs) in zip("①②③",rows.items()):
    gs.append({"no":no,"title":t,"rows":[[a,b,RAD.get(re.split(r"[（(]",a)[0],""),c] for a,b,c in rs]})
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
def card(ch,head,pinyin,level,parent,sections,aliases=None):
    dd={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: dd["aliases"]=aliases
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("虛","虛（虗𠧝𣦄𧆳）","xū",2,"虍",[
 {"key":"benyi","label":"本义","text":BEN,"gdir":"inline/虛"},
 {"key":"zhuanyi","label":"转义","text":ps[244].replace("轉義：","",1)},
 {"key":"shengmu","label":"声母拟态","text":"x「续消」取「消」：丘中空闊，其形消散（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}],aliases=["虚","虗","𠧝","𣦄","𧆳"])
m=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"虛",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":"（按今读音取拟态义一面，推。）"},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}])
        m+=1
print("glyphs",len(fs),"inline",k,"groups",[(g["title"],len(g["rows"])) for g in gs],"cards",m)