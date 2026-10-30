import os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("帝","蒂","示","市"):
    g=r"D:\系统汉字\web\public\glyphs\%s"%ch
    i=r"D:\系统汉字\web\public\glyphs\inline\%s"%ch
    print(ch,"glyphs",len(os.listdir(g)) if os.path.isdir(g) else 0,
          "inline",{d:len(os.listdir(os.path.join(i,d))) for d in os.listdir(i)} if os.path.isdir(i) else None)