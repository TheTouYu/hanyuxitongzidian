import docx,re
ps=[p.text.strip() for p in docx.Document(r"D:\字谱智能体\卷八十三  鼎.docx").paragraphs if p.text.strip()]
for i,t in enumerate(ps):
    if re.match(r"^(51[1-9]|52\d)\.",t):
        print("==",t[:18]); print("  ",[x for x in ps[i+1:i+4]][0][:200])