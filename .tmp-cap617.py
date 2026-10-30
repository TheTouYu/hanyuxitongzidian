# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
pat=re.compile(r'<img class="gin" src="([^"]+)" alt="字形">')
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=False
    for s in d.get("sections",[]):
        if isinstance(s,dict) and isinstance(s.get("text"),str) and '<img class="gin"' in s["text"]:
            s["text"]=pat.sub(lambda m:"{{gin:"+m.group(1)+"}}",s["text"]); ch=True
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("转标记",n)
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace(".replace(/&lt;img class=&quot;gin&quot; src=&quot;([^&]*)&quot; alt=&quot;字形&quot;&gt;/g,'<img class=\"gin\" src=\"$1\" alt=\"字形\">')",
                ".replace(/\\{\\{gin:([^}]+)\\}\\}/g,'<img class=\"gin\" src=\"$1\" alt=\"字形\">')")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"renderer ok")