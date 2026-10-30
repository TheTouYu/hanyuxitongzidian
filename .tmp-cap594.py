# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
M={"鉃":("sh","失收","失","箭鏃一發即失，鋒利收於一點"),
"㞺":("z","凿总","凿","族之聚，如鏃之攢鑿"),
"𦳿":("c","刺持","持","鳥巢聚枝而持"),
"䂠":("sh","失收","失","石墮之聲如箭之逝"),
"𡱁":("sh","失收","失","排泄而去，如矢之失"),
"䐅":("x","续消","消","臀肉消軟"),
"薙":("t","涂突","突","除草如箭之突"),
"䉜":("zh","凿总","总","幼竹細直而攢聚"),
"䒨":("s","失收","收","蒿草收而可食"),
"𦱵":("sh","失收","失","草名，借聲記音"),
"笶":("sh","失收","失","俗「矢」字，借形記音"),
"䛈":("sh","失收","失","折箭為誓，失而後信"),
"雉":("zh","凿总","凿","雉羽斑斕如鏃之鑿"),
"䀢":("sh","失收","失","目瞬如箭之過"),
"垁":("zh","凿总","总","城堵聚土"),
"𩲶":("ch","刺持","刺","鬼魅刺人"),
"𢇻":("zh","凿总","凿","古「知」字，報靶之聲"),
"聅":("ch","刺持","刺","以箭貫耳，刺而入"),
"𩶇":("sh","失收","失","大魚之謂，借聲記音"),
"𡧦":("h","豁活","活","衡橫而平，如橫木之活"),
"𥎪":("sh","失收","失","詞之所之如矢"),
"𥎭":("d","囤动","囤","短小囤聚")}
n=0
for ch,(ini,grp,face,why) in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shengmu": s["text"]=f"{ini}「{grp}」取「{face}」：{why}（推）。"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
capj=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=capj.get("captions") or capj
for k,ch,cap in ((56,"薙","辛夷花"),(66,"雉","野雞")):
    rid=None
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try:
                    if len(parts[v].blob)>3000: rid=v
                except KeyError: pass
    if not rid: print("noimg",ch); continue
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    os.makedirs(os.path.join(P,ch),exist_ok=True)
    fn="01"+ext; open(os.path.join(P,ch,fn),"wb").write(b)
    ph[ch]=[fn]; cm[ch]=[cap]
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("声母改",n,"图",[(c,ph.get(c)) for c in ("薙","雉")])