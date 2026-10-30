# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
def rows(a,b):
    out=[];pat=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002FA1F]{1,3})(（[^）]*）)?([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
    for k in range(a,b):
        m=pat.match(ps[k])
        if m: out.append([m.group(1),m.group(3),"",ps[k]])
    return out
g1=rows(82,86); g2=rows(89,101)
lei={"𥿮":"糸","𧙢":"衣","鉽":"金","栻":"木","弒":"殺","𪀦":"鳥","試":"言","侙":"人","拭":"手","烒":"火","𢎎":"氏","𥅞":"目","𧊖":"虫","𧶣":"貝","𩗎":"風","軾":"車"}
for g in (g1,g2):
    for r in g: r[2]=lei.get(r[0],"")
d={"char":"式","trad":"式","pinyin":"shì","level":2,"parent":"弋","bus":[{"num":26,"name":"弋"}],
 "sections":[
  {"key":"benyi","label":"本义","text":ps[74].replace("本義：","")+ps[75],"cites":[]},
  {"key":"zhuanyi","label":"转义","text":ps[77].replace("轉義：","")+"\n"+ps[78]+"\n"+ps[79],"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「失」：墨線彈而失準，故取法以正之（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[{"title":"①指式狀，表示繃緊的線繩","note":"","rows":g1},
                                                      {"title":"②指彈式，表示試探、拂拭","note":"","rows":g2}],"cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}],
 "head":"式","photos":["01.png"],"captions":["太乙九宫占盘（西漢）"]}
json.dump(d,io.open(os.path.join(C,"式.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
F={"sh":("失收","失"),"zh":("凿总","凿"),"ch":("刺持","持"),"s":("失收","收"),"f":("附分","分")}
n=0
for g in (g1,g2):
    for r in g:
        ch,py_=r[0],r[1]; ini=re.sub(r"[^a-z]","",py_.lower())[:2]; key=ini if ini in F else ini[:1]
        grp,face=F.get(key,("失收","收"))
        card={"char":ch,"trad":ch,"pinyin":py_,"level":3,"parent":"式","bus":[{"num":26,"name":"弋"}],
          "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
                      {"key":"shengmu","label":"声母拟态","text":f"{key}「{grp}」取「{face}」：{r[3].split('《')[0][:12]}（推）。","cites":[]},
                      {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}]}
        json.dump(card,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("式族卡",n,"表行",len(g1)+len(g2))