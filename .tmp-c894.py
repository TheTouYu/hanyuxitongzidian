import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
# 订正 亶 卡：原稿以「蟺（黄鳝）之初文」为本义，《说文》「多谷」不确
p=r"web\public\cards\亶.json"; c=json.load(open(p,encoding="utf-8"))
new="【第592部「冬部」·亶族】亶＝甲骨文从它从㐭（它＝蛇，㐭＝挂在高处），蟺（蟮、黄鳝）之初文；黄鳝无鳞→袒露（但、袒、襢）；栖泥洞钻行→難行不進（邅）；色赤黄→檀；辨证《说文》「多谷也，从㐭旦声」据战国加旦声之篆文，形义均不确（亶无「多谷」用例）；音源本㐭声，因袒义而义音同「旦」。"
for s in c["sections"]:
    if s["key"]=="bengen": s["text"]=new
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
F="【第592部「冬部」·亶族】亶＝蟺（黄鳝）之初文：无鳞→袒露平坦、钻泥洞→難行不進、色赤黄→檀、面瘠色黄→顲；音源本㐭声，义音同「旦」。"
D=[("壈","lǎn",F,"从土稟聲：壈坎也（《玉篇》），坎壈，不平；又失志。","l「拢离」取「拢」：坎聚而拢。"),
("𨎹","lǎn",F,"从車稟聲：輡𨎹，車不進（《集韻》），車不平。","l取拢离：車滯而拢。"),
("𤒀","yào",F,"从火稟聲：仰也（《廣韻》「䶳，仰也」），火仰。","y「续消」取「续」：火仰而续。"),
("𤃨","làn",F,"从水稟聲：𤃨㶒，浮皃（《廣韻》），水浮。","l取拢离：水浮而拢。"),
("𤎭","lǐn",F,"从炎㐭聲：㑴火也（《說文》「㑴火也」），漸燒之火；又 火盛。","l取拢离：火漸而拢。"),
("燣","lán",F,"从火稟聲：黃色（《玉篇》）；又 熱、煼、色焦。","l取拢离：火焦而拢。"),
("顲","lǎn",F,"从頁𤎭聲：面䫲顲皃（《說文》），面瘠色黃，形容枯槁如㐭。","l取拢离：面瘠而拢。"),
("𨟏","yín",F,"从邑𤎭聲：地名（《說文》「讀若淫」）。","y取续消：邑名而续。"),
("皽","zhāo",F,"从皮亶聲：肉之魄莫（《集韻》），皮肉上薄膜；又 皮寬。","zh「凿总」取「凿」：皮薄而凿。"),
("澟","lǐn",F,"从水稟聲：寒也（《玉篇》），淒清。","l取拢离：水寒而拢。")]
for ch,pn,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亶族取「無鱗袒露、鑽洞、色黃」一面：皽薄皮、壈坎、𨎹車滯、𤒀火仰、𤃨水浮；稟族取「火盛焦黄、面瘠」：𤎭漸火、燣焦色、顲面瘠、𨟏邑名、澟寒；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":pn,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{pn}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,pn,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡592f.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592f{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))