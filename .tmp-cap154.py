# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"乞":"q「亲缺」取「缺」：氣缺於內而開口求於外。",
"气":"q「亲缺」取「缺」：天地間之氣，虛而若缺，故屈曲以象流動。",
"氣":"q「亲缺」取「缺」：氣本虛而若缺，故从气。",
"汽":"q「亲缺」取「缺」：水蒸為氣，散而若缺。",
"炁":"q「亲缺」取「缺」：火氣上行，虛而若缺（推）。",
"迄":"q「亲缺」取「缺」：行至而止，前路缺而後至。",
"忔":"q「亲缺」取「缺」：心中不足而缺（推）。",
"忥":"x「续消」取「续」：氣息續而不絕。",
"愾":"x「续消」取「续」：太息連續，氣續而後消（推）。",
"嘅":"k「口控」取「控」：嘆息出口，口控其聲。",
"慨":"k「口控」取「控」：慨歎出口，口控而後放（推）。",
"極":"j「聚决」取「聚」：屋脊聚木於頂而至極。",
"极":"j「聚决」取「聚」：驢上負版，木聚而載（推）。",
"殛":"j「聚决」取「聚」：誅戮聚而加身（推）。",
"亟":"j「聚决」取「聚」：急則事聚於一時。",
"旡":"j「聚决」取「聚」：打嗝氣聚而上逆。",
"旣":"j「聚决」取「聚」：食畢氣聚而盡。",
"暨":"j「聚决」取「聚」：日既聚而及（推）。",
"概":"g「隔估」取「隔」：平斗斛之木，隔定其量。",
"溉":"g「隔估」取「隔」：引水灌田，水隔畦而行。",
"摡":"g「隔估」取「隔」：拭滌去垢，隔而後淨（推）。",
"犵":"g「隔估」取「隔」：獠人異族，隔而不通（推）。",
"扢":"g「隔估」取「隔」：摩拭去垢，隔而後明（推）。",
"盵":"q「亲缺」取「缺」：望而氣缺（推）。",
"黖":"x「续消」取「续」：物黑而氣續（推）。",
"鎎":"x「续消」取「续」：金氣續而消（推）。",
"刏":"j「聚决」取「决」：刀決而傷。",
"㰟":"j「聚决」取「决」：冀望而決（推）。",
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