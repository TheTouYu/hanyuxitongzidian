import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FD="【第538部「畕部」】畕＝从二田，田界相比相鄰（《說文》「比田也」），為疆之聲根。"
FH="【第539部「鬯部」】鬯＝象以器盛黑黍酒、中加香草之形，《說文》「以秬釀鬱艸，芬芳攸服以降神也」；引申暢通、抒發。"
N="字形：古文字字形库未收。"
D=[("疆","jiāng",FD,"从土彊聲：界也（《說文》），田界、疆域。","j「聚决」取「聚」：界聚而决。"),
("彊","qiáng",FD,"从弓畺聲：弓有力也（《說文》）；引申強盛、強迫。","q「亲缺」取「亲」：弓强而缺。"),
("僵","jiāng",FD,"从人畺聲：僨也（《說文》），倒地不動，僵硬。","j取聚决：人僵而聚。"),
("繮","jiāng",FD,"从糸畺聲：馬韁（繫馬之繩）。","j取聚决：系马而聚。"),
("韁","jiāng",FD,"从革畺聲：馬韁，皮製繫馬繩。","j取聚决：革系而聚。"),
("薑","jiāng",FD,"从艸畺聲：生薑，辛辣之菜。","j取聚决：草辛而聚。"),
("畺","jiāng",FD,"从田从三（界画）：界也（《說文》），田界，畕之繁。","j取聚决：田界而聚。"),
("礓","jiāng",FD,"从石畺聲：礓礫，小石。","j取聚决：石聚而决。"),
("疅","jiāng",FD,"从田畺聲：界也（《說文》），田邊。","j取聚决：田界而聚。"),
("㹔","jiāng",FD,"从牛畺聲：白牛（《說文》「牛白脊也」）。","j取聚决：牛聚而决。"),
("鬯","chàng",FH,"象器盛黑黍香草酒以祭；引申暢通、抒發（暢之本字）。","ch「刺持」取「持」：香持而通。"),
("秬","jù",FH,"从禾巨聲：黑黍也（《說文》），釀鬯所用。","j取聚决：黍聚而实。")]
for ch,p,F0,xp,sm in D:
    bn=538 if ch!="鬯" and ch!="秬" else 539
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"畕系同取「田界相鄰、引而強直」一面（疆土、彊弓、繮韁、薑辛）；鬯系言香酒通神（鬯、秬）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"畕" if bn==538 else "鬯"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljiang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第538－539部（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡539a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡539a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡539a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))