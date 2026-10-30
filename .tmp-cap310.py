# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    m=re.search(r"const isZX\s*=\s*[^\n;]+",h)
    print(os.path.basename(f),"->",m.group(0)[:120] if m else "NO isZX")