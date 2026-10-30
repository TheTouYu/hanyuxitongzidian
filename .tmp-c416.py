import json,subprocess,os,glob
B8=("部首皕（bì）：依据「衋」的西周早期金文，应从「自」的二叠。「自」指鼻子，二叠表示极致，故象意鼻子很大，或反应强烈。"
    "轉義：鼻子是呼吸器官，由呼吸急促之状引申指盛怒（分化如奭）；鼻子受刺激而流涕流血，引申指痛苦（分化如衋）。"
    "辯證：「自」「百」形近而讹变从「百」，故《说文》「二百也」所析不确——「二百」作此写法反而繁复，不合书写习惯；「自」与「㐁」也相近，亦相混。"
    "音源：音源字，源自鼻息声。字族衍义：①鼻息急促表盛怒 ②鼻流涕表悲伤 ③形近「㐁」之讹。")
N="字形：古文字字形库未收；原稿该部图未配（可参「鼻」部字形）。"
D=[
("奭","shì",B8,"从大从皕，皕亦声（《说文》「盛也…读若郝，诗亦切」）；《集韵》「吓，怒也。或作䓇、奭。通作赫」——鼻息急促之盛怒，与「赫」通。","主组①：以「大」定其势，盛怒如火。","sh「失收」取「失」：怒气失收而外放。"),
("衋","xì",B8,"从血、聿，皕声（《说文》「伤痛也」，许力切）；段注「聿者，所以书也；血聿者，取披沥之意」——血泊与痛哭流涕之状。","主组②：以「血」定其痛，涕血俱下。","x「续消」取「消」：伤痛如泪血之消。"),
("襫","shì",B8,"《唐韵》「施只切，音释。襏襫，雨衣」；《集韵》「襏襫，蓑襞也」——蓑衣，上小下大，披挂如鼻而沥雨如涕。","主组②之妙：以「衣」定其类，形如鼻而雨如涕。","sh「失收」取「收」：雨衣收雨而不入。"),
("𢐤","bì",B8,"《龙龛》「𢐈𢐀𢐡𢐤㢶弻，六俗；㢸，古；弼，今。平密反，辅也，重也，备也」；据「弼」西周金文应从「㐁」象席形。","主组③之辨：非鼻子义，是形近之讹——原从席（㐁），讹成二自。","b「闭剥」取「闭」：弓檠辅闭而正。"),
("皕","bì",B8,"部头本字：从自二叠，象鼻子很大（已具卡）。","主组：部头本字。","b「闭剥」取「闭」：鼻塞而息闭。"),
("弼","bì",B8,"《说文》「輔也，重也」；《尚书》「梦帝赉予良弼」——辅正弓弩之器（檠），引申辅佐。","主组③之同：本从席形之「㐁」，象弓檠夹持而正。","b「闭剥」取「闭」：夹弓使正而不弛。"),
("赫","hè",B8,"《说文》「火赤皃」；《诗》「赫如渥赭」——火色赤盛，与奭通（盛怒如火）。","主组①之同：以「赤」定色，火盛与怒盛相通。","h「豁活」取「豁」：火豁然而赤。"),
("嚇","hè",B8,"《集韵》「怒也。或作䓇、奭。通作赫」；今语恐吓——以盛怒之状加「口」，出声以威人。","主组①之直：以「口」定其声，怒而吓人。","h「豁活」取「豁」：气豁出而喝。"),
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
ST={"奭":"《说文》「盛也。从大从皕，皕亦声」；《集韵》「吓，怒也。或作䓇、奭。通作赫」——鼻息急促之盛怒。","衋":"《说文》「伤痛也。从血、聿，皕声」；段注血聿取披沥之意，皕指痛哭流涕之状。","襫":"《唐韵》「襏襫，雨衣」；《集韵》「蓑襞也」——上小下大，披挂如鼻而沥雨如涕。","𢐤":"《龙龛》「辅也，重也，备也」，俗弼字；据西周金文应从「㐁」象席形。","皕":"部头本字：从自二叠，象鼻子很大，或反应强烈。","弼":"《说文》「辅也，重也」——辅正弓弩之檠，引申辅佐。","赫":"《说文》「火赤皃」；《诗》「赫如渥赭」——火色赤盛，与奭通。","嚇":"《集韵》「怒也。或作䓇、奭。通作赫」——以盛怒之状加口出声以威人。"}
BK="源自《系統漢語》第398部「皕部」（卷六十五 鼻）；字卡五步规程。"
cl=[{"id":f"bfu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":BK,"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡398皕部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡398皕部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡398皕部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))