import glob,re,docx
out=[]
for f in sorted(glob.glob(r"D:\修订\x\*.docx")):
    try: d=docx.Document(f)
    except Exception: continue
    page=0
    for p in d.paragraphs:
        if 'w:br' in p._p.xml and 'type="page"' in p._p.xml: page+=1
        t=p.text.strip()
        m=re.match(r"^(\d{2,3})\.([^\s]{1,3})部",t)
        if m and int(m.group(1))>=463 and int(m.group(1))<=520:
            out.append((int(m.group(1)),m.group(2)[:1],f.split("\\")[-1],page))
for r in sorted(out)[:14]: print(r)