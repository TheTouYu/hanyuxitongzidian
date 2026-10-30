# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
new=[("𨍀","𨍀（輊）","zhì","𨍀（輊）zhì《五音篇海》：『與輊同』。車前重。","zh「凿总」取「凿」：車前重而鑿然下（推）。",["輊"]),
("箌","箌（罩䈇）","zhào","箌（罩䈇）zhào《集韻》：『罩，捕魚器，或作箌』。《正字通》：『同䈇』。捕魚的竹籠。","zh「凿总」取「凿」：竹籠鑿口以取魚（推）。",["罩","䈇"])]
for base,head,py_,txt,sm,al in new:
    d={"char":base,"head":head,"pinyin":py_,"level":3,"parent":"到","bus":[{"num":16,"name":"矢"}],"aliases":al,
       "sections":[{"key":"shiyi","label":"释义","text":txt,"cites":[]},
         {"key":"shengmu","label":"声母拟态","text":sm,"cites":[]},VOL]}
    json.dump(d,io.open(os.path.join(C,base+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=os.path.join(C,"到.json"); z=json.load(io.open(p,encoding="utf-8"))
for s in z["sections"]:
    if s["key"]=="zizu":
        rows=s["groups"][0]["rows"]
        if not any(r[0].startswith("𨍀") for r in rows):
            rows.append(["𨍀（輊）","zhì","車","《五音篇海》「與輊同」；車前重"])
            rows.append(["箌（罩䈇）","zhào","竹","《集韻》「罩，捕魚器，或作箌」；《正字通》「同䈇」"])
json.dump(z,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("补 𨍀/箌，到表行",len(rows))