import json,subprocess,os,glob
BF=("【402 夨部】部首夨（zè）：象人侧着头的样子（《说文》「倾头也，从大，象形」）。音源：借音字，有偏侧之意而义音同「则」；但衍生字多与舞有关，实为音源字，源自跳舞歌呼声。字族衍义：多指侧头，表示倾斜。")
BS=("【403 史部】部首史（㕜shǐ）：甲骨文从又持「中」——「中」指中心、中正，从「又」指握持，也可指司事；象意调解矛盾纠纷、物资交易时的中间人（民间称公证人，朝廷称史官），这类人需执笔书写调解书与契约。"
    "轉義：由史官引申指史书（《广韵》「史籍」）。辯證：①「事」本从又持干，「干」指树杈，为狩猎作战武器，故本义当指狩猎或作战（zì 插入、刺入；引申树立建立，《释名》「事，倳也，倳，立也」）；②「中」「干」甲骨文形近，战国古文或混同，故《说文》「事，职也，从史之省声」析形不确；③「史、事」混同致「吏」字源难辨，据战国古文当是「事」的分化——持武器者维持秩序为吏，持干狩猎代指生产劳动为事；④「夬」与「史」形近，本从夬（扳指，引申分决、空缺）者或讹从史。本应分史部、事部二部，因字混淆而合置一部。"
    "音源：借音字，古事、采可通（《书》「载采采」《史记》作「事事」）；古事、士通用（《礼记》「大夫七十而致事」他书作「致仕」）。字族衍义：①指「干」的刺入（应从吏或事）②指「中」的公正明了（应从史）③形近「夬」之讹，指分决。")
N1="字形：古文字字形库未收；原稿史部有「▲民国时期的契约文书」可参。"
N2="字形：古文字字形库未收。"
D=[
("䜁","xǐ",BF,N2,"《集韵》「謑，《说文》耻也，或从奊」，一曰「謑诟，小人怒」；「䜁訽，怒也」——羞辱、怒诟。","夨族之言：以「言」定其用，斜行而诟。","x「续消」取「消」：怨消而诟。"),
("鉂","shǐ",BS,N1,"《玉篇》「镮也」；《篇海》「刺也」——环与刺。","史族①之器：以「金」定其质，干之刺入。","sh「失收」取「收」：刺入而收。"),
("剚","zì",BS,N1,"《集韵》「插刀也，或从金」；《正韵》「置也，东方人以物插地皆曰剚，又通作倳」——插刀入地。","史族①之直：以「刀」定其势，插入而立。","z「凿总」取「凿」：凿地而插。"),
("䭄","shì",BS,N1,"《集韵》「仕吏切，音事。嗜食也」——嗜食。","史族①之食：以「食」定其欲，好之如刺入。","sh「失收」取「收」：食收入腹。"),
("𩰢","shǐ",BS,N1,"从鬯吏声，《说文》「列也」疏吏切——酒气酷烈；《广韵》「香之美者」。","史族①之香：以「鬯」定其气，烈而列。","sh「失收」取「失」：香失而散。"),
("𩢲","shì",BS,N1,"《新附》「疾也，从马吏声」——驾驭马；《龙龛》「俗驶字，音使，水流速也」。","史族①之疾：以「马」定其动，疾驰如刺。","sh「失收」取「失」：马失而奔。"),
("𧳅","shì",BS,N1,"《广雅》「𧳅，貁也」；《集韵》「江东呼貉为𧳅」——犬科狸属，体小腿短，穴居群处，昼伏夜出，善爬树，冬季休眠。","史族①之兽：以「豸」定其类，穴居刺入土中。","sh「失收」取「收」：伏而收。"),
("使","shǐ",BS,N1,"从人吏声，《说文》「伶也」疏士切——命令、派遣；《六书统》「从人从事，令人治事也」，《尔雅》「从也」。","史族②之用：以「人」定其人，受命而行事。","sh「失收」取「收」：受命而收其事。"),
("諫","jiàn",BS,N1,"《集韵》「忘也」；《六书统》「古文谏字」——谏诤。","史族②之言：以「言」定其用，正言以明。","j「聚决」取「决」：谏而决之。"),
("𣆘","shǐ",BS,N1,"《玉篇》「色滓切。明」——明亮。","史族②之日：以「日」定其光，中正而明。","sh「失收」取「失」：明失而晦。"),
("𣳪","shì",BS,N1,"《集韵》「㳏，水名，在河南，或从吏」——水名。","史族①之水：以「水」定其名。","sh「失收」取「收」：水收于道。"),
("夬","guài",BS,N1,"《说文》「分决也」——钩弦用的扳指，引申分决、空缺；与「史」形近，故从夬之字多讹从史。","史族③之本：记其本形本义，以见讹变之源。","g「隔估」取「隔」：决而隔断。"),
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
ST={"䜁":"《集韵》「謑，《说文》耻也，或从奊」；又「䜁訽，怒也」——羞辱、怒诟。","鉂":"《玉篇》「镮也」；《篇海》「刺也」。","剚":"《集韵》「插刀也」；《正韵》「置也，东方人以物插地皆曰剚，又通作倳」。","䭄":"《集韵》「嗜食也」。","𩰢":"《说文》「列也，从鬯吏声」——酒气酷烈；《广韵》「香之美者」。","𩢲":"《新附》「疾也，从马吏声」——驾驭马；俗驶字，水流速也。","𧳅":"《广雅》「𧳅，貁也」；江东呼貉为𧳅——狸属，体小腿短，穴居群处。","使":"《说文》「伶也，从人吏声」——命令、派遣；《六书统》「令人治事也」。","諫":"《集韵》「忘也」；《六书统》「古文谏字」。","𣆘":"《玉篇》「色滓切。明」。","𣳪":"《集韵》「㳏，水名，在河南，或从吏」。","夬":"《说文》「分决也」——钩弦之扳指，引申分决、空缺。"}
def B(ch): return "源自《系統漢語》第402部「夨部」（卷六十六 采）；字卡五步规程。" if ch=="䜁" else "源自《系統漢語》第403部「史部」（卷六十六 采）；字卡五步规程。"
cl=[{"id":f"bsh-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡402夨部清完+403史部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡403史部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡403史部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))