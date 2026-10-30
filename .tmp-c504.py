import json,subprocess,os,glob
F="【425 秝部】秝＝从二禾，象禾苗排列稀疏或秸秆堆积；歷支取「禾之春种秋收→逐一经过」一面：历法、经历、过滤、夹持，皆由一行行经过而来。"
N="字形：古文字字形库未收。"
D=[("歷","lì","甲骨文从止秝声，象经过的时间如同庄稼的生长周期；《说文》「过也」——经历、经过，亦作历、曆。","l「拢离」取「离」：一程程离去。"),
("瀝","lì","《说文》「浚也，一曰水下滴沥」——过滤、液体一滴一滴下落。","l取离：水滴离析而下。"),
("癧","lì","《集韵》「瘰疬，病也」——颈部腋下淋巴结结核，累累成串。","l取离：结核颗颗相离。"),
("讈","lì","《集韵》「䜍讈，言不明」——说话含混不清。","l取离：言语支离散乱。"),
("爏","lì","《集韵》「火貌」——火光闪烁。","l取离：火光明灭离散。"),
("靂","lì","《集韵》「霹雳，雷之急激者」——雷声震动。","l取离：雷裂云而离。"),
("嚦","lì","《集韵》「呖呖，声也」——象声，多形容鸟鸣。","l取离：声细碎而离。"),
("䟐","lì","《集韵》「䟐𧻕，盗行」——踮脚快走，行步轻捷。","l取离：举足轻离地。"),
("藶","lì","《集韵》「葶苈，草名」，性急善逐水走泄。","l取离：药性走泄使水离。"),
("櫪","lì","《说文》「櫪㯕，椑指也」——夹手指的刑具；又马槽、马房、蚕箔。","l取离：木条并列相夹。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取歷「逐一经过／离析」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"bl2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第425部「秝部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡425b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡425b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡425b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))