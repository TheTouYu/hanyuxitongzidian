import json,subprocess,os,glob
A="【421 革部】革＝甲骨文象剖剥摊开的整张兽皮，引申去毛、更改、革除、急；又指皮制品、老迈、翅膀。音源：借音字，由兵革防御之义而义音同「戒」。"
C="【421 革部·䨣声族】䨣＝从雨从革，皮革挡雨（《说文》「雨濡革也」）；皮虽挡雨而不能久，久则渗漏、濡湿处发胀凸起（《段注》「雨濡革则虚起」），故此族多取「鼓起、虚胀、覆压」义，分化出霸、坝、欛、怕、灞。"
N="字形：古文字字形库未收。"
D=[("鞂","jiē","《集韵》「稭，禾槁去其皮，祭天以为席」——或作秸、鞂，通作戛。","j「聚决」取「聚」：禾聚为席。",A),
("㗆","gé","《集韵》「㗆噊，鸟鸣也」——或作嗝，又作助词「的」。","g「隔估」取「隔」：声隔而鸣。",A),
("䨣","gé","从雨从革——皮革挡雨，久则濡湿虚起。","g「隔估」取「隔」：皮隔雨而胀。",C),
("霸","pò","《说文》「月始生，霸然也」——月始生之光（承大月二日，承小月三日）；由「虚起」义分化。","b「闭剥」取「闭」：月闭而始生。",C),
("壩","bà","《集韵》「堰也」——截住河流的建筑物。","b「闭剥」取「闭」：水闭而坝。",C),
("欛","bà","《广韵》「刀柄名」——器物之柄，便于握持（俗作把）。","b「闭剥」取「闭」：手握而闭。",C),
("𢺞","bǎ","《正字通》「俗把字」——把持。","b「闭剥」取「闭」：把而持之。",C),
("怕","pà","《集韵》「怕，惧也」——因怕而抚胸、脸色发白。","p「拼辟」取「辟」：气辟而惧。",C),
("䨰","pò","《玉篇》「雨也」；濼之或体，陂泽、古国名。","p「拼辟」取「辟」：雨辟而落。",C),
("灞","bà","《广韵》「水名」——灞水出蓝田谷，通作霸。","b「闭剥」取「闭」：水闭而潴。",C)]
for ch,p,xp,sm,b in D:
    sec=[{"key":"bengen","label":"字根本义","text":b,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取革部「皮革绷张／雨濡虚起」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第421部「革部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm,b) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡421c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡421c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡421c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))