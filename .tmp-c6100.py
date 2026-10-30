# -*- coding: utf-8 -*-
import json,io,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards")
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
rows=[]
for k in range(233,262):
    t=ps[k]
    if not t or t.startswith("▲"): continue
    m=re.match(r"^([^\s（(]{1,3})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",t)
    if m: rows.append([m.group(1)+(m.group(2) or ""),m.group(3),"",t])
head={"char":"弟","head":"弟（𠂖𢦢）","pinyin":"dì","level":1,"bus":[{"num":28,"name":"弟"}],
 "sections":[
  {"key":"benyi","label":"本义","text":"象木橛上纏絲之形。本指纏有繒絲的弋。","cites":[]},
  {"key":"zhuanyi","label":"转义","text":"由繒絲的依次纏繞在木橛上，引申指次第、次序。dì，《釋名》：「弟，第也，相次第而上也。」進而引申指同輩比自己年紀小的男性；學生對老師自稱或別人指稱。《爾雅》：「男子先生為兄，後生為弟。」\n由纏繞的繒絲，引申指柔順、頹唐。tuí，《集韻》：「弟靡，不窮皃。一曰遜伏。」","cites":[]},
  {"key":"bianzheng","label":"辩证","text":"《說文》：「韋束之次第也。从古字之象。凡弟之屬皆从弟。，古文弟。从古文韋省，丿聲。特計切。」將「弋」與所纏繩視為「韋」，析形不確。","cites":[]},
  {"key":"yinyuan","label":"音源","text":"音源字。源自弋射時，線軸轉動時所發出的聲音。義音同「夷」：《易·渙》：「匪夷所思。」《釋文》：「荀作匪弟。」","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"d「囤動」取「囤」：繒絲依次囤繞木橛而上（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"多指依次、次第","groups":[{"title":"多指依次、次第","note":"","rows":rows}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
json.dump(head,io.open(os.path.join(C,"弟.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
SM={"递":"d「囤動」取「囤」：依次囤疊而傳（推）。","娣":"d「囤動」取「囤」：次第相從之妹（推）。",
"睇":"d「囤動」取「囤」：目聚而斜視（推）。","悌":"t「涂突」取「突」：敬兄之情突發（推）。",
"銻":"t「涂突」取「涂」：火鐮與石相涂擦（推）。","梯":"t「涂突」取「突」：木階節節突出（推）。",
"鬀":"t「涂突」取「突」：刀突而盡髮（推）。","涕":"t「涂突」取「涂」：液涂於面（推）。",
"綈":"t「涂突」取「涂」：絲層層涂疊（推）。","𧋘":"t「涂突」取「突」：蟬鳴突起（推）。",
"鮷":"t「涂突」取「涂」：鯰處泥涂（推）。","蕛":"t「涂突」取「涂」：草布地涂生（推）。",
"豑":"zh「凿总」取「总」：爵次總聚而有序（推）。","第":"d「囤動」取「囤」：次第囤列（推）。",
"祶":"d「囤動」取「囤」：祭品囤聚於廟（推）。","焍":"d「囤動」取「囤」：聚火灼龜（推）。",
"俤":"d「囤動」取「囤」：相比而囤近（推）。","珶":"d「囤動」取「囤」：佩玉囤聚（推）。",
"𦯔":"t「涂突」取「涂」：初生草涂地（推）。","䑯":"d「囤動」取「囤」：船囤載而浮（推）。",
"挮":"t「涂突」取「突」：拭而去之使突（推）。","罤":"t「涂突」取「涂」：網涂張以掩兔（推）。",
"䬾":"t「涂突」取「涂」：粉涂而為餅（推）。","鵜":"t「涂突」取「突」：大喙突出（推）。"}
made=0
for r in rows:
    ch=r[0]; bare=re.sub(r"（.*?）","",ch)
    f=os.path.join(C,bare+".json")
    if os.path.exists(f): continue
    d={"char":bare,"head":ch,"pinyin":r[1],"level":3,"parent":"弟","bus":[{"num":28,"name":"弟"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":SM.get(bare,"d「囤動」取「囤」：次第囤列（推）。"),"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("rows",len(rows),"cards",made)