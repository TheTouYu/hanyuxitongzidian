# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        try:
            d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
            if isinstance(d,dict): cards[d.get("char") or f[:-5]]=d
        except Exception: pass
n=0
for ch,d in list(cards.items()):
    pr=d.get("parent")
    if not pr or pr not in cards: continue
    pd=cards[pr]
    keep=[s for s in pd.get("sections",[]) if s.get("key") in ("benyi","zhuanyi","bianzheng","yinyuan") and s.get("text")]
    if not keep: continue
    b=pd.get("bus") or {}
    if isinstance(b,list): b=b[0] if b else {}
    lv={1:"一級字根",2:"二級字根"}.get(pd.get("level"),"谐声字")
    head="「"+str(pd.get("head") or pd.get("char") or pr)+"」 "+str(pd.get("pinyin") or "")+" · "+lv+(" · 第%s部 %s"%(b.get("num"),b.get("name")) if b.get("num") else "")
    gdir=os.path.join(G,pr); gs=sorted([x for x in os.listdir(gdir) if x.lower().endswith((".png",".jpg",".gif"))]) if os.path.isdir(gdir) else []
    gline="".join("{{gin:glyphs/%s/%s}}"%(pr,g) for g in gs[:12]) if gs else ""
    body="\n".join((s.get("label","")+"：" if s.get("label") else "")+str(s["text"]).lstrip("本義：本义：轉義：转义：辯證：辩证：音源：").strip() for s in keep)
    text=head+("\n"+gline if gline else "")+"\n"+body
    secs=[s for s in d.get("sections",[]) if not (s.get("key") in ("rootembed","zigen") and str(s.get("label","")).startswith("字根「"))]
    secs.append({"key":"rootembed","label":"字根「"+str(pd.get("char") or pr)+"」","text":text,"cites":[]})
    d["sections"]=secs
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("written",n)