# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"
t=io.open(p,encoding="utf-8").read()
add='''
def _rows_ok(d, err, bu):
    for s in d.get("sections", []):
        if s.get("key") != "zizu":
            continue
        for g in s.get("groups", []):
            for r in g.get("rows", []):
                if not isinstance(r, list) or len(r) < 4:
                    err.append(f"{bu}: 族表行不足四格 {r!r}")
                elif not (r[2] or "").strip():
                    err.append(f"{bu}: 族表「{r[0]}」类属为空")
'''
if "_rows_ok" not in t:
    t=t.replace("def main", add+"\ndef main",1)
    t=t.replace("    return err", "    _rows_ok(d, err, bu)\n    return err",1) if "    return err" in t else t
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
    print("patched")
else: print("already")