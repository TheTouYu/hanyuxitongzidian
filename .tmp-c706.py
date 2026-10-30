import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FQ="【第541部「求部」】求＝象獸皮衣（裘之初文），引申求索。"
FJ="【第542部「九部」】九＝甲骨文象人臂屈曲之形（肘之初文），借為數詞九；轉義究盡、極數（《說文》「陽之變也，象其屈曲究盡之形」）。"
N="字形：古文字字形库未收。"
D=[("梂","qiú",FQ,"从木求聲：櫟實（橡子），《說文》「櫟實也」。","q「亲缺」取「亲」：木实而缺。"),
("觩","qiú",FQ,"从角求聲：角曲貌（《說文》「角貌」）。","q取亲缺：角曲而缺。"),
("絿","qiú",FQ,"从糸求聲：急也（《說文》「急也」）。","q取亲缺：絲急而缺。"),
("銶","qiú",FQ,"从金求聲：鑿屬（《說文》），鑿一類工具。","q取亲缺：刃親而缺。"),
("賕","qiú",FQ,"从貝求聲：以財物枉法相謝（《說文》），行賄。","q取亲缺：財求而缺。"),
("莍","qiú",FQ,"从艸求聲：椒樧實（《說文》），茱萸子聚生。","q取亲缺：草實而聚。"),
("九","jiǔ",FJ,"象臂屈曲（肘之初文），借为数词九；转义究尽极数。","j「聚决」取「聚」：屈聚而决。"),
("究","jiū",FJ,"从穴九聲：窮也（《說文》），推極到底。","j取聚决：穴穷而决。"),
("軌","guǐ",FJ,"从車九聲：車轍（《說文》「車轍也」），引申法度。","g「隔估」取「隔」：辙隔而循。"),
("鳩","jiū",FJ,"从鳥九聲：鳩，鳥名（《說文》「鶻鵃也」）；又聚（鳩合）。","j取聚决：鳥聚而决。"),
("仇","qiú",FJ,"从人九聲：讎也（《說文》），匹配（公侯好仇）、仇敵。","q取亲缺：匹配而缺。"),
("宄","guǐ",FJ,"从宀九聲：姦也（《說文》「姦也，外為盜，內為宄」）。","g取隔估：内奸而隔。")]
for ch,p,F0,xp,sm in D:
    bn=541 if ch not in "九究軌鳩仇宄" else 542
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"求系同取「皮衣、干求」一面（梂橡實、觩角曲、賕行賄）；九系同取「屈曲究盡」一面（究窮、軌轍、仇匹、宄姦）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"求" if bn==541 else "九"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljiu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第541－542部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡542a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡542a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡542a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))