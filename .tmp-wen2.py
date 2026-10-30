import glob,docx,re,os
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except: continue
    for j,t in enumerate(ps):
        if t.startswith("慍") or t.startswith("𥁕"):
            head=[x for x in ps[max(0,j-12):j] if re.match(r"^\d{3}[.．、]",x)]
            print(os.path.basename(f),j,t[:60],"| head:",head[-1] if head else None)
            break