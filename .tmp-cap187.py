# -*- coding: utf-8 -*-
import json,io,os,re,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
FACES={"续消":("续","消"),"亲缺":("亲","缺"),"聚决":("聚","决"),"隔估":("隔","估"),
"口控":("口","控"),"豁活":("豁","活"),"凿总":("凿","总"),"拢离":("拢","离"),
"附分":("附","分"),"闭剥":("闭","剥"),"拼辟":("拼","辟"),"蒙末":("蒙","末"),
"囤动":("囤","动"),"涂突":("涂","突"),"纳弄":("纳","弄"),"柔锐":("柔","锐"),
"刺持":("刺","持"),"失收":("失","收")}
KW={ # face -> keywords
"聚":"聚合結總束集積匯","决":"決裂破解斷","续":"連續接長流延絲繩","消":"消散盡亡終滅失",
"亲":"親近附貼昵","缺":"缺少不滿虧損","隔":"隔阻塞閉界","估":"估度量",
"口":"口張說言","控":"控制引節","豁":"開張空通廣","活":"流動生",
"凿":"刺尖銳入刻","总":"總合聚","拢":"攏收聚","离":"離散別",
"附":"依附貼近","分":"分別離裂","闭":"閉合關","剥":"剝落脫","拼":"拼並合",
"辟":"開闢張","蒙":"蒙覆蔽","末":"末梢盡","囤":"囤積聚","动":"動移行",
"涂":"塗漫布","突":"突出穿","纳":"納入受","弄":"弄玩把","柔":"柔軟弱","锐":"銳利尖",
"刺":"刺扎尖銳","持":"持握執守","失":"失亡逸","收":"收斂束","活":"流動生"}
PHR={"续":"相連不斷","消":"漸散而盡","聚":"總聚於一","决":"決然而分","隔":"相隔而分","估":"度其大小",
"口":"張口而出","控":"受控而節","豁":"豁然開張","活":"流動而生","凿":"如鑿之入","总":"總合於一",
"拢":"收攏而聚","离":"離散而分","附":"依附而近","分":"分判而別","闭":"封閉不開","剥":"剝落而解",
"拼":"拼合而並","辟":"開闢而張","蒙":"蒙覆在上","末":"末梢之盡","囤":"囤積而聚","动":"動而後移",
"涂":"塗布而漫","突":"突入而出","纳":"納入而收","弄":"把弄而把玩","柔":"柔軟可曲","锐":"銳利可入",
"刺":"刺入而傷","持":"持守不放","失":"失而不守","收":"收而後止","亲":"相親而近","缺":"缺而不完"}
n=0; samples=[]
for f in glob.glob(C+r"\*.json"):
    if "index" in f or "variants" in f: continue
    d=json.load(io.open(f,encoding="utf-8"))
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm or "取一面" not in (sm[0].get("text") or ""): continue
    old=sm[0]["text"]
    m=re.search(r"「(.{2})」",old) or re.search(r"取一面",old)
    pair=m.group(1) if m and m.lastindex else ""
    faces=FACES.get(pair)
    gloss=""
    for k in ("benyi","shiyi"):
        s0=[s for s in d["sections"] if s.get("key")==k]
        if s0: gloss=(s0[0].get("text") or "").strip(); break
    gloss=re.sub(r"^[^：:]*[：:]","",gloss)[:40]
    gloss=re.sub(r"（推）$","",gloss)
    face=None
    if faces:
        for fc in faces:
            if any(ch in gloss for ch in KW.get(fc,"")): face=fc; break
    if not face: face=faces[0] if faces else ""
    pre=re.match(r"^\s*([A-Za-z])",old)
    ini=pre.group(1) if pre else (d.get("pinyin") or "x")[:1]
    txt=f"{ini}「{pair}」取「{face}」：{gloss}，{PHR.get(face,'')}（推）。"
    sm[0]["text"]=txt
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    if len(samples)<8: samples.append(d["char"]+" → "+txt)
print("改",n)
for s in samples: print("  ",s)