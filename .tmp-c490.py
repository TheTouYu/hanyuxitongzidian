import json,subprocess,os,glob
B="【419 犮部（叐）】犮与亥同源，商代晚期金文象直立的旱獭正面形，足部加一丿表示抬起前肢（《说文》误以形近「犬」释为「走犬皃」）。转义：直立→挺拔抽引（拔）、往前扑（跋）、毛皮细软面小宜作蔽膝（袚）、穴居掘根致沙化→旱灾（魃）、毛发（髮）、腿肉（胈）。音源：源自旱獭叫声。"
N="字形：古文字字形库未收。"
D=[
{"ch":"祓","p":"fú","xp":"《说文》「除恶祭也」——除灾求福、洁也。","sm":"f「附分」取「分」：祭以分灾。"},
{"ch":"𨈩","p":"bó","xp":"《字汇》「行急也」。","sm":"b「闭剥」取「剥」：足剥地而急。"},
{"ch":"䮂","p":"bó","xp":"《广韵》「䮂䮧，蕃中马也」——汗血马。","sm":"b「闭剥」取「剥」：马蹄剥地。"},
{"ch":"菝","p":"bá","xp":"《广韵》「菝葀，瑞草」；菝葜俗称金刚刺、金刚藤——《本草》「茎蔓坚强短小，故名」。","sm":"b「闭剥」取「剥」：蔓剥而短硬。"},
{"ch":"鮁","p":"bō","xp":"《说文》「鳣鲔鲅鲅」——鱼掉尾而游貌；又鲅鱼。","sm":"b「闭剥」取「剥」：鱼尾剥水。"},
{"ch":"柭","p":"bā","xp":"《说文》「棓也」——拐杖；拄杖以挺立，故有拔义；又连枷。","sm":"b「闭剥」取「剥」：杖剥地而挺。"},
{"ch":"䳁","p":"bó","xp":"《说文》「鸟也」——大鸟；似凫、似雉。","sm":"b「闭剥」取「剥」：鸟剥羽而飞。"},
{"ch":"詙","p":"bá","xp":"古人名用字；bó 读「评詙」——评论、估量。","sm":"b「闭剥」取「剥」：言剥而评。"},
{"ch":"秡","p":"bó","xp":"《玉篇》「禾伤」——粃谷，禾穗直立状。","sm":"b「闭剥」取「剥」：禾剥而穗直。"},
{"ch":"𥬒","p":"pō","xp":"《类篇》「䈇也」——罩鱼的竹器。","sm":"p「拼辟」取「辟」：器辟而罩。"},
{"ch":"䯋","p":"bó","xp":"《集韵》「䯋𩨮，骨高貌」——肩髆骨；又骨端。","sm":"b「闭剥」取「剥」：骨剥而高。"},
{"ch":"沷","p":"fā","xp":"《玉篇》「寒也」；《正字通》「渫也，通流也」——疏浚。","sm":"f「附分」取「分」：水分为流。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取犮部「直立·抽引／短硬·扑出」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第419部「犮部」（卷七十 亥）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡419b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡419b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡419b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))