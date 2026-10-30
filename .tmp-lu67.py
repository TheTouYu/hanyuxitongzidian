# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"墟":"x「续消」取「消」：故丘已墟，形迹消盡（推）。",
"噓":"x「续消」取「消」：張口緩緩出氣，氣續而消（推）。",
"魖":"x「续消」取「消」：耗神耗物，使財物消盡（推）。",
"歔":"x「续消」取「消」：抽泣出氣，氣斷續而消（推）。",
"譃":"x「续消」取「消」：虛言吹噓，實處消盡（推）。",
"憈":"q「亲缺」取「缺」：志氣怯缺，心中空虛（推）。",
"𡃧":"x「续消」取「消」：謷言虛張，聲出而消（推）。",
"𤮆":"x「续消」取「消」：缶器中空，虛而能受（推）。",
"𧇺":"h「豁活」取「豁」：火勢豁然而起（推）。",
"驉":"x「续消」取「消」：駏驉似騾，行遠而力消（推）。",
"㠊":"q「亲缺」取「缺」：山勢崎嶇多缺（推）。",
"鱋":"q「亲缺」取「缺」：比目兩眼同側，形缺而相並（推）。",
"覷":"q「亲缺」取「缺」：眯眼從細縫窺看（推）。",
"𥕰":"x「续消」取「消」：石形消剝成皃（推）。",
"戱":"x「续消」取「消」：戲謔之言，隨口而消（推）。",
"𤂴":"x「续消」取「消」：水名，水流消長（推）。",
"㩬":"x「续消」取「消」：擊而使之消散（推）。",
"𢴮":"q「亲缺」取「缺」：擊打使缺口（推）。",
"𣚛":"q「亲缺」取「缺」：鐘磬之柎，兩柱相缺而立（推）。",
"𧝔":"q「亲缺」取「缺」：繫結使不缺（推）。"}
n=0
for ch,txt in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("updated",n)