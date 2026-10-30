# -*- coding: utf-8 -*-
import json,io,os,re,struct,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); INL=os.path.join(ROOT,"web","public","glyphs","inline","弔")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
def dims(b):
    if b[:4]==b"\x89PNG": return struct.unpack(">II",b[16:24])
    return (0,0)
sec=None; out={}; cnt={}
for k in range(265,274):
    p=doc.paragraphs[k]; t=p.text.strip()
    if not t: continue
    for key,pre in (("benyi","本義"),("zhuanyi","轉義"),("bianzheng","辯證"),("yinyuan","音源")):
        if t.startswith(pre): sec=key; break
    if sec is None: continue
    buf=[]
    # 跳过 ▲ 图注整段
    if t.lstrip().startswith("▲"): continue
    for r in p.runs:
        rid=None
        for el in r._r.iter():
            for a,v in el.attrib.items():
                if a.endswith("}embed") or a.endswith("}id"): rid=v
        if rid:
            try: b=parts[rid].blob
            except KeyError:
                buf.append(r.text); continue
            w,h=dims(b)
            if b[:4]==b"\x89PNG" and w<=1 and h<=1:
                buf.append(r.text); continue
            d=os.path.join(INL,sec); os.makedirs(d,exist_ok=True)
            n=cnt.get(sec,0)+1; cnt[sec]=n; fn="%02d.%s"%(n,kd(b))
            open(os.path.join(d,fn),"wb").write(b)
            buf.append("{{%s/%s}}"%(sec,fn))
        else: buf.append(r.text)
    out.setdefault(sec,[]).append("".join(buf))
txt={k:"\n".join(v) for k,v in out.items()}
p=os.path.join(C,"弔.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key") in txt:
        s["text"]=txt[s["key"]].replace("本義：","",1).replace("轉義：","",1).replace("辯證：","",1).replace("音源：","",1)
        s["gdir"]="inline/弔"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(cnt)