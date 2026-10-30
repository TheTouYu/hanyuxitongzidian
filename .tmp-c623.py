import json,re,os,glob,subprocess
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FIX=[("惋",449,"夗","夗＝轉卧不安","clm_9A5696908DEB7DCCFD5558160F","惋","wǎn"),
("愆",461,"川","川＝水流漫衍","clm_9420D0865CD81551E4F84519A5","愆","qiān"),
("慧",481,"彗","彗＝掃帚掃除","clm_7D2F7B1F42CF08AB0C8FB561BA","慧","huì"),
("慷",597,"用","用＝器用有節","clm_7C82A10EE0B7B61E3490DBC160","慷","kāng"),
("憨",181,"甘","甘＝口中含物而味美","clm_8631D5540EAEE8390C6BB7E435","憨","hān"),
("憾",185,"戌","戌＝斧鉞之兵","clm_CEB2036C156194E75FA24E94F1","憾","hàn"),
("懇",140,"勹","勹＝俯伏包裹","clm_74FB3309F0ABAE30674F5ABC41","懇","kěn")]
for ch,num,name,gloss,cid,_,py_ in FIX:
    p=rf"web\public\cards\{ch}.json"
    c=json.load(open(p,encoding="utf-8"))
    c["bus"]=[{"num":num,"name":name}]
    for s in c["sections"]:
        if s["key"]=="bengen":
            s["text"]=f"【第{num}部「{name}部」】{name}：{gloss}；{ch}从{name}得聲，歸{name}部。"
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(FIX))
txt=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
def stmt(cid):
    m=re.search(r"<!-- CLAIM:START "+cid+r" -->\s*\r?\n\s*### .+?\r?\n\s*\r?\n(.+?)\r?\n\s*#### 适用边界",txt,re.S)
    return m.group(1).strip() if m else None
out=run("knowledge-plan","init","--intent","双证部属订正2026-10-23","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0); print("plan",pid)
for ch,num,name,gloss,cid,_,py_ in FIX:
    s=stmt(cid)
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",s,
      "--boundary",f"源自《系統漢語》第{num}部「{name}部」；字卡五步规程。",
      "--semantic-declaration","clarify","--reason","部属订正（条目行+字族清单双证）")
    print(ch, '"ok": true' in r)
fin=run("knowledge-plan","finalize",pid,"--format","json")
m=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"[\s\S]*?"content_hash":\s*"([0-9a-f]+)"',fin)
print("bundle",m.group(1) if m else None)
if m:
    run("bundle-approve",m.group(1),"--apply","--content-hash",m.group(2))
    run("bundle-apply",m.group(1),"--apply","--content-hash",m.group(2))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))