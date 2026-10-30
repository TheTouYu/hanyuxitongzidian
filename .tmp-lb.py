# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"本義":"本义","轉義":"转义","辯證":"辩证","聲母擬態":"声母拟态","字族衍義":"字族衍义","所屬卷":"所属卷","釋義":"释义","字族衍义":"字族衍义"}
names=["彥"]+["顏","𪃛","遃","𨂪","楌","嵃","㘖","喭","諺","齴","偐","𩜽","𧱱"]
for n in names:
    p=os.path.join(C,n+".json")
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("label") in M: s["label"]=M[s["label"]]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("normalized",len(names))