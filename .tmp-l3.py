import re
for f in [r"D:\系统汉字\knowledge\hanzi-yinyuan\03d-yi-jie.md", r"D:\系统汉字\knowledge\hanzi-yinyuan\11a-zhu.md"]:
    t=open(f,encoding="utf-8").read()
    print("==",f.split("\\")[-1])
    for cid,title,body in re.findall(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n(.*?)#### 适用边界", t, re.S):
        if "ㄗ" in title or "ㄗ" in body[:120] or title.startswith("南"):
            print(cid, title.strip()[:40], "|", body.strip().replace("\n"," ")[:110])