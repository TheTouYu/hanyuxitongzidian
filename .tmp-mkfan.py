# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
BEN=("从又厂聲。“厂”若指懸崖；从“又”，象意手作厂形的樣子，表示攀、扣之意。“扳（pān）”的初文，《廣雅》：“援也。”\n\n"
"“厂”若指雁陣形；从“又”，則象意大雁的回歸、反轉，表示返回。fǎn，《說文》：“覆也。从又，厂反形。，古文。府遠切。”")
d={"char":"反","head":"反（𠬡）","pinyin":"fǎn","level":2,"parent":"厂","bus":["35"],"sections":[
 {"key":"benyi","label":"本义","text":BEN},
 {"key":"zhuanyi","label":"转义","text":"由翻轉引申指反復，或表示慎重之意。fàn，《集韻》：“難也。《詩》：‘威儀反反。’毛萇說。一曰順習皃。”《廣韻》：“反覆。又不順也。”"},
 {"key":"bianzheng","label":"辩证","text":"或以其象意以手攀崖。貌似合理，但翻轉、反復之意無从出。而“厂”既指石，从“又”，本有“度”字。\n\n因此，“反”所从“厂”，很可能跟“雁”一樣，是指雁陣形。雁陣的出現，是在雁群遷徙的時候：秋分時節南飛；春分時節北歸。從而引申指返回、反歸之義。"},
 {"key":"shengmu","label":"声母拟态","text":"f「附分」取「分」：翻轉而分離，去而復返（推）。"},
 {"key":"zizu","label":"字族衍义","text":"","groups":[
   {"t":"①指翻轉、回返","rows":[
     ["飯","fàn","食","《說文》「食也」；上古以手抓飯"],
     ["返","fǎn","辵","《說文》「還也」；《玉篇》「復也」"],
     ["䡊","fǎn","車","《說文》「車耳反出也」，旁出障塵"],
     ["阪","bǎn","阜","《說文》「坡者曰阪」；山脅"],
     ["昄","bǎn","日","《說文》「大也」；疑本指倒影"],
     ["汳","biàn","水","《說文》汴水；今作汴"],
     ["叛","pàn","半","《說文》「半也」，分離背叛"],
     ["眅","pān","目","《說文》「多白眼也」，翻白眼"],
     ["瓪","bǎn","瓦","《說文》「敗也」，燒過外翻之瓦"],
     ["㽹","fǎn","疒","《方言》「惡也」；惡心嘔吐"],
     ["㤆","fàn","心","《玉篇》「噁心也，急性也」"],
     ["𡞟","pàn","女","《集韻》「㛶𡞟，無儀適也」"],
     ["扳","pān","手","《廣雅》「援也」；攀之初文"],
     ["舨","bǎn","舟","《集韻》「艟舨，舟也」，兩頭翹起"]]},
   {"t":"②指反復","rows":[
     ["板","bǎn","木","《玉篇》「片木也」；與版同"],
     ["蝂","bǎn","虫","《廣韻》「蝂蝜，蟲」，好負重物"],
     ["魬","bǎn","魚","《正字通》比目魚名版魚"],
     ["畈","fàn","田","《正字通》「田畈，平疇也」"],
     ["仮","fǎn","人","《類篇》「反覆也」"],
     ["粄","bǎn","米","《玉篇》「米餅」，反復舂成"],
     ["販","fàn","貝","《說文》「買賤賣貴者」"],
     ["版","bǎn","片","《說文》「判也」，分木為片"]]}]},
 {"key":"suoshu","label":"所属卷","text":"卷五 雁（第35部 厂·二级字根 反）"}]}
json.dump(d,io.open(os.path.join(C,"反.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
rows={}
for g in d["sections"][4]["groups"]:
    for r in g["rows"]: rows[r[0]]=r
# family cards with 原文 paragraph text pulled from docx
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
idx={"飯":258,"返":259,"䡊":260,"阪":261,"昄":262,"汳":263,"叛":264,"眅":265,"瓪":266,"㽹":267,"㤆":268,"𡞟":269,"扳":270,"舨":271,"板":273,"蝂":274,"魬":275,"畈":276,"仮":277,"粄":278,"販":279,"版":280}
ZERO="f「附分」取「分」：翻轉而分離，去而復返（推）。"
n=0
for ch,k in idx.items():
    dd={"char":ch,"head":ch,"pinyin":"","level":3,"parent":"反","bus":["35"],
        "sections":[{"key":"shiyi","label":"释义","text":ps[k]},{"key":"shengmu","label":"声母拟态","text":ZERO}]}
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# add erji links to 厂
p=os.path.join(C,"厂.json"); h=json.load(io.open(p,encoding="utf-8"))
h.setdefault("sections",[]).insert(5,{"key":"erji","label":"本部二级字根","text":"","links":[{"ch":"反","label":"反"},{"ch":"彥","label":"彥"},{"ch":"炭","label":"炭"},{"ch":"產","label":"產"},{"ch":"詹","label":"詹"}]})
json.dump(h,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("反 +",n)