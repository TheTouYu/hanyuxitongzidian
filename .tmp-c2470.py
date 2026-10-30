# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"敊":"ch「刺持」取「持」：收而持之（推）。",
"洟":"t「涂突」取「突」：涕液突自鼻出（推）。",
"眱":"d「囤動」取「囤」：目聚視而囤（推）。",
"茮":"j「聚決」取「聚」：花椒結實聚簇（推）。",
"荑":"t「涂突」取「突」：茅草初生，芽突土而出（推）。",
"銕":"t「涂突」取「突」：鐵質堅突而硬（推）。",
"鮛":"sh「失收」取「收」：魚小而收聚成群（推）。",
"鮧":"t「涂突」取「突」：鮧魚首大突出（推）。",
"鴺":"t「涂突」取「突」：鳥突飛而起（推）。",
"𡧯":"j「聚決」取「聚」：無人聲則聲聚而寂（推）。",
"𢻃":"ch「刺持」取「刺」：支刺而止（推）。",
"𪀖":"q「親缺」取「缺」：禿鶖頂羽缺失（推）。",
}
for ch,s in M.items():
    p=C+"\\"+ch+".json"
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: print("miss",ch); continue
    for sec in d["sections"]:
        if sec["key"]=="shengmu": sec["text"]=s
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def mk(ch,py_,head,shiyi,sm):
    d={"char":ch,"head":head,"pinyin":py_,"level":3,"parent":"曳","bus":[{"num":26,"name":"弋"}],
       "sections":[{"key":"shiyi","label":"释义","text":shiyi,"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":sm,"cites":[]},
                   {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(d,io.open(C+"\\"+ch+".json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
mk("㡼","yì","㡼","㡼yì：曳族字（原稿族行所列，釋義未見於本段）。","y「零聲母」不系：零聲母，緒論七組未列（照實）。")
mk("𢂝","yì","𢂝","𢂝yì：曳族字（原稿族行所列，釋義未見於本段）。","y「零聲母」不系：零聲母，緒論七組未列（照實）。")
print("改12+补2")