import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F589="【第589部「要部」】要＝甲骨文从𦥑从妟，象雙手叉腰、抱腰，腰之初文（《玉篇》「腰，骻也，本作要」）；轉義 中間命門→重要、關鍵、簡略；腰柔→舒緩嫋娜；抱腰→請求、索要、約束。本批取「腰狀柔細」一面。"
F590="【第590部「淼部」】淼＝从三水疊加：象水面浩瀚無際、看不到邊（《說文》「大水也，从三水，或作渺」）；音源借音，義音同「眇」（《字彙》「俗作渺，非」）；未形成字族。"
D=[("䌁","yāo",F589,"从糸要聲：衣襻也（《集韻》「衣襻也，或从糸」），束腰的帶子。","y「续消」取「续」：帶束而续。"),
("𧍔","yāo",F589,"从虫要聲：毒蛇名（《玉篇》），青𧍔。","y取续消：蛇行而续。"),
("㫏","yǎo",F589,"从㫃要聲：旗屬（《說文》「旗屬」），旗皃。","y取续消：旗動而续。"),
("葽","yāo",F589,"从艸要聲：艸也（《說文》引《詩》「四月秀葽」）；《廣雅》莠也（狗尾草）；又 遠志。","y取续消：草蔓而续。"),
("䳩","yāo",F589,"从鳥要聲：鳥如山雞，尾長赤身，其鳴自呼（《廣韻》）。","y取续消：鳴續而续。"),
("騕","yǎo",F589,"从馬要聲：騕褭，古之良馬（《集韻》）。","y取续消：馬行而续。"),
("㴗","yōu",F589,"从水要聲：深也（《集韻》「音幽，深也」）。","y取续消：水深而续。"),
("䁏","yǎo",F589,"从目要聲：䁏眇，遠視（《集韻》）；火光飛騰貌。","y取续消：視遠而续。"),
("𧷋","yāo",F589,"从貝要聲：青𧷋，小獸名（《字彙補》），《宛委餘編》「青𧷋食虎」。","y取续消：獸小而续。"),
("淼","miǎo",F590,"从三水：大水也（《說文》「大水也，从三水」），水淼茫貌，浩瀚無際。","m「蒙末」取「蒙」：水蒙而末。"),
("𡂊","yú",F590,"从口淼聲：水名（《篇海類編》「音餘，水名」）。","y「续消」取「续」：水名而续。"),
("𡡺","miǎo",F590,"从女淼聲：女字（《龍龕》「彌小切」）。","m取蒙末：女小而末。")]
for ch,p,F0,xp,sm in D:
    bus=[{"num":590,"name":"淼"}] if ch in ("淼","𡂊","𡡺") else [{"num":589,"name":"要"}]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"要部同取「腰细、柔長」一面：䌁束腰帶、𧍔青蛇、㫏旗、葽草秀、䳩長尾鳥、騕良馬、㴗深水、䁏遠視、𧷋小獸；淼部取「浩渺無邊」：淼、𡂊水名、𡡺女字；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":bus,"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    num,name=("590","淼") if ch in ("淼","𡂊","𡡺") else ("589","要")
    cl.append({"id":f"lyao589-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{name}部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
p=r"intake\20261024-字卡589a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡589a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))