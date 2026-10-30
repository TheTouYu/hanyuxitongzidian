# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"; s=io.open(h,encoding="utf-8").read()
old_start=s.find("      const root=chain.length?chain[0]:t.c;")
old_end=s.find("      rel=`<span")
assert old_start>0 and old_end>old_start
new=("      const kids=IDX.filter(x=>x.pr===t.c).map(x=>x.c);\n"
"      const sibs=t.pr?IDX.filter(x=>x.pr===t.pr&&x.c!==t.c).map(x=>x.c):[];\n"
"      const ln=(ch)=>`<a data-c=\"${esc(ch)}\" style=\"color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer\">${esc(ch)}</a>`;\n"
"      const rl=chain.length?chain.slice().reverse().map(ln).join(' → '):'—';\n"
"      const fam=kids.length?`　字族　${kids.map(ln).join('')}`:(sibs.length?`　同族（${t.pr}）　${sibs.map(ln).join('')}`:'');\n")
s=s[:old_start]+new+s[old_end:]
s=s.replace("      rel=`<span style=\"margin-left:14px\">字根　${rl}`+(kids.length?`　字族　${kids.map(ln).join('')}`:'')+`</span>`;",
            "      rel=`<span style=\"margin-left:14px\">字根　${rl}`+fam+`</span>`;")
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("patched")