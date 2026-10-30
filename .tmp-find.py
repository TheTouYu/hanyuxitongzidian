import sys,os,re,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
root=r"D:\字谱智能体"
name=sys.argv[1]
for f in os.listdir(root):
    if not f.endswith(".docx"): continue
    from docx import Document
    doc=Document(os.path.join(root,f))
    for k,p in enumerate(doc.paragraphs):
        t=p.text.strip()
        if t.startswith(name) or ("（"+name in t[:12]):
            print(f,k,t[:100])