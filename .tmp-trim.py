# -*- coding: utf-8 -*-
import sys,os
from PIL import Image
import numpy as np
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\碬\01.png"
im=Image.open(p).convert("RGB"); a=np.array(im); h=a.shape[0]
# 底部图注条（白底 46px）
cap=im.crop((0,h-46,im.width,h))
photo=im.crop((0,0,im.width,h-46))
b=np.array(photo).mean(axis=(1,2))
cut=len(b)
for y in range(len(b)-1,-1,-1):
    if b[y]>70: break
    cut=y
photo=photo.crop((0,0,photo.width,max(cut,10)))
out=Image.new("RGB",(photo.width,photo.height+46),(255,255,255))
out.paste(photo,(0,0)); out.paste(cap,(0,photo.height))
out.save(p); print("trimmed",photo.size,"->",out.size)