# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"; s=io.open(h,encoding="utf-8").read()
old="      const ln=(ch)=>`<a data-c=\"${esc(ch)}\""
new=("      const ln=(ch)=>{const it=IDX.find(x=>x.c===ch||x.a===ch);const lab=(it&&it.a)?(it.c+'（'+it.a+'）'):ch;return `<a data-c=\"${esc(ch)}\"")
assert old in s
s=s.replace(old,new,1)
# 关闭箭头函数：原行以 >${esc(ch)}</a>`; 结尾
old2="cursor:pointer\">${esc(ch)}</a>`;"
new2="cursor:pointer\">${esc(lab)}</a>`;};"
assert old2 in s
s=s.replace(old2,new2,1)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("patched chips label")