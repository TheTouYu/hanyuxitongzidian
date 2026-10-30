# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]
PY="a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü"
groups=[("①指雁叫，表示歌唱、呵斥、贊許、大笑",(137,147)),("②指雁身，表示上細長而下肥大",(148,161)),
        ("③指雁的浮水",(162,165)),("④指雁的姿態，表示宛曲",(166,179)),("⑤指雁（鵝）羽，表示白色",(180,183))]
pat=re.compile(r"^([\u3400-\u9fff\uf900-\ufaff\U00020000-\U0002A6DF]+)(?:（[^）]*）)?\s*([" + PY + r"][^《]*?)《")
rows=[]
for title,(a,b) in groups:
    gr=[]
    for k in range(a,b+1):
        t=ps[k]
        if not t: continue
        m=pat.match(t)
        if not m: print("MISS",k,t[:30]); continue
        ch=m.group(1); py=m.group(2).strip().rstrip("、，,")
        gr.append([ch,py,"",t[m.end():]])
    rows.append((title,gr)); print(title[:8],len(gr),gr[0][:2] if gr else None)
d=json.load(io.open(os.path.join(C,"可.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["groups"]=[{"title":t,"note":"","rows":r} for t,r in rows]
json.dump(d,io.open(os.path.join(C,"可.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# clean stray cards named with latin
for f in os.listdir(C):
    if f.endswith(".json") and re.search(r"[A-Za-z]",f):
        b=f[:-5]
        if b.startswith("笴"): os.remove(os.path.join(C,f)); print("rm",f)
print("done")