# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def sec(k,l,t): return {"key":k,"label":l,"text":t}
LEI={"籱":"竹","㰌":"木","臛":"肉","瀖":"水","𩱶":"水","𨯟":"金","𡾜":"山","鸖":"鳥","嚯":"口","𤣅":"至","㱋":"土","攉":"手","𠠰":"刀","𦒧":"羽","癨":"疒","㸌":"火","𧆑":"艸","礭":"石","𥽥":"米","𠐶":"人","皬":"白","𤜅":"牛","𩧏":"馬","曤":"日","矐":"目","㺢":"犬"}
groups=[("①",81,88),("②",88,96),("③",96,103),("④",103,107),("⑤",107,114)]
pat=re.compile("^([^\\sA-Za-z]+?)([A-Za-z\u00C0-\u024F\u0300-\u036F、，\\s]+)《")
rows=[]
for tag,a,b in groups:
    rr=[]
    for i in range(a+1,b):
        t=ps[i]
        if not t or t.startswith("▲"): continue
        m=pat.match(t)
        if m:
            ch=m.group(1); py=re.sub(r"[、，\\s]+","、",m.group(2)).strip("、")
            rr.append([ch,py,LEI.get(ch.split("（")[0],""),t])
    rows.append({"no":tag,"title":"","rows":rr})
head={"c":"靃","head":"靃（霍）","pinyin":"huò","lv":2,"parent":"隺","bus":[{"num":39,"name":"隺"}],
 "sections":[sec("benyi","本义",ps[74].split("：",1)[1]),
  sec("zhuanyi","转义","\n\n".join(ps[i].split("：",1)[1] for i in range(75,78))),
  sec("bianzheng","辩证",ps[78].split("：",1)[1]),sec("yinyuan","音源",ps[79].split("：",1)[1]),
  sec("shengmu","声母拟态","h「豁活」取「豁」：鶴羽一揮，其聲霍然（推）。"),
  {"key":"zizu","label":"字族衍义","groups":rows},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]}
json.dump(head,io.open(os.path.join(C,"靃.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=1
for g in rows:
    for ch,py,lei,txt in g["rows"]:
        base=ch.split("（")[0]; p=os.path.join(C,base+".json")
        if os.path.exists(p): continue
        json.dump({"c":base,"head":ch,"pinyin":py,"lv":3,"parent":"靃","bus":[{"num":39,"name":"隺"}],
          "sections":[sec("shiyi","释义",txt),sec("shengmu","声母拟态","（按今读声母取擬態義一面，推。）"),
           {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]},
          io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# photos
def grab(k,dst,cap):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; os.makedirs(dst,exist_ok=True)
                for f in os.listdir(dst): os.remove(os.path.join(dst,f))
                ext="png" if b[:4]==b"\x89PNG" else "jpg"
                open(os.path.join(dst,"01."+ext),"wb").write(b)
                return "01."+ext
p1=grab(33,os.path.join(P,"隺"),"《松鶴圖》局部（清 沈銓）")
p2=grab(90,os.path.join(P,"𡾜"),"南嶽祝融峰")
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=idx.get("photos") or idx
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
if p1: m["隺"]=[p1]; cm["隺"]=["《松鶴圖》局部（清 沈銓）"]
if p2: m["𡾜"]=[p2]; cm["𡾜"]=["南嶽祝融峰"]
json.dump({"photos":m},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("cards",n,"photos",p1,p2,"rows",sum(len(g["rows"]) for g in rows))