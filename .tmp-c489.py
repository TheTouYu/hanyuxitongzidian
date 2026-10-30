import json,subprocess,os,glob
B418="【418 亥部】亥＝甲骨文象直立的旱獭形，「鼥」之初文；转义：掘食草根→荄，直立放哨→警惕·防备（该）、受惊竖立（骇），爪尖善掘→刻镂，传播鼠疫近似疟疾→痎，借指地支末位。音源：源自旱獭叫声，因有直挺义而义音同「介」。"
B419="【419 犮部（叐）】犮与亥同源，商代晚期金文象直立的旱獭正面形，足部加一丿表示抬起前肢（《说文》误以形近「犬」释为「走犬皃」）。转义：直立→挺拔抽引（拔）、往前扑（跋）、旱獭毛皮细软珍贵而面小宜作蔽膝之类（袚）、穴居掘根致地表塌陷沙化→旱灾（魃）、毛发（髮）、腿肉（胈）。音源：源自旱獭叫声。"
N="字形：古文字字形库未收。"
D=[
{"ch":"𩠚","p":"hái","xp":"《字汇》「首也」——人的头。","ben":B418,"sm":"h「豁活」取「豁」：首豁在上。"},
{"ch":"𥞨","p":"jiē","xp":"同「秸」——农作物收割后的茎。","ben":B418,"sm":"j「聚决」取「聚」：茎聚成把。"},
{"ch":"𦈲","p":"kāi","xp":"《集韵》「器名」；又藏也。","ben":B418,"sm":"k「口控」取「控」：器控而藏。"},
{"ch":"𦷷","p":"hài","xp":"《直音》「蒿也」——蒿草。","ben":B418,"sm":"h「豁活」取「豁」：草豁而长。"},
{"ch":"𧊏","p":"gāi","xp":"《玉篇》「虫名」；《正字通》以为讹字。","ben":B418,"sm":"g「隔估」取「隔」：虫隔于壳。"},
{"ch":"𩰶","p":"hái","xp":"《集韵》「麧也，一曰糜中块」——粥中的块。","ben":B418,"sm":"h「豁活」取「活」：糜中有块。"},
{"ch":"烗","p":"kài","xp":"《广韵》「炽也、盛也」——火盛。","ben":B418,"sm":"k「口控」取「控」：火控而炽。"},
{"ch":"拔","p":"bá","xp":"《说文》「擢也」——连根拽出；引申挺、攻取、尽。","ben":B419,"sm":"b「闭剥」取「剥」：拔根而剥。"},
{"ch":"跋","p":"bá","xp":"《说文》「蹎跋也」——往前扑、踏行；跋涉、跋尾。","ben":B419,"sm":"b「闭剥」取「剥」：足剥地而行。"},
{"ch":"袚","p":"bá","xp":"《广韵》「蛮夷蔽膝」——旱獭毛皮面小宜作蔽膝。","ben":B419,"sm":"b「闭剥」取「剥」：皮剥而蔽。"},
{"ch":"魃","p":"bá","xp":"《说文》「旱鬼也」——旱獭掘根致草原沙化，故引申旱灾。","ben":B419,"sm":"b「闭剥」取「剥」：地剥而旱。"},
{"ch":"髮","p":"fà","xp":"《说文》「根也」——头发；西周金文所从与甲骨文「亥」相似（直立旱獭侧面形）。","ben":B419,"sm":"f「附分」取「分」：发分而覆。"},
{"ch":"胈","p":"bá","xp":"《说文》「股肉也」——腿上的肉。","ben":B419,"sm":"b「闭剥」取「剥」：肉附骨如剥。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":e["ben"],"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取旱獭「直立／皮毛／掘根」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":("源自《系統漢語》第418部「亥部」（卷七十 亥）；字卡五步规程。" if e["ben"]==B418 else "源自《系統漢語》第419部「犮部」（卷七十 亥）；字卡五步规程。"),
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡418d419a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡418d419a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡418d419a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))