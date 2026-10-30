# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
GRP={"b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐",
     "z":"凿总","zh":"凿总","c":"刺持","ch":"刺持","s":"失收","sh":"失收","j":"聚决","q":"亲缺","x":"续消",
     "g":"隔估","k":"口控","h":"豁活"}
def ini(py):
    py=(py or "").strip().lower()
    m=re.match(r"([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",py)
    if not m: return None
    s=m.group(1)
    for two in ("zh","ch","sh"):
        if s.startswith(two): return two
    c=s[0]
    return c if c in "bpmfdtnlgkhjqxrzcsyw" else None
A=re.compile(r"^[聲声]母(?:義|义)?[：:]\s*(?:[聲声]母)?\s*([a-z]{1,2})\s*[（(]\s*擬態[「\"](.+?)[」\"]\s*[)）]\s*[，,]\s*取[「\"](.+?)[」\"]\s*[：:]?\s*(.*)$",re.S)
n=0; left=[]
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    chg=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=(s.get("text") or "").strip()
        if not t or ("「" in t and "」取「" in t): continue
        if t.startswith("零聲母") or t.startswith("零声母"): continue
        m=A.match(t)
        if m:
            s["text"]=f"{m.group(1)}「{m.group(2)}」取「{m.group(3)}」：{m.group(4).strip()}"; chg=True; continue
        i=ini(d.get("pinyin"))
        fm=re.search(r"取[「\"]([^」\"]{1,6})[」\"]",t)
        if i and i in GRP and fm:
            s["text"]=f"{i}「{GRP[i]}」取「{fm.group(1)}」：{t}"; chg=True; continue
        if ("不系" in t) or t.startswith("喻母"):
            s["text"]="零聲母，绪论七组未列，不系（照實）"; chg=True; continue
        left.append((ch,t[:24]))
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("再规范",n,"剩余",len(left),left[:6])