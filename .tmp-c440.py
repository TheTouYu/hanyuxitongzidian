import json,subprocess,os,glob
BP=("【407 足部·頻（二级）】頻（瀕频𩔤𩓯𩕘濵pín、bīn）：頻实为瀕的省形（正作𩕘），从川（或水）从步从見——「川」指江河，「步」为止的二叠表示反复光顾，象意水流反复冲刷岸边，示岸边；「見」指人临水照影。"
    "轉義：反复冲击岸边→屡次、连续、急迫（《广韵》「數也」，《字彙》「連也」）；并列、接近、邻近（《广韵》「比也」）；四季水位不同使岸边留下如水线波纹→皱眉、着急（《正字通》引《广韵》「睂蹙也」）。"
    "辯證：涉亦从水从步，但涉之两止分处水两侧，瀕则止在水旁；《说文》「从頁从涉」析形不妥。音源：音源字，源自水拍岸声；因反复光顾而义音同「賓」（《禹貢》「海濱廣斥」，《漢志》引作瀕）。字族衍义：①岸边及相关物 ②岸边之状→皱眉或类似纹路 ③频数→众多、匹偶。")
N="字形：古文字字形库未收。"
D=[
("頻","pín",BP,N,"从川从步从見，象水反复冲岸；引申屡次、连续、急迫、邻近、皱眉。","部头本字：川定其境，步定其反复。","p「拼辟」取「辟」：水辟岸而刷。"),
("𨽗","bīn",BP,N,"《集韵》「濵，水厓也，或从頻」；pín 同「嚬」，皱眉——水边。","岸边族①之阜：以「阜」定其处，水崖之岸。","b「闭剥」取「闭」：水闭于岸。"),
("蘋","pín",BP,N,"《玉篇》「大萍也」——四叶菜、田字草，叶柄顶端集生四片小叶，取其长于水滨之意；píng 苹果。","岸边族①之艸：以「艸」定其类，生在水滨。","p「拼辟」取「辟」：叶辟四出。"),
("𦇖","pín",BP,N,"《玉篇》「擣衣」——捣衣，取在水边进行之意。","岸边族①之糸：以「糸」定其物，水边捣练。","p「拼辟」取「辟」：杵辟而捣。"),
("㰋","pín",BP,N,"《说文》「木也，从木𩔤聲」；即槟榔树，树表呈环状纹路；又㰋婆果（频婆子，红色似皂）。","岸边纹族②之木：以「木」定其类，树皮环纹如水线。","p「拼辟」取「辟」：纹辟如波。"),
("顰","pín",BP,N,"《说文》「涉水顰蹙，从頻卑聲」；《玉篇》「顰蹙，憂愁不樂之狀」——皱眉。","岸边纹族②之页：以「页」定其处，眉间水线成皱。","p「拼辟」取「辟」：眉辟而蹙。"),
("嚬","pín",BP,N,"《玉篇》「笑皃」；《正字通》「眉蹙也」——笑貌、皱眉。","岸边纹族②之口：以「口」定其动，笑而眉蹙。","p「拼辟」取「辟」：口辟而笑。"),
("𧭹","pín",BP,N,"《说文》「匹也，从言頻聲」；《玉篇》「多言」——匹偶、多言。","频数族③之言：以「言」定其声，言多而频。","p「拼辟」取「辟」：言辟而频。"),
("𧮝","pín",BP,N,"《说文长笺》「匹也」——匹偶。","频数族③之言之续：以「言」定其义，两相为匹。","p「拼辟」取「辟」：两辟相配。"),
("𧔪","pín",BP,N,"《类篇》「蟲名，負盤也」——蟑螂。","频数族③之虫：以「虫」定其类，繁殖频多。","p「拼辟」取「辟」：虫辟而多。"),
("𠐺","pín",BP,N,"《漢典》「𠐺伽，音譯字」，梵语「加羅𠐺伽」略译，鸟名，义为妙音鸟。","频数族③之人：音译专用，以「人」定其形。","p「拼辟」取「辟」：借声无义。"),
("𨏞","pín",BP,N,"《正字通》「顰字之訛」；《集韵》「車也」——车。","讹混族③之车：以「车」定其物，形近而讹。","p「拼辟」取「辟」：车辟而行。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,Nx,a,b,c in D:
    json.dump(card(ch,p,Bx,Nx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"頻":"《广韵》「數也」；《字彙》「連也」——从川从步，水反复冲岸，引申屡次、邻近、皱眉。","𨽗":"《集韵》「濵，水厓也，或从頻」——水边。","蘋":"《玉篇》「大萍也」——四叶菜、田字草，生水滨。","𦇖":"《玉篇》「擣衣」——水边捣衣。","㰋":"《说文》「木也，从木𩔤聲」——槟榔树，树表环纹。","顰":"《说文》「涉水顰蹙，从頻卑聲」——皱眉。","嚬":"《玉篇》「笑皃」；《正字通》「眉蹙也」。","𧭹":"《说文》「匹也，从言頻聲」。","𧮝":"《说文长笺》「匹也」。","𧔪":"《类篇》「蟲名，負盤也」——蟑螂。","𠐺":"音译字，梵语「加羅𠐺伽」略译，妙音鸟。","𨏞":"《正字通》「顰字之訛」；《集韵》「車也」。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根頻部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdl-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407頻部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407頻部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407頻部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))