import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第573部「萬部」】萬（𧍣）＝象蠍子形（尾部常蜷曲，又名全蟲）；因冬眠成堆潛伏、負子於背，引申數目極多、大；音源為借音（蠍不鳴），字族多取「栗」（硬殼毒刺）之音。字族四面：①多盛 ②凶惡燒灼 ③舉尾高 ④殼狀粗糙。"
N="字形：古文字字形库未收。"
D=[("萬","wàn",F,"象蠍子形（《說文》「蟲也」），引申十千、極多、大。","w「?」取弯曲聲。"),
("贎","wàn",F,"从貝萬聲：貨也（《說文》），財貨多。","w取万声。"),
("勱","mài",F,"从力萬聲：勉力也（《說文》引《周書》），努力盡力。","m「蒙末」取「末」：力盡而末。"),
("𩧃","lì",F,"从馬萬聲：次第馳也（《說文》），一曰馴。","l「拢离」取「离」：馬馳而离。"),
("噧","xiè",F,"从口蠆省聲：高氣多言也（《說文》引《春秋傳》），聲音高而話多。","x「续消」取「消」：聲高而消。"),
("䜕","mài",F,"从言萬聲：譀也（《說文》），誇大、言過其實。","m取蒙末：言大而末。"),
("𢤆","lì",F,"从心萬聲：驚也（《集韻》），驚恐；又惡。","l取拢离：驚散而离。"),
("癘","lì",F,"从疒蠆省聲：惡疾也（《說文》），麻風病，又瘟疫。","l取拢离：疾散而离。"),
("禲","lì",F,"从示萬聲：鬼災曰禲（《集韻》），厲鬼之災。","l取拢离：鬼災而离。"),
("曞","lì",F,"从日萬聲：日光盛（《集韻》）。","l取拢离：日盛而离。"),
("鱱","lì",F,"从魚萬聲：魚名（《集韻》），即鱧（黑魚、烏魚）。","l取拢离：魚伏而离。"),
("爄","lì",F,"从火萬聲：止火（《集韻》），以瓦石蓋火；又火斷。","l取拢离：火掩而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"萬部同取「蠍之多、毒、舉尾、硬殼」一面：贎貨多、勱勉力、𩧃馳、噧多言、䜕誇、𢤆驚、癘惡疾、禲鬼災、曞日盛、鱱黑魚、爄止火；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":573,"name":"萬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lwan-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第573部「萬部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡573a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡573a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))