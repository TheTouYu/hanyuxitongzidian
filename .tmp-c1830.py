# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"配.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        s["text"]="字族衍義："
        s["groups"]=[{"title":"字族衍義：未形成字族","note":"","rows":[
            ["嶏（圮）","pèi","屵","《說文》：「崩聲。从屵配聲。讀若費。」崩塌的聲音。pǐ，《玉篇》：「毀也。或作圮。」"],
            ["蓜","pèi","艸","義未詳。疑指茅草，古祭神時用以宿酒。"]]}]
d.pop("photos",None); d.pop("captions",None)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
P=r"D:\系统汉字\web\public\glyphs\photos"
ip=os.path.join(P,"index.json"); ph=json.load(io.open(ip,encoding="utf-8"))["photos"]
ph.pop("配",None)
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
dd=os.path.join(P,"配")
if os.path.isdir(dd):
    for f in os.listdir(dd): os.remove(os.path.join(dd,f))
    os.rmdir(dd)
print("配：两字成组、插图清除")