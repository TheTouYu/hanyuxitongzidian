import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第547部「酉部」】酉＝尖底酒瓶（酒之初文），轉義地支八月、成熟成就。"
FL="【第548部「翏部」】翏＝从羽㐱聲，象鳥高飛、風聲，《說文》「高飛也」；引申空寥（寥）、殺戮（戮）、膠黏（膠）。"
N="字形：古文字字形库未收。"
D=[("梄","yǒu",FY,"从木酉聲：積薪燒之也（《說文》「積木燎之也」）。","y「柔锐」取「锐」：火锐而燎。"),
("庮","yǒu",FY,"从广酉聲：久屋朽木（《說文》「久屋朽木」），臭也。","y取柔锐：朽而锐。"),
("莤","sù",FY,"从艸酉聲：束茅縮酒（《說文》「《禮》祭束茅加於祼圭而灌鬯酒」）。","s「失收」取「收」：茅束而收。"),
("糟","zāo",FY,"从米曹聲：酒滓也（《說文》「酒滓也」），糟粕。","z「凿总」取「凿」：滓實而凿。"),
("綇","xū",FY,"从糸酉聲：繒也（《說文》「繒也」）。","x「续消」取「续」：絲續而消。"),
("揂","jiū",FY,"从手酋聲：聚也（《說文》「聚也」）。","j「聚决」取「聚」：手聚而决。"),
("楢","yóu",FY,"从木酋聲：柔木也（《說文》「柔木也」），可為薪。","y取柔锐：木柔而锐。"),
("崷","qiú",FY,"从山酋聲：崷崪，山高貌。","q「亲缺」取「亲」：山高而缺。"),
("蕕","yóu",FY,"从艸酋聲：水邊草（《說文》「蕕，水邊艸也」），臭草。","y取柔锐：草臭而锐。"),
("鰌","qiū",FY,"从魚酋聲：泥鰍（鰍之或体），善鑽泥。","q取亲缺：魚潛而缺。"),
("蝤","qiú",FY,"从虫酋聲：蝤蛴（木中蠹蟲），天牛幼蟲。","q取亲缺：蟲鑽而缺。"),
("翏","liù",FL,"从羽㐱聲：高飛也（《說文》），風聲、空寥。","l「拢离」取「离」：飛離而遠。")]
for ch,p,F0,xp,sm in D:
    bn=547 if ch!="翏" else 548
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"酉系同取「酒、熟、聚」一面（梄燎、庮朽、糟滓、揂聚）；翏系言高飛寥遠；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"酉" if bn==547 else "翏"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyou2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第547－548部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡548a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡548a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡548a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))