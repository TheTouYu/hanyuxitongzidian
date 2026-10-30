import docx,re
d=docx.Document(r"D:\字谱智能体\卷七十七  蛙.docx")
p_on=False;out=[]
for p in d.paragraphs:
    t=p.text.strip()
    if not t: continue
    if t.startswith("469.龜部"): p_on=True
    if t.startswith("471.鬼部"): break
    if p_on and (t.startswith("469.") or t.startswith("470.") or t.startswith("本義") or t.startswith("轉義") or t.startswith("音源") or t.startswith("字族衍義")):
        out.append(t[:260])
print("\n".join(out))