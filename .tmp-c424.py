import json,subprocess,os,glob
BL=("【401 则部】部首则（zé）：从鼎从刀，「鼎」指铸鼎的泥模（刀刻不了鼎），制模刻铭、敷泥脱范，故模型即范本。轉義：法则（《尔雅》「法也」「常也」）；填塞遮盖（𡍫「遏遮也」）、逼仄；旁边（側「旁也」，脱范后不用模）。辯證：「鼎」「貝」形近，战国古文讹从贝，小篆从之，故《说文》「从刀从贝」析形不确。音源：借音字，因有侧义而义音同「才」。字族衍义：①侧边 ②填塞遮拦测度 ③形近「㔍、斯」之讹。")
BZ="【401 则部·贼】「贼（贼戝𧵪𧶱）」从戈则声：「戈」指武器，「则」指偏斜，象意不正当使用武力，表示违法、犯罪（《玉篇》「盗也、伤害人也」，《说文》「败也」昨则切）。字族衍义：①指伤害、残害 ②形近「贱」之讹。"
BF=("【402 夨部】部首夨（zè）：象人侧着头的样子（《说文》「倾头也，从大，象形」阻力切）。音源：借音字，有偏侧之意而义音同「则」；但因其衍生字主要跟舞有关，实际上成了音源字，源自跳舞时的歌呼声。字族衍义：多指侧头，表示倾斜。")
N1="字形：古文字字形库未收；原稿则部有「▲制作鼎的模型」「▲方鼎铸范与装配示意图」。"
N2="字形：古文字字形库未收。"
D=[
("賊","zéi",BZ,N1,"从戈则声，《玉篇》「盗也、伤害人也」，《说文》「败也」昨则切——以不正之武伤人。","贼族之直：以「戈」定其器，偏斜而用武。","z「凿总」取「凿」：戈凿而伤人。"),
("鱡","zéi",BZ,N1,"《集韵》「《说文》乌鰂，鱼名，或从贼、从即」——墨鱼、乌贼鱼。","贼族①之鱼：以「鱼」定其类，喷墨自蔽而害渔者。","z「凿总」取「凿」：墨凿而蔽。"),
("蠈","zéi",BZ,N1,"《集韵》「蠈，蝗食禾节者，或从则」——专吃禾节的蝗虫。","贼族①之虫：以「虫」定其类，节节而害禾。","z「凿总」取「凿」：啮凿禾节。"),
("𨆎","zéi",BZ,N1,"《集韵》「践害之也」——践踏而害。","贼族①之足：以「足」定其动，践而害之。","z「凿总」取「凿」：足凿于地。"),
("𦽒","zéi",BZ,N1,"《玉篇》「木𦽒草」；《本草纲目》「此草有节而糙涩，治木骨者用之磋擦则光净，犹云木之贼也，故名木贼草」。","贼族①之草：以「艸」定其类，磋木之草名为「木之贼」。","z「凿总」取「凿」：糙叶凿木。"),
("𣿐","zé",BZ,N1,"《玉篇》「测也」；jiàn《正字通》「溅字之讹」。","贼族②之讹：形近而误，记作讹变借形。","z「凿总」取「凿」：水凿而溅。"),
("𠷌","jī",BL,N1,"《正字通》「同喞」；zé《字彙补》「子得切，音则」——见内典。","主组③之声：以「口」定其用，音近而借。","j「聚决」取「聚」：声聚于口。"),
("䶡","shí",BL,N1,"《篇海》「士乙切，音实。咬声」；《正字通》「俗齰字，因声近而讹」——咬物之声。","主组③之齿：以「齿」定其动，啮而声。","sh「失收」取「收」：齿收而啮。"),
("𠗧","sī",BL,N1,"《玉篇》「古文凘字」；《正字通》「凘字之讹」——解冻后流动的冰块。","主组③之冰：以「冫」定其物，形近而讹。","s「失收」取「失」：冰失而流。"),
("昃","zè",BF,N2,"从日仄声，《说文》「日在西方时，侧也」阻力切——太阳偏西。","夨族之直：以「日」定其时，日侧而昃。","z「凿总」取「凿」：日凿西山。"),
("奊","xié",BF,N2,"从夨圭声，《说文》「头衺骫奊态也」——头不正貌；又指胸心狭隘、性情乖戾；蜀语「胸次不坦彝」；《正字通》引顾起元《客座赘语》谓其「形如篱落」。","夨族之最：以「圭」定其形，圭头倾侧。","x「续消」取「消」：斜而消。"),
("捑","zè",BF,N2,"《集韵》「攴也」——小击。","夨族之击：以「手」定其动，侧手而击。","z「凿总」取「凿」：侧击如凿。"),
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
ST={"賊":"《玉篇》「盗也、伤害人也」；《说文》「败也，从戈则声」——不正当使用武力，违法犯罪。","鱡":"《集韵》「《说文》乌鰂，鱼名，或从贼、从即」——墨鱼、乌贼鱼。","蠈":"《集韵》「蠈，蝗食禾节者，或从则」。","𨆎":"《集韵》「践害之也」。","𦽒":"《玉篇》「木𦽒草」；《本草纲目》「此草有节而糙涩，治木骨者用之磋擦则光净，犹云木之贼也」——木贼草。","𣿐":"《玉篇》「测也」；《正字通》「溅字之讹」。","𠷌":"《正字通》「同喞」；《字彙补》「音则」。","䶡":"《篇海》「咬声」；《正字通》「俗齰字，因声近而讹」。","𠗧":"《玉篇》「古文凘字」——解冻后流动的冰块。","昃":"《说文》「日在西方时，侧也，从日仄声」——太阳偏西。","奊":"《说文》「头衺骫奊态也」——头不正貌；又指胸心狭隘、性情乖戾。","捑":"《集韵》「攴也」——小击。"}
def B(ch): return "源自《系統漢語》第401部「则部」（卷六十六 采）；字卡五步规程。" if ch not in ("昃","奊","捑") else "源自《系統漢語》第402部「夨部」（卷六十六 采）；字卡五步规程。"
cl=[{"id":f"bzf-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡401贼族余+402夨部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡401则部余.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡401则部余.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))