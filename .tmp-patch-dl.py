# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\delogo.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace("        r.save(p,quality=92); n+=1; touched.append(ch+\"/\"+f)",
"""        try:
            r.save(p,quality=92); n+=1; touched.append(ch+"/"+f)
        except Exception as e:
            fails.append(ch+"/"+f+":"+type(e).__name__)""")
t=t.replace("n=0; touched=[]","n=0; touched=[]; fails=[]")
t=t.replace('print("cleaned",n); print(touched[:15])','print("cleaned",n); print("failed",len(fails),fails[:5]); print(touched[:10])')
io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("patched")