import json,subprocess,os,glob
F="【451 回部·𠄢（亘）支】亘＝回旋、终而复始之形；诸字取「环绕、绵延、大」诸面。"
N="字形：古文字字形库未收。"
D=[("亘","gèn",F,"《说文》「求亘也，从二从囗」；《广韵》「通也」——回旋绵延，终而复始。","g「隔估」取「隔」：回环而隔。"),
("咺","xuǎn",F,"《说文》「朝鮮謂兒泣不止曰咺」——哭声回旋不止。","x「续消」取「续」：泣续而消。"),
("垣","yuán",F,"《说文》「牆也，从土亘聲」——环绕四周的墙。","y「柔锐」取「锐」：墙围而锐。"),
("狟","huán",F,"《说文》「犬行也」；《广韵》「狟狟，武勇皃」——犬行、武勇。","h「豁活」取「活」：犬行而活。"),
("貆","huán",F,"《说文》「貉之類，从豸亘聲」——貉类小兽，毛可制裘。","h取活：兽穴而活。"),
("桓","huán",F,"《说文》「亭郵表也，从木亘聲」——路旁表木；引申大、威武（桓桓）。","h取活：木表而活。"),
("洹","huán",F,"《说文》「水，在齊魯間」——水名，即安阳洹水，殷墟所在。","h取活：水回而活。"),
("烜","xuǎn",F,"《说文》「爟，火也」；《玉篇》「光明也」——火盛光明。","x取续：火续而消。"),
("絙","gēng",F,"《集韵》「大索也」——粗绳，取绵亘之长。","g取隔：索长而隔。"),
("恒","héng",F,"《说文》「常也，从心从舟，在二之間上下」——心亘古今而不变。","h取活：心常而活。"),
("宣","xuān",F,"《说文》「天子宣室也，从宀亘聲」——宽大之室；引申宣布、宣扬、宣泄。","x取续：气宣而消。"),
("愃","xuān",F,"《说文》「寬嫻心腹皃」——心宽闲适。","x取续：心宽而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取亘支「环绕绵延」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbn-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))