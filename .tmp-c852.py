import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第583部「巢部」】巢＝从木上有西（西＝鳥窩）；字族五面：鳥巢之狀／高、抄掠／小／吵鬧／形近之訛。"
N="字形：古文字字形库未收。"
D=[("𢀌","jiǎo",F,"音剿（《金鏡》），巢部餘文。","j「聚决」取「决」：殘而决。"),
("𦟳","jù",F,"从肉巢聲：與醵同（《龍龕》），合錢飲酒。","j取聚决：湊而决。"),
("𧑀","lüè",F,"从虫巢聲：渠𧑀，朝生暮死蟲（《龍龕》），蜉蝣（群飛水面如抄掠）。","l「拢离」取「离」：群飛而离。"),
("䲃","zǎo",F,"从魚巢聲：魚名，似鯉而雞足（《山海經》）；又魚子（《集韻》）。","z「凿总」取「总」：魚聚而总。"),
("𡡊","cháo",F,"从女巢聲：女字（《篇海類編》）。","ch「刺持」取「持」：女名而持。"),
("𧷣","suǒ",F,"从貝巢聲：同䞆（《字彙》），骨也。","s「失收」取「收」：骨收而收。"),
("𪍨","suǒ",F,"从麥巢聲：小麥屑之覈（《集韻》引《說文》）。","s取失收：麥屑而收。"),
("𠻥","zhào",F,"从口巢聲：眾聲也（《集韻》），人聲嘈雜。","zh「凿总」取「总」：聲雜而总。"),
("𦗔","zhāo",F,"从耳巢聲：耳鳴也（《玉篇》），聲擾耳。","zh取凿总：耳鳴而总。"),
("䜈","chāo",F,"从言巢聲：代人說也（《玉篇》），與勦同。","ch取刺持：代言而持。"),
("㺐","lǎo",F,"从犬巢聲：西南夷謂之䝤（《集韻》），土人自謂獠。","l取拢离：夷落而离。"),
("璅","suǒ",F,"从玉巢聲：石之似玉者（《說文》）；又瑣之或體，玉聲。","s取失收：玉細而收。"),
("𥲀","cháo",F,"从竹巢聲：大笙，有十九簧（《玉篇》）。","ch取刺持：笙大而持。"),
("隟","xì",F,"从阜巢聲：隙之俗字（《龍龕》「隟、隙，二俗；𨻶，正」），裂也、孔也。","x「续消」取「消」：隙裂而消。"),
("𧈈","sè",F,"从虫巢聲：虎驚貌（《字彙補》），應為「虩」之訛（《廣韻》「虩，虎驚皃」）。","s取失收：虎驚而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"巢部收尾同取「巢之形、抄掠、小、鳴噪」一面：𢀌殘、𦟳醵、𧑀蜉蝣、䲃魚、𡡊女字、𧷣骨、𪍨麥屑、𠻥眾聲、𦗔耳鳴、䜈代言、㺐夷落、璅玉、𥲀大笙；隟、𧈈為形近之訛。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":583,"name":"巢"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchao3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第583部「巢部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡583c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡583c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))