# -*- coding: utf-8 -*-
import json,io,glob,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
BORROW=re.compile(r"(記音|记音|借聲|音譯|音译|聲記音|声记音)")
NAMEY=re.compile(r"[木艸草魚鱼金水鳥鸟山邑人名地]名") 
MAP=[("聚","聚合結總束集積"),("囤","堆積聚底根"),("续","連續接長流延"),
 ("消","消散盡亡終"),("隔","隔阻塞閉"),("亲","親近附貼"),("缺","缺少虧損"),
 ("豁","開張空通"),("活","流動生"),("刺","刺扎尖銳"),("持","持握執守"),
 ("分","分別離裂"),("附","依附貼近"),("动","動移行趨"),("突","突出穿"),
 ("纳","納入受"),("柔","柔軟弱"),("锐","銳利"),("凿","刻鑿"),("总","總合")]
PAIR={"祟":"zong","柰":"nai","款":"kuan","祡":"chai","示":"shi","士":"shi","家":"jia",
"𢑓":"shi","野":"ye","巵":"zhi","危":"wei","赦":"she","罘":"fu","貍":"li","稽":"ji","贛":"gan","亟":"ji","乞":"qi","欠":"qian","桀":"jie","㠯":"yi","里":"li","市":"shi"}
changed=0; bor=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    bus=d.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if not isinstance(num,int) or not(1<=num<=10): continue
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm: continue
    t=sm[0]["text"]
    if not ("取一面" in t or "待按字義定面" in t or "待按字义定面" in t): continue
    g=""
    for k in ("benyi","shiyi"):
        s0=[x for x in d["sections"] if x["key"]==k]
        if s0: g=(s0[0].get("text") or ""); break
    if BORROW.search(g) or NAMEY.search(g):
        sm[0]["text"]="聲旁只記音，不取義（原稿作「"+("名物記音" if NAMEY.search(g) else "借聲")+"」）。"; bor+=1
    else:
        face=None
        for fc,kws in MAP:
            if any(k in g for k in kws): face=fc; break
        if not face: face="取義待定"
        par=d.get("parent") or ""
        grp=PAIR.get(par,"x")
        sm[0]["text"]=f"{grp}組取「{face}」：{g[:24]}（推）。" if face!="取義待定" else f"聲旁不取義（原稿未明取義，{g[:20]}）。"
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); changed+=1
print("处理",changed,"其中借声",bor)