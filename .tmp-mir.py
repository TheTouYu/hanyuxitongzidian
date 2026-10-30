import json,sys,os,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
R=r"D:\系统汉字"; C=os.path.join(R,"web","public","cards")
v=json.load(open(os.path.join(R,"web","public","variants.json"),encoding="utf-8"))
v={k:(x[0] if isinstance(x,list) else x) for k,x in v.items()}
idx=json.load(open(os.path.join(C,"index.json"),encoding="utf-8"))
have={x["c"] for x in idx}
made=[]
for s,t in v.items():
    for src,dst in ((s,t),(t,s)):
        if src in have and dst not in have:
            d=json.load(open(os.path.join(C,src+".json"),encoding="utf-8"))
            d=dict(d); d["char"]=dst
            json.dump(d,open(os.path.join(C,dst+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
            idx.insert(0,{"c":dst,"p":d.get("pinyin",""),"b":(d.get("bus") or [{}])[0].get("num",""),
                          "n":(d.get("bus") or [{}])[0].get("name",""),"lv":d.get("level",0),
                          "t":[x["text"][:60] for x in d.get("sections",[]) if x.get("text")][:3]})
            have.add(dst); made.append(src+"→"+dst)
json.dump(idx,open(os.path.join(C,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("mirrored",len(made)); print("; ".join(made))
print("index",len(idx))