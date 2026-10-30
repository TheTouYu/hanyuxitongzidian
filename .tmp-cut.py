# -*- coding: utf-8 -*-
import sys,os
from PIL import Image, ImageDraw
from collections import deque
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\系统汉字\web\public\glyphs\photos\砨\01.jpg"
im=Image.open(src).convert("RGB").crop((25,140,600,410))
w,h=im.size; px=im.load()
def near(c1,c2,t=38): return abs(c1[0]-c2[0])<=t and abs(c1[1]-c2[1])<=t and abs(c1[2]-c2[2])<=t
seeds=[(0,0),(w-1,0),(0,h-1),(w-1,h-1)]
bg=[px[x,y] for x,y in seeds]
seen=[[False]*w for _ in range(h)]
q=deque()
for x in range(w):
    for y in (0,h-1):
        q.append((x,y))
for y in range(h):
    for x in (0,w-1):
        q.append((x,y))
while q:
    x,y=q.popleft()
    if x<0 or y<0 or x>=w or y>=h or seen[y][x]: continue
    c=px[x,y]
    if not any(near(c,b,30) for b in bg): continue
    seen[y][x]=True; px[x,y]=(255,255,255)
    q.extend(((x+1,y),(x-1,y),(x,y+1),(x,y-1)))
out=r"D:\系统汉字\web\public\glyphs\photos\砨\01.png"
im.save(out)
print("saved",im.size)