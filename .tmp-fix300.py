# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\app.html"
t=io.open(p,encoding="utf-8").read()
old="""    if (s.gimgs && s.gimgs.length) {
      html += '<div class="glyphs many">' + s.gimgs.map((f, i) =>
        `<figure><img src="glyphs/${encodeURI(f)}" alt="参证字形${i + 1}" loading="lazy"><figcaption>${i + 1}</figcaption></figure>`).join('') + '</div>';
    }"""
new="""    if (s.gimgs && s.gimgs.length) {
      const grp = [];
      for (const f of s.gimgs) {
        const lab = String(f).includes('/') ? String(f).split('/')[0] : '';
        const last = grp[grp.length - 1];
        if (last && last.lab === lab) last.items.push(f); else grp.push({ lab, items: [f] });
      }
      let k = 0;
      html += grp.map(g =>
        `<div class="gimg-grp">` +
        (g.lab ? `<div class="gimg-lab">${esc(g.lab)}</div>` : '') +
        '<div class="glyphs many">' + g.items.map(f => {
          k += 1;
          return `<figure><img src="glyphs/${encodeURI(f)}" alt="参证字形${k}" loading="lazy"><figcaption>${k}</figcaption></figure>`;
        }).join('') + '</div></div>').join('');
    }"""
assert old in t
t=t.replace(old,new,1)
css=".gimg-grp{margin:6px 0 2px}\n.gimg-lab{font-size:13px;color:var(--acc,#8a5a2b);margin:2px 0 4px;letter-spacing:.05em}\n"
if ".gimg-grp{" not in t:
    t=t.replace("</style>", css+"</style>",1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched")