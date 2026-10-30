import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第572部「歺部」】𡿪支＝从水从歺（以水洗骨，洗骨葬），引申分裂、促迫擠壓。"
F2="【第572部「歺部」】死＝从歺从人（殘骨旁之人），生命終結；屍＝从尸死聲，屍體。"
F3="【第572部「歺部」】𣦼／粲支＝从歺从又（殘骨在手），餐＝吞食；粲＝稻餅、鮮明。"
N="字形：古文字字形库未收。"
D=[("桚","zā",F1,"从木𡿪聲：笮也（《集韻》），狹迫、擠壓。","z「凿总」取「总」：迫聚而总。"),
("拶","zā",F1,"从手𡿪聲：逼拶也（《玉篇》），擠壓；拶指為酷刑具。","z取凿总：手逼而总。"),
("𣴖","zá",F1,"从水𡿪聲：水濺也（《集韻》），或从賛。","z取凿总：水濺而总。"),
("𨀨","zuǒ",F1,"从足𡿪聲：蹙𨀨，行貌（《集韻》），行相迫蹙。","z取凿总：足迫而总。"),
("𠡝","yì",F1,"从力𡿪聲：動也（《字彙補》）。","y「远渊」取「远」：動散而远。"),
("死","sǐ",F2,"从歺从人：生命終結（《說文》「澌也，人所離也」），引申死板、極甚。","s「失收」取「收」：氣收而尽。"),
("屍","shī",F2,"从尸死聲：屍體（《說文》「終主」），死屍。","sh取失收：体收而藏。"),
("餐","cān",F3,"从食𣦼聲：吞也（《說文》「吞也」），進食、飯食。","c「刺持」取「持」：食入而持。"),
("㛑","càn",F3,"从女𣦼聲：三女為㛑，美也（《說文》），指女膚色白。","c取刺持：色白而持。"),
("䱗","cān",F3,"从魚𣦼聲：魚名（《集韻》），即鱎魚。","c取刺持：魚游而持。"),
("粲","càn",F3,"从米𣦼聲：稻餅也（《說文》），又鮮明、露齒笑。","c取刺持：米白而持。"),
("燦","càn",F3,"从火粲聲：燦爛（《集韻》），光彩鮮明。","c取刺持：火明而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𡿪支取「洗骨促迫」（桚、拶、𣴖、𨀨、𠡝）；死支取「殘骨在人旁」（死、屍）；𣦼支取「殘骨在手」（餐、㛑、䱗、粲、燦）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":572,"name":"歺"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lsii-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第572部「歺部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡572c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡572c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))