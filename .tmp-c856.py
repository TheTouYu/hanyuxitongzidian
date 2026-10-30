import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第584部「喿部」】喿＝眾口在木上鳴叫（噪之初文）；字族五面：聲音之雜／狀態之雜／色彩之雜／行為之雜／心理之雜。"
N="字形：古文字字形库未收。"
D=[("𦗵","jiǎo",F,"从耳喿聲：耳鳴（《集韻》「音劋，耳鳴」）。","j「聚决」取「决」：耳鳴而决。"),
("𤢖","sāo",F,"从犬喿聲：山𤢖（山魈），《神異經》「西方深山有人長丈餘……名山𤢖」。","s「失收」取「收」：山鬼而收。"),
("𩙈","sāo",F,"从風喿聲：颾之或體，風聲（《集韻》）。","s取失收：風聲而收。"),
("橾","shū",F,"从木喿聲：車轂中空也（《說文》），貫軸之空腔（轉動有聲）；又鍬之或體。","sh「刺持」取「持」：轂空而持。"),
("𩯟","sān",F,"从髟喿聲：鬖之或體，髮亂皃（《集韻》）；又長毛皃。","s取失收：髮亂而收。"),
("𥼾","sǎn",F,"从米喿聲：糝之或體，以米和羹（《說文》「以米和羹也」）。","s取失收：米和而收。"),
("𥽹","cào",F,"从米喿聲：米穀雜也（《字彙補》），雜亂。","c「刺持」取「持」：穀雜而持。"),
("璪","zǎo",F,"从玉喿聲：玉飾如水藻之文（《說文》引《虞書》「璪火黺米」）。","z「凿总」取「总」：玉文而总。"),
("䵲","qiāo",F,"从麻喿聲：麻苦雨生壞也（《集韻》），生麻；又雀斑。","q「亲缺」取「亲」：麻壞而亲。"),
("繰","zǎo",F,"从糸喿聲：帛如紺色（《說文》「帛如紺色」），黑紅；又繅絲。","z取凿总：帛色而总。"),
("𧂈","jiǎo",F,"从艸喿聲：似薺菜（《玉篇》），山薺（多葉碎米薺）。","j取聚决：草細而决。"),
("藻","zǎo",F,"从艸从水喿聲：水艸也（《說文》），水藻；又文辭（文采如藻布列）。","z取凿总：水草而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"喿部同取「雜亂、細碎」一面：𦗵耳鳴、𤢖山魈、𩙈風聲、橾轂空、𩯟髮亂、𥼾米和、𥽹穀雜、璪玉文、䵲麻壞、繰帛色、𧂈山薺、藻水草；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":584,"name":"喿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第584部「喿部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡584b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡584b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))