import json,subprocess,os,glob
F="【427 聿部】聿＝手持半竹，作书写之具；本部余字分四路：笔之蘸墨（黑、滤）、笔之记述（声、言）、笔之蘸写（笔、草行）、笔之状（尖细）。"
N="字形：古文字字形库未收。"
D=[("𪑯","lèi","《玉篇》「黑也」——黑色。","l「拢离」取「离」：墨色离散而黑。"),
("𥞰","lǜ","《奇姓通》「游𥞰，复姓」——《通志》作游𣑵氏，𣑵之讹。","l取离：借形记姓。"),
("𢯰","lǜ","《集韵》「去滓汁曰𢯰」——滤去渣滓取清汁。","l取离：渣滓离析。"),
("𢫫","lù","《玉篇》「捽也，捋也」——揪、捋。","l取离：手捋而离。"),
("㖀","lè","《集韵》「声也」——声音。","l取离：声散而离。"),
("𠷈","lǜ","《集韵》「呜也」；liè《类篇》「鸡鸣」。","l取离：鸣声散布。"),
("𢗱","zhì","《川篇》同「志」——心之所向。","zh「凿总」取「总」：志总于心。"),
("𧧪","qián","《龙龛》「讪，正；𧧪，俗」——谤毁、讥讪。","q「亲缺」取「缺」：言缺而讪。"),
("𥒠","huò","《五侯鲭字海》同「砉」——《广韵》「皮骨相离声」。","h「豁活」取「豁」：骨豁然而离。"),
("筆","bǐ","从竹从聿，聿亦声——书写用的笔；《说文》「秦谓之笔」，徐锴「笔尚便疌，故从聿」；引申记述、文笔。","b「闭剥」取「剥」：笔落墨剥于竹。"),
("𨅗","bǐ","《玉篇》「走貌」，《集韵》「走也」——疾走。","b取剥：足剥地而走。"),
("𨖷","shà","《集韵》「行书也」——秦使徒隶助官书草行之间，取其疾速不留意楷法；运笔书写。","b取剥：笔疾剥纸。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取聿部笔写一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))