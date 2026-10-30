import json,subprocess,os,glob,re
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F0="【第594部「彡部」】參（二級字根）＝商代金文象簪滿珠玉髮飾的跪跽人形，本義插簪（此義分化為「篸/簪」）；轉義 下拜見上（參謁）、加入查驗、參差不齊、眾多；借指數字三、參宿三星。"
D=[("參","shēn",F0,"从簪满珠玉之跪人：插簪；转义 参谒、参预、参差、众多；借为三、参宿（三星并列）。音源本「三」声，义音同「兓」（憯/惨）。","sh「失收」取「收」：簪插而收。"),
("㺑","shān","【第594部「彡部」】參系；㺑＝从犬參聲，犬容頭進也（《說文》），狗从窄处鑽过。","从犬參聲：犬容頭進也（《說文》「犬容頭進也」），一曰賊疾。","sh取失收：犬鑽而收。"),
("穇","shān","【第594部「彡部」】參系；穇＝禾穗不實（《集韻》「稴穇，禾穗不實」）。","从禾參聲：禾穗不實，禾短曰𥤇；穇子生水田下濕地。","sh取失收：穗虛而收。"),
("墋","chěn","【第594部「彡部」】參系；墋＝从土參聲，土也（《說文》），沙土。","从土參聲：土也（《說文》「土也」），沙土難行。","ch「刺持」取「持」：土雜而持。"),
("磣","chěn","【第594部「彡部」】參系；磣＝从石參聲，食有沙（《集韻》），牙磣。","从石參聲：食有沙，牙磣；又 醜貌。","ch取刺持：沙礫而持。"),
("醦","chěn","【第594部「彡部」】參系；醦＝从酉參聲，酢也（《集韻》），酸味。","从酉參聲：酢也（《集韻》），酸味；醦醦，酸甚。","ch取刺持：味酸而持。"),
("鏒","sǎn","【第594部「彡部」】參系；鏒＝从金參聲，金鏒（《集韻》），金器細碎之聲。","从金參聲：金鏒，金器細碎；一曰 鐵之軟者。","s取失收：金碎而收。"),
("摻","shǎn","【第594部「彡部」】參系；摻＝从手參聲，執也（《說文》「執也」）。","从手參聲：執也（《說文》「執也」）；摻摻，纖美之貌（《詩》「摻摻女手」）。","sh取失收：手執而收。"),
("傪","cān","【第594部「彡部」】參系；傪＝从人參聲，好貌（《集韻》）。","从人參聲：好貌（《集韻》「好皃」），人美好。","c取刺持：人好而持。"),
("犙","sān","【第594部「彡部」】參系；犙＝从牛參聲，牛名（《集韻》）。","从牛參聲：牛名（《集韻》），三歲牛。","s取失收：牛聚而收。"),
("㜗","cān","【第594部「彡部」】參系；㜗＝从女參聲，婪也（《集韻》），貪婪。","从女參聲：婪也（《集韻》），貪而多欲。","c取刺持：貪而持。"),
("瘮","shèn","【第594部「彡部」】參系；瘮＝从疒參聲，寒病（《集韻》「瘮，寒病」）。","从疒參聲：寒病（《集韻》），寒慄。","sh取失收：寒聚而收。")]
rows=[]
for it in D:
    ch,p,F0_,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0_,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"參系同取「插入、混雜、細碎」一面：參簪插、㺑犬鑽、穇穗虛、墋沙土、磣牙磣、醦酸、鏒金碎、摻手執、傪人好、犙三歲牛、㜗貪、瘮寒；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshan5-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第594部「彡部」·參系（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 594彡部參系12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡594e.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594e{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡594e.json"); print(git("commit","-m","knowledge: 594彡部參系12条")[-60:])