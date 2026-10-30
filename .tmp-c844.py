import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第582部「小部」·雀支】雀＝小之疊體（雀之初文从雀省），其字族取「細小、截斷、節制、咀嚼」諸面；雀支字多含「截／節」聲義。"
N="字形：古文字字形库未收。"
D=[("截","jié",F,"从戈雀聲：斷也（《說文》「截，斷也」），截斷、齊平。","j「聚决」取「决」：斷而决。"),
("嚼","jiáo",F,"从口爵聲（雀支）：咀嚼（《說文》「齧也」），以牙磨碎。","j取聚决：齒合而决。"),
("穧","jì",F,"从禾齊聲（雀支）：穫禾聚把（《說文》「穫禾聚把也」）。","j取聚决：禾聚而决。"),
("節","jié",F,"从竹即聲：竹約也（《說文》「竹約也」），竹節→節制、符節。","j取聚决：分段而决。"),
("巀","jié",F,"从山截聲：巀嶭，山高峻（《說文》「巀嶭，山也」）。","j取聚决：山高而决。"),
("癤","jiē",F,"从疒節聲：癤子（《集韻》），皮膚腫結。","j取聚决：毒聚而决。"),
("蠘","jié",F,"从虫截聲：梭子蟹（《集韻》），甲殼尖利。","j取聚决：殼尖而决。"),
("蠽","jié",F,"从虫雀聲：蟬屬（《說文》「蠽，蟬屬」）。","j取聚决：鳴聚而决。"),
("籖","qiān",F,"从竹韱聲：驗也（《說文》作「籤」），竹簽、籤驗。","q「亲缺」取「亲」：簽入而亲。"),
("熦","jué",F,"从火雀聲：炬火（《集韻》），小火。","j取聚决：火聚而决。"),
("噍","jiào",F,"从口焦聲：齧也（《說文》「噍，齧也」），咀嚼；又聲。","j取聚决：齧合而决。"),
("擮","jié",F,"从手截聲：拔也（《集韻》），拔取。","j取聚决：拔斷而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"雀支同取「截斷、節制、細小」一面：截斷、嚼齧、穧聚、節約、巀高、癤結、蠘殼、蠽蟬、籖驗、熦火、噍齧、擮拔；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":582,"name":"小"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiao3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第582部「小部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡582c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡582c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))