import json,subprocess,os,glob
BX=("【407 足部·徙（二级）】徙（𢓊𡕝𡲴𨑭𨔀𨖤𨗬xǐ）：从行从步——「行」指大道，「步」指徒步，象意大道上人来人往，表示徜徉、徘徊（《广雅》「仿佯，徙倚也」）；或象行人成群结队，表示迁移。"
    "轉義：由迁移引申指躲避、谪戍、流放（《玉篇》「移也、遷也、避也」）。音源：音源字，源自群体行走的脚步声，义音同「師」（《集韵》「籭，竹器也，可以取粗去細」或作簛、簁、篩）。"
    "字族衍义：①迁移→成群移动、众多 ②徜徉→徐行、踩踏。")
N="字形：古文字字形库未收。"
D=[
("徙","xǐ",BX,N,"从行从步，象大道上人来人往（徜徉）或成群迁移；引申躲避、流放。","部头本字：行定其道，步定其行。","x「续消」取「续」：人续而行。"),
("縰","xǐ",BX,N,"《集韵》「纚，《說文》『冠織也，謂以緇帛韜髮』，或作縰」；又縰縰，众多貌。","迁移族①之糸：以「糸」定其物，束发之帛众多。","x「续消」取「续」：丝续而众。"),
("蹝","xǐ",BX,N,"《集韵》「躧，《說文》『舞履也』，或从革、从徙」——舞鞋。","迁移族①之足：以「足」定其物，舞履轻举。","x「续消」取「续」：步续而舞。"),
("漇","xǐ",BX,N,"《集韵》「潤也」；《正字通》「流貌」——滋润、水流貌。","迁移族①之水：以「水」定其状，流而润。","x「续消」取「续」：水续而流。"),
("𢇌","cǐ",BX,N,"《集韵》「𠈈，《說文》『小皃』，引《詩》『𠈈𠈈彼有屋』，或作𢇌、佌」。","迁移族①之人：以「人」定其形，屋小而人多。","c「刺持」取「刺」：人刺而密。"),
("褷","shī",BX,N,"《广韵》「襹，𧞬襹，毛羽衣皃，褷，上同」——毛羽之衣。","迁移族①之衣：以「衣」定其物，毛羽纷披。","sh「失收」取「收」：毛收而披。"),
("𥛨","shī",BX,N,"《龙龛》「襳𥛨，毛羽入也」——毛羽深入之状。","迁移族①之示：以「示」定其祭，毛羽入于礼。","sh「失收」取「收」：羽收而入。"),
("㿅","xuǎn",BX,N,"《集韵》「癬，《說文》『乾瘍也』，或作㿅」；《释名》「癬，徙也，移徙處自廣也」——癣。","迁移族①之疒：以「疒」定其疾，癣会移徙扩散。","x「续消」取「续」：癣续而蔓。"),
("𢊚","xǐ",BX,N,"《玉篇》「移也」——移动。","迁移族①之广：以「广」定其处，屋移而他迁。","x「续消」取「续」：屋续而移。"),
("簁","shāi",BX,N,"《说文》「簁箄，竹器也，从竹徙聲」；《集韵》「可以取粗去細」——筛子。","迁移族①之竹：以「竹」定其物，筛使粗细相徙。","sh「失收」取「收」：筛收细者。"),
("蓰","xǐ",BX,N,"《集韵》「物數也，五倍曰蓰」；又草名，疑本指五倍子。","迁移族①之艸：以「艸」定其类，五倍之草。","x「续消」取「续」：数续而倍。"),
("𣯪","xǐ",BX,N,"《字彙》「毛垂貌」——《集韵》「𢒩，毛垂皃」。","迁移族①之毛：以「毛」定其状，毛垂而拂。","x「续消」取「续」：毛续而垂。"),
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
ST={"徙":"从行从步——大道上人来人往（徜徉）或成群迁移；引申躲避流放。","縰":"《集韵》「纚，《說文》『冠織也』，或作縰」——束发之帛；又众多貌。","蹝":"《集韵》「躧，《說文》『舞履也』」——舞鞋。","漇":"《集韵》「潤也」；《正字通》「流貌」。","𢇌":"《集韵》「𠈈，《說文》『小皃』」。","褷":"《广韵》「襹，毛羽衣皃」。","𥛨":"《龙龛》「襳𥛨，毛羽入也」。","㿅":"《集韵》「癬，《說文》『乾瘍也』」。","𢊚":"《玉篇》「移也」。","簁":"《说文》「簁箄，竹器也，从竹徙聲」——筛子。","蓰":"《集韵》「五倍曰蓰」；艸名，疑五倍子。","𣯪":"《字彙》「毛垂貌」。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根徙部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407徙部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407徙部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407徙部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))