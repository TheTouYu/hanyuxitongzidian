import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第556部「辛部」】辛（䇂）＝象小刻刀形（上柄下刃、中有護手），用於刻字、紋身（郭沫若說，婦好墓出土玉刻刀可證）；紋身刺痛故引申辛辣、辛苦，紋身為商人身份象徵故引申新生。"
N="字形：古文字字形库未收。"
D=[("辛","xīn",FH,"象小刻刀形：上柄、下刃、中為護手（郭沫若《甲骨文字研究》），用於刻字紋身；引申辛辣、辛苦、新生。","x「续消」取「续」：刺痛而续。"),
("言","yán",FH,"从口从辛：以辛刀刻口所出（直言曰言，《說文》「直言曰言，論難曰語」）。","y「续消」取「消」：口出而消。"),
("唁","yàn",FH,"从口言聲：弔生也（《說文》「弔生也」），弔唁。","y取续消：弔而消。"),
("誾","yín",FH,"从言門聲：和說而諍也（《說文》「和說而諍也」），誾誾。","y取续消：言和而续。"),
("信","xìn",FH,"从人从言：誠也（《說文》「誠也」），人言為信。","x取续消：言實而续。"),
("詈","lì",FH,"从网从言：罵也（《說文》「罵也」），网罪人而詈。","l「拢离」取「拢」：网拢而離。"),
("這","zhè",FH,"从辵言聲：迎也（《說文》「迎也」），借為指示詞。","zh「凿总」取「凿」：迎而凿。"),
("親","qīn",FH,"从見𣓀聲：至也（《說文》「至也」），親近、親屬。","q「亲缺」取「亲」：見而亲。"),
("櫬","chèn",FH,"从木親聲：棺也（《說文》「棺也」），近身之棺。","ch「刺持」取「持」：木持而棺。"),
("新","xīn",FH,"从斤从木：取木也（《說文》「取木也」），析木為新，引申新旧。","x取续消：木析而续。"),
("薪","xīn",FH,"从艸新聲：蕘也（《說文》「蕘也」），柴薪。","x取续消：柴续而消。"),
("毅","yì",FH,"从殳豙聲：有決也（《說文》「有決也」），剛毅。","y取续消：決而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"辛系同取「刻刀刺痛、直言、新生」一面：言直言、唁弔、誾諍、信誠、詈罵、這迎、親至、櫬棺、新析木、薪柴、毅決；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":556,"name":"辛"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxin-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第556部「辛部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡556a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡556a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡556a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))