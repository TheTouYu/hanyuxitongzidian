# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
def strip_lab(t,lab):
    t=t.strip()
    return re.sub(r'^%s[：:]'%lab,'',t).strip()
benyi=strip_lab(ps[142],"本義")+"\n"+strip_lab(ps[143],"本義")
zhuanyi=strip_lab(ps[146],"轉義")+"\n"+strip_lab(ps[147],"轉義")
marks=[(149,"①","指鶴色，表示紅色、青色、白色",154),(154,"②","指鶴足，表示度量、張開、劃開",164),
       (164,"③","指鶴姿，表示高、遠",170),(170,"④","指鶴飛，表示撲騰、翻滾",178),
       (178,"⑤","指鶴爪，表示抓取、纏束",182),(182,"⑥","指鶴鳴，表示大叫、喉音",187),
       (187,"⑦","指鶴視，表示圓睜雙眼注視之狀",192)]
ROW=re.compile(r'^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(?:（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)*)?\s*(.*)$')
groups=[]; members=[]
for i,(idx,no,title,end) in enumerate(marks):
    rows=[]
    for k in range(idx+1,end):
        t=ps[k]
        if not t or t.startswith("▲") or k in (154,164,170,178,182,187): continue
        m=ROW.match(t)
        if not m: continue
        c,ann,p,g=m.group(1),m.group(2) or "",(m.group(3) or "").strip(" 、"),m.group(4)
        disp=c+("（"+ann+"）" if ann else "")
        rows.append([disp,p,"",g])
        members.append((c,ann,p,g,title))
    groups.append({"no":no,"title":title,"rows":rows})
print("groups",[len(g["rows"]) for g in groups],"members",len(members))
MB={"d":("囤動","囤"),"t":("涂突","突"),"n":("纳弄","纳"),"l":("拢离","拢"),"g":("隔估","隔"),"k":("口控","口"),
    "h":("豁活","豁"),"j":("聚决","聚"),"q":("亲缺","亲"),"x":("续消","续"),"zh":("凿总","凿"),"ch":("刺持","刺"),
    "sh":("失收","收"),"r":("柔锐","锐"),"z":("凿总","凿"),"c":("刺持","刺"),"s":("失收","收"),"b":("闭剥","闭"),
    "p":("拼辟","拼"),"f":("附分","分"),"m":("蒙末","蒙"),"y":("零聲母","不系")}
def sm(py_,ch,grp):
    x=re.sub(r'[^a-z]','',py_.lower())
    key=None
    for k in ("zh","ch","sh"):
        if x.startswith(k): key=k
    if key is None: key=x[:1]
    if key not in MB or key=="y": return 'y「零聲母」不系：零聲母，緒論七組未列（照實）。'
    g,f=MB[key]
    return '%s「%s」取「%s」：%s從%s一面取「%s」之義（推）。'%(key,g,f,ch,grp,f)

head={"char":"蒦","head":"蒦","pinyin":"huò","level":2,"parent":"隻","bus":[{"num":40,"name":"隻"}],"aliases":[],
 "sections":[
  {"key":"benyi","label":"本义","text":benyi},
  {"key":"zhuanyi","label":"转义","text":zhuanyi},
  {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：規蒦張開以度量，度其廣狹（推）。"},
  {"key":"zizu","label":"字族衍义","groups":groups},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"蒦.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for c,ann,p,g,grp_title in members:
    d={"char":c,"head":c+("（"+ann+"）" if ann else ""),"pinyin":p,"level":3,"parent":"蒦",
       "bus":[{"num":40,"name":"隻"}],"aliases":sorted(set(list(ann))) if ann else [],
       "sections":[{"key":"shiyi","label":"释义","text":g},
                   {"key":"shengmu","label":"声母拟态","text":sm(p,c,grp_title)},
                   {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(d,io.open(os.path.join(C,c+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards",n+1)