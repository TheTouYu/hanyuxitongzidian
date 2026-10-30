import io,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in glob.glob(r"D:\系统汉字\web\public\*.html")+glob.glob(r"D:\系统汉字\web\*.html"):
    t=io.open(f,encoding="utf-8").read()
    if "命中" in t:
        print(f, "alias" if "(x.a||[])" in t or "x.a||[]" in t else "NO-ALIAS", len(t))