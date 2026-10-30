# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"𠣊":"l「拢离」取「离」：勉勵誘導，使離其懈怠（推）。",
"儢":"l「拢离」取「离」：心散離而不欲為（推）。",
"𢣿":"ch「刺持」取「刺」：憂思刺於心而不去（推）。",
"𧭜":"l「拢离」取「离」：詐言離實（推）。",
"濾":"l「拢离」取「离」：漉去渣滓，離析雜質（推）。",
"鑢":"l「拢离」取「离」：磋磨使之離其不平（推）。",
"爈":"l「拢离」取「离」：火燒山界，火勢離散及遠（推）。",
"櫖":"l「拢离」取「离」：藤蔓離披牽引（推）。",
"𥶌":"l「拢离」取「离」：篾席離析竹片而成（推）。",
"𡾅":"l「拢离」取「离」：山名，照實記音（推）。",
"攄":"sh「失收」取「收」：舒散而復收（推）。",
"𣀞":"l「拢离」取「离」：侵而離之（推）。",
"𥌠":"l「拢离」取「离」：目珠離光而視（推）。",
"𥖼":"l「拢离」取「离」：石名，照實記音（推）。",
"𦢛":"l「拢离」取「离」：傳語離口而下（推）。",
"𧓻":"l「拢离」取「离」：蟲名，照實記音（推）。",
"𤻱":"l「拢离」取「离」：痞結而氣離（推）。",
"𪇸":"l「拢离」取「离」：長頸分立如離（推）。",
"藘":"l「拢离」取「离」：莖刺離披，可染絳（推）。"}
n=0
for ch,txt in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("updated",n)