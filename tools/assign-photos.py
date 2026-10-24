import sys,os,json,hashlib,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
CM=json.load(open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
IDX=r"D:\系统汉字\web\public\glyphs\photos\index.json"
idx=json.load(open(IDX,encoding="utf-8")); ph=idx.get("photos") or idx
def entry_char(t):
    t=t.strip()
    for k in (1,2,3):
        c=t[:k]
        if c in CM:
            rest=t[k:k+12]; py=CM[c]["py"] or ""
            if rest.startswith(py) or rest[:1] in "（(《": return c
    return None
tot=0; new=0
for doc in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=Document(doc)
    except Exception as e: print("skip",os.path.basename(doc),e); continue
    parts=d.part.related_parts
    def imgs(el):
        out=[]
        for bl in el.iter():
            for a,v in bl.attrib.items():
                if a.endswith('}embed') or a.endswith('}id'):
                    try:
                        p=parts[v]
                        if hasattr(p,'blob') and p.content_type.startswith('image'): out.append(v)
                    except KeyError: pass
        return out
    cur=None; got={}
    for p in d.paragraphs:
        c=entry_char(p.text)
        if c: cur=c
        if not cur: continue
        for rid in imgs(p._p):
            blob=parts[rid].blob
            if len(blob)<20000: continue
            got.setdefault(cur,[]).append(blob)
    for ch,blobs in got.items():
        tot+=1
        if ph.get(ch): continue
        dst=rf"D:\系统汉字\web\public\glyphs\photos\{ch}"; os.makedirs(dst,exist_ok=True)
        names=[]
        for j,blob in enumerate(blobs[:3],1):
            ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
            fn=f"{j:02d}{ext}"; open(os.path.join(dst,fn),"wb").write(blob); names.append(fn)
        ph[ch]=names; new+=1
json.dump({"photos":ph},open(IDX,"w",encoding="utf-8"),ensure_ascii=False)
print("有图字头",tot,"新增",new,"总条目",len(ph))