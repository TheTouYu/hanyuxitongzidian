import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=io.open(r"D:\系统汉字\.tmp-page.js",encoding="utf-8").read()
idx=json.load(open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
pre='''const __store={};
function __el(id){return {id,innerHTML:"",textContent:"",dataset:{},addEventListener(){},querySelectorAll:()=>[],style:{},classList:{add(){},remove(){}}};}
globalThis.document={querySelector:(s)=>{const k=s.replace("#","");__store[k]=__store[k]||__el(k);return __store[k];},querySelectorAll:()=>[],addEventListener(){},createElement:()=>__el("x"),getElementById:()=>__el("x")};
globalThis.window={};globalThis.fetch=async()=>({json:async()=>({})});globalThis.location={search:""};
'''
suf='''
IDX=__IDX; try{ render("疑"); console.log("HINT", JSON.stringify(__store["hint"].innerHTML).slice(0,400)); }catch(e){ console.log("ERR", e.message); }
'''
out=pre+"const __IDX="+json.dumps(idx,ensure_ascii=False)+";\n"+src+"\n"+suf
io.open(r"D:\系统汉字\.tmp-run2.mjs","w",encoding="utf-8",newline="\n").write(out)
print("ok")