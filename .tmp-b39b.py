# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); ps=[p.text.strip() for p in doc.paragraphs]
pat=re.compile("^([^\\sA-Za-z]+?)([A-Za-z\u00C0-\u024F\u0300-\u036F、，\\s]+)《")
def sec(k,l,t): return {"key":k,"label":l,"text":t}
rows={"①":[],"②":[],"③":[],"④":[]}; cur=None
for i in range(47,72):
    t=ps[i]
    if not t: continue
    if re.match("^[①②③④⑤]",t): cur=t[0]; continue
    m=pat.match(t)
    if m and cur:
        ch=m.group(1); py=re.sub(r"[、，\\s]+","、",m.group(2)).strip("、")
        rows[cur].append([ch,py,"",t])
LEI={"㴶":"水","𦞦":"肉","篧":"竹","榷":"木","䥃":"金","搉":"手","𣤇":"土","𢞕":"心","𦑱":"羽","傕":"人","𨢜":"酉","確":"石","㹊":"牛","雤":"鳥","䮤":"馬","㿥":"白","𤌍":"火","𣉒":"日","𥉑":"目","髉":"骨","蒮":"艸"}
for g in rows.values():
    for r in g: r[2]=LEI.get(r[0].split("（")[0],"")
beny=ps[32].split("：",1)[1]
zhuan="\n\n".join(ps[i].split("：",1)[1] for i in range(35,41))
bian="\n\n".join([ps[41].split("：",1)[1],ps[42],ps[43],ps[44]])
head={"c":"隺","head":"隺（寉鶴）","pinyin":"hè","lv":1,"bus":[{"num":39,"name":"隺"}],
 "sections":[sec("benyi","本义",beny),sec("zhuanyi","转义",zhuan),sec("bianzheng","辩证",bian),
  sec("yinyuan","音源",ps[45].split("：",1)[1]),
  sec("shengmu","声母拟态","h「豁活」取「豁」：鶴鳴高亮，其聲豁然而遠（推）。"),
  {"key":"zizu","label":"字族衍义","groups":[{"no":k,"title":"","rows":v} for k,v in rows.items() if v]},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]}
json.dump(head,io.open(os.path.join(C,"隺.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=1
for g in rows.values():
    for ch,py,lei,txt in g:
        base=ch.split("（")[0]; p=os.path.join(C,base+".json")
        if os.path.exists(p): continue
        d={"c":base,"head":ch,"pinyin":py,"lv":3,"parent":"隺","bus":[{"num":39,"name":"隺"}],
           "sections":[sec("shiyi","释义",txt),sec("shengmu","声母拟态","（按今读声母取擬態義一面，推。）"),
            {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]}
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("written",n,"rows",sum(len(v) for v in rows.values()))