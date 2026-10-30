const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('D:/系统汉字/web/public/test.html','utf8');
let js=html.match(/<script>([\s\S]*)<\/script>/)[1];
js+="\n;globalThis.__api={open,render};";
const els=new Map();
function mk(sel){const e={_html:'',sel,addEventListener(){},classList:{add(){},remove(){}},style:{},value:'',textContent:'',querySelectorAll:()=>[],appendChild(){},focus(){}};
 Object.defineProperty(e,'innerHTML',{get(){return e._html},set(v){e._html=v}}); return e;}
const doc={querySelector:(s)=>{if(!els.has(s))els.set(s,mk(s));return els.get(s)},getElementById:(s)=>doc.querySelector('#'+s),querySelectorAll:()=>[],addEventListener(){},createElement:()=>mk('x'),body:mk('body')};
const ctx={document:doc,window:null,location:{hash:''},history:{replaceState(){}},console,setTimeout,clearTimeout,fetch,encodeURIComponent,decodeURIComponent,JSON,Promise,URLSearchParams,Math,Date,String,Number,Array,Object};
ctx.window=ctx; ctx.globalThis=ctx;
vm.createContext(ctx); vm.runInContext(js,ctx);
(async()=>{
  try{ await ctx.__api.open('易'); const m=els.get('#main'); console.log('MAIN len',m._html.length); console.log(m._html.slice(0,200)); }
  catch(e){ console.log('THROW',e.message); }
})();