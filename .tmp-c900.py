import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第593部「林部」】林＝二木並立，平土有叢木曰林（《說文》「平土有叢木曰林」）；本卷音源字為殸（擊磬）與冬（冰淩），林為借音字，取懸磬或懸冰成林之狀為意；轉義 眾多、匯聚。"
D=[("林","lín",F,"从二木：平土有叢木曰林（《說文》）；轉義 眾多、匯聚。","l「拢离」取「拢」：木聚而拢。"),
("森","sēn",F,"从三木：木多皃（《說文》「木多皃」），繁密陰森。","s「失收」取「收」：木密而收。"),
("淋","lín",F,"从水林聲：以水沃也（《說文》「以水沃也」），澆淋。","l取拢离：水沃而拢。"),
("霖","lín",F,"从雨林聲：雨三日以往為霖（《說文》「雨三日以往為霖」），久雨。","l取拢离：雨久而拢。"),
("痳","lín",F,"从疒林聲：疝病（《說文》「疝病」），小便不通；又 麻痺。","l取拢离：病聚而拢。"),
("郴","chēn",F,"从邑林聲：桂陽縣（《說文》「桂陽縣」），今郴州。","ch「刺持」取「持」：邑聚而持。"),
("綝","chēn",F,"从糸林聲：止也（《說文》「止也」），又 綝纚，衣裳毛羽垂皃。","ch取刺持：絲止而持。"),
("罧","shèn",F,"从网林聲：積柴水中以取魚（《說文》「積柴水中以取魚」）。","sh「失收」取「收」：魚聚而收。"),
("崊","lín",F,"从山林聲：山名（《集韻》），山深。","l取拢离：山聚而拢。"),
("潹","chán",F,"从水林聲：水聲（《集韻》）。","ch取刺持：水激而持。"),
("焚","fén",F,"从火林聲：燒田也（《說文》「燒田也」），焚燒。","f「附分」取「附」：火附而分。"),
("婪","lán",F,"从女林聲：貪也（《說文》「貪也」），婪酣。","l取拢离：貪聚而拢。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"林部同取「木聚成林、懸冰成林」一面：林叢木、森木多、淋沃水、霖久雨、痳疝病、郴邑、綝絲止、罧取魚、崊山、潹水聲、焚燒田、婪貪；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":593,"name":"林"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llin-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第593部「林部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡593a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡593a{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))