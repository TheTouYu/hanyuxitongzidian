# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-huo.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace('if key not in MB: return \'y「零聲母」不系：零聲母，緒論七組未列（照實）。\'',
            'if key not in MB or key=="y": return \'y「零聲母」不系：零聲母，緒論七組未列（照實）。\'')
io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("ok")