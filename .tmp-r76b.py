import docx,re
d=docx.Document(r"D:\字谱智能体\卷七十六  又.docx")
out=[];page=0;on=False
for p in d.paragraphs:
    x=p._p.xml
    if 'w:br' in x and 'type="page"' in x: page+=1
    t=p.text.strip()
    if not t: continue
    if re.match(r"^46[45]\.",t) or re.match(r"^(46[45])．",t): on=True
    if on: out.append(f"[p{page}] {t}")
print("\n".join(out[:80]))