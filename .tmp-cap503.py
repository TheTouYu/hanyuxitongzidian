import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-cap502.py"
t=io.open(p,encoding="utf-8").read()
t=t.replace('"昹":"ǎi→零聲母":"",','"昹":"零聲母（ǎi），緒論七組未列，不系（照實）。",')
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched")