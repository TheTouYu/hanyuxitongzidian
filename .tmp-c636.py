import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FL="【第521部「良部」】良＝甲骨文象口之上下各有兩獠牙，為「狼」之初文（有獠牙的肉食動物）；轉義狼崇拜、引申善美；辯證牙形小篆訛作「亡」，《說文》「从亯省亡聲」析形不確；音源為狼嚎聲。"
N="字形：古文字字形库未收。"
D=[("良","liáng",FL,"本部字根：露獠牙之獸，引申善美、良善。","l「拢离」取「拢」：牙拢而噬。"),
("狼","láng",FL,"从犬良聲：似犬銳頭白頰，善逐獸（《說文》）。","l取拢离：群狼相攏。"),
("浪","làng",FL,"从水良聲：滄浪之水（《說文》），引申波浪、放浪。","l取拢离：水湧而離。"),
("踉","liáng",FL,"从足良聲：跳踉、踉蹡，行不迅。","l取拢离：足跳而離。"),
("硠","láng",FL,"从石良聲：石聲（《說文》），硠硠堅也。","l取拢离：石擊而散。"),
("琅","láng",FL,"从玉良聲：琅玕，似珠之玉（《說文》）。","l取拢离：玉潤而攏。"),
("俍","liáng",FL,"从人良聲：良工（《集韻》），善於其事；又長貌。","l取拢离：人之良。"),
("桹","láng",FL,"从木良聲：高木（《說文》），桄桹似椶櫚。","l取拢离：木高而離。"),
("榔","láng",FL,"从木郎聲：榔榆木質堅密，又檳榔。","l取拢离：木結而攏。"),
("蜋","láng",FL,"从虫良聲：堂蜋即螳螂，前肢尖銳有鉤（《說文》）。","l取拢离：臂攏而勾。"),
("鋃","láng",FL,"从金良聲：鋃鏜，鎖鏈（《說文》），又鐘聲。","l取拢离：鏈攏而鎖。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：取「狼之行為／遊蕩」（良／狼／浪／踉）、取「嚎叫大聲」（硠）、取「獠牙銳長」（琅／俍／桹／榔／蜋／鋃）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":521,"name":"良"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"liang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第521部「良部」（卷八十六 良）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡521a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡521a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡521a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))