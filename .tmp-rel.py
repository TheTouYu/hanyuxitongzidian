# -*- coding: utf-8 -*-
import io,re,sys,json,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
old="  $('#hint').textContent=q?`命中 ${rows.length} 张`:`共 ${IDX.length} 张卡`;"
new=("  const base=q?`命中 ${rows.length} 张`:`共 ${IDX.length} 张卡`;\n"
"  let rel='';\n"
"  if(q){const t=IDX.find(x=>x.c===q||x.a===q)||rows[0];\n"
"    if(t){const kids=IDX.filter(x=>x.pr===t.c).map(x=>x.c);\n"
"      const ln=(ch)=>`<a data-c=\"${esc(ch)}\" style=\"color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #c8a#;margin:0 2px;cursor:pointer\">${esc(ch)}</a>`;\n"
"      rel=`<span style=\"margin-left:14px\">字根　${t.pr?ln(t.pr):'—'}`+(kids.length?`　字族　${kids.map(ln).join('')}`:'')+`</span>`;\n"
"    }}\n"
"  }\n"
"  $('#hint').innerHTML=base+rel;\n"
"  document.querySelectorAll('#hint a[data-c]').forEach(a=>a.onclick=()=>open(a.dataset.c));")
assert old in s
s=s.replace(old,new)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
# index 增加 pr 字段
C=r"D:\系统汉字\web\public\cards"; items=[]
for f in glob.glob(C+r"\*.json"):
    b=os.path.basename(f)
    if b in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except Exception: continue
    bu=(d.get("bus") or [{}])[0]
    items.append({"c":d.get("trad") or d.get("char",""),"a":d.get("simp",""),"p":d.get("pinyin",""),"t":[x.get("label","") for x in d.get("sections",[]) if isinstance(x,dict)],"b":bu.get("num",0),"n":bu.get("name",""),"lv":d.get("level",0),"pr":d.get("parent","")})
items.sort(key=lambda x:x["c"]); json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("index",len(items),"with parent:",sum(1 for x in items if x["pr"]))