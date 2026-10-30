# -*- coding: utf-8 -*-
import sys,os,re,json,io,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
def blobs(a,b):
    o=[]
    for k in range(a,b+1):
        for el in doc.paragraphs[k]._p.iter():
            if el.tag.split("}")[-1]=="blip":
                rid=[v for x,v in el.attrib.items() if x.endswith("}embed") or x.endswith("}id")]
                if rid:
                    try:o.append(parts[rid[0]].blob)
                    except KeyError:pass
    return o
bs=blobs(380,380); d=os.path.join(G,"畫")
if os.path.isdir(d): shutil.rmtree(d)
os.makedirs(d,exist_ok=True)
n=0
for i,b in enumerate(bs):
    ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else None)
    if not ext: continue
    n+=1; open(os.path.join(d,"%02d.%s"%(n,ext)),"wb").write(b)
g=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=g["chars"]
ch["畫"]={"files":["畫/%02d.png"%i for i in range(1,n+1)]}
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
def sec(k,l,t): return {"key":k,"label":l,"text":t}
rows=[]
for k in range(387,398):
    t=ps[k]
    if not t or t.startswith("▲"): continue
    m=re.match(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(（[^）]*）)?([^《]*)?(.*)$",t)
    if m: rows.append({"ch":m.group(1),"alt":(m.group(2) or "").strip("（）"),"py":(m.group(3) or "").strip(" 、，"),"text":t})
SM={"劃":"h「豁活」取「豁」：以刀劃開，界面豁然而分（推）。","嫿":"h「豁活」取「豁」：嫺靜而容色分明（推）。",
"繣":"h「豁活」取「豁」：結帶兩頭分張而豁（推）。","澅":"h「豁活」取「活」：水名，水流活活有聲（推）。",
"㗲":"h「豁活」取「豁」：叫呼聲豁然而出（推）。","㦎":"h「豁活」取「豁」：乖戾不屈，氣豁而不通（推）。",
"䐸":"h「豁活」取「豁」：曲膝後窩深陷如裂（推）。","㩇":"h「豁活」取「豁」：擗裂之聲豁然（推）。",
"𢄶":"h「豁活」取「豁」：裂帛之聲豁然（推）。","𨐶":"h「豁活」取「豁」：辛味刺口而氣豁（推）。",
"𥊮":"h「豁活」取「豁」：目病，睫間開豁（推）。"}
heads={"char":"畫","head":"畫","pinyin":"huà","level":1,"parent":None,"bus":[{"num":43,"name":"畫"}],
 "aliases":["畵","晝","𠚇","𡇍","𤰱","𤱪","𨽶","𦘕","𦘚","𤲯","𤲿"],
 "sections":[sec("benyi","本义",ps[381]),sec("zhuanyi","转义",ps[383]),sec("bianzheng","辩证",ps[384]),sec("yinyuan","音源",ps[385]),
   sec("shengmu","声母拟态","h「豁活」取「豁」：規畫圓界，分畫而豁然（推）。"),
   {"key":"zizu","label":"字族衍义","text":"","groups":[{"no":"①","title":"多指劃開、裂開","rows":[[r["ch"]+("（"+r["alt"]+"）" if r["alt"] else ""),r["py"],"刀／女／糸／水／口／心／肉／手／巾／辛／目",r["text"]] for r in rows]}]}]}
json.dump(heads,io.open(os.path.join(C,"畫.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    json.dump({"char":r["ch"],"head":r["ch"],"pinyin":r["py"],"level":3,"parent":"畫","bus":[{"num":43,"name":"畫"}],
      "aliases":[r["alt"]] if r["alt"] else [],
      "sections":[sec("shiyi","释义",r["text"]),sec("shengmu","声母拟态",SM.get(r["ch"],"（按今讀聲母取一面，推。）"))],"groups":[]},
      io.open(os.path.join(C,r["ch"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("畫 imgs",n,"fams",len(rows))