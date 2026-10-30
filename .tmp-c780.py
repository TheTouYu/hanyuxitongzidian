import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第568部「棘部」】棘＝从朿並疊（朿象木有刺），象橫向成叢的刺木（《說文》「小棗叢生者」）；引申刺人、棘手、急迫、瘦、陳列；音義同「脊」（刺密如脊）。"
N="字形：古文字字形库未收。"
D=[("棘","jí",F,"从二朿並疊：叢生多刺之木（《正字通》「朿木叢生凡有刺者皆曰棘」），或專指酸棗；引申刺、急、瘦、陳列。","j「聚决」取「聚」：刺聚而决。"),
("襋","jí",F,"从衣棘聲：衣領也（《說文》「衣領也」）；領為衣之亟者，故从棘。","j取聚决：領合而决。"),
("僰","bó",F,"从人棘聲：犍為蠻夷（《說文》），西南少數民族；《玉篇》「屛之遠方曰僰，僰之言偪也」。","b「闭剥」取「闭」：遠屛而闭。"),
("䪂","gé",F,"从革棘聲：靶也、勒也（《玉篇》），轡首、馬勒。","g「隔估」取「隔」：勒馬而隔。"),
("𠢠","lì",F,"从力棘聲：趙魏間呼棘曰𠢠（《方言》），又力也。","l「拢离」取「离」：力散而离。"),
("㻷","jí",F,"从玉棘聲：垂㻷，地名（《集韻》），本作棘，以其出美玉故从玉。","j取聚决：玉美而决。"),
("蕀","jí",F,"从艸棘聲：顚蕀（《爾雅》），細葉有刺蔓生，即天門冬；又遠志。","j取聚决：刺蔓而决。"),
("棗","zǎo",F,"从二朿相承：重朿為棗（《埤雅》），多刺之高樹，棗樹果實黑紅。","z「凿总」取「总」：實聚而总。"),
("𤒗","zhì",F,"从肉从炙：炙之古作（《正字通》），穿肉炙烤之鐵釺，鐵釺如長刺。","zh取凿总：炙聚而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"棘部二支：①以棘為藩籬（襋領、僰遠屛、䪂勒）②棘狀多刺（𠢠、㻷、蕀、棗、𤒗炙釺）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":568,"name":"棘"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lji-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第568部「棘部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡568a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡568a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡568a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))