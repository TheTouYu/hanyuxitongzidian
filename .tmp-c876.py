import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F588="【第588部「杳部」】杳＝从日在木下，象太陽落下，表夜晚、幽冥（《說文》「冥也」）；轉義 幽深、寬廣（《玉篇》「深、廣、寛皃」）；音源借音，因幽微而義音同「幺」（《莊子》「居於窈冥」一本作杳）。"
F589="【第589部「要部」】要＝甲骨文从𦥑从妟（妟為女子安樂），象雙手叉腰，或指抱住女子腰部，腰之初文（《玉篇》「腰，骻也，本作要」）；轉義 中間命門→重要、關鍵、簡略；腰柔→舒緩嫋娜；抱腰→請求、索要、約束。"
D=[("杳","yǎo",F588,"从日在木下：冥也（《說文》），象日落夜晚；轉義 幽深寬廣；音源借音同「幺」。","y「续消」取「续」：日沉而续。"),
("𨓳","yāo",F588,"从辵杳聲：遠皃（《集韻》「音要，遠皃」）。","y取续消：行遠而续。"),
("鬐","qí",F588,"从髟耆聲：馬鬣（《漢典》）；此條為形近字「耆」之訛。","q「亲缺」取「缺」：鬣分而缺。"),
("香","xiāng",F588,"从黍从甘：黍稷馨香；此條為形近字「香」之訛（《字彙補》「與香同」）。","x取续消：氣香而续。"),
("要","yāo",F589,"甲骨文从𦥑从妟：象雙手叉腰、抱腰，腰之初文（《玉篇》「腰，骻也，本作要」）；轉義 重要、關鍵、簡略；又 請求、索要、約束。","y取续消：腰束而续。"),
("腰","yāo",F589,"从肉要聲：身中也（《說文》）；約結而小（《釋名》「腰，約也，在體之中」）。","y取续消：腰約而续。"),
("偠","yǎo",F589,"从人要聲：偠紹，舒緩皃（《集韻》）；偠㒟，細腰也（《玉篇》）。","y取续消：體柔而续。"),
("楆","yāo",F589,"从木要聲：要棗（《爾雅》「邊，要棗」），子細腰，今鹿盧棗。","y取续消：棗細而续。"),
("崾","yǎo",F589,"从山要聲：山名（《集韻》），疑本指半山腰。","y取续消：山腰而续。"),
("䙅","yào",F589,"从衣要聲：衣襻（《集韻》「衣襻」），衣之束腰處。","y取续消：衣束而续。"),
("闄","yǎo",F589,"从門要聲：門要（《集韻》），門之要處。","y取续消：門隔而续。"),
("喓","yāo",F589,"从口要聲：喓喓，蟲鳴聲（《詩》「喓喓草蟲」）。","y取续消：鳴細而续。")]
for ch,p,F0,xp,sm in D:
    bus=[{"num":588,"name":"杳"}] if ch in ("杳","𨓳","鬐","香") else [{"num":589,"name":"要"}]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取「幽深、腰細、要約」一面：杳冥、𨓳遠、鬐鬣、香馨；要腰、偠細腰、楆細腰棗、崾山腰、䙅衣襻、闄門要、喓蟲鳴；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":bus,"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    num,name=("588","杳") if ch in ("杳","𨓳","鬐","香") else ("589","要")
    cl.append({"id":f"lyao588-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{name}部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
p=r"intake\20261024-字卡588a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡588a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))