import json,subprocess,os,glob
F="【450 叀部】叀＝纺专（纺锤）之初文，把多股纤维拈成一根；转义专一、擅自、悬挂、旋转、成团、谨慎；字族多取「圆转、专一」之状。"
N="字形：古文字字形库未收。"
D=[("叀","zhuān",F,"象纺专之形：拈线时悬垂旋转、把多股纤维合成一缕；引申专一、悬挂、旋转、成团、谨慎。","zh「凿总」取「总」：线合而总。"),
("專","zhuān",F,"《玉篇》「自是也、小謹也、擅也、獨也、業也、壹也。今作專」——纺叀拈线成一根，故专一、专擅。","zh取总：线聚而专。"),
("嫥","zhuān",F,"《说文》「壹也，从女專聲」——专一；《玉篇》「可愛之皃」；tuán 美。","zh取总：女专而总。"),
("囀","zhuàn",F,"《集韵》「聲轉也」——鸟婉转地啼叫，如线之旋转曲折。","zh取总：声转而总。"),
("慱","tuán",F,"《尔雅》「慱慱，憂也」；《字彙》「古作團字」——忧思团团、圆满。","t「涂突」取「突」：心团而突。"),
("竱","zhuǎn",F,"《说文》「等也，从立專聲」——《国语》「竱本肇末」：齐等、相当。","zh取总：立齐而总。"),
("𡭐","shuàn",F,"《说文》「小巵有耳蓋者，从巵專聲」——有耳有盖的小圆酒器。","sh「失收」取「收」：器圆而收。"),
("篿","tuán",F,"《说文》「圜竹器也」——圆形竹器；zhuān 楚人折竹占卜曰篿。","t取突：竹圆而突。"),
("漙","tuán",F,"《说文》新附「露皃」——露水团团；zhuān 通「湍」。","t取突：露聚而突。"),
("鄟","zhuān",F,"《玉篇》「邾婁之邑」——春秋鲁附庸小国，在今山东郯城东北。","zh取总：地名借声。"),
("鏄","tuán",F,"《集韵》「塊鐵」——圆形铁块。","t取突：铁圆而突。"),
("檲","tuán",F,"《集韵》「大木」——大木，取圆团之状。","t取突：木大而突。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取叀部「纺线圆转、专一」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第450部「叀部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡450a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡450a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡450a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))