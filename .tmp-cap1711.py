import hashlib,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in (r"D:\系统汉字\web\public\glyphs\photos\ㄗ\01.png", r"D:\系统汉字\web\public\glyphs\photos\卽\01.png", r"D:\系统汉字\web\public\glyphs\photos\卽\02.jpg"):
    print(p.split("photos\\")[1], hashlib.sha1(open(p,"rb").read()).hexdigest()[:12])