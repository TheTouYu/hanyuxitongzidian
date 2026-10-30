# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
d=os.path.join(G,"盧"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[161]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1; fn="%02d.png"%n
            open(os.path.join(d,fn),"wb").write(b); fs.append("盧/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["盧"]={"doc":"卷八 虎","files":fs}
json.dump(idx,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
RAD={"壚":"土","纑":"糸","黸":"黑","驢":"馬","䰕":"髟","矑":"目","瓐":"玉","𢐸":"弓","櫨":"木","蠦":"虫","曥":"日","蘆":"艸","艫":"舟","顱":"頁","籚":"竹","鸕":"鳥","廬":"广","瀘":"水","臚":"肉","攎":"手","㪭":"攴","𡳬":"广","𤬛":"瓜","𤮧":"瓦","獹":"犬","嚧":"口","爐":"火","鱸":"魚","㠠":"山","𤴅":"瓦","𩙙":"風","𪖌":"鼠","𪙾":"齒","鑪":"金","轤":"車","𩍼":"革","𨇖":"足","𠐳":"人","㔧":"力","㿖":"疒","𥜠":"示"}
rows={}; cur=None
for k in range(165,215):
    t=ps[k]; 
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
def card(ch,head,pinyin,level,parent,sections,aliases=None):
    dd={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: dd["aliases"]=aliases
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("盧","盧（卢𥃈𧆣）","lú",2,"虍",[
 {"key":"benyi","label":"本义","text":ps[162].replace("本義：","",1)},
 {"key":"shengmu","label":"声母拟态","text":"l「拢离」取「拢」：爐膛收攏火光與熱（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}],aliases=["卢","𥃈","𧆣"])
m=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"盧",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":"l「拢离」取「拢」：攏聚其形色於一器一物（推）。"},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}])
        m+=1
# 两幅插图：p164 陶爐→盧；p178 黃櫨木→櫨
for para,ch,cap in ((163,"盧","仰韶文化遺址出土的陶爐（7000年前）"),(177,"櫨","黃櫨木")):
    dd=os.path.join(P,ch); os.makedirs(dd,exist_ok=True)
    for f in os.listdir(dd): os.remove(os.path.join(dd,f))
    for el in doc.paragraphs[para]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
                open(os.path.join(dd,"01."+ext),"wb").write(b); break
    for name,key in (("index.json","photos"),("captions.json","captions")):
        p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); mm=x.get(key) or x
        mm[ch]=["01.jpg"] if key=="photos" else [cap]
        json.dump({key:mm},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
    gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
    gi.setdefault("photos",{})[ch]=[{"file":"photos/%s/01.jpg"%ch,"caption":cap}]
    json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(fs),"groups",[(g["title"],len(g["rows"])) for g in gs],"cards",m)