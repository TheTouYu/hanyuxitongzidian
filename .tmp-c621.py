import re,os,glob,json,subprocess
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
txt=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
def stmt(cid):
    m=re.search(r"<!-- CLAIM:START "+cid+r" -->\s*\r?\n\s*### .+?\r?\n\s*\r?\n(.+?)\r?\n\s*#### 适用边界",txt,re.S)
    return m.group(1).strip() if m else None
FIX={"忠":(123,"中","clm_6520651ABB1A1826B1055DEE9F"),"忍":(344,"刃","clm_36B834AF29BF1E9543BC926642"),
"恥":(333,"耳","clm_D9CE1477AF9937E1099C484D52"),"悉":(434,"釆","clm_3D97EDCDDC0AF6A41D5229FCED"),
"恭":(502,"𠬞","clm_FD8B8FA8EEF3039D1AD66A956B"),"悔":(262,"母","clm_DA331C21FD0512CD53CEB319DE"),
"悚":(372,"束","clm_1253E0683810C4311FA774BF09"),"惋":(449,"夗","clm_9A5696908DEB7DCCFD5558160F"),
"惰":(239,"左","clm_BE01EF5346ED693CA093FDDBD1"),"想":(529,"相","clm_BF2C59F16046EC3F5E71524142"),
"愁":(540,"秋","clm_95147DAB74B35D34D54B52D65F"),"愆":(461,"川","clm_9420D0865CD81551E4F84519A5"),
"慧":(481,"彗","clm_7D2F7B1F42CF08AB0C8FB561BA"),"慷":(597,"用","clm_7C82A10EE0B7B61E3490DBC160"),
"憨":(181,"甘","clm_8631D5540EAEE8390C6BB7E435"),"憫":(272,"文","clm_429A1C3127889AE6152F2611BE"),
"憾":(185,"戌","clm_CEB2036C156194E75FA24E94F1"),"懇":(140,"勹","clm_74FB3309F0ABAE30674F5ABC41"),
"懲":(482,"帚","clm_4513B35984AA2FBE8E7D282F86"),"戀":(446,"䜌","clm_B9CE869102F1BCA2B3B42D27FC")}
out=run("knowledge-plan","init","--intent","心部误归订正b2026-10-23","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0); print("plan",pid)
bad=0
for ch,(num,name,cid) in FIX.items():
    s=stmt(cid)
    if not s: print("nostmt",ch); bad+=1; continue
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",s,"--boundary",
        f"源自《系統漢語》第{num}部「{name}部」；字卡五步规程。","--semantic-declaration","clarify","--reason","部属订正")
    if "error" in r.lower(): print(ch,"ERR",r[-100:]); bad+=1
print("bad",bad)
fin=run("knowledge-plan","finalize",pid,"--format","json"); print("fin ok:", '"ok": true' in fin or '"ok":true' in fin)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))