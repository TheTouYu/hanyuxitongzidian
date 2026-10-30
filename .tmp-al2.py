import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
old="  try{ d=await (await fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now())).json(); }"
new=("  try{ let r=await fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now());\n"
     "    if(!r.ok){ const it=IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch))); if(it&&it.c&&it.c!==ch){ ch=it.c; cur=ch; r=await fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now()); } }\n"
     "    if(!r.ok) throw 0; d=await r.json(); }")
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched open()")