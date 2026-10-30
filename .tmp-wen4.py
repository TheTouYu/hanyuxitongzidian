import glob,re
for f in glob.glob(r"knowledge\**\*.md",recursive=True):
    t=open(f,encoding="utf-8").read()
    for m in re.finditer(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\r?\n\s*### ([^\r\n]*昷[^\r\n]*)",t):
        seg=t[m.end():m.end()+600]
        print(f.split("\\")[-1],m.group(1),m.group(2))
        print(seg.split("<!-- CLAIM:END")[0][:420].strip()[:420]);print("---")