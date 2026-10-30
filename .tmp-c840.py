import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第582部「小部」】小＝甲骨文象麻雀的腳印（麻雀後趾短，落地只顯前三趾），「雀」之初文；又作三點疊體表細微；引申微小、細；音源為麻雀叫聲。（部內分支：肖、雀、少、屑、尗、塵、尖）"
N="字形：古文字字形库未收。"
D=[("小","xiǎo",F,"象雀三趾腳印（《說文》「物之微也」），引申細微、微小。","x「续消」取「消」：微末而消。"),
("㭂","jiǎo",F,"从木小聲：相高也（《說文》），木忽高；樹梢。","j「聚决」取「聚」：木末而决。"),
("釥","qiǎo",F,"从金小聲：美金也（《玉篇》），好、淨；又利。","q「亲缺」取「亲」：金精而亲。"),
("𩵖","xiǎo",F,"从魚小聲：魚名（《玉篇》），細小魚。","x取续消：魚小而消。"),
("䒕","xiǎo",F,"从艸小聲：葽䒕，艸名（《集韻》），即遠志（莖葉纖細）。","x取续消：草細而消。"),
("仦","miáo",F,"从人小：小兒也（《字彙補》引《說略》），幼小。","m「蒙末」取「末」：童小而末。"),
("尕","gǎ",F,"从小：小也（《字彙補》），西北方言「尕娃」。","g「隔估」取「估」：小可估。"),
("尘","chén",F,"从小从土：塵之俗字（《字彙補》），飛塵細微。","ch「刺持」取「持」：塵聚而持。"),
("尛","mó",F,"从三小：麼之古字（《字彙補》），細小。","m取蒙末：微末而末。"),
("肖","xiào",F,"从肉小聲：骨肉相似也（《說文》），像、似；不肖＝子不似父。","x取续消：似續而消。"),
("宵","xiāo",F,"从宀肖聲：夜也（《說文》「宵，夜也」），夜晚。","x取续消：夜深而消。"),
("消","xiāo",F,"从水肖聲：盡也（《說文》「消，盡也」），融化、消滅。","x取续消：水散而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"小部同取「細微」一面：小、㭂、釥、𩵖、䒕、仦、尕、尘、尛、肖、宵、消；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":582,"name":"小"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第582部「小部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡582a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡582a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))