import json,subprocess,os,glob
BC=("【407 足部·楚（二级）】楚（椘檚䠂𣕑𣗂chǔ）：从林从疋（足）——「林」指荆楚丛木，「疋」指腿脚，象意人走入丛木之中，为枝条所阻滞。"
    "轉義：由絆足阻滞→阻碍、滞涩；由丛木之刺→痛楚、酸楚；由荆条之用于笞打→呵斥、痛楚。字族衍义：①指楚的絆足，表示阻碍、滞涩 ②指楚的笞打，表示呵斥、痛楚。")
N="字形：古文字字形库未收。"
D=[
("楚","chǔ",BC,N,"从林从疋，象意人入丛木为枝条所阻；引申阻碍、痛楚、呵斥；又指荆楚之地。","部头本字：林定其境，疋定所困（足）。","ch「刺持」取「刺」：荆刺而阻。"),
("礎","chǔ",BC,N,"《新附》「礩也，从石楚聲」；《廣韻》「柱下石也」——柱脚石。","阻涩族①之石：以「石」定其质，柱下承重之石。","ch「刺持」取「持」：石持柱而不动。"),
("𨆄","zhù",BC,N,"《集韻》「與跙同」；《類篇》「行不正也，一曰馬蹄痛病」。","阻涩族①之足：以「足」定其动，行不正、蹄痛。","zh「凿总」取「凿」：足凿而滞。"),
("濋","chǔ",BC,N,"《爾雅·釋水》「濟為濋」，郭注「大水溢出別為小水之名」。","阻涩族①之水：以「水」定其形，大水溢而分支。","ch「刺持」取「刺」：水刺而分。"),
("璴","chǔ",BC,N,"似玉之石。","阻涩族①之玉：以「玉」定其质，石似玉而滞。","ch「刺持」取「持」：石持而温。"),
("𨼪","chǔ",BC,N,"《玉篇》「阪也」——斜坡。","阻涩族①之阜：以「阜」定其势，坡陡而难行。","ch「刺持」取「持」：坡持而滞。"),
("儊","chù",BC,N,"《廣韻》「不滑也」——不滑、滞涩。","阻涩族①之人：以「人」定其状，行而不滑。","ch「刺持」取「持」：持而滞。"),
("𠿝","chū",BC,N,"《廣韻》「呵叱人也」——呵斥。","笞打族②之口：以「口」定其声，叱而责之。","ch「刺持」取「刺」：言刺而斥。"),
("齼","chǔ",BC,N,"《玉篇》「齒傷醋也」——牙根酸楚。","笞打族②之齿：以「齿」定其感，酸楚及齿。","ch「刺持」取「刺」：酸刺而楚。"),
("憷","chù",BC,N,"《集韻》「痛也，或从疒」；「通作楚」——心痛、畏缩。","笞打族②之心：以「心」定其情，痛而畏。","ch「刺持」取「刺」：痛刺于心。"),
("𤻇","chǔ",BC,N,"《集韻》「俗作痛楚字」——痛楚之病。","笞打族②之疒：以「疒」定其疾，痛楚成病。","ch「刺持」取「刺」：病刺而楚。"),
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
ST={"楚":"从林从疋，象意人入丛木为枝条所阻——阻碍、痛楚、呵斥。","礎":"《新附》「礩也，从石楚聲」；《廣韻》「柱下石也」——柱脚石。","𨆄":"《類篇》「行不正也，一曰馬蹄痛病」。","濋":"《爾雅·釋水》「濟為濋」，大水溢出别为小水之名。","璴":"似玉之石。","𨼪":"《玉篇》「阪也」——斜坡。","儊":"《廣韻》「不滑也」——滞涩。","𠿝":"《廣韻》「呵叱人也」——呵斥。","齼":"《玉篇》「齒傷醋也」——牙根酸楚。","憷":"《集韻》「痛也，通作楚」——心痛畏缩。","𤻇":"《集韻》「俗作痛楚字」——痛楚之病。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根楚部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdg-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407楚部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407楚部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407楚部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))