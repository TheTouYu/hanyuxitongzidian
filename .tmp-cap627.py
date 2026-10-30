import hashlib,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
def hs(d):
    p=rf"D:\系统汉字\web\public\glyphs\{d}"
    return {f:hashlib.sha1(open(os.path.join(p,f),"rb").read()).hexdigest()[:8] for f in sorted(os.listdir(p))}
z=hs("智"); zhi=hs("知")
print("智",z); print("知",zhi)
print("相同", set(z.values())&set(zhi.values()))