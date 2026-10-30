# -*- coding: utf-8 -*-
import sys,os
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ch="\U000208EC"; outdir=r"D:\系统汉字\.tmp-ch"
os.makedirs(outdir,exist_ok=True)
for name in ("msyh.ttc","msyhbd.ttc","simhei.ttf","simkai.ttf","mingliu.ttc","msgothic.ttc","arialuni.ttf","seguisym.ttf"):
    fp=os.path.join(r"C:\Windows\Fonts",name)
    if not os.path.exists(fp): print("no",name); continue
    try:
        f=ImageFont.truetype(fp,52,index=0)
        im=Image.new("L",(72,72),255); d=ImageDraw.Draw(im); d.text((6,2),ch,font=f,fill=0)
        px=im.load(); dark=sum(1 for y in range(72) for x in range(72) if px[x,y]<128)
        im.save(os.path.join(outdir,name.replace('.','_')+".png"))
        print(name,"dark",dark)
    except Exception as e: print("fail",name,e)