import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
t=io.open(h,encoding="utf-8").read()
if "const vhtml=await variantsFor(ch);" not in t:
    t=t.replace("  const g=(GLYPH[ch]&&(GLYPH[ch].files||[]))||[];",
                "  const vhtml=await variantsFor(ch);\n  const g=(GLYPH[ch]&&(GLYPH[ch].files||[]))||[];",1)
    t=t.replace('main.innerHTML=`<div class="card"><div class="chead">',
                'main.innerHTML=`${vhtml}<div class="card"><div class="chead">',1)
    io.open(h,"w",encoding="utf-8",newline="\n").write(t)
print("vhtml_in:", "const vhtml=await" in t, "| injected:", "`${vhtml}<div class=\"card\">" in t)