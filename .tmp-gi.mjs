const fs=require("fs");
const idx=JSON.parse(fs.readFileSync("web/public/glyphs/index.json","utf8"));
for (const ch of ["虍","虎"]){
  const e=idx.chars[ch];
  try{
    const files=(e.files||[]).map(f=>"/glyphs/"+(String(f).includes("/")?String(f):ch+"/"+String(f)).split("/").map(encodeURIComponent).join("/"));
    console.log(ch, files.length, files[0]);
  }catch(err){ console.log(ch,"ERR",err.message); }
}
console.log("photos", idx.photos["虍"]);