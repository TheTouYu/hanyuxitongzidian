from PIL import Image, ImageDraw, ImageFont
import os
SRC=r"D:\系统汉字\web\public\glyphs\羅"; OUT=r"D:\系统汉字\intake\20261021-释罗-字形.png"
fh=ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc",28); fn=ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc",20)
fs=sorted(f for f in os.listdir(SRC) if f.endswith(".png"))
ims=[Image.open(os.path.join(SRC,f)).convert("RGB") for f in fs]
H=190; ims=[i.resize((int(i.width*H/i.height),H),Image.LANCZOS) for i in ims]
GAP,COLS,M=26,7,40
rows=[ims[i:i+COLS] for i in range(0,len(ims),COLS)]
T="羅（网部字族，从网从維）—— 以丝罟鸟；甲骨文作「网＋隹」，象网罩住鸟"
W=int(max(max(sum(i.width for i in r)+GAP*(len(r)-1) for r in rows), fh.getlength(T)))+2*M
Hh=24+44+len(rows)*(H+8)+70
img=Image.new("RGB",(W,Hh),"white"); d=ImageDraw.Draw(img)
d.text((M,22),T,font=fh,fill=(25,25,25)); y=22+44
for r in rows:
    x=M
    for i in r: img.paste(i,(x,y)); x+=i.width+GAP
    y+=H+8
d.text((M,y+10),"「䍜」是羅的初文：网罩住鸟，令其不飞走；春秋金文加「糸」，才成「羅」。",font=fn,fill=(110,104,98))
d.text((M,y+40),"简化字「罗」本身无古文字字形，取「羅」的字形。",font=fn,fill=(130,124,118))
img.save(OUT); print(OUT,img.size,len(ims))