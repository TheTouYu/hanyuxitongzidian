import docx,re,sys
d=docx.Document(sys.argv[1])
out=[]
for p in d.paragraphs:
    t=p.text.strip()
    if re.match(r"^\d{3}\.",t) or t.startswith("本義") or t.startswith("音源"):
        out.append(t[:200])
print("\n".join(out[:24]))