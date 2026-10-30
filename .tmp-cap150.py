# -*- coding: utf-8 -*-
import json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"欠":"q「亲缺」取「缺」：張口氣出，體乏而缺。",
"歖":"x「续消」取「续」：笑聲續而消。",
"吹":"ch「刺持」取「持」：撮口持氣而吹。",
"炊":"ch「刺持」取「持」：持火蒸飯。",
"䶴":"ch「刺持」取「持」：持管吹樂。",
"欹":"q「亲缺」取「缺」：器偏斜而缺。",
"坎":"k「口控」取「控」：地有坎而控水。",
"肷":"q「亲缺」取「缺」：牛馬脊後肉少而缺。",
"杴":"x「续消」取「续」：鍬入土續而消。",
"歉":"q「亲缺」取「缺」：食不飽而缺。",
"芡":"q「亲缺」取「缺」：芡實外殼有刺而缺（推）。",
"缼":"q「亲缺」取「缺」：器缺。",
"贛":"g「隔估」取「隔」：蚌以殼隔水自護（推）。",
"戇":"zh「凿总」取「凿」：愚戇如鑿不通。",
"䀍":"k「口控」取「控」：目控而視。",
"㔶":"g「隔估」取「隔」：小杯隔而分飲（推）。",
"扻":"zh「凿总」取「凿」：手擊如鑿。",
"癡":"ch「刺持」取「持」：痴呆持而不化。",
"擬":"n「纳弄」取「纳」：擬議納定。",
"凝":"n「纳弄」取「纳」：氣納而凝。",
"儗":"n「纳弄」取「纳」：比擬相納。",
"薿":"n「纳弄」取「纳」：草茂相納。",
"𥣖":"n「纳弄」取「纳」：禾聚相納（推）。",
"𦡸":"n「纳弄」取「纳」：肉聚相納（推）。",
"㘈":"y 零聲母，緒論七組未列，不系（照實）。",
"𠏤":"g「隔估」取「隔」：器隔而藏（推）。",
"竷":"k「口控」取「控」：鼓聲控而節（推）。",
}
ZERO=re.compile(r"^[aāáǎàeēéěèoōóǒòw]")
n=0; z=0
for p in glob.glob(C+r"\*.json"):
    if "index" in p or "variants" in p: continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    b=d.get("bus") or []
    num=b[0].get("num") if isinstance(b,list) and b and isinstance(b[0],dict) else None
    if num!=5: continue
    ch=d["char"]; py_=(d.get("pinyin") or "").strip()
    txt=M.get(ch)
    if not txt and py_ and ZERO.match(py_):
        txt="零聲母（今讀 "+py_+"），緒論七組未列，不系（照實）。"; z+=1
    if not txt: continue
    secs=d["sections"]
    if any(s.get("key")=="shengmu" for s in secs):
        for s in secs:
            if s.get("key")=="shengmu": s["text"]=txt
    else: secs.append({"key":"shengmu","label":"声母拟态","text":txt,"cites":[]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n,"其中零声母",z)