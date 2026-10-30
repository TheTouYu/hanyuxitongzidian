import docx,re
d=docx.Document(r"D:\字谱智能体\卷七十八  夒.docx")
out=[]
for p in d.paragraphs:
    t=p.text.strip()
    if re.match(r"^\d{3}\.",t) or t.startswith("本義") or t.startswith("轉義") or t.startswith("音源"):
        out.append(t[:200])
print("\n".join(out[:24]))