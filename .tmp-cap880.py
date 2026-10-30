# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read()
for enc in ("gb18030","utf-16","utf-8"):
    try:
        t=raw.decode(enc)
        print(enc,"OK 字数",len(t)); print(repr(t[:120])); break
    except Exception as e: print(enc,"fail")