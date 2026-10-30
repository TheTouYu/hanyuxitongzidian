import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\𠈐.json"; d=json.load(io.open(p,encoding="utf-8"))
t=""
for s in d["sections"]:
    if s["key"] in ("shiyi","benyi") and s.get("text"): t=s["text"]; break
ez=""
for s in d["sections"]:
    if s["key"]=="ezhi" and s.get("text"): ez=s["text"]; break
d={"char":"𠈐","head":d.get("head","𠈐"),"pinyin":d.get("pinyin",""),"noRoot":True,"bus":d.get("bus") or [],
 "sections":[{"key":"shiyi","label":"释义","text":t,"cites":[]},
  {"key":"ezhi","label":"讹字说明","text":ez or "原文字族衍義所列为形近之訛。","cites":[]}]}
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("ok",t[:20])