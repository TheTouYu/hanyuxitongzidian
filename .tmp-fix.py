import io,os,json
CARDS=r"web\public\cards"
fix={"裹":254,"窠":256,"稞":259,"裸":261,"輠":255,"蜾":257,"粿":260,"惈":262}
for ch,pg in fix.items():
    fp=os.path.join(CARDS,ch+".json")
    c=json.load(io.open(fp,encoding="utf-8"))
    out=[]
    for s in c["sections"]:
        if isinstance(s,list):
            s={"key":s[0],"label":s[1],"text":s[2],"cites":[]}
        if s.get("key")=="xing":
            s["text"]=f"字形图：本部字头（果）之古文字形见 intake/20261022-释涡-字形.png 同批抽图；本字原稿插图见 web/public/glyphs/photos/{ch}/01.jpg（原稿 p{pg}）。"
        out.append(s)
    c["sections"]=out
    io.open(fp,"w",encoding="utf-8",newline="\n").write(json.dumps(c,ensure_ascii=False,indent=1))
    print(ch,"ok",len(out))