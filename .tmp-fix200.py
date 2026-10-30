# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\app.html"
t=io.open(p,encoding="utf-8").read()
old="""    } else {
      html += render(s.text);
    }"""
new="""    } else {
      html += render(s.text);
    }
    if (s.gimgs && s.gimgs.length) {
      html += '<div class="glyphs many">' + s.gimgs.map((f, i) =>
        `<figure><img src="glyphs/${encodeURI(f)}" alt="参证字形${i + 1}" loading="lazy"><figcaption>${i + 1}</figcaption></figure>`).join('') + '</div>';
    }"""
assert old in t, "pattern missing"
t=t.replace(old,new,1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched app.html")