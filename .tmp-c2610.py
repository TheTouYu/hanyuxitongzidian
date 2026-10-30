import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"督":"d「囤動」取「動」：督之而動（推）。","惄":"n「納弄」取「納」：飢而思食，納念於心（推）。",
"錖":"d「囤動」取「囤」：皮帶扣囤束而固（推）。","𦵦":"d「囤動」取「囤」：草旱盡而光禿囤露（推）。",
"菽":"sh「失收」取「收」：豆熟而收其實（推）。","𤬂":"d「囤動」取「囤」：瓠圓而囤（推）。",
"椒":"j「聚決」取「聚」：椒實聚生成房（推）。"}
for ch,s in M.items():
    p=C+"\\"+ch+".json"; d=json.load(io.open(p,encoding="utf-8"))
    for sec in d["sections"]:
        if sec["key"]=="shengmu": sec["text"]=s
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")