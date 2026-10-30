import json,subprocess,os,glob
B5=("部首斯（sī）：从斤其聲——斤指斧，其指箕；箕以竹篾柳條編成，斧斫之自然散成細條；《說文》「析也」，引《詩》「斧以斯之」，息移切。"
    "轉義：分散分開分離（《廣雅》裂也分也、《爾雅》離也）、盡與全部、近指此也；散成一條條又引申指束髮帛巾。字族衍義：多指破裂、離析、分散。")
B6=("部首几（𠀃jī）：象几案形；甲骨文上加小點，表示體積小或放置小物；《說文》「几，踞几也，象形」，古人憑坐之器（《字彙》「古人憑坐者」）。"
    "几與案不同：几是坐時依憑之具，案是進食讀書之具。轉義：由憑靠放置引申安穩、盛大（《廣雅》「几几，盛也」）、偕同一起、差不多（幾乎）。"
    "辯證：几與丌本是兩種東西，因表面都平整可置物，故音義可通（期之戰國古文或从丌、或从几）。音源：借音字，今「幾」簡化作「几」，擴大其義。")
N="字形：古文字字形庫未收；原稿該部有插圖可參。"
D=[
("嘶","sī",B5,"从口斯聲，《玉篇》「噎也，馬鳴也」——馬鳴聲嘶。","主組：以口定落點，聲裂而嘶。","s「失收」取「失」：聲嘶而失其清。"),
("㯕","xī",B5,"从木斯聲，《說文》「櫪㯕也」（先稽切），用木套壓手指；《正字通》謂馬廄細柵如指排；《集韻》小木也、木下枝。","主組：木枝散列如指，以木定落點。","x「續消」取「消」：枝消而散。"),
("燍","sī",B5,"从火斯聲，《玉篇》「焦氣也」，《廣韻》「火焦臭也」；xī 烴燍，焦皃。","主組：物焦而氣散，以火定落點。","s「失收」取「失」：氣失而焦。"),
("簛","sī",B5,"从竹斯聲，《集韻》「竹枝也」，《類篇》「竹節也」；shāi 即籭（篩），竹器可除粗取細。","主組：竹枝析而為篩，以竹定落點——去粗取細正是「析」。","s「失收」取「失」：粗者失而去。"),
("廝","sī",B5,"从广斯聲，《廣韻》「廝養也、役也、使也」；《集韻》「析薪養馬者」——劈柴養馬的賤役。","主組之社會義：析薪之人為廝，以广（屋）定落點。","s「失收」取「失」：身失而役人。"),
("蟖","sī",B5,"从虫斯聲，《爾雅·釋蟲》「蟔，蛅蟖」——毛蟲，鱗翅目幼蟲，體被鱗片。","主組：毛蟲蠕動而鱗散，以虫定落點。","s「失收」取「失」：毛散而落。"),
("𪆁","sī",B5,"从鳥斯聲，《集韻》「鸒𪆁，雅烏也」——烏鴉，指其叫聲嘶啞。","主組：以鳥定落點——鴉聲嘶。","s「失收」取「失」：聲嘶而失。"),
("㽄","sī",B5,"从瓦斯聲，《集韻》引《字林》「罋破也」，一曰瓶也；《方言》瓦破聲。","主組之直證：瓦破而散，正是「析」在瓦上的落點。","s「失收」取「失」：瓦失其全。"),
("䔮","sī",B5,"从艸斯聲，《集韻》「艸名，生水中，華可食」。","主組：水草披散，以艸定落點。","s「失收」取「失」：葉散而失。"),
("𥕶","sī",B5,"从石斯聲，《集韻》引《博雅》「磨也」，通作磃。","主組：石磨而屑散，以石定落點。","s「失收」取「失」：石失其形。"),
("鐁","sī",B5,"从金斯聲，《集韻》「平木器名」；《釋名》「鐁，鐁彌也，釿有高下之跡，以此鐁彌其上而平之」——刨子。","主組：刨木而使不平者散，以金定落點。","s「失收」取「失」：高者失而平。"),
("几","jī",B6,"部頭本字：象几案形，古人憑坐之具；《說文》「踞几也」。","几部之根：與机、麂、肌、飢、凥（居）、処（處）等同取「憑靠、置物」，各以形符定落點。","j「聚決」取「聚」：憑而聚氣。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"嘶":"《玉篇》「噎也，马鸣也」——马鸣声嘶。","㯕":"《说文》「櫪㯕也」，用木套压手指；《正字通》谓马厩细栅如指排。","燍":"《玉篇》「焦气也」，《广韵》「火焦臭也」。","簛":"《集韵》「竹枝也」；shāi 即籭（筛），竹器可除粗取细。","廝":"《广韵》「廝养也、役也、使也」；《集韵》「析薪养马者」。","蟖":"《尔雅·释虫》「蟔，蛅蟖」——毛虫，鳞翅目幼虫。","𪆁":"《集韵》「鸒𪆁，雅乌也」——乌鸦，指其叫声嘶哑。","㽄":"《集韵》引《字林》「罋破也」；《方言》瓦破声。","䔮":"《集韵》「艸名，生水中，华可食」。","𥕶":"《集韵》引《博雅》「磨也」，通作磃。","鐁":"《集韵》「平木器名」；《释名》「鐁，鐁弥也……以此鐁弥其上而平之」——刨子。","几":"象几案形，古人凭坐之具；《说文》「踞几也」。甲骨文上加小点，表示体积小或放置小物。"}
cl=[]
for i,(ch,p,Bx,a,b,c) in enumerate(D,1):
    BK="源自《系統漢語》第395部「斯部」；字卡五步规程。" if i<=11 else "源自《系統漢語》第396部「几部」；字卡五步规程。"
    cl.append({"id":f"btc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡395斯部清396几部首2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡395清396头.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡395清396头.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))