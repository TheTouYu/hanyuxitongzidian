# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
for fn in ("卷六  鶴.docx","卷五  雁.docx"):
    doc=Document(r"D:\字谱智能体"+os.sep+fn); parts=doc.part.related_parts
    for k,p in enumerate(doc.paragraphs):
        if "罩魚者也" in p.text:
            n=0; buf=[]
            for el in p._p.iter():
                tag=el.tag.split("}")[-1]
                if tag=="t": buf.append(el.text or "")
                elif tag in ("blip","imagedata"):
                    rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
                    if rid:
                        try: b=parts[rid[0]].blob
                        except KeyError: continue
                        ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
                        n+=1; fn2="%02d.%s"%(n,ext)
                        D=os.path.join(G,"inline","篧","shiyi"); os.makedirs(D,exist_ok=True)
                        open(os.path.join(D,fn2),"wb").write(b); buf.append("{{shiyi/%s}}"%fn2)
            print(fn,k,"imgs",n,p.text[:50])
            if n:
                txt="".join(buf).strip()
                cp=os.path.join(C,"篧.json"); d=json.load(io.open(cp,encoding="utf-8"))
                for s in d["sections"]:
                    if s.get("key")=="shiyi": s["text"]=txt; s["gdir"]="inline/篧"
                json.dump(d,io.open(cp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
                print("embedded",txt[:80]); raise SystemExit