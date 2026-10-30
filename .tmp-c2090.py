# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
P=os.path.join(C,"睪.json"); d=json.load(io.open(P,encoding="utf-8"))
lei={"𢍰":"廾","釋":"釆","𥼶":"米","澤":"水","𤑹":"示","擇":"手","醳":"酉","䁺":"目","鸅":"鳥","繹":"糸","譯":"言","驛":"馬","圛":"囗","嶧":"山","襗":"衣","𩏪":"韋","鐸":"金","墿":"土","𥜃":"示","𦔥":"耒","䕪":"艸","凙":"冫","殬":"歹","懌":"心","𩍜":"革","斁":"攴","蘀":"艸","蠌":"虫","燡":"火","㘁":"口","䐾":"肉","籜":"竹","檡":"木","皋":"白"}
Z="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
sm={"釋":"sh「失收」取「收」：分別米與糠而收之（推）。","𥼶":"sh「失收」取「收」：淘米收其淨（推）。","澤":"z「凿总」取「总」：水聚而總為澤（推）。","擇":"z「凿总」取「凿」：揀選如鑿別（推）。","鸅":"z「凿总」取「总」：囊總收魚水（推）。","繹":"y「零聲母」取「總」：抽絲總聚（推）。" if False else Z}
pat=re.compile(r"^([^\sa-zA-Z（(]+)")
out=[]
for g in d["sections"]:
    if g["key"]!="zizu": continue
    for grp in g["groups"]:
        for r in grp["rows"]:
            m=re.match(r"^([^\s（(]{1,3}?)(（[^）]*）)?([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、]+)",r[3])
            ch=m.group(1) if m else r[0]
            py_=m.group(3).split("、")[0] if m else r[1]
            out.append((ch,py_,r[3]))
        grp["rows"]=[[c,p,lei.get(c,""),t] for c,p,t in [(o[0],o[1],o[2]) for o in out if True]][-len(grp["rows"]):] if False else grp["rows"]
# 重写所有 rows 为干净四列
idx=0
for g in d["sections"]:
    if g["key"]!="zizu": continue
    for grp in g["groups"]:
        new=[]
        for r in grp["rows"]:
            ch,py_,t=out[idx]; idx+=1
            new.append([ch,py_,lei.get(ch,""),t])
        grp["rows"]=new
json.dump(d,io.open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for ch,py_,t in out:
    p=os.path.join(C,ch+".json")
    card={"char":ch,"trad":ch,"pinyin":py_,"level":3,"parent":"睪","bus":[{"num":25,"name":"睪"}],
      "sections":[{"key":"shiyi","label":"释义","text":t,"cites":[]},
                  {"key":"shengmu","label":"声母拟态","text":sm.get(ch,Z),"cites":[]},
                  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷三矢","label":"卷三 矢"}],"cites":[]}]}
    json.dump(card,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("rows",len(out),"cards",n)