# -*- coding: utf-8 -*-
import json,io,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
KEYS=("shiyi","benyi","zhuanyi","bianzheng","yinyuan")
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        if isinstance(d,dict) and d.get("char"): cards[d["char"]]=d
fixed=[]; skipped=[]
for fp in glob.glob(r"D:\字谱智能体\*.docx")+glob.glob(r"D:\字谱智能体\[0-9]*.docx"):
    try: doc=Document(fp)
    except Exception: continue
    parts=doc.part.related_parts
    for k,p in enumerate(doc.paragraphs):
        t=p.text.strip()
        if len(t)<12: continue
        n=sum(1 for el in p._p.iter() if el.tag.split("}")[-1] in ("blip","imagedata"))
        if not n: continue
        ch=t[0]; d=cards.get(ch)
        if not d: continue
        b=d.get("bus"); num=None
        if isinstance(b,list) and b and isinstance(b[0],dict): num=b[0].get("num")
        elif isinstance(b,dict): num=b.get("num")
        if not isinstance(num,int) or num>38: continue
        if any("{{" in (s.get("text") or "") for s in d.get("sections") or []): continue
        # 从该段重建文本
        buf=[]; cnt=0
        for el in p._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": buf.append(el.text or "")
            elif tag in ("blip","imagedata"):
                rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
                if rid:
                    try: blob=parts[rid[0]].blob
                    except KeyError: continue
                    ext="png" if blob[:4]==b"\x89PNG" else ("jpg" if blob[:2]==b"\xff\xd8" else "emf")
                    cnt+=1; buf.append("\x00%d.%s\x00"%(cnt,ext))
        newtxt="".join(buf).strip()
        if cnt==0: continue
        # 找对应 section
        key=None
        for s in d.get("sections") or []:
            st=(s.get("text") or "").replace("{{","").strip()
            if st and newtxt.replace("\x00","").startswith(st[:6]):
                key=s.get("key"), s; break
        if not key or key[0] not in KEYS:
            skipped.append((ch,num,"nosect")); continue
        _,sec=key; kk=sec.get("key")
        D=os.path.join(G,"inline",ch,kk); os.makedirs(D,exist_ok=True)
        # 保存图片并替换占位
        i=0
        def rep(m):
            nonlocal i
            fn=m.group(0).strip("\x00"); i+=1
            # 重新读取 blob
            return "{{%s/%s}}"%(kk,fn)
        final=re.sub(r"\x00[^\x00]+\x00",rep,newtxt)
        # 写入文件
        idx=0
        for el in p._p.iter():
            if el.tag.split("}")[-1] in ("blip","imagedata"):
                rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
                if not rid: continue
                try: blob=parts[rid[0]].blob
                except KeyError: continue
                ext="png" if blob[:4]==b"\x89PNG" else ("jpg" if blob[:2]==b"\xff\xd8" else "emf")
                idx+=1; open(os.path.join(D,"%02d.%s"%(idx,ext)),"wb").write(blob)
        sec["text"]=final; sec["gdir"]="inline/"+ch
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        fixed.append((ch,kk,idx))
print("fixed",len(fixed),fixed[:12])
print("skipped",len(skipped),skipped[:10])