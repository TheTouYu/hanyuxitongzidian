# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; CM=r"D:\系统汉字\.tmp-charmap.json"
cm=json.load(io.open(CM,encoding="utf-8"))
row="斤：釿斫（眲）斲（𦘣）斮匠𪀘庍（㾙𦜓廳）頎斱（斫𣃑）赾䞪祈（䃽𣄨）劤（勁）蚚齗（齴）听（聽）妡靳䓄旂𧞐（𧞗）馸䖐㹞（齗啀）忻昕訢𪛊（䇵𥭦）沂圻（垠畿崎碕）盺炘（焮）峾近（𣥍）垽伒𪏴邤菦芹"
row=row.split("：",1)[1]
SKIP=set("斦斯賓听析折兵欣所")
toks=re.findall(r"([\u3400-\u9fff\U00020000-\U0002A6DF])(?:（([^）]*)）)?",row)
items=[(c,al) for c,al in toks if c not in SKIP]
print("族字",len(items))
GNAME={"b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","r":"柔锐","l":"拢离","g":"隔估","k":"口控","h":"豁活","j":"聚决","q":"亲缺","x":"续消","z":"凿总","c":"刺持","s":"失收","zh":"凿总","ch":"刺持","sh":"失收","y":"","w":"","":"",}
def ini(py):
    py=(py or "").lower()
    for k in ("zh","ch","sh"):
        if py.startswith(k): return k
    return py[:1] if py else ""
def bupang(t):
    m=re.search(r"从([\u3400-\u9fff\U00020000-\U0002A6DF])",t or "")
    return m.group(1) if m else ""
rows=[];made=0
for ch,al in items:
    e=cm.get(ch) or {}
    py=e.get("py","") or ""; txt=e.get("txt","") or ""
    aliases=[a for a in re.findall(r"[\u3400-\u9fff\U00020000-\U0002A6DF]",al or "")]
    rows.append({"ch":ch,"py":py,"lei":bupang(txt),"dian":txt})
    p=os.path.join(C,ch+".json")
    if os.path.exists(p): continue
    i=ini(py); g=GNAME.get(i,"")
    sm=(f"{i}「{g}」：聲符取義隨文，暫記聲母一面（推）。" if g else f"{i}「零聲母」不系（照實）。")
    card={"char":ch,"head":ch+("（"+aliases[0]+"）" if aliases else ""),"pinyin":py,"bus":{"num":44,"name":"斤"},"parent":"斤","level":3,"aliases":aliases,
          "sections":[{"key":"shiyi","label":"释义","text":txt or "（原稿字族行列出，未單獨立條）","cites":[]},{"key":"shengmu","label":"声母拟态","text":sm,"cites":[]},
                      {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
    json.dump(card,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
# 写回 斤 的 zizu 表
p=os.path.join(C,"斤.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["groups"]=[{"no":"①","title":"斤之族：斧斤砍斫、求祈、聲近諸字","rows":rows}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("族表行",len(rows),"新卡",made)