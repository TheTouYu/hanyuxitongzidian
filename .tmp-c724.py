import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FL="【第548部「翏部」】翏＝从羽㐱聲，象鳥高飛、風聲（《說文》「高飛也」）；引申空寥、殺戮、膠黏。"
FH="【第549部「好部」】好＝从女从子，象婦人抱子，《說文》「美也」；引申美好、喜愛（去聲）、友好。"
N="字形：古文字字形库未收。"
D=[("戮","lù",FL,"从戈翏聲：殺也（《說文》「殺也」），刑戮、戮力（并力）。","l「拢离」取「离」：刃離而戮。"),
("寥","liáo",FL,"从宀翏聲：空虛也，寥廓、寂寥。","l取拢离：空而离。"),
("膠","jiāo",FL,"从肉翏聲：胾也（《說文》「胾也」，用動物膠），膠黏。","j「聚决」取「聚」：黏聚而决。"),
("謬","miù",FL,"从言翏聲：狂者之妄言（《說文》「狂者之妄言也」），謬誤。","m「蒙末」取「末」：言妄而末。"),
("繆","miù",FL,"从糸翏聲：枲之十絜（《說文》），綢繆、紕繆。","m取蒙末：絲結而末。"),
("勠","lù",FL,"从力翏聲：并力也（《說文》「并力也」），戮力同。","l取拢离：合力而离。"),
("瘳","chōu",FL,"从疒翏聲：疾瘉也（《說文》「疾瘉也」），病癒。","ch「刺持」取「持」：病去而持。"),
("鏐","liú",FL,"从金翏聲：美金也（《說文》「美金也」），紫磨金。","l取拢离：金美而离。"),
("鷚","liù",FL,"从鳥翏聲：天鸙（《說文》「天鸙也」），雲雀一類。","l取拢离：鳥高而离。"),
("漻","liáo",FL,"从水翏聲：清深也（《說文》「清深也」）。","l取拢离：水清而离。"),
("熮","liáo",FL,"从火翏聲：火貌（《說文》「火貌」）。","l取拢离：火揚而离。"),
("好","hǎo",FH,"从女从子（婦人抱子）：美也（《說文》）；引申美好、喜愛、友好。","h「豁活」取「豁」：美而豁。")]
for ch,p,F0,xp,sm in D:
    bn=548 if ch!="好" else 549
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"翏系同取「高飛、空遠、糾結」一面（戮殺、寥空、膠黏、繆結）；好系言母子相抱之美；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"翏" if bn==548 else "好"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lliao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第548－549部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡549a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡549a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡549a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))