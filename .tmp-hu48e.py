# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; ip=os.path.join(G,"index.json")
d=json.load(io.open(ip,encoding="utf-8"))
chars=d.setdefault("chars",{}); photos=d.setdefault("photos",{})
def files(ch):
    p=os.path.join(G,ch); return sorted(ch+"/"+f for f in os.listdir(p))
chars["虍"]={"doc":"卷八 虎","files":files("虍")}
chars["虎"]={"doc":"卷八 虎","files":files("虎")}
photos["虍"]=["01.png","02.png"]
for k in ("虍","虎","glyphs"):
    if k in d and k not in ("chars","photos"): d.pop(k,None)
json.dump(d,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("虍",len(chars["虍"]["files"]),"虎",len(chars["虎"]["files"]),"photos",photos["虍"])