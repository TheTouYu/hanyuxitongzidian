# -*- coding: utf-8 -*-
"""去掉插图角落的水印/logo：只在四个角落区检测“高亮低饱和”文字块，用邻域中值填充。"""
import os,sys
from PIL import Image, ImageFilter
import numpy as np
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字\web\public\glyphs\photos"
def corners(w,h):
    return [(0,int(h*0.82),int(w*0.40),h),(int(w*0.60),int(h*0.82),w,h),
            (0,0,int(w*0.40),int(h*0.16)),(int(w*0.60),0,w,int(h*0.16))]
def clean(im):
    a=np.asarray(im.convert("RGB")).astype(np.int16); h,w,_=a.shape
    r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    mx=a.max(2); mn=a.min(2); sat=mx-mn
    mask=np.zeros((h,w),bool)
    for x0,y0,x1,y1 in corners(w,h):
        sub=(mx[y0:y1,x0:x1]>=215)&(sat[y0:y1,x0:x1]<=45)
        if sub.sum()<40: continue
        # 仅当该角落存在成块的亮斑（水印/logo）时启用
        m=np.zeros((h,w),bool); m[y0:y1,x0:x1]=sub
        mask|=m
    if mask.sum()<40: return None
    med=np.asarray(Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.MedianFilter(9))).astype(np.int16)
    out=a.copy(); out[mask]=med[mask]
    return Image.fromarray(out.astype(np.uint8))
n=0; touched=[]; fails=[]
for ch in sorted(os.listdir(ROOT)):
    d=os.path.join(ROOT,ch)
    if not os.path.isdir(d): continue
    for f in sorted(os.listdir(d)):
        if not f.lower().endswith((".jpg",".jpeg",".png")): continue
        p=os.path.join(d,f)
        try: im=Image.open(p)
        except Exception: continue
        r=clean(im)
        if r is None: continue
        try:
            r.save(p,quality=92); n+=1; touched.append(ch+"/"+f)
        except Exception as e:
            fails.append(ch+"/"+f+":"+type(e).__name__)
print("cleaned",n); print("failed",len(fails),fails[:5]); print(touched[:10])