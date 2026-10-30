import json,subprocess,os,glob
F="【464 尤部·余支】尤支转义有二：一为「寄生的、不动的」——肬为赘瘤、𩑣为头颤、忧为不动、𧰰为疣猪；一为「形近之讹」——㞃、𣏞、㕱皆讹字。"
N="字形：古文字字形库未收。"
D=[("𩑣","yòu",F,"从頁尤声——《说文》「顫也」，头不停摇动之病。","y「柔锐」取「锐」：头摇而锐。"),
("肬","yóu",F,"从肉尤声——《说文》「贅也」，肉瘤，出皮上聚如丘。","y取锐：瘤突而锐。"),
("蚘","yóu",F,"从虫尤声——蚩尤之「尤」通作蚘；又读 huí，即蛔虫。","y取锐：虫聚而锐。"),
("訧","yóu",F,"从言尤声——《说文》「罪也」，《周书》「報以庶訧」。","y取锐：罪责而锐。"),
("忧","yòu",F,"从心尤声——《说文》「不動也」；今为「憂」之简化字，发愁。","y取锐：心定而锐。"),
("𤘜","yóu",F,"从牛尤声——《字彙》「不動也」，牛静而不动。","y取锐：牛静而锐。"),
("𧰰","yóu",F,"从豕尤声——《玉篇》「豕也」，当指疣猪（眼下有疣）。","y取锐：豕突而锐。"),
("㞃","jí",F,"从尢尤声——倦㞃；《正字通》以为「谻」之讹。","j「聚决」取「决」：倦而决。"),
("𣏞","yóu",F,"从木尤声——樟属、梓属；《正字通》疑为「杅」之讹。","y取锐：木直而锐。"),
("㕱","yóu",F,"从口尤声——《玉篇》「犬吠也」，疑为「吠」之讹。","y取锐：吠声而锐。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取尤部「寄生不动／形近致讹」两面，形符各定落点：頁主颤、肉主瘤、虫豕主物、言心主情。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第464部尤部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡464b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡464b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡464b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))