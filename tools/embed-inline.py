# -*- coding: utf-8 -*-
"""把原稿某字条各栏里的行内古文字形，嵌入卡片对应栏（{{栏/NN.png}}）并写 gdir。
用法: python tools/embed-inline.py 字 段落起 段落止 [docx文件名]
默认 docx 为 卷六  鶴.docx；段落区间含两端，按 run 顺序保序。"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs\inline"
char=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
docname=sys.argv[4] if len(sys.argv)>4 else "卷六  鶴.docx"
doc=Document(os.path.join(r"D:\字谱智能体",docname)); parts=doc.part.related_parts
p=os.path.join(C,char+".json"); d=json.load(io.open(p,encoding="utf-8"))
total=0
for sec in d["sections"]:
    key=sec.get("key"); 
    if key not in ("benyi","zhuanyi","bianzheng","yinyuan"): continue
    dd=os.path.join(G,char,key); os.makedirs(dd,exist_ok=True)
    n=0; out=[]
    for k in range(a,b+1):
        buf=[]
        for el in doc.paragraphs[k]._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": buf.append(el.text or "")
            elif tag=="blip":
                rid=[v for x,v in el.attrib.items() if x.endswith("}embed") or x.endswith("}id")]
                if rid:
                    bl=parts[rid[0]].blob; n+=1
                    ext="png" if bl[:4]==b"\x89PNG" else ("jpg" if bl[:2]==b"\xff\xd8" else "emf")
                    fn="%02d.%s"%(n,ext); open(os.path.join(dd,fn),"wb").write(bl)
                    buf.append("{{%s/%s}}"%(key,fn))
        t="".join(buf).strip(); t=re.sub(r'^(本義|轉義|辯證|音源)[：:]','',t).strip()
        if t and not re.match(r'^[①-⑦]',t): out.append(t)
    if n:
        sec["text"]="\n".join(out); sec["gdir"]="inline/"+char; total+=n
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(char,"inline imgs",total)