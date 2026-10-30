# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="""  if (path.startsWith('/card/')) {
    const ch = decodeURIComponent(path.slice(6)).replace(/\\.html$/, '');
    const html = renderCard(ch);"""
new="""  if (path.startsWith('/card/')) {
    let ch = decodeURIComponent(path.slice(6)).replace(/\\.html$/, '');
    try {
      if (!existsSync(join(CARD_DIR, ch + '.json'))) {
        const idx = JSON.parse(readFileSync(join(CARD_DIR, 'index.json'), 'utf8'));
        const items = Array.isArray(idx) ? idx : (idx.items || []);
        const hit = items.find((it) => (it.a || []).includes(ch));
        if (hit && hit.c && existsSync(join(CARD_DIR, hit.c + '.json'))) {
          res.writeHead(302, { Location: '/card/' + encodeURIComponent(hit.c) }); return res.end();
        }
      }
    } catch (e) {}
    const html = renderCard(ch);"""
assert old in t, "anchor"
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")