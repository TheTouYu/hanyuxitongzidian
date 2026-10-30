# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    # 给单卡与字根卡请求加缓存戳
    h=re.sub(r"fetch\('cards/'\+\s*([A-Za-z0-9_.]+)\+'\.json'\)", r"fetch('cards/'+\1+'.json?v='+Date.now())", h)
    h=re.sub(r"fetch\('cards/'\+\s*(encodeURIComponent\([^)]*\))\+'\.json'\)", r"fetch('cards/'+\1+'.json?v='+Date.now())", h)
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    else: print(os.path.basename(f),"no-change")
    print("  has", h.count(".json?v='+Date.now()"))