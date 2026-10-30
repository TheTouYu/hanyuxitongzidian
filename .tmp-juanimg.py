# -*- coding: utf-8 -*-
import io,json,os,re,sys,glob,hashlib
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
H=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
# 1) 卷 → docx（首个部号落于卷范围）
files=glob.glob(r"D:\字谱智能体\*.docx"); jmap={}
for f in files:
    try: ps=[x for x in Document(f).paragraphs]
    except Exception: continue
    first=None
    for p in ps:
        t=p.text.strip()
        if not t: continue
        m=H.match(t)
        if m: first=int(m.group(1)); break
    if first is None: continue
    for j in Z["juan"]:
        if j["from"]<=first<=j["to"]: jmap.setdefault(j["no"],(f,ps)); break
PH=json.load(io.open(os.path.join(G,"photos","index.json"),encoding="utf-8")); PH=PH.get("photos") or PH
saved=0
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"])
    if j["no"] in jmap:
        f,ps=jmap[j["no"]]; buf=[]; rid=[]
        for p in ps:
            t=p.text.strip()
            if t and H.match(t): break
            buf.append(p)
        seen=set(); out=os.path.join(G,"photos",nm); os.makedirs(out,exist_ok=True)
        for f0 in os.listdir(out): os.remove(os.path.join(out,f0))
        k=0
        for p in buf:
            for bl in p._p.iter():
                for a,v in bl.attrib.items():
                    if not (a.endswith("}embed") or a.endswith("}id")): continue
                    try: part=ps and Document  # placeholder
                    except Exception: pass
        # 直接从 relationship 取 blob（按 rId 顺序）
        rels=[]
        for p in buf:
            for bl in p._p.iter():
                for a,v in bl.attrib.items():
                    if a.endswith("}embed") or a.endswith("}id"): rels.append(v)
        dparts=None
        try: dparts=Document(f).part.related_parts
        except Exception: dparts=None
        for r in rels:
            if r in seen: continue
            seen.add(r)
            try: blob=dparts[r].blob
            except Exception: continue
            if len(blob)<10000: continue
            h=hashlib.sha1(blob).hexdigest()
            if h in {x for x in []}: pass
            k+=1; ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(out,"%02d%s"%(k,ext)),"wb").write(blob)
            if k>=10: break
        if k:
            PH[nm]=sorted(os.listdir(out)); saved+=1
        else:
            PH.pop(nm,None)
json.dump({"photos":PH},io.open(os.path.join(G,"photos","index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("卷插图重抽",saved)