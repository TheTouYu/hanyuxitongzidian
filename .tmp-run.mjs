import fs from 'fs';
const src=fs.readFileSync('D:/系统汉字/.tmp-page.js','utf8');
const idx=JSON.parse(fs.readFileSync('D:/系统汉字/web/public/cards/index.json','utf8'));
const store={};
const el=(id)=>({id,innerHTML:'',textContent:'',dataset:{},addEventListener(){},querySelectorAll:()=>[],style:{}});
global.document={querySelector:(s)=>{const k=s.replace('#','');store[k]=store[k]||el(k);return store[k];},querySelectorAll:()=>[],addEventListener(){},createElement:()=>el('x')};
global.window={};
global.fetch=async(u)=>({json:async()=> (String(u).includes('cards/index.json')?idx:(String(u).includes('glyphs/index.json')?{chars:{}}:(String(u).includes('photos')?{photos:{}}:{})))});
global.encodeURI=encodeURI;
const mod=src+"\nexport {render};";
const fn=new Function('module','IDX',mod.replace('export {render};','return {render};'));
try{ const api=fn({},idx); api.render('疑'); console.log('HINT:',store['hint'].innerHTML.slice(0,300)); }catch(e){ console.log('ERR',e.message); }