import json,re,os,subprocess
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FIX=[("忠",123,"中","中＝旗杆立於中央；字族衍義①指中間、正直、中心","clm_6520651ABB1A1826B1055DEE9F"),
("忍",344,"刃","刃＝刀刃；轉義引申堅柔，忍取堅而含忍","clm_36B834AF29BF1E9543BC926642"),
("恥",333,"耳","耳＝耳朵；恥取聞過自愧、耳熱面赤（《六書總要》从心耳會意）","clm_D9CE1477AF9937E1099C484D52"),
("悉",434,"釆","釆＝獸爪翻扒、分辨細物；悉指辨別、詳盡知悉","clm_3D97EDCDDC0AF6A41D5229FCED"),
("恭",502,"𠬞","𠬞＝兩手拱舉；字族衍義多指拱手之狀，恭＝自拱持而肅","clm_FD8B8FA8EEF3039D1AD66A956B"),
("悔",262,"母","母（𣫭）＝生育之母；悔取如梅子之酸、孕期反應（《說文》从心𣫭聲）","clm_DA331C21FD0512CD53CEB319DE"),
("悚",372,"束","束＝捆縛；悚通聳，懼而毛骨聳然","clm_1253E0683810C4311FA774BF09"),
("惰",239,"左","左＝左手輔佐；隋下垂引申懶惰、順從","clm_BE01EF5346ED693CA093FDDBD1"),
("想",529,"相","相＝以目視木；字族衍義①交互相對，想＝冀思、心有所著","clm_BF2C59F16046EC3F5E71524142"),
("愁",540,"秋","秋＝禾熟而肅殺；愁取秋氣之憂","clm_95147DAB74B35D34D54B52D65F"),
("憫",272,"文","文（閔从門文聲）＝文飾；憫取傷病而憂憐","clm_429A1C3127889AE6152F2611BE"),
("懲",482,"帚","帚＝掃除之器；懲＝㣻也，懲治使改而止","clm_4513B35984AA2FBE8E7D282F86"),
("戀",446,"䜌","䜌＝繫連不絕；戀＝慕也，繫連而留戀","clm_B9CE869102F1BCA2B3B42D27FC")]
for ch,num,name,gloss,cid in FIX:
    p=rf"web\public\cards\{ch}.json"
    c=json.load(open(p,encoding="utf-8"))
    c["bus"]=[{"num":num,"name":name}]
    for s in c["sections"]:
        if s["key"]=="bengen":
            s["text"]=f"【第{num}部「{name}部」】{gloss}；{ch}从{name}得聲，歸{name}部。"
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(FIX))
txt=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
def stmt(cid):
    m=re.search(r"<!-- CLAIM:START "+cid+r" -->\s*\r?\n\s*### .+?\r?\n\s*\r?\n(.+?)\r?\n\s*#### 适用边界",txt,re.S)
    return m.group(1).strip() if m else None
out=run("knowledge-plan","init","--intent","十三字部属订正2026-10-23","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0)
ok=0
for ch,num,name,gloss,cid in FIX:
    s=stmt(cid)
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",s,
      "--boundary",f"源自《系統漢語》第{num}部「{name}部」；字卡五步规程。",
      "--semantic-declaration","clarify","--reason","部属订正（条目行＋字族衍義组双证）")
    ok+= '"ok": true' in r
print("revised",ok,"/",len(FIX))
run("knowledge-plan","check",pid,"--mode","delta","--format","json")
fin=run("knowledge-plan","finalize",pid,"--format","json")
m=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"[\s\S]*?"content_hash":\s*"([0-9a-f]+)"',fin)
print("bundle",m.group(1) if m else fin[:200])
if m:
    run("bundle-approve",m.group(1),"--apply","--content-hash",m.group(2)); run("bundle-apply",m.group(1),"--apply","--content-hash",m.group(2))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))