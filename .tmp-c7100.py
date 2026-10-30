# -*- coding: utf-8 -*-
import json,io,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); P=os.path.join(ROOT,"web","public","glyphs","photos")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
sec={"benyi":[], "zhuanyi":[], "bianzheng":[], "yinyuan":[]}
cur=None
for k in range(265,274):
    t=ps[k]
    if not t: continue
    if t.startswith("本義："): cur="benyi"; sec[cur].append(t[3:]); continue
    if t.startswith("轉義："): cur="zhuanyi"; sec[cur].append(t[3:]); continue
    if t.startswith("辯證："): cur="bianzheng"; sec[cur].append(t[4:]); continue
    if t.startswith("音源"): cur="yinyuan"; sec[cur].append(re.sub(r"^音源[：:]?","",t)); continue
    if cur: sec[cur].append(t)
rows=[("盄","zhāo","皿","《說文》：「器也。从皿弔聲。止遙切。」《通訓定聲》：「今蘇俗煎茶器曰吊子，即此盄字。」煮茶的器皿。","zh「凿总」取「总」：器總聚水而煮（推）。"),
("鈟（釣魡）","diào","金","《字彙》：「同釣。」釣，《集韻》：「《說文》：『鉤魚也。』或作魡。」","d「囤動」取「動」：鉤動而引魚（推）。"),
("屌","diǎo","尸","《字彙》：「丁了切，貂上聲。男子陰。」男性外生殖器。","d「囤動」取「囤」：垂囤而下（推）。"),
("伄","diào","人","《玉篇》：「伄當，不常也。」不經常，不長久。","d「囤動」取「動」：不久而動（推）。"),
("䘟（𧘨）","diāo","衣","《說文》：「棺中縑裏。从衣、弔。讀若雕。都僚切。」用絹貼棺中。《玉篇》：「蠻夷衣也。」《廣韻》：「死人衣。」","d「囤動」取「囤」：絹囤貼於棺（推）。"),
("𨑩","dì","辵","《說文》：「至也。从辵弔聲。都曆切。」《玉篇》：「又都叫切。」","d「囤動」取「動」：行而至（推）。")]
g1={"title":"①指懸吊","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:4]]}
g2={"title":"②指憑弔","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[4:]]}
head={"char":"弔","head":"弔（吊𢎣𢎨𢎱）","pinyin":"diào","level":1,"bus":[{"num":29,"name":"弔"}],
 "sections":[{"key":"benyi","label":"本义","text":"\n".join(sec["benyi"]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(sec["zhuanyi"]),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":"\n".join(sec["bianzheng"]),"cites":[]},
  {"key":"yinyuan","label":"音源","text":"\n".join(sec["yinyuan"]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"d「囤動」取「囤」：弋線收回囤聚於人（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[g1,g2]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
# 插图
fn=None
for k in range(264,268):
    for el in ps[k] if False else doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>8000:
                    ext=".png" if b[:4]==b"\x89PNG" else ".jpg"; fn="01"+ext
                    D=os.path.join(P,"弔"); os.makedirs(D,exist_ok=True); open(os.path.join(D,fn),"wb").write(b)
    if fn: break
if fn:
    head["photos"]=[fn]; head["captions"]=["青海宗日遺址的骨制魚鉤（5000年前）"]
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx; ph["弔"]=[fn]
    json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["弔"]=["青海宗日遺址的骨制魚鉤（5000年前）"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump(head,io.open(os.path.join(C,"弔.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
made=0
for r in rows:
    bare=re.sub(r"（.*?）","",r[0]); f=os.path.join(C,bare+".json")
    if os.path.exists(f): continue
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"弔","bus":[{"num":29,"name":"弔"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("rows",len(rows),"cards",made,"photo",fn)