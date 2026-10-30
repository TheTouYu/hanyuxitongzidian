import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
ch=[x["c"] for x in idx if x.get("c","").startswith("第") and "章" in x["c"]]
vo=[x["c"] for x in idx if x.get("c","").startswith("卷")]
print("章",len(ch),sorted(ch)[:3],"卷",len(vo),"有卷一百壽:", "卷一百壽" in vo)
d=json.load(io.open(r"D:\系统汉字\web\public\cards\卷一百壽.json",encoding="utf-8"))
g=[s for s in d["sections"] if s.get("key")=="zizu"][0]["groups"][0]
print("卷一百",d["cname"],"rows",len(g["rows"]),"links",len(g["links"]))
c=json.load(io.open(r"D:\系统汉字\web\public\cards\第十二章老.json",encoding="utf-8"))
gc=[s for s in c["sections"] if s.get("key")=="zizu"][0]["groups"][0]
print("第十二章",c["cname"],"rows",len(gc["rows"]))