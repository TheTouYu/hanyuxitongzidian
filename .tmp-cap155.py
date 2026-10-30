# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"桀":"j「聚决」取「决」：兩足分張（舛）而立於木上，決然特立。",
"傑":"j「聚决」取「决」：才出眾而決然獨立。",
"杰":"j「聚决」取「决」：才出眾而決然獨立。",
"磔":"zh「凿总」取「凿」：分裂支解，如鑿之破物。",
"搩":"zh「凿总」取「凿」：以手擘裂如鑿。",
"謋":"h「豁活」取「豁」：骨肉分裂，豁然有聲。",
"𧤠":"zh「凿总」取「凿」：角破裂如鑿（推）。",
"榤":"j「聚决」取「决」：木架決然而立。",
"滐":"j「聚决」取「决」：水激而決。",
"嵥":"j「聚决」取「决」：山特立而決。",
"𡩣":"j「聚决」取「决」：屋高而決（推）。",
"𥠹":"j「聚决」取「决」：禾高出而決（推）。",
"𧎩":"j「聚决」取「决」：蟲特出而決（推）。",
"䮪":"ch「刺持」取「持」：馬名，形近借形，不取義（照實）。",
"𦵴":"ch「刺持」取「持」：形近乘之訛，不取義（照實）。",
"㻧":"ch「刺持」取「持」：形近朵之訛，不取義（照實）。",
"𠓲":"ch「刺持」取「持」：乘者持轡而坐。",
}
n=0
for p in os.listdir(C):
    if not p.endswith(".json") or p in ("index.json","variants.json"): continue
    ch=p[:-5]
    if ch not in M: continue
    d=json.load(io.open(os.path.join(C,p),encoding="utf-8")); secs=d["sections"]
    if any(s.get("key")=="shengmu" for s in secs):
        for s in secs:
            if s.get("key")=="shengmu": s["text"]=M[ch]
    else: secs.append({"key":"shengmu","label":"声母拟态","text":M[ch],"cites":[]})
    json.dump(d,io.open(os.path.join(C,p),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)