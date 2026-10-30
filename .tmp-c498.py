import json,subprocess,os,glob
B="【422 克部】克＝从革从由（两字皆从口，故省一口）：革指剥下的生皮，由指油；生皮去毛之外还须脱脂，鞣染后又须加油以复柔软防裂，故本义是给干皮脱脂或加油使之柔软，引申制服、获胜（《玉篇》「能也、获也、胜也」）。音源：本「革」声，今字形已看不出革，故单立部；义音同「亥」。"
N="字形：古文字字形库未收。"
D=[("勀","kè","《说文》「尤极也」——极其尽力辛劳；又胜也、自强。","k「口控」取「控」：力控而极。"),
("剋","kè","《广韵》「剋己，又必也、杀也、急也」；剋期＝约定期日；与克同。","k「口控」取「控」：控而必取。"),
("𢭪","kē","《字海》「拿」——握持。","k「口控」取「控」：手控而拿。"),
("娔","kè","《广韵》「骂女老」——詈骂老妇。","k「口控」取「控」：口控而骂。"),
("殑","qíng","《集韵》「殑㱡，欲死貌」；《玉篇》「掣缩也」。","q「亲缺」取「亲」：气亲而缩。"),
("𠗌","jìng","《集韵》「𠗌冼，寒貌」。","j「聚决」取「聚」：寒聚而缩。"),
("𠳭","kè","象声词——罗𠳭，啰嗦。","k「口控」取「控」：声控而絮。"),
("氪","kè","无色惰性气体元素 Kr——音译。","k「口控」取「控」：气控而惰。"),
("㳳","kè","㳳介子（原子），介子的一种，符号 K——音译。","k「口控」取「控」：微粒借声。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取克部「脱脂加油——由刚柔、由柔胜」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第422部「克部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡422b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡422b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡422b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))