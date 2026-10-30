import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open("web/public/app.html",encoding="utf-8").read().split("\n")
for i,l in enumerate(t):
    if "index.json" in l or "IDX" in l or "SEARCH" in l or "hits" in l.lower():
        print(i+1,"|",l.strip()[:160])