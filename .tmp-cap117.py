# -*- coding: utf-8 -*-
import glob,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\字谱智能体"; one=os.path.join(src,"单栏"); bak=os.path.join(src,"_原始备份")
os.makedirs(bak,exist_ok=True)
orig=sorted(glob.glob(src+r"\*.docx"))
n1=0
for f in orig:
    t=os.path.join(bak,os.path.basename(f))
    if not os.path.exists(t): shutil.copy2(f,t); n1+=1
print("备份",n1,"/",len(orig))
n2=0
for f in sorted(glob.glob(one+r"\*.docx")):
    shutil.copy2(f,os.path.join(src,os.path.basename(f))); n2+=1
print("覆盖",n2)