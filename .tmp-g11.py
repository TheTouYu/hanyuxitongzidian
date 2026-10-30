import docx,re
for f in [r"D:\字谱智能体\卷八十八  昜.docx",r"D:\字谱智能体\卷八十七  羊.docx"]:
    d=docx.Document(f); print("==",f.split("\\")[-1])
    for p in d.paragraphs:
        t=p.text.strip()
        m=re.match(r"^(\d{3})[\.．]",t)
        if m and int(m.group(1))>=520: print("  ",t[:40])