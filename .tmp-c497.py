import json,subprocess,os,glob
from docx import Document
d=Document(r"D:\字谱智能体\卷七十  亥.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(241,258):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:64])
B="【422 克部】克＝从革从由（「革」「由」皆从口，故省一口）：革指剥下的生皮，由指油。加工生皮除毛外还须脱脂；而皮鞣制、染色后又要加油以复柔软、防僵硬开裂。故本义是给干皮脱脂或加油使之柔软，引申制服、获胜（《玉篇》「能也、获也、胜也」）。辯證：革下皮形与「人」形相近，故《说文》「肩也，象屋下刻木之形」不确。音源：本「革」声，今字形已看不出革，故单立部；义音同「亥」（《书·吕刑》「其审克之」，《汉书·刑法志》引作「核」）。"
N="字形：古文字字形库未收。"
D=[("克","kè","本部部首字——从革从由，脱脂加油使皮柔软；引申制服、战胜。","k「口控」取「控」：控皮而使柔。",B)]
for ch,p,xp,sm,b in D:
    sec=[{"key":"bengen","label":"字根本义","text":b,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取克部「治皮使柔→制伏」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第422部「克部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm,b) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡422a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡422a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡422a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))