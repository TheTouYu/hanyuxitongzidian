# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\㿣.json"
d=json.load(io.open(p,encoding="utf-8"))
sec=[s for s in d["sections"]]
have={s["key"] for s in sec}
def add(k,l,t):
    if k not in have: sec.insert(0,{"key":k,"label":l,"text":t,"cites":[]})
add("benyi","本义","《玉篇》：「皏㿣，白也。又淺薄色也。」（原文只此一句，㿣與皏連用，不單見）")
for s in sec:
    if s["key"]=="shengmu":
        s["text"]="原稿「㿣」只出现在「皏㿣」复合词中，无单字训释与单读，聲母擬態不系（照實）。"
d["sections"]=sec
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")