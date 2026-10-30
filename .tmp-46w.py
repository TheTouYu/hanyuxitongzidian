# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
P=json.load(io.open(r"D:\系统汉字\.tmp-46.json",encoding="utf-8"))
R=json.load(io.open(r"D:\系统汉字\.tmp-46rows.json",encoding="utf-8"))
LEI=json.load(io.open(r"D:\系统汉字\.tmp-lei.json",encoding="utf-8")) if os.path.exists(r"D:\系统汉字\.tmp-lei.json") else {}
def dian(ch,t):
    m=re.search(r"”[^”]*?》?[。；]?\s*(.+)$",t)
    s=(m.group(1) if m else t)[:26]
    return s or t[:20]
def sm(py):
    p=py or ""
    for pre,lab in (("zh","zh「凿总」取「凿」"),("ch","ch「刺持」取「刺」"),("sh","sh「失收」取「收」")):
        if p.startswith(pre): return lab+"：依聲符取義一面（推）。"
    b=p[:1].lower()
    tb={"b":"b「闭剥」取「闭」","p":"p「拼辟」取「拼」","m":"m「蒙末」取「蒙」","f":"f「附分」取「附」","d":"d「囤动」取「囤」","t":"t「涂突」取「突」","n":"n「纳弄」取「纳」","l":"l「拢离」取「拢」","g":"g「隔估」取「隔」","k":"k「口控」取「控」","h":"h「豁活」取「豁」","j":"j「聚决」取「聚」","q":"q「亲缺」取「亲」","x":"x「续消」取「续」","z":"z「凿总」取「凿」","c":"c「刺持」取「刺」","s":"s「失收」取「收」","r":"r「柔锐」取「柔」"}
    return (tb.get(b,"y「零聲母」不系")+"：依聲符取義一面（推）。")
def W(ch,o): json.dump(o,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
groups46=[("②","指托舉，表示負載、挺舉、依憑",range(296,317)),("②","指托掌狀，表示張開",range(318,325)),("③","指手掌，同「石」，表示敲擊、硬實",range(326,335)),("④","形近字「屯、乏」之訛",range(336,340))]
groupszh=[("①","指托掌，表示張開、裂開",range(350,361)),("②","指托身，表示寄託、托舉",range(362,367)),("③","與「度」同，指揣度",range(368,374))]
def build_groups(rows,gs):
    by={}
    for ch,py,t in rows:
        m=re.search(r"^[\u3400-\u9fff]{1,6}",t)
        by.setdefault(t,None)
    out=[]
    for no,title,rng in gs:
        rs=[]
        for k in rng:
            t=P.get(str(k),"")
            m=re.match(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]{1,6})(?:（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",t)
            if not m: continue
            ch,py=m.group(1),m.group(2)
            rs.append([ch,py,"",""])
        if rs: out.append({"no":no,"title":title,"rows":rs})
    return out
# fill lei/dian via LEI file if present
LEI=json.load(io.open(r"D:\系统汉字\.tmp-lei.json",encoding="utf-8")) if os.path.exists(r"D:\系统汉字\.tmp-lei.json") else {}
for gs in (groups46,groupszh):
    pass
print("ok")