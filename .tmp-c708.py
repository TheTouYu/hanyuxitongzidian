import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FJ="【第542部「九部」】九＝象臂屈曲（肘之初文），借为数词九；轉義究盡、極數。"
FY="【第543部「玉部」】玉＝象玉串形（三玉相連、一貫其間），《說文》「石之美……象三玉之連，ㄧ其貫也」；轉義玉製品、瑞玉、佩玉、美稱；音源借音（古玉、九通用）。"
N="字形：古文字字形库未收。"
D=[("氿","guǐ",FJ,"从水九聲：水厓枯土也（《說文》）；又氿泉（側出泉）。","g「隔估」取「隔」：崖隔而止。"),
("尻","kāo",FJ,"从尸九聲：脽也（《說文》），臀部、尾骨。","k「口控」取「控」：骨控而屈。"),
("訄","qiú",FJ,"从言九聲：迫也（《說文》），逼迫。","q「亲缺」取「亲」：言迫而缺。"),
("馗","kuí",FJ,"从首九聲：九達之道（《說文》「九達道也」），四通之路。","k取口控：道控而通。"),
("艽","jiāo",FJ,"从艸九聲：艽，秦艽（藥草）；又獸蓐。","j「聚决」取「聚」：草聚而决。"),
("鼽","qiú",FJ,"从鼻九聲：病寒鼻窒也（《說文》），鼻塞。","q取亲缺：鼻塞而缺。"),
("玉","yù",FY,"象玉串形；引申玉制品、瑞玉、美稱、磨煉。","y「柔锐」取「锐」：玉润而锐。"),
("玊","sù",FY,"从王有点：朽玉也（《說文》），玉工。","s「失收」取「收」：玉朽而收。"),
("璞","pú",FY,"从玉菐聲：玉未治者（《說文》），璞玉需琢。","p「拼辟」取「拼」：璞拼而琢。"),
("璧","bì",FY,"从玉辟聲：瑞玉，圓形中有孔（《說文》「瑞玉圜也」）。","b「闭剥」取「闭」：璧圆而闭。"),
("瑾","jǐn",FY,"从玉堇聲：瑾瑜，美玉（《說文》「瑾瑜，美玉也」）。","j取聚决：美玉而聚。"),
("瑜","yú",FY,"从玉俞聲：瑾瑜，美玉；又玉之光澤。","y取柔锐：玉光而锐。")]
for ch,p,F0,xp,sm in D:
    bn=542 if ch in "氿尻訄馗艽鼽" else 543
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"九系同取「屈曲究盡」一面（氿崖、尻臀、馗九達）；玉系同取「石之美、需琢」一面（璞未治、璧瑞玉、瑾瑜美玉）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"九" if bn==542 else "玉"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第542－543部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡543a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡543a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡543a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))