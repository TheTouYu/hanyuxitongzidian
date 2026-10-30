const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('D:/系统汉字/web/public/test.html','utf8');
let js=html.match(/<script>([\s\S]*)<\/script>/)[1];
js+="\n;globalThis.__api={open};";
const els=new Map();
const mk=(s)=>{const e={_h:'',sel:s,addEventListener(){},classList:{add(){},remove(){}},style:{},value:'',textContent:'',querySelectorAll:()=>[],appendChild(){},focus(){},dataset:{}};
Object.defineProperty(e,'innerHTML',{get(){return e._h},set(v){e._h=v}});return e;};
const doc={querySelector:s=>{if(!els.has(s))els.set(s,mk(s));return els.get(s)},getElementById:s=>doc.querySelector('#'+s),querySelectorAll:()=>[],addEventListener(){},createElement:()=>mk('x'),body:mk('b')};
const f=(u)=>fetch('http://127.0.0.1:8089/'+u.replace(/^\//,''));
const ctx={document:doc,location:{hash:''},history:{replaceState(){}},console,setTimeout,clearTimeout,fetch:f,encodeURIComponent,decodeURIComponent,JSON,Promise,URLSearchParams,Math,Date,String,Number,Array,Object};
ctx.window=ctx;ctx.globalThis=ctx;
vm.createContext(ctx); vm.runInContext(js,ctx);
(async()=>{ try{ await ctx.__api.open('易'); const m=els.get('#main'); console.log('LEN',m._h.length); console.log('hasTable',m._h.includes('<table'),'hasZD',m._h.includes('字理分析'),'hasPhoto',m._h.includes('插图')); }
catch(e){ console.log('THROW',e.message);} })();