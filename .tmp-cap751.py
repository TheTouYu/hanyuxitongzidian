# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
rows1=[["薹","tái","艸","《集韻》「堂來切，音台。芸薹，菜名」「草名，夫須也」；薹菜即油菜，或薹草即夫須"],
["籉","tái","竹","《集韻》「笠子，可禦雨」；斗笠，戴在頭上如高臺"],
["檯","tái","木","《玉篇》「木名」；今指桌子、几案"],
["擡","tái","手","《博雅》「擡揌，動也」；《廣韻》「擡，舉也」"],
["𤗿","tǎi","片","《集韻》「吳人謂逆剡木曰𤗿」；从下往上削木頭"],
["𧭏","tāi","言","《集韻》「諟也」；訂正，即在文章擡頭空白處書寫"]]
rows2=[["𩦽（駘）","tái","馬","《字彙補》「與駘同」；馬不進"],
["儓","tái","人","《韻會》「陪儓，臣也」；《廣雅》「醜也」「當也」"],
["㘆","tǎi","口","《玉篇》「㘆𠷂，言不正」；《集韻》「言舛也」"],
["𤐽（炱）","tái","火","《字海》「同炱」；煙氣凝積而成的黑灰"],
["懛","dāi","心","《廣韻》「懛剴，失志皃」；同「呆」，癡呆笨拙"],
["𪒴","tái","黑","《玉篇》「黑也」；《廣韻》「𪑚𒒴，大黑之皃」"],
["嬯","tái","女","《說文》「遲鈍也。从女臺聲」；《玉篇》「鈍劣也」"]]
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
def strip(t):
    for q in ("本義：","轉義：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
z={"char":"臺","head":"臺（台坮㙵䑓㙜𡋛𦤼𡌫𡎲𡐉𡔼𡌬）","pinyin":"tái","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],"rootLevel":2,
"aliases":["台","坮","㙵"],"sections":[
 {"key":"benyi","label":"本义","text":strip(ps[244]),"cites":[]},
 {"key":"zhuanyi","label":"转义","text":strip(ps[247])+strip(ps[248]),"cites":[]},
 {"key":"yinyuan","label":"音源","text":strip(ps[249]),"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"t「涂突」取「突」：築土高起而突出於平地（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"原文分兩組：","cites":[],
  "groups":[{"title":"①指臺形，表示高平之物","note":"","rows":rows1},{"title":"②指臺狀，表示僵挺、木然的樣子","note":"","rows":rows2}]},
 VOL]}
json.dump(z,io.open(os.path.join(C,"臺.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
M={"薹":"t「涂突」取「突」：莖高抽薹突出（推）。","籉":"t「涂突」取「突」：笠如高臺突出頭上（推）。",
"檯":"t「涂突」取「突」：几案高平如臺（推）。","擡":"t「涂突」取「突」：舉物而突出（推）。",
"𤗿":"t「涂突」取「突」：逆削而突起（推）。","𧭏":"t「涂突」取「突」：於擡頭空白突起而書（推）。",
"𩦽":"d「囤动」取「囤」：馬不進而囤（推）。","儓":"t「涂突」取「突」：陪儓而突立（推）。",
"㘆":"t「涂突」取「突」：言不正而突（推）。","𤐽":"t「涂突」取「突」：煙炱突積（推）。",
"懛":"d「囤动」取「囤」：失志而囤然（推）。","𪒴":"t「涂突」取「突」：黑而突現（推）。",
"嬯":"t「涂突」取「突」：遲鈍而突（推）。"}
n=0
for r in rows1+rows2:
    ch=r[0]; base=ch.split("（")[0]; par=ch[len(base)+1:-1] if "（" in ch else ""
    d={"char":base,"head":ch,"pinyin":r[1],"level":3,"parent":"臺","bus":[{"num":16,"name":"矢"}],
       "aliases":list(par) if par else [],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
         {"key":"shengmu","label":"声母拟态","text":M[base],"cites":[]},VOL]}
    json.dump(d,io.open(os.path.join(C,base+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# 插图：p245 图，注 p246
rid=None
for k in range(243,248):
    for el in ps[k] and doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if (a.endswith("}embed") or a.endswith("}id")):
                try:
                    if len(parts[v].blob)>30000: rid=v
                except KeyError: pass
if rid:
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,"臺"); os.makedirs(D,exist_ok=True); fn="01"+ext
    open(os.path.join(D,fn),"wb").write(b)
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
    ph["臺"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["臺"]=["河南登封的觀星臺（元）"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("臺卡+族",n,"图",bool(rid))