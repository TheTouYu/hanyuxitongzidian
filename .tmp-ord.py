import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
if "const SEC_ORDER" not in s:
    s=s.replace("async function cardBody(ch,d){",
"""const SEC_ORDER=['benyi','benyi2','zhuanyi','bianzheng','yinyuan','shengmu','zizu','zigen'];
const secRank=k=>{const i=SEC_ORDER.indexOf(k);return i<0?99:i;};
async function cardBody(ch,d){""",1)
    # 排序：在 secs 定义后插入
    s=s.replace("const secs=(d.sections||[]).filter(s=>!isZX(s)).map(s=>{",
                "const secs=(d.sections||[]).filter(s=>!isZX(s)).sort((a,b)=>secRank(a.key)-secRank(b.key)).map(s=>{",1)
    io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("order applied:", "SEC_ORDER" in s, "| sort:", "secRank(a.key)" in s)