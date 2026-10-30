import json,io,sys
from docx import Document
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
C=r'D:\系统汉字\web\public\cards'
ps=[p.text.strip() for p in Document(r'D:\字谱智能体\卷六  鶴.docx').paragraphs]
def join_(a,b):
    out=[]
    for i in range(a,b):
        t=ps[i]
        if not t: continue
        if t.startswith('轉義：'): t=t[3:]
        out.append(t)
    return chr(10).join(out)
for name,a,b in (('隺',35,41),('靃',75,78)):
    p=C+chr(92)+name+'.json'
    d=json.load(io.open(p,encoding='utf-8'))
    for s in d['sections']:
        if s['key']=='zhuanyi': s['text']=join_(a,b)
    json.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(name,'ok',len([s for s in d['sections'] if s['key']=='zhuanyi'][0]['text']))