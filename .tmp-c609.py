import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【500 工部】工＝象規矩之器（一說夯築之具），本義工具、工匠、工巧（《說文》「巧飾也」）；轉義工程、官吏、擅長。部內从工諸字多取「器用、工巧、中空方正」三面。"
N="字形：古文字字形库未收。"
D=[("工","gōng",F,"本部部首字：規矩之器→工匠、工巧、工程、擅長。","g「隔估」取「隔」：規矩相隔。"),
("巨","jù",F,"象人手持矩之形：矩所以為方，引申巨大、豈。","j「聚决」取「聚」：聚規成巨。"),
("巧","qiǎo",F,"从工丂聲：工之善者曰巧（《說文》「技也」）。","q「亲缺」取「缺」：巧在缺處。"),
("攻","gōng",F,"从攴工聲：擊也（《說文》「擊也」），引申攻治。","g取隔：擊以隔物。"),
("功","gōng",F,"从力工聲：以力成事曰功，取工之成就。","g取隔：力隔而成。"),
("扛","káng",F,"从手工聲：以肩舉物（《說文》「橫關對舉也」）。","k「口控」取「控」：控舉而扛。"),
("江","jiāng",F,"从水工聲：長江、大川，取工之聲。","j取聚：水聚成江。"),
("空","kōng",F,"从穴工聲：穴中空虛（《說文》「竅也」），引申虛、天。","k取口控：孔竅受控。"),
("孔","kǒng",F,"从乙从子：象乳子之形，本義通、甚；借為孔竅。","k取口控：竅口受控。"),
("項","xiàng",F,"从頁工聲：頸後曰項，引申條目、款項。","x「续消」取「续」：頸續於項。"),
("汞","gǒng",F,"从水工聲：水銀，其性流走而固。","g取隔：質重而隔。"),
("貢","gòng",F,"从貝工聲：獻功於上曰貢（《說文》「獻功也」）。","g取隔：獻而相隔。"),
("邛","qióng",F,"从邑工聲：地名（邛崍），又「邛邛」獸名。","q取亲缺：地缺而邛。"),
("釭","gāng",F,"从金工聲：車轂中鐵（《說文》「車轂中鐵也」），又燈。","g取隔：鐵隔轂中。"),
("仝","tóng",F,"从人工聲：「同」之異體，取工之聲。","t「涂突」取「涂」：合而同。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取工部「器用、工巧、中空」一面：水取其流，穴取其虛，金取其固。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lcu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第500部工部（卷八十二 工）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡500a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡500a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡500a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))