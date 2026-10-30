# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
pat=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002FA1F]{1,3})(（([^）]*)）)?([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
rows=[]
for k in range(110,117):
    m=pat.match(ps[k])
    if m: rows.append([m.group(1),m.group(4),"",ps[k]])
lei={"敊":"攴","𢻃":"豆","𪀖":"鳥","𣢰":"欠","𡧯":"宀","鮛":"魚","茮":"艸"}
for r in rows: r[2]=lei.get(r[0],"")
d={"char":"尗","trad":"尗","pinyin":"shú","level":2,"parent":"弋","bus":[{"num":26,"name":"弋"}],
 "sections":[
  {"key":"benyi","label":"本义","text":ps[102].replace("本義：",""),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[k].replace("轉義：","") for k in (103,104)),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":"\n".join(ps[k].replace("辯證：","") for k in (106,107)),"cites":[]},
  {"key":"yinyuan","label":"音源","text":ps[108].replace("音源：",""),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「失」：豆熟而落，取收其實（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":ps[109],"groups":[{"title":"","note":"","rows":rows}],"cites":[]},
  {"key":"erji","label":"本部二级字根","text":"","links":[{"ch":"叔","label":"叔"}],"cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}],
 "head":"尗","aliases":[]}
json.dump(d,io.open(os.path.join(C,"尗.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
F={"ch":("刺持","持"),"q":("亲缺","亲"),"sh":("失收","失"),"s":("失收","收"),"j":("聚决","聚"),"z":("凿总","凿")}
n=0
for r in rows:
    ch,py_=r[0],r[1]; ini=re.sub(r"[^a-z]","",py_.lower())[:2]; key=ini if ini in F else ini[:1]
    grp,face=F.get(key,("失收","收"))
    card={"char":ch,"trad":ch,"pinyin":py_,"level":3,"parent":"尗","bus":[{"num":26,"name":"弋"}],
      "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
                  {"key":"shengmu","label":"声母拟态","text":f"{key}「{grp}」取「{face}」：{r[3].split('《')[0][:12]}（推）。","cites":[]},
                  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}]}
    json.dump(card,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("尗族卡",n)