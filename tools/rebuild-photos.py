# -*- coding: utf-8 -*-
import sys,os,json,glob,hashlib,re,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
CM=json.load(open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
PH=os.path.join(ROOT,"web","public","glyphs","photos")
def ishead(t):
    t=t.strip()
    if not t: return None
    c=t[0]
    if c not in CM: return None
    rest=t[1:]
    py=CM[c].get("py") or ""
    if rest.startswith("（") or rest.startswith("("): return c
    if rest.startswith(py[:2]) and py: return c
    if rest.startswith("《") or rest.startswith("。"): return c
    return None
def imgs(p,parts):
    out=[]
    for bl in p.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    q=parts[v]
                    if hasattr(q,"blob") and q.content_type.startswith("image"): out.append(q.blob)
                except KeyError: pass
    return out
got={}; caps={}
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    try: d=__import__("docx").Document(doc)
    except Exception as e: print("skip",os.path.basename(doc)); continue
    parts=d.part.related_parts
    cur=None; pend=[]
    for p in d.paragraphs:
        t=p.text.strip()
        h=ishead(t); 
        if h: cur=h; pend=[]
        if not cur: continue
        for b in imgs(p._p,parts):
            if len(b)<20000: continue
            got.setdefault(cur,[]).append(b); pend.append(cur)
        if t.startswith("▲") and pend:
            caps.setdefault(pend[-1],[]).append(t.lstrip("▲ ").strip())
            pend=[]
# 写盘：保留旧目录中不在新映射里的图？——统一以新扫描为准
index={}; capout={}
for ch,blobs in got.items():
    d=os.path.join(PH,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    seen=set(); files=[]
    for b in blobs:
        h=hashlib.sha1(b).hexdigest()
        if h in seen: continue
        seen.add(h)
        ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
        fn=f"{len(files)+1:02d}{ext}"; open(os.path.join(d,fn),"wb").write(b); files.append(fn)
    index[ch]=files
    if ch in caps: capout[ch]=caps[ch][:len(files)]
json.dump({"photos":index},open(os.path.join(PH,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":capout},open(os.path.join(PH,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("chars",len(index),"caps",len(capout))
for c in ("帝","啇","蒂","示","市"): print(c,index.get(c),capout.get(c))