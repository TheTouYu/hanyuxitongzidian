import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第524部「永部」·羕系（二级字根）】羕＝从永从羊（羊亦聲）：「永」為有支流之大河，「羊」象水勢如羊群浩蕩、白浪起伏，故《說文》「水長也」。轉義：長大（《廣韻》）。字族分二面：似羊之物／蕩漾移動。"
N="字形：古文字字形库未收。"
D=[("羕","yàng",FY,"从永从羊：水長也（《說文》引《詩》「江之羕矣」）；引申長大。","y「圆容」取「圆」：水長而周。"),
("𤡀","yàng",FY,"从犬羕聲：獸名，如狻猊，食熊羆，即「㺊」（《集韻》）。","y取圆容：獸猛而周。"),
("𩞭","yàng",FY,"从食羕聲：餌也、糕餅（《集韻》引《方言》）。","y取圆容：食團而圓。"),
("㨾","yàng",FY,"从手羕聲：式㨾，法也，眾从之意；今「榜樣」正作此（《類篇》）。","y取圆容：法立而周。"),
("樣","xiàng",FY,"从木羕聲：栩實、橡實，葉可飼柞蠶（《說文》）；借為式樣。","x「续消」取「续」：蠶續而絲。"),
("漾","yàng",FY,"从水羕聲：河名（西漢水），又水搖動貌、蕩漾（《集韻》）。","y取圆容：水蕩而周。"),
("𠍵","yàng",FY,"从人羕聲：立動貌（《集韻》音㨾）。","y取圆容：人立而動。"),
("𡡂","yàng",FY,"从女羕聲：女字（《集韻》）。","y取圆容：借聲為字。"),
("𢟣","yàng",FY,"从心羕聲：悵恨也，與「怏」通（《正字通》）。","y取圆容：心悵而周。"),
("𧫛","yàng",FY,"从言羕聲：聲變也（《集韻》音漾）。","y取圆容：聲轉而周。"),
("𨖌","yàng",FY,"从辵羕聲：走也（《字彙》音漾）。","y取圆容：走遠而周。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"羕系同族分二面：似羊之物（𤡀獸／𩞭餌／㨾式／樣橡實）、蕩漾移動（漾／𠍵／𡡂／𢟣／𧫛／𨖌）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":524,"name":"永"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqing-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第524部「永部」·羕系（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡羕系2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡羕系.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡羕系.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))