import docx
d=docx.Document(r"D:\字谱智能体\卷七十六  又.docx")
out=[];page=0
for p in d.paragraphs:
    x=p._p.xml
    if 'w:br' in x and 'type="page"' in x: page+=1
    t=p.text.strip()
    if t: out.append(f"[p{page}] {t}")
print("\n".join(out))