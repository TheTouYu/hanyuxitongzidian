# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ch="\U000208EC"
for fp in (r"C:\Windows\Fonts\simsun.ttc", r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\mingliu.ttc"):
    try:
        f=ImageFont.truetype(fp,52)
        im=Image.new("L",(72,72),255); d=ImageDraw.Draw(im); d.text((6,2),ch,font=f,fill=0)
        out=r"D:\系统汉字\web\public\glyphs\chars\208ec.png"
        im.save(out); print("ok",fp)
        break
    except Exception as e: print("fail",fp,e)