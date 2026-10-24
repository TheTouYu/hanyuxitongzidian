import sys,os,json,hashlib
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
CM=json.load(open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
NAMES={v["nm"] for v in CM.values()}
IDX=r"D:\系统汉字\web\public\glyphs\photos\index.json"
idx=json.load(open(IDX,encoding="utf-8")); ph=idx.get("photos") or idx

def entry_char(t):
    t=t.strip()
    for k in (1,2,3):
        c=t[:k]
        if c in CM:
            rest=t[k:k+12]
            py=CM[c]["py"] or ""
            if rest.startswith(py) or rest[:1] in "（(" or rest[:1] in "《":
                return c
    return None

doc=r"D:\字谱智能体\卷一  雞.docx"
d=Document(doc); parts=d.part.related_parts
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
for i,p in enumerate(d.paragraphs):
    c=entry_char(p.text)
    if c: cur=c
    if not cur: continue
    for rid in imgs(p._p):
        blob=parts[rid].blob
        if len(blob)<20000: continue
        h=hashlib.md5(blob).hexdigest()
        got.setdefault(cur,[]).append((h,blob))
n=0
for ch,items in got.items():
    if ph.get(ch): continue
    dst=rf"D:\系统汉字\web\public\glyphs\photos\{ch}"; os.makedirs(dst,exist_ok=True)
    names=[]
    for j,(h,blob) in enumerate(items[:3],1):
        ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
        fn=f"{j:02d}{ext}"; open(os.path.join(dst,fn),"wb").write(blob); names.append(fn)
    ph[ch]=names; n+=1
json.dump({"photos":ph},open(IDX,"w",encoding="utf-8"),ensure_ascii=False)
print("rows",len(got),"assigned",n,"| 旨",ph.get("旨"),"麂",ph.get("麂"))