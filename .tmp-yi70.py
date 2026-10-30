# -*- coding: utf-8 -*-
import json,io,os,shutil,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
d=os.path.join(G,"䖒"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[269]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1; fn="%02d.png"%n
            open(os.path.join(d,fn),"wb").write(b); fs.append("䖒/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["䖒"]={"doc":"卷八 虎","files":fs}
RAD={"𤮙":"缶","𧕆":"虫","𤬘":"瓜","𤃪":"水","𨞘":"邑","隵":"阜","巇":"山","㸍":"火","戲":"戈","𢹍":"手","嚱":"口","𣤴":"欠","𢨛":"口","㱆":"欠","𧇔":"几","㺣":"犬","覻":"見","𦟚":"鼻"}
SM={"𤮙":"x「续消」取「消」：缶中空，聲消而受（推）。","𧕆":"x「续消」取「消」：蠡瓢中空，水消其中（推）。","𤬘":"x「续消」取「消」：瓠瓢中空，盛而消（推）。","𤃪":"x「续消」取「消」：水名，水流消長（推）。","𨞘":"x「续消」取「消」：魯地名，照實記音（推）。","隵":"x「续消」取「消」：山崖險缺，形勢消剝（推）。","巇":"x「续消」取「消」：山相對危險，中多罅隙（推）。","㸍":"x「续消」取「消」：燒而使物消（推）。","戲":"x「续消」取「消」：擊鼓進軍，聲威消長（推）。","𢹍":"x「续消」取「消」：擊而使之消散（推）。","嚱":"x「续消」取「消」：吹氣成聲，聲出而消（推）。","𣤴":"x「续消」取「消」：吹聲而出，旋出旋消（推）。","𢨛":"x「续消」取「消」：相笑之皃，笑意消融（推）。","㱆":"x「续消」取「消」：相笑，笑氣消融（推）。","𧇔":"k「口控」取「口」：樂聲從口出而可控（推）。","㺣":"x「续消」取「消」：豕屬，照實記音（推）。","覻":"q「亲缺」取「缺」：從細縫窺看（推）。","𦟚":"zh「凿总」取「凿」：鼻上皰，鑿然而起（推）。"}
rows={}; cur=None
for kk in range(280,302):
    t=ps[kk]
    if not t: continue
    if t.startswith("▲") or t.startswith("字族衍義"): continue
    m=re.match(r"^([①②③④])(.+)$",t)
    if m: cur=m.group(2); rows[cur]=[]; continue
    m=re.match(r"^(\S+?)\s*([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)?)\s*(.*)$",t)
    if m and cur: rows[cur].append((m.group(1),m.group(2),m.group(3)))
gs=[]
for no,(t,rs) in zip("①②③④",rows.items()):
    gs.append({"no":no,"title":t,"rows":[[a,b,RAD.get(re.split(r"[（(]",a)[0],""),c] for a,b,c in rs]})
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
def card(ch,head,pinyin,level,parent,sections,aliases=None,grade=None,rootLevel=None):
    dd={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: dd["aliases"]=aliases
    if grade: dd["grade"]=grade
    if rootLevel: dd["rootLevel"]=rootLevel
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
BEN=ps[270].replace("本義：","",1)+"\n"+ps[271]
ZHUAN="\n".join(ps[k] for k in range(274,278)).replace("轉義：","",1)
card("䖒","䖒（𧆲）","xī",2,"虍",[
 {"key":"benyi","label":"本义","text":BEN},
 {"key":"zhuanyi","label":"转义","text":ZHUAN},
 {"key":"bianzheng","label":"辩证","text":ps[278].replace("辯證：","",1)},
 {"key":"shengmu","label":"声母拟态","text":"x「续消」取「消」：器中空，擊之聲出而消（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}],aliases=["𧆲"])
m=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"䖒",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":SM.get(base,"（按今读音取拟态义一面，推。）")},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}])
        m+=1
# 陶鼓图归 䖒
dd=os.path.join(P,"䖒"); os.makedirs(dd,exist_ok=True)
for f in os.listdir(dd): os.remove(os.path.join(dd,f))
shutil.copy(r"D:\系统汉字\.tmp-taogu.jpg", os.path.join(dd,"01.jpg"))
cap="甘肅馬家窯文化陶鼓（4500年前）"
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); mm=x.get(key) or x
    mm["䖒"]=["01.jpg"] if key=="photos" else [cap]
    json.dump({key:mm},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["䖒"]=[{"file":"photos/䖒/01.jpg","caption":cap}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(fs),"groups",[(g["title"],len(g["rows"])) for g in gs],"cards",m)