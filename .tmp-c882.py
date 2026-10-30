import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第591部「殸部」】殸＝擊懸石（磬之初文）；字族第二面＝磬懸空不著物，取「空、盡」之義；第三面＝形近字「㱿」之訛。"
D=[("漀","qǐng",F,"从水殸聲：側出泉也（《說文》「側出泉也」），旁出如醡；又傾水漿。","q「亲缺」取「缺」：泉側而缺。"),
("謦","qǐng",F,"从言殸聲：欬也（《說文》「欬也」），咳嗽清喉；謦欬，言笑。","q取亲缺：言咳而缺。"),
("㷫","qǐng",F,"从火殸聲：火乾出也（《集韻》），火氣乾物。","q取亲缺：火乾而缺。"),
("罄","qìng",F,"从缶殸聲：器中空也（《說文》「器中空也」），陶器中空敲如磬聲，引申盡、用盡。","q取亲缺：器空而缺。"),
("䅽","gǔ",F,"从禾殸聲：同穀（《漢典》），糧食作物總稱；今讀與馨同。","g「隔估」取「隔」：穀聚而隔。"),
("螜","hú",F,"从虫殸聲：同螜，天螻（《爾雅》「螜，天螻」），螻蛄。","h「豁活」取「豁」：蟲穴而豁。"),
("撀","gòu",F,"从手殸聲：取牛羊乳也（《篇海》「古鬬切，音遘」），擠奶。","g取隔估：擠而隔。"),
("彀","gòu",F,"从弓殸聲：張弓也（《字彙補》「張弓也，亦作彀」），張弩。","g取隔估：弓張而隔。"),
("瞉","kòu",F,"从目殸聲：瞉瞀，無睱也（《奚韻》），目不明；又久視。","k「口控」取「控」：目盲而控。"),
("𩌊","huò",F,"从革殸聲：緊束（《漢典》），疑即觳（盛觵巵、射具、盡）。","h取豁活：束而豁。"),
("𧹲","hù",F,"从赤殸聲：日出赤貌（《字彙補》「與𧹲同」）。","h取豁活：日出而豁。"),
("𨢋","hú",F,"从酉殸聲：濁酒（《集韻》）。","h取豁活：酒濁而豁。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"殸部第二面取「空、盡」：漀側泉、謦咳、㷫火乾、罄器空；第三面取「㱿訛變」：䅽穀、螜螻、撀擠乳、彀張弓、瞉目盲、𩌊緊束、𧹲日出赤、𨢋濁酒；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":591,"name":"殸"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqing2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第591部「殸部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡591b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡591b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))