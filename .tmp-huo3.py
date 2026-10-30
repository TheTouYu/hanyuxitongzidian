# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
def sl(t,lab): return re.sub(r'^%s[：:]'%lab,'',t.strip()).strip()
ROW=re.compile(r'^([\u3400-\u9fff\U00020000-\U0002A6DF]+)(?:（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)*)?\s*(.*)$')
MB={"d":("囤動","囤"),"t":("涂突","突"),"n":("纳弄","纳"),"l":("拢离","拢"),"g":("隔估","隔"),"k":("口控","口"),
    "h":("豁活","豁"),"j":("聚决","聚"),"q":("亲缺","亲"),"x":("续消","续"),"zh":("凿总","凿"),"ch":("刺持","刺"),
    "sh":("失收","收"),"r":("柔锐","锐"),"z":("凿总","凿"),"c":("刺持","刺"),"s":("失收","收"),"b":("闭剥","闭"),
    "p":("拼辟","拼"),"f":("附分","分"),"m":("蒙末","蒙")}
def sm(py_,ch,grp):
    x=re.sub(r'[^a-z]','',(py_ or '').lower()); key=None
    for k in ("zh","ch","sh"):
        if x.startswith(k): key=k
    if key is None: key=x[:1]
    if key not in MB: return 'y「零聲母」不系：零聲母，緒論七組未列（照實）。'
    g,f=MB[key]; return '%s「%s」取「%s」：%s於%s一面取「%s」之義（推）。'%(key,g,f,ch,grp,f)
def build(char,head,pinyin,variants,level,parent,sections,marks):
    groups=[];members=[]
    for idx,no,title,end in marks:
        rows=[]
        for k in range(idx+1,end):
            t=ps[k]
            if not t or t.startswith("▲"): continue
            m=ROW.match(t)
            if not m: continue
            c,ann,p,g=m.group(1),m.group(2) or "",(m.group(3) or "").strip(" 、"),m.group(4)
            rows.append([c+("（"+ann+"）" if ann else ""),p,"",g]); members.append((c,ann,p,g,title))
        groups.append({"no":no,"title":title,"rows":rows})
    d={"char":char,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":[{"num":41,"name":"戈"}],
       "aliases":variants,"sections":sections+[{"key":"zizu","label":"字族衍义","groups":groups},
       {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]}
    json.dump(d,io.open(os.path.join(C,char+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    for c,ann,p,g,grp in members:
        cd={"char":c,"head":c+("（"+ann+"）" if ann else ""),"pinyin":p,"level":3,"parent":char,
            "bus":[{"num":41,"name":"戈"}],"aliases":sorted(set(list(ann))) if ann else [],
            "sections":[{"key":"shiyi","label":"释义","text":g},{"key":"shengmu","label":"声母拟态","text":sm(p,c,grp)},
                        {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷六鶴","label":"卷六 鶴"}]}]}
        json.dump(cd,io.open(os.path.join(C,c+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    return [len(g["rows"]) for g in groups],len(members)
s2=[{"key":"benyi","label":"本义","text":"\n".join(sl(ps[k],"本義") for k in (262,263) if ps[k].strip())},
    {"key":"zhuanyi","label":"转义","text":sl(ps[268],"轉義")},
    {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：口張如戈刃，豁然而出聲（推）。"}]
print("或",build("或","或（㦯𢈿𢦙）","huò",["㦯","𢈿","𢦙"],2,"戈",s2,
  [(272,"①","指疆域，表示區域、邊界",282),(282,"②","指疆域，表示惑亂、不定",284),(284,"③","指疆域，表示包束、囊括",289),(289,"④","指切割，表示破裂、割取",295),(295,"⑤","指口利，表示風聲、風害",304)]))
s3=[{"key":"benyi","label":"本义","text":sl(ps[304],"本義")},{"key":"zhuanyi","label":"转义","text":sl(ps[307],"轉義")},
    {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「豁」：戈守四圍，豁然有界（推）。"}]
print("國",build("國","國（囯囶囻圀）","guó",["囯","囶","囻","圀"],2,"戈",s3,
  [(309,"①","指國的四圍有界，表示包括、窩狀物",320),(320,"②","指切割，表示砍斫、批擊",325),(325,"③","指疆域，表示惑亂、不定",328),(328,"④","指口利，表示叫聲、響聲的大",334)]))