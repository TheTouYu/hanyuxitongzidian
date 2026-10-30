# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
ps=json.load(io.open(r"D:\系统汉字\.tmp-ps.json",encoding="utf-8"))["ps"]
gf=json.load(io.open(r"D:\系统汉字\.tmp-gf.json",encoding="utf-8"))
PY=re.compile(r"([a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜê\u00e0-\u01ff]{1,12}(?:、[a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]{1,12})*)")
def clean(t): return re.sub(r"^(本義|轉義|辯證|音源|字族衍義)[：:]","",t).strip()
def row(ch):
    for t in ps:
        if t.startswith(ch) and len(t)>len(ch)+3: return t
    return ""
def py_of(t,ch):
    m=PY.search(t[len(ch):]) if t.startswith(ch) else None
    return m.group(1) if m else ""
def card(ch,head,pinyin,level,parent,sections,aliases=None):
    d={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,
       "bus":[{"num":45,"name":"石"}],"sections":sections}
    if aliases: d["aliases"]=aliases
    if ch in gf["橐"] or (ch=="庶"): pass
    fl=(gf["橐"]|gf["庶"]).get(ch)
    if fl: d["glyphs"]=fl
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    return d
shujuan={"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第45部 石）","links":[{"ch":"卷七斤","label":"卷七 斤"}]}
# 橐
tuo_rows=[("𣟄","木"),("驝","馬"),("蠹","虫")]
rows=[]
for ch,lei in tuo_rows:
    t=clean(row(ch)); rows.append([ch,py_of(row(ch),ch),lei,t])
card("橐","橐（槖𢅇𡇈）","tuó",2,"石",[
 {"key":"benyi","label":"本义","text":clean(ps[238]),"cites":[]},
 {"key":"zhuanyi","label":"转义","text":clean(ps[240])+"\n"+clean(ps[241]),"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"t「涂突」取「突」：中空之木，擊之突突有聲（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"①指橐的鼓起 ②指橐的中空","groups":[{"no":"①","title":"指橐的鼓起","rows":rows[:2]},{"no":"②","title":"指橐的中空","rows":rows[2:]}]},
 shujuan],aliases=["槖","𢅍","𡇈"])
# 庶
g1=[("遮","辵"),("嗻","口"),("蹠","足"),("謶","言"),("嫬","女"),("𠌮","人"),("墌","土"),("㵂","水"),("䭖","食"),("𡻠","山"),("㫂","斤"),("蟅","虫")]
g2=[("蔗","艸"),("鷓","鳥"),("樜","木"),("熫","火")]
g3=[("摭","手"),("𤳯","匚")]
def mk(lst): return [[ch,py_of(row(ch),ch),lei,clean(row(ch))] for ch,lei in lst]
card("庶","庶（𢉙）","shù",2,"石",[
 {"key":"benyi","label":"本义","text":clean(ps[249]),"cites":[]},
 {"key":"zhuanyi","label":"转义","text":"\n".join(clean(ps[k]) for k in (251,252,253,254)),"cites":[]},
 {"key":"bianzheng","label":"辩证","text":"\n".join(clean(ps[k]) for k in range(255,260)),"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「收」：燒紅之石，收聚而煨煮（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"①指遮蓋、眾多 ②指石頭燒紅時的紅褐色 ③指煮後的揀拾石頭","groups":[{"no":"①","title":"指遮蓋、眾多","rows":mk(g1)},{"no":"②","title":"指石頭燒紅時的紅褐色","rows":mk(g2)},{"no":"③","title":"指煮後的揀拾石頭","rows":mk(g3)}]},
 shujuan],aliases=["𢉙"])
# 族卡
allrows=[(c,l) for c,l in tuo_rows+g1+g2+g3]
for ch,lei in allrows:
    t=clean(row(ch))
    card(ch,ch,py_of(row(ch),ch),3,("橐" if ch in ("𣟄","驝","蠹") else "庶"),[
     {"key":"shiyi","label":"释义","text":t,"cites":[]},
     {"key":"shengmu","label":"声母拟态","text":"（所屬部之聲母擬態取面，見本部部頭。推）","cites":[]},
     shujuan])
print("cards done",len(allrows)+2)