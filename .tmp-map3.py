import docx,re,glob,os,json
def iscjk(ch): return '\u4e00'<=ch<='\u9fff' or '\u3400'<=ch<='\u4dbf' or '\uf900'<=ch<='\ufaff'
m={}
files=sorted(glob.glob(r"D:\字谱智能体\*.docx"))
for f in files:
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except Exception: continue
    cur=None
    for t in ps:
        h=re.match(r"^(\d{3})\.([^\s：]+)",t)
        if h and ("部" in t[:20] or len(h.group(2))<=3):
            cur=(int(h.group(1)),h.group(2).replace("部",""))
            continue
        if cur and "：" in t and len(t)<400:
            head=t.split("：")[0]
            if sum(1 for c in head if iscjk(c))>=1 and ("（" in head or len(head)<60):
                for c in head:
                    if iscjk(c) and c not in m: m[c]=cur
json.dump({k:v for k,v in m.items()},open(r"D:\系统汉字\.tmp-charbu2.json","w",encoding="utf-8"),ensure_ascii=False)
print("files",len(files),"chars",len(m))
chars="情慍懼憾懌悔恨怖怯恭恥悉慰慷慨慕憲愆懲憊惕悚惋懣懃愍憫憨懇戀志忠忌忘忍忽怠惟惰意愚慈慧想愁心杺芯伈訫孞吢応沁鈊抋"
ok=0
for c in chars:
    v=m.get(c)
    if v: ok+=1
    print(c,v)
print("resolved",ok,"/",len(chars))