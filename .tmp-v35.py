import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for nm in ["第二章谷","卷八虎","第一章士","卷一雞"]:
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{nm}.json",encoding="utf-8"))
    g=[s for s in d["sections"] if s.get("key")=="zizu"]
    n=len(g[0]["groups"][0]["rows"]) if g else 0
    print(nm,"|",d.get("cname"),"|",d.get("chapterCard"),"|rows",n,"|links",len(g[0]["groups"][0].get("links",[])) if g else 0)
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print("total",len(idx),"chapters",sum(1 for x in idx if x.get("ch") and x.get("c","").startswith("第")),"volumes",sum(1 for x in idx if x.get("c","").startswith("卷")))