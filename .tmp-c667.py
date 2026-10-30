import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FD="【第527部「向部」·當系（二级字根）】當＝从田尚聲，田與田相值（《說文》「田相值也」）；轉義對等相值→承受擔任→正當、應當，又表曾經。字族三面：相值對當／承受擔任／器物之中（底、當）。"
N="字形：古文字字形库未收。"
D=[("壋","dǎng",FD,"橫築河中或低窪田地擋水的小堤；或同「凼」，塘、水坑。","d「囤动」取「囤」：土擋而囤。"),
("儅","dāng",FD,"《廣韻》「止也」；又「不中」、正中、倜儅不羈。","d取囤动：人當而囤。"),
("簹","dāng",FD,"《廣韻》「篔簹，竹名」；《玉篇》「車簹管」，車前後屏蔽。","d取囤动：竹當而囤。"),
("澢","dǎng",FD,"《玉篇》「水也」，水氹。","d取囤动：水聚而囤。"),
("艡","dāng",FD,"《集韻》「𦨢艡，舟也」，大船。","d取囤动：舟當而囤。"),
("礑","dàng",FD,"《正字通》「底也」，凡物有底者皆曰當，加石為贅。","d取囤动：石底而囤。"),
("闣","tāng",FD,"《五音集韻》「盛皃」；又鼓聲（鼞之或體）、閃闣人。","t「涂突」取「涂」：門盛而突。"),
("㼕","dāng",FD,"《玉篇》「瓜中實」；《正字通》「瓜底曰㼕」。","d取囤动：瓜實而囤。"),
("劏","tāng",FD,"方言，宰殺——剖開之意。","t取涂突：剖開而突。"),
("㽆","dāng",FD,"《集韻》「甌屬」，或指瓦當。","d取囤动：瓦當而囤。"),
("螳","táng",FD,"从虫當聲：螳螂，前足如鐮，捕蟬為食。","t取涂突：蟲臂而突。"),
("蟷","dāng",FD,"从虫當聲：蟷蠰，即螳螂（《爾雅》）。","d取囤动：蟲當而囤。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"當系諧聲字分三面：相值對當（壋／儅／闣）／承受擔任（簹／艡／螳／蟷）／器物之中（礑／㼕／㽆／澢／劏）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜，當系）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527g2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527g.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527g.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))