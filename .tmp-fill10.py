# -*- coding: utf-8 -*-
import json,io,glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for f in glob.glob(C+r"\*.json"):
    b=os.path.basename(f)
    if b in ("index.json","variants.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except: continue
    if isinstance(d,dict) and d.get("char"): cards[d["char"]]=d
MIME={"b":"闭剥","p":"拼辟","m":"蒙末","f":"附分","d":"囤动","t":"涂突","n":"纳弄","l":"拢离",
"g":"隔估","k":"口控","h":"豁活","j":"聚决","q":"亲缺","x":"续消","zh":"凿总","ch":"刺持",
"sh":"失收","r":"柔锐","z":"凿总","c":"刺持","s":"失收","y":"","w":""}
def ini(py_):
    s=(py_ or "").lower()
    for k in ("zh","ch","sh"):
        if s.startswith(k): return k
    c=s[:1]
    return c if c.isalpha() else ""
missing={}
for ch,d in list(cards.items()):
    bus=d.get("bus"); bnum=bname=0,None
    if isinstance(bus,list) and bus and isinstance(bus[0],dict): bnum=bnum if False else bus[0].get("num",0); bname=bus[0].get("name","")
    vol=None
    for s in d.get("sections",[]):
        if s.get("links"):
            vol=s["links"][0] if isinstance(s["links"][0],dict) else {"ch":s["links"][0]}
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in (g.get("rows") or []):
                if not isinstance(r,list) or not r: continue
                c0=re.sub(r"（.*?）|\(.*?\)","",str(r[0])).strip()
                if len(c0)!=1 or c0 in cards or c0 in missing: continue
                missing[c0]={"py":str(r[1] or ""),"cls":str(r[2] or ""),"gloss":str(r[3] or ""),
                             "root":ch,"num":bus[0].get("num",0) if isinstance(bus,list) and bus and isinstance(bus[0],dict) else 0,
                             "name":bus[0].get("name","") if isinstance(bus,list) and bus and isinstance(bus[0],dict) else "","vol":vol}
print("missing",len(missing))
open(r"D:\系统汉字\.tmp-missing.json","w",encoding="utf-8").write(json.dumps(missing,ensure_ascii=False,indent=0))
n=0
for ch,m in missing.items():
    i=ini(m["py"]); mn=MIME.get(i,"")
    sm=(f"{i}「{mn}」取一面："+("零聲母不系" if not mn else "與本義相協（推）。"))
    secs=[{"key":"shiyi","label":"释义","text":f"{ch}，{m['py']}：{m['gloss']}（原稿字族表摘要）","cites":[]},
          {"key":"shengmu","label":"声母拟态","text":sm,"cites":[]}]
    if m["vol"]: secs.append({"key":"suoshu","label":"所属卷","text":"","cites":[],"links":[m["vol"]]})
    d={"char":ch,"trad":ch,"simp":ch,"pinyin":m["py"],"level":3,"parent":m["root"],
       "bus":[{"num":m["num"],"name":m["name"]}],"sections":secs}
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("created",n)