# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="""        const hit = items.find((it) => (it.a || []).includes(ch));
        if (hit && hit.c && existsSync(join(CARD_DIR, hit.c + '.json'))) {
          res.writeHead(302, { Location: '/card/' + encodeURIComponent(hit.c) }); return res.end();
        }"""
new="""        const hits = items.filter((it) => (it.a || []).includes(ch) && it.c && existsSync(join(CARD_DIR, it.c + '.json')));
        if (hits.length === 1) {
          res.writeHead(302, { Location: '/card/' + encodeURIComponent(hits[0].c) }); return res.end();
        }
        if (hits.length > 1) {
          const seen = new Set(); const links = [];
          for (const h of hits) { if (seen.has(h.c)) continue; seen.add(h.c); links.push('<li><a href="/card/'+encodeURIComponent(h.c)+'">'+escH(h.c)+'</a>'+(h.h&&h.h!==h.c?'（'+escH(h.h)+'）':'')+'</li>'); }
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
          return res.end('<!doctype html><meta charset="utf-8"><h3>「'+escH(ch)+'」兼作多字的或体</h3><p>请选择要看的字头：</p><ul>'+links.join('')+'</ul>');
        }"""
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched resolver")