const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('D:/系统汉字/web/public/test.html','utf8');
const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const el=()=>({addEventListener(){},classList:{add(){},remove(){}},style:{},set innerHTML(v){},get innerHTML(){return ''},textContent:'',value:'',querySelectorAll:()=>[],appendChild(){},focus(){}});
const doc={getElementById:()=>el(),querySelectorAll:()=>[],addEventListener(){},createElement:()=>el(),body:el()};
const ctx={document:doc,window:{},location:{hash:''},console,setTimeout,clearTimeout,fetch:()=>Promise.reject(new Error('no net')),encodeURIComponent,decodeURIComponent,JSON,history:{replaceState(){}}};
ctx.window=ctx; ctx.globalThis=ctx;
try{ vm.createContext(ctx); vm.runInContext(js,ctx,{timeout:3000}); console.log('OK top-level'); }
catch(e){ console.log('ERR', e.message, '\n', (e.stack||'').split('\n').slice(0,3).join('\n')); }