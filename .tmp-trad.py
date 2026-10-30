import io,sys,json,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
# 1) 规则
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
rule="""
### 字头用繁体、简体可搜（2026-10-24 主人定）

字卡一律以**原文繁体本字**为字头、正文也用繁体呈现；简体只作检索别名：

- 卡结构加两个字段：`trad`（繁体本字，显示用）、`simp`（对应简体，检索用）；字卡 `char` 取繁体。
- 搜索索引同时收繁体与简体（`c`＝繁体、`a`＝简体别名），查简体照样命中。
- **本义**栏首句须交代简体对应，如「衞……今简体作“卫”」「榖……今简化为“谷”之借字」。
"""
assert "字头用繁体" not in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.rstrip()+"\n"+rule)
# 2) test.html: 搜索支持 a 别名
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
s=s.replace("const exact=IDX.filter(x=>x.c===q);","const exact=IDX.filter(x=>x.c===q||x.a===q);",1)
s=s.replace("IDX.filter(x=>x.c!==q&&(norm(x.p).startsWith(q)||x.t.some(t=>norm(t).includes(q))))",
            "IDX.filter(x=>x.c!==q&&norm(x.a)!==q&&(norm(x.p).startsWith(q)||x.t.some(t=>norm(t).includes(q))))",1)
s=s.replace("return IDX.filter(x=>norm(x.c).includes(q)||norm(x.p).includes(q)||x.t.some(t=>norm(t).includes(q))).slice(0,120);",
            "return IDX.filter(x=>norm(x.c).includes(q)||norm(x.a||'').includes(q)||norm(x.p).includes(q)||x.t.some(t=>norm(t).includes(q))).slice(0,120);",1)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
# 3) 索引带 a
C=r"D:\系统汉字\web\public\cards"
items=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except: continue
    b=(d.get("bus") or [{}])[0]
    num,name=(b.get("num",0),b.get("name","")) if isinstance(b,dict) else (0,b)
    tags=[x.get("label","") for x in d.get("sections",[]) if isinstance(x,dict)]
    if name: tags.append(name+"部")
    items.append({"c":d.get("trad") or d.get("char",""),"a":d.get("simp",""),"p":d.get("pinyin",""),"t":tags,"b":num,"n":name,"lv":d.get("level",0)})
items.sort(key=lambda x:x["c"])
json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("rule+ui+index ok",len(items))