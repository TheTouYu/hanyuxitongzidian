import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FX="【第545部「休部」】休＝从人从木（依木而息、坐臥止息），《說文》「息止也，从人依木」；轉義止、完了；木或作禾（秸秆座墊）。"
FJ="【第546部「臼部」】臼＝本與凵同源，象坎穴形（古者掘地為臼），後穿木石為臼，《說文》「舂也……中，米也」；轉義舂具、陷穴。"
N="字形：古文字字形库未收。"
D=[("休","xiū",FX,"从人依木而息；引申止、完成（死亦曰休）。","x「续消」取「续」：息而續。"),
("茠","hāo",FX,"从艸休聲：茠，除草（薅之或体）。","h「豁活」取「豁」：草除而豁。"),
("鵂","xiū",FX,"从鳥休聲：鵂鶹，鴟鵂（貓頭鷹一類）。","x取续消：鳥夜而續。"),
("貅","xiū",FX,"从豸休聲：貔貅，猛獸名。","x取续消：獸猛而续。"),
("庥","xiū",FX,"从广休聲：庇也（《說文》「庇也」），蔭庇。","x取续消：庇而續。"),
("髹","xiū",FX,"从髟休聲：赤黑漆（《說文》「桼也」），以漆飾物。","x取续消：漆而續。"),
("咻","xiū",FX,"从口休聲：噢咻，病痛之聲（《說文》「嚾也」）。","x取续消：聲續而消。"),
("烋","xiāo",FX,"从火休聲：炰烋，氣健自矜貌（《說文》引《詩》）。","x取续消：火盛而消。"),
("恘","qiū",FX,"从心休聲：戾也（《集韻》），恘戾。","q「亲缺」取「亲」：心戾而缺。"),
("銝","xiū",FX,"从金休聲：銝，鐵之耎者（《集韻》）。","x取续消：金柔而续。"),
("臼","jiù",FJ,"象坎穴形，掘地為臼，後穿木石；引申舂具、陷穴。","j「聚决」取「聚」：米聚而决。"),
("齨","jiù",FJ,"从齒臼聲：齨，老人齒（《說文》「老人齒」）。","j取聚决：齿聚而决。")]
for ch,p,F0,xp,sm in D:
    bn=545 if ch!="臼" and ch!="齨" else 546
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"休系同取「依木而息、蔭庇」一面（茠除草、庥庇、髹漆、貅獸）；臼系言坎穴舂米（臼、齨）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"休" if bn==545 else "臼"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第545－546部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡546a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡546a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡546a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))