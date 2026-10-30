import os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
I=set(os.listdir(r"D:\系统汉字\web\public\glyphs\inline"))
C=set(f[:-5] for f in os.listdir(r"D:\系统汉字\web\public\cards") if f.endswith(".json"))
print("inline字头",len(I),"卡字头",len(C),"交集",len(I&C))
print("仅inline样例",sorted(I-C)[:10])