import docx,re
d=docx.Document(r"D:\字谱智能体\卷八十  干.docx")
ps=[p.text.strip() for p in d.paragraphs if p.text.strip()]
out=[]
for i,t in enumerate(ps):
    if re.match(r"^49[5-9]\.|^50\d\.",t):
        out.append(t[:30]); 
        for j in range(i+1,min(i+3,len(ps))):
            if ps[j].startswith("本義"): out.append("  "+ps[j][:200]); break
print("\n".join(out[:24]))