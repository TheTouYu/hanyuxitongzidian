import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第587部「幺部」】幺＝象蠶剛吐出的絲形（蠶吐絲時頭部左右搖擺，絲呈兩股相交）；轉義 細小、幼、後（排行最小，《字彙》「豕之最後生者為幺」）；辯證《說文》「象子初生之形」與字形不符；音源借音，義音同「交」（幺、交古通）。"
N="字形：古文字字形库未收。"
D=[("幺","yāo",F,"象蠶所吐細絲（兩股相交）：小也（《說文》）；轉義 幼小、排行最小；音源借音同「交」。","y「续消」取「续」：絲細而续。"),
("吆","yāo",F,"从口幺聲：吆吆，聲也（《集韻》），大聲呼喊。","y取续消：聲喊而续。"),
("𢆴","diǎo",F,"从幺：𠄏之或體，懸也（《集韻》「趙魏之間曰𠄏」），懸掛。","d「囤动」取「囤」：懸聚而囤。"),
("𢩼","yí",F,"从手幺聲：持救（《漢典》）。","y取续消：持而续。"),
("㭃","gāng",F,"从糸：綱之古文（《說文》「綱，維紘繩也」），網之大繩。","g「隔估」取「隔」：綱張而隔。"),
("幼","yòu",F,"从幺从力：少也（《說文》「幼，少也」），年幼。","y取续消：少小而续。"),
("黝","yǒu",F,"从黑幼聲：微青黑（《說文》「黝，微青黑色」）。","y取续消：色黑而续。"),
("泑","yōu",F,"从水幼聲：澤名（《說文》「泑澤」），水聚。","y取续消：水聚而续。"),
("呦","yōu",F,"从口幼聲：鹿鳴聲（《詩》「呦呦鹿鳴」）。","y取续消：鳴而续。"),
("窈","yǎo",F,"从穴幼聲：深遠也（《說文》「窈，深遠也」），幽靜。","y取续消：穴深而续。"),
("拗","ǎo",F,"从手幼聲：折也（《集韻》），拗折；又違。","y取续消：手折而续。"),
("眑","yǎo",F,"从目幼聲：深目皃（《集韻》），視。","y取续消：目深而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"幺部同取「絲細、幼小」一面：吆呼、𢆴懸、𢩼持、㭃綱、幼少、黝黑、泑澤、呦鳴、窈深、拗折、眑視；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":587,"name":"幺"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第587部「幺部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡587a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡587a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))