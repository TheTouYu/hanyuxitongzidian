import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第575部「𠧪部」】𠧪＝象栗、粟之類草木子實垂形（讀若調）；子實在房中如器皿盛食，故引申為酒器「卣」；因𠧪、西形近，栗、粟皆誤从西；音源為借音（可釀酒，義音同酉）。"
N="字形：古文字字形库未收。"
D=[("𠧪","tiáo",F,"象草木子實垂𠧪𠧪然（《說文》），籀文三𠧪為𠧪。","t「涂突」取「突」：實垂而下。"),
("卣","yǒu",F,"从皿从𠧪：中樽器也（《玉篇》），古代盛酒器（商代青銅卣）。","y「?」取酉声。"),
("𦵵","yóu",F,"从艸𠧴聲：艸也（《說文》），或作莤（以茅束灌鬯酒）。","y取由声。"),
("𢈞","yóu",F,"从广𠧴聲：檐㮰謂之庮（《集韻》），久屋朽木。","y取由声。"),
("𧡹","yòu",F,"从見𠧴聲：下視深也（《說文》），向下看幽深處。","y取由声。"),
("栗","lì",F,"从木从𠧪：栗木（《說文》「栗木也」），果實；假借戰栗。","l「拢离」取「离」：果堅而离。"),
("粟","sù",F,"从米从𠧪：穀實（《說文》「嘉穀實也」），去殼即小米。","s「失收」取「收」：穀收而聚。"),
("瑮","lì",F,"从玉栗聲：玉英華相帶如瑟弦（《說文》）。","l取拢离：玉列而离。"),
("鷅","lì",F,"从鳥栗聲：鷅鶹（《集韻》），鳥名，似鷂。","l取拢离：鳥飛而离。"),
("凓","lì",F,"从冫栗聲：寒也（《說文》「凓，寒也」），寒氣逼人。","l取拢离：寒收而离。"),
("慄","lì",F,"从心栗聲：懼也（《廣韻》），戰慄、恐懼。","l取拢离：心散而离。"),
("溧","lì",F,"从水栗聲：水名（《說文》「溧水，出丹陽」），溧陽。","l取拢离：水行而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𠧪部同取「子實垂垂、房中開口」一面：卣酒器、𦵵草、𢈞朽木、𧡹下視、栗實、粟穀、瑮玉、鷅鳥、凓寒、慄懼、溧水；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":575,"name":"𠧪"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ltiao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第575部「𠧪部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡575a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡575a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))