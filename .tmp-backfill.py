# -*- coding: utf-8 -*-
import json,io,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs\inline"
DOCS=glob.glob(r"D:\字谱智能体\*.docx")
# 建立全库段落索引（含图）
index=[]
for fn in DOCS:
    try: doc=Document(fn)
    except Exception: continue
    parts=doc.part.related_parts
    for k,p in enumerate(doc.paragraphs):
        txt=[]; imgs=[]
        for el in p._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": txt.append(el.text or "")
            elif tag=="blip":
                rid=[v for x,v in el.attrib.items() if x.endswith("}embed") or x.endswith("}id")]
                if rid:
                    try: b=parts[rid[0]].blob
                    except KeyError: continue
                    imgs.append(b); txt.append("\x00")
        t="".join(txt).strip()
        if imgs: index.append((t.replace("\x00",""), imgs))
print("paras with imgs", len(index))
def probe(s):
    s=re.sub(r'\s+','',s)
    return s[:16]
pairs=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    ch=d.get("char") or f[:-5]
    for s in d.get("sections",[]):
        if s.get("key") not in ("benyi","zhuanyi","bianzheng","yinyuan"): continue
        t=s.get("text") or ""
        if "《說文》" not in t and "《说文》" not in t: continue
        if s.get("gdir"): continue
        pairs.append((ch,s["key"],t))
print("candidates",len(pairs))
fixed=0
for ch,key,t in pairs:
    pr=probe(re.sub(r'^(本義|轉義|辯證|音源)[：:]','',t))
    if len(pr)<8: continue
    hit=None
    for t2,imgs in index:
        if re.sub(r'\s+','',t2).startswith(pr) or pr in re.sub(r'\s+','',t2):
            hit=(t2,imgs); break
    if not hit: continue
    t2,imgs=hit
    dd=os.path.join(G,ch,key); os.makedirs(dd,exist_ok=True)
    parts_txt=[]; n=0
    # 重建：按 t2 中 \x00 顺序还原不可行（t2 已去图），改为：把图插入引用其周围文字的近似位置——
    # 采用保守法：逐图插到「距其最近的、在当前文本中出现的 6 字上下文之后」不可行，故仅当图数==1 且《說文》引文里只有一个空位时追加到「度也。」类位置
    if len(imgs)!=1: continue
    b=imgs[0]; ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
    fn="01."+ext; open(os.path.join(dd,fn),"wb").write(b)
    # 在《說文》引文的「」之间：找 「，X或从」 前插入
    t3=t
    m=re.search(r'([。，])([^。，]{0,2})(或从|或作|或省)',t3)
    if not m: continue
    pos=m.start(1)+1
    t3=t3[:pos]+"{{%s/%s}}"%(key,fn)+t3[pos:]
    p=os.path.join(C,ch+".json"); dd2=json.load(io.open(p,encoding="utf-8"))
    for s in dd2["sections"]:
        if s["key"]==key: s["text"]=t3; s["gdir"]="inline/"+ch
    json.dump(dd2,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    fixed+=1
print("fixed",fixed)