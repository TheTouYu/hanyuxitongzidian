# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; s=io.open(p,encoding="utf-8").read()
s=re.sub(r"\}\);const DUPSEG=.*?\n", "});\n", s, flags=re.S)
line="async function serveStatic(res, pathname) {\n"
fix=line+"  pathname = pathname.replace(/^\\/glyphs\\/([^\\/]+)\\/\\1\\/(.+)$/, '/glyphs/$1/$2');\n"
if "pathname = pathname.replace" not in s:
    s=s.replace(line, fix, 1)
io.open(p,"w",encoding="utf-8",newline="\n").write(s)
print("dup removed:", "DUPSEG" not in s, "fix in:", "pathname = pathname.replace" in s)