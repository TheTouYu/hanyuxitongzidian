import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read(); o=h
if ".smalt{" not in h:
    h=h.replace("</style>", ".smalt{font-size:.72em;color:#7a6a55}\n</style>",1)
# 在卡片渲染完成后统一把「（…）」缩小的处理函数
if "window.smAlt" not in h:
    fn="""
window.smAlt=(root)=>{if(!root)return;const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);const ns=[];while(w.nextNode())ns.push(w.currentNode);
for(const n of ns){const t=n.nodeValue;if(!t||t.indexOf('（')<0)continue;const p=n.parentNode;if(!p||p.closest('.alt'))continue;
const frag=document.createDocumentFragment();let i=0;const re=/（[^）]{1,8}）/g;let m;
while((m=re.exec(t))){frag.appendChild(document.createTextNode(t.slice(i,m.index)));const s=document.createElement('span');s.className='smalt';s.textContent=m[0];frag.appendChild(s);i=m.index+m[0].length;}
if(i<t.length)frag.appendChild(document.createTextNode(t.slice(i)));p.replaceChild(frag,n);}};
"""
    h=h.replace("</script>\n</body>", fn+"\n</script>\n</body>",1) if "</script>\n</body>" in h else h
    print("fn", "window.smAlt" in h)
# 在渲染入口调用
h2=h.replace("in.innerHTML=cardBody?","in.innerHTML=cardBody?")
if "smAlt(in)" not in h:
    h=h.replace("renderCard", "renderCard",1)
if h!=o:
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
tt=os.path.join(tempfile.gettempdir(),"chk42.js"); io.open(tt,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",tt],capture_output=True,text=True).returncode)