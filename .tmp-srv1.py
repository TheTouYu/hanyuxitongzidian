# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
ins=("  for (const s of (d.sections||[]).filter(x=>x.key===\"ziatt\")){\n"
     "    h+=\"<p><b>\"+ext(s.label||\"\")+\"</b> \"+((s.gimgs||[]).map(f=>\"<img class=\\\"cim\\\" src=\\\"/glyphs/\"+String(f).split(\"/\").map(encodeURIComponent).join(\"/\")+\"\\\" style=\\\"height:2.2em;margin:0 6px 0 2px\\\">\").join(\"\"))+\"</p>\";\n"
     "  }\n")
a="  try { const gi=glyphInfo(d.char);"
assert a in t and ins not in t
t=t.replace(a, ins+a,1)
b="  for (const s of (d.sections||[])){"
assert b in t
t=t.replace(b,"  for (const s of (d.sections||[])){ if (s.key===\"ziatt\") continue;",1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched")