import hashlib,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
def h(p):
    return hashlib.sha1(open(p,"rb").read()).hexdigest()[:12]
for c in ("霾","貍","士","野"):
    p=rf"D:\系统汉字\web\public\glyphs\photos\{c}\01.jpg"
    try: print(c,h(p))
    except Exception as e: print(c,"none")