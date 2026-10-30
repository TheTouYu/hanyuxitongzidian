import docx,re,glob,os,json
chars=set("情慍懼憾懌悔恨怖怯恭恥悉慰慷慨慕憲愆懲憊惕悚惋懣懃愍憫憨懇戀志忠忌忘忍忽怠惟惰意愚慈慧想愁心杺芯伈訫孞吢応沁鈊抋")
ent={}
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except Exception: continue
    cur=None
    for t in ps:
        h=re.match(r"^(\d{3})\.([^\s：]{1,6})",t)
        if h and ("部" in t[:24]): cur=(int(h.group(1)),h.group(2).replace("部","")); continue
        m=re.match(r"^([\u4e00-\u9fff])(（[^）]*）)?[：:]",t)
        if m and m.group(1) in chars and cur:
            c=m.group(1)
            if c not in ent or (cur[0]<ent[c][0]):
                ent[c]=(cur[0],cur[1],os.path.basename(f))
for c in sorted(chars):
    v=ent.get(c)
    print(c, v if v else "—")
print("found",len(ent),"/",len(chars))
json.dump({k:list(v) for k,v in ent.items()},open(r"D:\系统汉字\.tmp-ent.json","w",encoding="utf-8"),ensure_ascii=False)