# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\慮.json"
d=json.load(io.open(p,encoding="utf-8"))
d["rootLevel"]=3        # 客户端据此显示「三級字根」
d["level"]=3; d["parent"]="盧"
d["grade"]="三级字根"    # 服务端据此显示「三级字根」
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print({k:d[k] for k in ("char","level","parent","rootLevel","grade")})