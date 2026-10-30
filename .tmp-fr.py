import sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
idx={"飯":258,"返":259,"䡊":260,"阪":261,"昄":262,"汳":263,"叛":264,"眅":265,"瓪":266,"㽹":267,"㤆":268,"𡞟":269,"扳":270,"舨":271,"板":273,"蝂":274,"魬":275,"畈":276,"仮":277,"粄":278,"販":279,"版":280}
io.open(r"D:\系统汉字\.tmp-fanrows.json","w",encoding="utf-8").write(json.dumps({k:ps[v] for k,v in idx.items()},ensure_ascii=False))
print(len(idx))