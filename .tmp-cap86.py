# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; s=io.open(p,encoding="utf-8").read()
if "DUPSEG" not in s:
    i=s.find("function serveStatic"); j=s.find("const pathname",i)
    ins='const DUPSEG=pathname.match(/^\\/glyphs\\/([^\\/]+)\\/\\1\\/(.+)$/); if(DUPSEG){pathname=`/glyphs/${DUPSEG[1]}/${DUPSEG[2]}`;} '
    s=s[:j]+ins+s[j:]; io.open(p,"w",encoding="utf-8",newline="\n").write(s); print("patched",i,j)
else: print("already")