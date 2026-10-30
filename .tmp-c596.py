import json,subprocess,os,glob
F="【479 爰部】爰＝兩手各持藤狀物一端相牽拉（金文上手下手分指俯拉、攀援），引申援助，又作虛詞「為、于、曰」；音源借猿善攀援。"
FY="【480 𥆞部】𥆞＝从𠃌（眼鏡蛇，取其頭背「眼鏡」花紋）从䀠（兩眼），象疲勞或疾病所致的黑眼圈（目圍）；《說文》讀若書卷之卷，古文以為「醜」字；音源因兩眼圓睜而義音同「袁」。"
N="字形：古文字字形库未收。"
D=[("蝯","yuán",F,"从虫爰聲：《集韻》「蝯，《說文》：善援，禺屬」，即猿的本字。","y「续消」取「续」：攀續而援。"),
("鍰","huán",F,"从金爰聲：古重量單位（六兩為鍰），引申罰金之錢。","h「豁活」取「豁」：金輕而豁。"),
("楥","xuàn",F,"从木爰聲：履法（鞋楦），取牽援使成形。","x「续消」取「续」：木續成器。"),
("煖","nuǎn",F,"从火爰聲：與暖同，火氣溫熱。","n「纳弄」取「纳」：火氣內納。"),
("𥆞","juàn",FY,"本部部首字：目圍黑圈→疲勞、醜；古文借為「醜」。","j「聚决」取「聚」：黑聚於眶。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「牽援成器、目眶圍黑」两面：金木火各定其用，目取其圍。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lch-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第479－480部（卷七十八 夒）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡480a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡480a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡480a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))