import json,subprocess,os,glob
B="【420 戒部】戒＝甲骨文双手持戈（或大持戈形），象意武装防范（《说文》「警也，从廾持戈，以戒不虞」）。转义：警戒→谨慎、准备；警告→告诉、命令；又引申指界限。音源：借音字，义音同「亥」，古戒、亥可通（《周礼》「鼓皆駴」《释文》「駴本亦作骇」）。字族衍义：①戒备→束缚、约止 ②警告→警示、凶暴 ③形近「夭」之讹。"
N="字形：古文字字形库未收。"
D=[("戒","jiè","本部部首字——双手持戈，武装防范。","j「聚决」取「聚」：兵聚而戒。"),
("悈","jiè","《说文》「饰（饬）也」——戒饬，即掩饰慌张强作镇定；又疾也、老也。","j「聚决」取「决」：心决而镇定。"),
("械","xiè","《说文》「桎梏也」——木制束缚手脚的刑具；引申器械、用具。","x「续消」取「续」：械续而用。"),
("祴","gāi","《说文》「宗庙奏祴乐」——祴夏之乐，客醉而出奏之，以为行步之节。","g「隔估」取「隔」：乐以隔节。"),
("裓","gé","《类篇》「衣裾」——衣襟；又堂涂（堂下阶前砖路）。","g「隔估」取「隔」：衣隔而蔽。"),
("誡","jiè","《说文》「敕也」——告诫、规劝；警也、命也、告也。","j「聚决」取「决」：言决而诫。"),
("㖑","xiè","《玉篇》「喝㖑也」——吆喝呵斥；又诋毁非议。","x「续消」取「消」：言消而斥。"),
("駴","hài","《玉篇》「雷击鼓也」——击鼓声如疾雷；与骇同。","h「豁活」取「豁」：鼓豁而雷。"),
("㑘","jiè","《说文》「善也」——善、大；或与介同，指介绍。","j「聚决」取「聚」：人聚而介。"),
("𤈪","kài","《集韵》「烗，炽也」——炽盛之火。","k「口控」取「控」：火控而炽。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取戒部「持戈戒备——束止／警示」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第420部「戒部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡420a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡420a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡420a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))