# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8",errors="surrogateescape").read()
anchor="  const path = url.pathname;"
if "/card/" in t:
    print("already"); raise SystemExit
ins=anchor+"""
  if (path.startsWith('/card/')) {
    const ch = decodeURIComponent(path.slice(6)).replace(/\\.html$/, '');
    const html = renderCard(ch);
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
    return res.end(html || '<!doctype html><meta charset="utf-8"><p>没有这个字。</p>');
  }"""
assert anchor in t
t=t.replace(anchor,ins,1)
io.open(p,"w",encoding="utf-8",errors="surrogateescape",newline="\n").write(t)
print("route added")