import docx,re,glob,os,json
chars=set("情慍懼憾懌悔恨怖怯恭恥悉慰慷慨慕憲愆懲憊惕悚惋懣懃愍憫憨懇戀志忠忌忘忍忽怠惟惰意愚慈慧想愁心杺芯伈訫孞吢応沁鈊抋")
res={}
pat=re.compile(r"^([\u4e00-\u9fff])(（[^）]*）)?([a-zA-Z\u0100-\u01ff\u0300-\u036f]{2,})")
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except Exception: continue
    cur=None
    for t in ps:
        h=re.match(r"^(\d{3})[.．、]\s*([^\s：]{1,4})",t)
        if h and len(t)<14: cur=(int(h.group(1)),h.group(2).replace("部","")); continue
        if not cur or not t: continue
        m=pat.match(t)
        if m and m.group(1) in chars and m.group(1) not in res: res[m.group(1)]=(cur[0],cur[1])
json.dump({k:list(v) for k,v in res.items()},open(r"D:\系统汉字\.tmp-ent4.json","w",encoding="utf-8"),ensure_ascii=False)
print("found",len(res),"/",len(chars))
print([ (c,res[c]) for c in sorted(res)][:40])