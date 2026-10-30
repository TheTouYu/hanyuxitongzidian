import io,json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V={"干":["乾","幹"],"斗":["鬥"],"谷":["榖"],"发":["發","髪"],"里":["裏"],"台":["臺"],"蜡":["蠟"],"松":["鬆"],"姜":["薑"],
   "云":["雲"],"后":["後"],"系":["係","繫"],"复":["復","複","覆"],"只":["祇","隻"],"蒙":["濛","矇","懞"],"冲":["沖","衝"]}
p=r"D:\系统汉字\web\public\cards\variants.json"
json.dump(V,open(p,"w",encoding="utf-8"),ensure_ascii=False)
h=r"D:\系统汉字\web\public\test.html"
t=io.open(h,encoding="utf-8").read()
assert "async function open(ch)" in t
if "VARIANT_MAP" not in t:
    t=t.replace("async function open(ch)",
"""let VARIANT_MAP=null;
async function variantsFor(ch){
  if(!VARIANT_MAP){
    try{VARIANT_MAP=await (await fetch('cards/variants.json?v='+Date.now())).json();}catch(e){VARIANT_MAP={};}
  }
  const list=VARIANT_MAP[ch]||[];
  if(!list.length) return '';
  const btns=list.map(v=>`<button class="vbtn" onclick="open('${v}')">${v}</button>`).join(' ');
  return `<div class="vbox"><span>对应繁体/借字：</span>${btns}<span class="vnote">（分卡各释本义，勿混）</span></div>`;
}
async function open(ch)""",1)
    t=t.replace("const data = await (await fetch('cards/'+ch+'.json?v='+Date.now())).json();",
"const data = await (await fetch('cards/'+ch+'.json?v='+Date.now())).json();\n  const vhtml = await variantsFor(ch);\n  const vwhere = document.getElementById('vslot'); if(vwhere) vwhere.innerHTML=vhtml;",1)
    if "vslot" not in t.split("function render")[0]:
        t=t.replace("<div id=\"detail\">","<div id=\"vslot\"></div><div id=\"detail\">",1)
    t=t.replace("</style>",".vbox{margin:8px 0;padding:8px 10px;background:#f6f0e4;border:1px solid #e2d4b8;border-radius:6px;font-size:14px}\n.vbtn{margin:0 4px;padding:2px 8px;border:1px solid #c9a86a;background:#fff;border-radius:4px;cursor:pointer}\n.vnote{color:#8a7a5c;font-size:12px}\n</style>",1)
    io.open(h,"w",encoding="utf-8",newline="\n").write(t)
    print("patched html")