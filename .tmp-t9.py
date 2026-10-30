# -*- coding: utf-8 -*-
import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
SECS={"矣":116,"氏":139,"氐":169,"巳":222,"了":245,"厶":106}
starts=sorted([k for k,t in enumerate(ps) if re.match(r"^（.*）：",t)]+[len(ps)])
ROW=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]{1,2})(（[^）]*）)?([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)([、a-zāāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]*)?《")
def parse(start):
    end=next(s for s in starts if s>start); grp=None; out=[]; fam=None
    for k in range(start,end):
        t=ps[k]
        if not t: continue
        m=re.match(r"^字族衍義[：:]?(.*)$",t)
        if m: fam=(m.group(1) or "").strip(); grp={"title":fam or "字族","note":"","header":["字","讀音","類屬","取義落點"],"rows":[]}; out.append(grp); continue
        m=re.match(r"^([①②③④⑤⑥⑦⑧])(.+)$",t)
        if m: grp={"title":m.group(1)+m.group(2)[:40],"note":"","header":["字","讀音","類屬","取義落點"],"rows":[]}; out.append(grp); continue
        if t.startswith("▲") or grp is None: continue
        r=ROW.match(t)
        if not r: continue
        ch=r.group(1); py_=r.group(3); body=t[r.end()-1:]
        gloss=body.split("。")[0].split("；")[0][:60]
        cm=re.search(r"从([\u3400-\u9fff])",body); cls=cm.group(1) if cm else ""
        grp["rows"].append([ch,py_,cls,(gloss+("；從"+cls+"定類" if cls else ""))[:80]])
    return [g for g in out if g["rows"]]
for root,st in SECS.items():
    gs=parse(st)
    p=rf"D:\系统汉字\web\public\cards\{root}.json"
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="zizu":
            s["text"]=f"{root}部字族衍義（照錄原稿）："; s["groups"]=gs
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(root,len(gs),sum(len(g["rows"]) for g in gs))