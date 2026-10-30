import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第593部「林部」】林＝二木並立（《說文》「平土有叢木曰林」），借音字，義音同「廩」（聚集）；轉義 眾多盛大、郊野、陰暗；本批取「林木茂密、遮蔽浸漬、幽深」一面。"
D=[("瀮","lián",F,"从水林聲：久雨（《字海》）。","l「拢离」取「拢」：雨久而拢。"),
("菻","lǐn",F,"从艸林聲：蒿屬（《說文》「蒿屬」），䕲蒿（莪蒿），叢生。","l取拢离：蒿叢而拢。"),
("㯬","liǎn",F,"从木林聲：功勤之稱（《廣韻》），功勞之記。","l取拢离：功聚而拢。"),
("㣩","lín",F,"从彳林聲：林鐘，古樂十二律之一（《集韻》「㣩鐘」）。","l取拢离：律聚而拢。"),
("晽","lín",F,"从日林聲：晽晽，欲所知之貌（《淮南子》注），林中微光。","l取拢离：光微而拢。"),
("箖","lín",F,"从竹林聲：箖箊竹，葉薄而廣（《竹譜》）；又 翳也。","l取拢离：竹密而拢。"),
("漤","lǎn",F,"从水林聲：鹽漬果（《廣韻》），水淹濡（《六書故》「濫，水淹濡也」），果漿。","l取拢离：水漬而拢。"),
("啉","lán",F,"从口林聲：貪也（《玉篇》）；酒巡匝曰啉；又 聒噪。","l取拢离：聲聒而拢。"),
("碄","lín",F,"从石林聲：碄碄，深皃（《集韻》），石深。","l取拢离：石深而拢。"),
("惏","lán",F,"从心林聲：河內之北謂貪曰惏（《說文》），貪多；又 惏慄，寒。","l取拢离：貪而拢。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"林部同取「茂密遮蔽、浸漬幽深」一面：瀮久雨、菻蒿叢、㯬功勤、㣩林鐘、晽微光、箖廣葉竹、漤果漿、啉酒巡、碄石深、惏貪多；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":593,"name":"林"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llin3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第593部「林部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡593c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡593c{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))