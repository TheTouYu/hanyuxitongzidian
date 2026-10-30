# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
x=json.load(io.open(p,encoding="utf-8"))
d=r"D:\系统汉字\web\public\glyphs\𦣞"
files=sorted("𦣞/"+f for f in os.listdir(d))
x["chars"]["𦣞"]={"doc":"第12部 𦣞部","desc":"象牙床形","variants":["𦣝"],"files":files}
s=json.dumps(x,ensure_ascii=False,indent=1)
s=s.encode("utf-8","replace").decode("utf-8")
io.open(p,"w",encoding="utf-8",newline="\n").write(s)
y=json.load(io.open(p,encoding="utf-8")); print("ok",len(y["chars"]),"𦣞" in y["chars"],len(files))