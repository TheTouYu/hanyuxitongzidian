import json,subprocess,os,glob
B9=("部首采（釆𤓳cǎi）：甲骨文从爪从木，象意采摘树上的果实或叶子（故「木」或作「果」与「枼」形）；《说文》「捋取也。从木从爪」仓宰切。"
    "轉義：由采摘引申指选择、获取（《广韵》「事也，又取也」）；采摘为采桑柞以饲蚕、或作染料以染布，故引申指色彩（《玉篇》「色也」），再引申布帛、文采、光彩、脸色、好运；采摘为食用，故引申指公卿大夫的封地（《集韵》「臣食邑谓之埰」），或指坟墓——死后的采食地。"
    "音源：音源字，源自采摘声。字族衍义：①采以为食（食物）②采以为染料（色彩）③采摘行为本身。")
N="字形：古文字字形库未收；原稿该部有「▲战国铜器上的采桑纹饰」可参。"
D=[
("菜","cài",B9,"从艸采声，《说文》「艸之可食者」苍代切——蔬菜，后泛指主食以外的食品。","主组①之直：以「艸」定其类，采而食之。","c「刺持」取「刺」：摘菜须掐断其茎。"),
("寀","cǎi",B9,"从宀采声，《新附》「同地为寀」仓宰切；《尔雅》「寀寮，官也」——官员的食邑。","主组①之引申：以「宀」定其居，采食之地为寀。","c「刺持」取「持」：据地而守其入。"),
("埰","cǎi",B9,"《方言》「冢，或谓之采」——死后的食邑地；cài《集韵》「臣食邑谓之埰」。","主组①之转：以「土」定其归，坟亦采食之地。","c「刺持」取「持」：土持其骨。"),
("䐆","cǎi",B9,"《集韵》「大腹也」——腹大如采食充盈。","主组①之状：以「肉」定其形，采食而腹大。","c「刺持」取「持」：腹持所食。"),
("棌","cǎi",B9,"《玉篇》「槲也」；《正字通》「柞木也」——栎树、柞树，坚果可采以为食，叶可饲柞蚕，又用以练丝。","主组①之木：以「木」定其体，采食练丝皆取于此。","c「刺持」取「刺」：柞叶有刺而蚕食之。"),
("彩","cǎi",B9,"从彡采声，《新附》「文章也」仓宰切；《广韵》「光彩」、《集韵》「文色也」——各种颜色。","主组②之直：以「彡」定其文，采草木为染而生色。","c「刺持」取「刺」：染采刺入布缕。"),
("婇","cǎi",B9,"《集韵》「女字」；《玉篇》「婇女也」——宫女。","主组②之转：以「女」定其人，如彩饰之列于宫。","c「刺持」取「持」：侍而不去。"),
("䰂","cài",B9,"《集韵》引《博雅》「髻也」，一曰覆巾；《方言》「络头，或谓之䰂带」——发髻、覆头巾。","主组②之饰：以「髟」定其发，采色饰首如彩。","c「刺持」取「持」：巾持其发。"),
("㥒","cǎi",B9,"从心采声，《说文》「奸也」仓宰切；《玉篇》「恨也、急也」；cāi《集韵》「猜，《说文》恨贼也」——嫉恨，如采摘般直接损害对方。","主组③之直：以「心」定其情，采而夺之则恨生。","c「刺持」取「刺」：猜忌如刺。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"菜":"《说文》「艸之可食者」苍代切——蔬菜，后泛指主食以外的食品。","寀":"《新附》「同地为寀」；《尔雅》「寀寮，官也」——官员的食邑。","埰":"《方言》「冢，或谓之采」——死后的食邑地；《集韵》「臣食邑谓之埰」。","䐆":"《集韵》「大腹也」。","棌":"《玉篇》「槲也」；《正字通》「柞木也」——栎柞之木，实可采食、叶可饲蚕、又用以练丝。","彩":"《新附》「文章也」；《广韵》「光彩」、《集韵》「文色也」——各种颜色。","婇":"《玉篇》「婇女也」——宫女。","䰂":"《集韵》引《博雅》「髻也」，一曰覆巾；《方言》「络头，或谓之䰂带」。","㥒":"《说文》「奸也，从心采声」；《集韵》「猜，《说文》恨贼也」——嫉恨如采摘般夺人。"}
BK="源自《系統漢語》第399部「采部」（卷六十六 采）；字卡五步规程。"
cl=[{"id":f"bca-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":BK,"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡399采部首9字2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡399采部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡399采部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))