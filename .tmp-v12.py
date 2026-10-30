# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for fp in glob.glob(C+r"\*.json"):
    if fp.endswith("index.json") or fp.endswith("variants.json"): continue
    d=json.load(io.open(fp,encoding="utf-8")); ch=False
    for s in d.get("sections",[]):
        if s.get("key")=="juan" and s.get("text"):
            s["text"]=""; ch=True
    if ch:
        json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cleared text on",n,"cards")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    old="<p>${esc(s.text)}</p>"
    new="${s.text?'<p>'+esc(s.text)+'</p>':''}"
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("renderer patched",f)