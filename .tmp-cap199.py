import glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
targets=("咺","㿩","䬞","伳","㞷","㠱")
hits={t:None for t in targets}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for t in targets:
        if hits[t]: continue
        for i,s in enumerate(ps):
            if s.startswith(t):
                hits[t]=(f.split("\\")[-1],i,s[:90]); break
    if all(hits.values()): break
for k,v in hits.items(): print(k,v)