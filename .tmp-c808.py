import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第573部「萬部」】萬（𧍣）＝象蠍子形，尾部蜷曲；引申數目極多；字族取「蠍之毒刺、硬殼、舉尾、群聚」諸面。"
N="字形：古文字字形库未收。"
D=[("犡","lì",F,"从牛厲聲：牛白脊也（《說文》）；《正字通》又謂牛病。","l「拢离」取「离」：牛病而离。"),
("邁","mài",F,"从辵蠆省聲：遠行也（《說文》），往、過、老。","m「蒙末」取「末」：行遠而末。"),
("𡿋","lì",F,"从山蠆聲：巍高也（《說文》「巍高也」），山高大。","l取拢离：山高而离。"),
("澫","màn",F,"从水萬聲：漫也（《正字通》引石鼓文），水漫；又與藕同。","m取蒙末：水漫而末。"),
("濿","lì",F,"从水厲聲：履石渡水也（《說文》「砅」），卷褲渡水。","l取拢离：涉水而离。"),
("厲","lì",F,"从厂蠆省聲：旱石也（《說文》），粗硬磨刀石；引申危險、猛烈、嚴整。","l取拢离：石厲而离。"),
("礪","lì",F,"从石厲聲：䃺也（《說文新附》），磨刀石、磨治。","l取拢离：磨石而离。"),
("𥣭","lì",F,"从禾厲聲：黍穰謂之䅀（《集韻》），黍莖。","l取拢离：禾穰而离。"),
("竊","qiè",F,"从穴从米禼：盜自中出（《說文》「盜自中出曰竊」），偷竊、私自。","q「亲缺」取「亲」：私取而亲。"),
("蠇","lì",F,"从蟲萬聲：蚌屬（《集韻》），牡蠣。","l取拢离：殼附而离。"),
("癩","lài",F,"从疒賴聲：惡疾也（《字彙》），疥癩、麻風。","l取拢离：疾散而离。"),
("糲","lì",F,"从米萬聲：粟重一石為米八斗曰糲（《說文》），粗米。","l取拢离：米粗而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"萬部餘字取「遠行、山高、涉水、磨石、粗米、竊取」一面：犡、邁、𡿋、澫、濿、厲、礪、𥣭、竊、蠇、癩、糲；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":573,"name":"萬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lwan2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第573部「萬部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡573b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡573b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))