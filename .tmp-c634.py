import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FG="【第519部「光部」】光＝从火在卩（跪人）上，象人借火光照明（《說文》「明也」）；轉義榮耀、色彩、裸露空盡；音源借「黃」（火光偏黃）。字族多取「耀眼／照亮」。"
N="字形：古文字字形库未收。"
D=[("光","guāng",FG,"本部字根：火在人上，引申明、榮、裸。","g「隔估」取「隔」：隔暗而明。"),
("洸","guāng",FG,"从水从光：水湧而閃光（《說文》「水湧光也」），又武貌。","g取隔估：水波隔光。"),
("晄","huǎng",FG,"从日光聲：明也（《說文》），明晃。","h「豁活」取「豁」：日豁而晃。"),
("胱","guāng",FG,"从肉光聲：膀胱，取薄而透光為義（《甲乙經》「胱者，廣也」）。","g取隔估：薄而透。"),
("幌","huǎng",FG,"从巾光聲：帷幔、窗簾（《玉篇》），又頭巾、酒招。","h取豁活：幔張而豁。"),
("恍","huǎng",FG,"从心光聲：恍惚、模糊不清（《玉篇》）。","h取豁活：心恍而豁。"),
("桄","guàng",FG,"从木光聲：充滿（《說文》「充也」）；織機、車船上的橫木。","g取隔估：木橫而隔。"),
("珖","guāng",FG,"从玉光聲：玉笛（《玉篇》「珖琯也」），玉名。","g取隔估：玉潤而隔。"),
("垙","guāng",FG,"从土光聲：田間小路（《集韻》「陌也」）。","g取隔估：路分而隔。"),
("侊","guāng",FG,"从人光聲：盛貌（《說文》「小皃」，段注謂當作大，光聲字多訓光大）。","g取隔估：人盛而隔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分二面：取「耀眼明晃」（光／洸／晄／胱／幌／恍／珖／垙／侊）、取「照亮橫木」（桄）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":519,"name":"光"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lguang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第519部「光部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡519a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡519a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡519a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))