# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="""h+='<div class="gs">'+gi.files.map((u,i)=>'<figure><img src="'+u+'" alt="字形'+(i+1)+'">"""
new="""h+='<div class="gs">'+gi.files.map((u,i)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="字形'+(i+1)+'">"""
assert old in t, "anchor"
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched cache-bust")