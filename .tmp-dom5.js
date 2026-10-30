const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('D:/系统汉字/web/public/test.html','utf8');
const all=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
let js=all[all.length-1]+"\n;globalThis.__api={open};";
const els=new Map();
const mk=(s)=>{const e={_h:'',sel:s,addEventListener(){},classList:{add(){},remove(){}},style:{},value:'',textContent:'',querySelectorAll:()=>[],appendChild(){},focus(){},dataset:{}};
Object.defineProperty(e,'innerHTML',{get(){return e._h},set(v){e._h=v}});return e;};
const doc={querySelector:s=>{if(!els.has(s))els.set(s,mk(s));return els.get(s)},getElementById:s=>doc.querySelector('#'+s),querySelectorAll:()=>[],addEventListener(){},createElement:()=>mk('x'),body:mk('b')};
const f=(u)=>fetch('http://127.0.0.1:8089/'+u.replace(/^\//,''));
const ctx={document:doc,location:{hash:''},history:{replaceState(){}},console,setTimeout,clearTimeout,fetch:f,encodeURIComponent,decodeURIComponent,JSON,Promise,URLSearchParams,Math,Date,String,Number,Array,Object};
ctx.window=ctx;ctx.globalThis=ctx;
vm.createContext(ctx); vm.runInContext(js,ctx);
(async()=>{ try{ await ctx.__api.open('易'); const m=els.get('#main'); console.log('LEN',m._h.length); console.log('table',m._h.includes('<table'),'rootbox',m._h.includes('字理分析'),'photo',m._h.includes('插图')); }
catch(e){ console.log('THROW',e.message);} })();