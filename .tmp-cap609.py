# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
import glob
C=r"D:\系统汉字\web\public\cards"; IN=r"D:\系统汉字\web\public\glyphs\inline"
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
files=glob.glob(r"D:\字谱智能体\*.docx")
pos={}
for f in files:
    try: ps=Document(f).paragraphs
    except Exception: continue
    for k,pp in enumerate(ps):
        t=pp.text.strip()
        m=pat.match(t)
        if m and m.group(1) not in pos: pos[m.group(1)]=(f,k)
print("索引字",len(pos))
resolved=0; miss=0
for fn in list(os.listdir(C)):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=d.get("char","")
    for s in d.get("sections",[]):
        if not isinstance(s,dict) or s.get("key")!="shiyi": continue
        t=s.get("text","")
        if not re.search(r"。，",t): continue
        if ch not in pos: miss+=1; break
        f,k=pos[ch]
        doc=Document(f); ps=doc.paragraphs; parts=doc.part.related_parts
        imgs=[]
        for el in ps[k]._p.iter():
            for a,v in el.attrib.items():
                if a.endswith("}embed") or a.endswith("}id"):
                    try:
                        b=parts[v].blob
                        if len(b)>400: imgs.append(b)
                    except KeyError: pass
        gaps=t.count("。，")
        if not imgs: miss+=1; break
        D=os.path.join(IN,ch,"shiyi"); os.makedirs(D,exist_ok=True)
        for i,b in enumerate(imgs):
            ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(D,f"{i+1:02d}{ext}"),"wb").write(b)
        # 逐个替换 gap
        for i in range(min(gaps,len(imgs))):
            ext=".png" if imgs[i][:4]==b"\x89PNG" else ".jpg"
            img=f'<img class="gin" src="glyphs/inline/{ch}/shiyi/{i+1:02d}{ext}" alt="字形">'
            t=t.replace("。，","。"+img+"，",1)
        s["text"]=t; resolved+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); break
print("插入",resolved,"未能定位",miss)