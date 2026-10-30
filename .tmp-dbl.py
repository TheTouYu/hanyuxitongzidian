import glob,docx,re,os,json
T="忠忍恥悉恭悔悚惋惰想愁愆慧慷憨憫憾懇懲戀"
ent={};fam={}
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except: continue
    cur=None
    for t in ps:
        h=re.match(r"^(\d{3})[.．、]\s*([^\s：]{1,4})",t)
        if h and len(t)<16: cur=(int(h.group(1)),h.group(2).replace("部","")); continue
        if not cur: continue
        m=re.match(r"^([\u4e00-\u9fff])[（(][^）)]*[）)]?([a-zA-Z\u0100-\u01ff]{2,})",t) or re.match(r"^([\u4e00-\u9fff])([a-zA-Z\u0100-\u01ff]{2,})",t)
        if m and m.group(1) in T and m.group(1) not in ent: ent[m.group(1)]=(cur,m.group(0)[:28])
        fm=re.match(r"^([\u4e00-\u9fff]{1,2})(（[^）]*）)?：(.{4,})",t)
        if fm:
            for c in T:
                if c in fm.group(3) and c not in fam: fam[c]=(cur,fm.group(1),t[:30])
for c in T:
    print(c,"E:",ent.get(c),"| F:",fam.get(c))