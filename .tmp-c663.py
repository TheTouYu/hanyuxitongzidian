import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第527部「向部」·尚系（二级字根）】尚＝从八向聲：分開并開窗，為「敞」之初文；字族三面：敞開敞亮／推舉罩覆／來回反復。"
N="字形：古文字字形库未收。"
D=[("敞","chǎng",FY,"从攴尚聲：平治高土可以遠望（《說文》）；開也、露也（《集韻》）。","ch「刺持」取「持」：開敞而持。"),
("氅","chǎng",FY,"从毛敞聲：析鳥羽為旗之屬（《說文》），大氅——以鳥羽製衣可如旗展開。","ch取刺持：羽展而持。"),
("鱨","cháng",FY,"从魚嘗聲：揚也（《說文》）；一名黃頰魚。","ch取刺持：魚揚而持。"),
("瓽","dàng",FY,"从瓦尚聲：大盆也（《說文》），可以盛水，或作甔。","d「囤动」取「囤」：盆盛而囤。"),
("廠","chǎng",FY,"从广敞聲：棚舍、敞屋（《集韻》）。","ch取刺持：敞屋而持。"),
("僘","chǎng",FY,"从人敞聲：高也、大也（《集韻》），本作敞。","ch取刺持：人高而持。"),
("躺","tǎng",FY,"从身尚聲：身臥也（《集韻》）。","t「涂突」取「涂」：身鋪展。"),
("𨜂","cháng",FY,"从邑尚聲：地名；或以為「黨」字之變（《字彙》）。","ch取刺持：邑名而持。"),
("棠","táng",FY,"从木尚聲：牡曰棠、牝曰杜（《說文》），棠梨。","t取涂突：木鋪而突。"),
("嘗","cháng",FY,"从旨尚聲：口味之也（《說文》）；以口試味→試探→曾經。","ch取刺持：口嘗而持。"),
("賞","shǎng",FY,"从貝尚聲：賜有功也（《說文》）。","sh「失收」取「收」：賜而收。"),
("常","cháng",FY,"从巾尚聲：下裙也（《說文》）；衣裳之常→恆久。","ch取刺持：裙垂而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"尚系諧聲字分三面：敞開敞亮（敞／氅／廠／僘）／推舉罩覆（賞／棠）／嘗試反復（嘗／常／躺／瓽）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))