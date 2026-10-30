import docx,re
d=docx.Document(r"D:\字谱智能体\卷七十七  蛙.docx")
out=[];page=0
for p in d.paragraphs:
    x=p._p.xml
    if 'w:br' in x and 'type="page"' in x: page+=1
    t=p.text.strip()
    if not t: continue
    if re.match(r"^46[6-9]\.|^47[0-5]\.",t) or t.startswith("本義") or t.startswith("轉義") or t.startswith("音源") or t.startswith("字族衍義") or re.match(r"^\d+\.[^部]{1,3}部$",t)==False and t.startswith("（"):
        out.append(f"[p{page}] {t[:300]}")
    if len(out)>90: break
print("\n".join(out[:90]))