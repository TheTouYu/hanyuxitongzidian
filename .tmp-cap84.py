import glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in sorted(glob.glob(r"D:\系统汉字\web\public\glyphs\祡\*.png"))[:4]:
    b=open(f,"rb").read(12); print(f.split("\\")[-1], b[:8])