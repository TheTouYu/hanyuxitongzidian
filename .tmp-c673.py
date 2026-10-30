import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FS="【第530部「爽部」】爽＝象人兩手提大器：孔武豪爽／器空粗疏→明亮→刮擦傷損；音源義同「相」。字族：①空明 ②刮擦。"
FG="【第531部「桑部」】桑（桒枽）＝甲骨文象枝條繁茂的桑樹（《玉篇》「蠶所食葉」）；轉義桑樹堅硬柔韌、老幹多圓鼓結節→圓而堅韌之物（車輞）；以葉飼蠶→蠶之狀（左右搖擺、用力推）。辯證：小篆枝葉訛作「叒」，《說文》析形不確。音源借音：桑葉被摘有空爽義，義音同「爽」（《書》「用爽厥師」一本作「喪」）。字族：①桑之結節（圓鼓硬物）②桑葉蠶事。"
N="字形：古文字字形库未收。"
D=[("樉","shuǎng",FS,"《集韻》「木名，一曰木茂皃」。","sh「失收」取「收」：木盛而收。"),
("鏯","shuǎng",FS,"同「鐵」；疑即鋾銼之類，與磢、㼽功用同，用金屬製成。","sh取失收：金磨而收。"),
("𦄍","shuǎng",FS,"《集韻》「緉𦄍，絞也」，一曰履底繩。","sh取失收：繩絞而收。"),
("䫪","shuǎng",FS,"《玉篇》「醜也、滿也」。","sh取失收：貌醜而收。"),
("傸","chuǎng",FS,"《集韻》「惡也」。","ch「刺持」取「持」：人惡而持。"),
("𠞮","chuǎng",FS,"《集韻》「皮傷也」，擦傷。","ch取刺持：皮傷而持。"),
("桑","sāng",FG,"甲骨文象枝葉繁茂的桑樹；引申圓韌之物、蠶事之狀。","s「失收」取「收」：葉摘而收。"),
("顙","sǎng",FG,"从頁桑聲：頟也（《說文》），額頭——如桑之鼓出。","s取失收：額鼓而收。"),
("嗓","sǎng",FG,"从口桑聲：喉也（《集韻》），喉嚨。","s取失收：喉鳴而收。"),
("磉","sǎng",FG,"从石桑聲：柱下石（《集韻》），柱礎。","s取失收：石鼓而收。"),
("䡦","sǎng",FG,"从車桑聲：車輞也（《集韻》），車輪外周。","s取失收：輪圓而收。"),
("搡","sǎng",FG,"从手桑聲：搷也（《集韻》），用力推——如蠶吐絲時左右搖擺。","s取失收：推搡而收。")]
for ch,p,F0,xp,sm in D:
    bn=530 if ch in "樉鏯𦄍䫪傸𠞮" else 531
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"爽系餘字（刮擦、醜惡、木茂）；桑系諧聲字分兩面：桑之結節（顙／嗓／磉／䡦）與桑葉蠶事（搡）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"爽" if bn==530 else "桑"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lsang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第530－531部（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡531a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡531a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡531a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))