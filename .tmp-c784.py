import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第569部「黍部」】利支＝「利」與「黎」同構，象意側重在「勿」（从刀外有小點，表崩口之刀，即犁），犂之初文；从禾表象種植穀物；引申鋒利、靈便、順利、美好。"
N="字形：古文字字形库未收。"
D=[("利","lì",F,"从禾从勿（崩口之刀＝犁）：犂之初文（《玉篇》「耕具也」），引申鋒利、順遂、美好。","l「拢离」取「离」：刃分而离。"),
("犂","lí",F,"从牛利聲：耕也（《說文》「耕也」），墾田器；亦指雜色牛。","l取拢离：牛耕而离。"),
("𨛫","lí",F,"从邑利聲：殷諸侯國（《說文》），西伯戡𨛫。","l取拢离：邑分而离。"),
("䬆","lì",F,"从風利聲：風雨暴疾也（《說文》），暴風驟雨。","l取拢离：風疾而离。"),
("鋓","chān",F,"从金利聲：銳也（《集韻》），剡物使薄。","ch「刺持」取「刺」：刃薄而刺。"),
("鏫","lí",F,"从金利聲：𨪏鏫，鐵撾（《集韻》），前端如蒺藜之垂錘。","l取拢离：錘垂而离。"),
("棃","lí",F,"从木利聲：果名（《說文》），梨樹；枝幹彎曲可作犁轅。","l取拢离：枝曲而离。"),
("剓","lí",F,"从刀利聲：剝也（《集韻》），割裂。","l取拢离：剝裂而离。"),
("蟍","lí",F,"从蟲利聲：螏蟍，蝍蛆、蜈蚣（《廣韻》）。","l取拢离：蟲行而离。"),
("鯬","lí",F,"从魚利聲：魚名（《埤倉》），鰣魚別稱，肥美多刺。","l取拢离：魚游而离。"),
("俐","lì",F,"从人利聲：伶俐（《字彙》「黠慧曰伶俐」），靈活、乾淨。","l取拢离：慧敏而离。"),
("猁","lì",F,"从犬利聲：猞猁（《漢典》），似貓而大、耳尖叢毛、善爬樹。","l取拢离：獸捷而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"利支同取「犁刃分土之銳」一面：利鋒、犂耕、𨛫邑、䬆暴風、鋓薄刃、鏫垂錘、棃木、剓剝、蟍蟲、鯬魚、俐慧、猁捷；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":569,"name":"黍"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第569部「黍部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡569b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡569b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡569b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))