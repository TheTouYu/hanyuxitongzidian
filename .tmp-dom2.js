const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('D:/系统汉字/web/public/test.html','utf8');
const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const el=()=>new Proxy({addEventListener(){},classList:{add(){},remove(){},toggle(){}},style:{},textContent:'',value:'',innerHTML:'',dataset:{},children:[],appendChild(){},remove(){},focus(){},querySelectorAll:()=>[],getBoundingClientRect:()=>({top:0})},{get(t,k){ if(k in t) return t[k]; if(k==='innerHTML') return ''; return undefined;},set(t,k,v){t[k]=v;return true;}});
const doc={getElementById:()=>el(),querySelector:()=>el(),querySelectorAll:()=>[],addEventListener(){},createElement:()=>el(),body:el()};
const ctx={document:doc,location:{hash:'',href:'http://x/'},history:{replaceState(){}},console,setTimeout,clearTimeout,fetch:()=>new Promise(()=>{}),encodeURIComponent,decodeURIComponent,JSON,Promise,URLSearchParams,Math,Date};
ctx.window=ctx; ctx.globalThis=ctx;
try{ vm.createContext(ctx); vm.runInContext(js,ctx,{timeout:4000}); console.log('OK top-level'); }
catch(e){ console.log('ERR:', e.message); console.log((e.stack||'').split('\n').slice(1,4).join('\n')); }