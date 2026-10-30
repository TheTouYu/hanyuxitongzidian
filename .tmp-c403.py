import json,subprocess,os,glob
B1=("部首奠（𠪝diàn）：从酉丌聲——《說文》「置祭也……下其丌也，《禮》有奠祭者」，堂練切，擺酒進行祭祀。"
    "轉義：由擺酒祭祀引申進獻（《廣雅》薦也）、憑藉（《集韻》假也）；由擺酒之狀引申放置平定（《廣雅》置也、《玉篇》定也）、停止（《釋名》「喪祭曰奠，奠，停也」）、儲存（飣）。"
    "音源：本丌聲；因有定意，義音同「丁」（鄭玄「奠，讀為定」，定本丁聲），或同「帝」。字族衍義：①放置平定（儲備停駐）②進獻（投擲）。")
B2=("部首𡱂（𦞠尻㞘𡰪𡱒tún）：甲骨文本為象事字——在人的屁股部位作一弧形或短撇標記，表示屁股之所在；西周晚期金文作象意字，从尸（人蹲形）、肉（肌肉）、丌（墊物底座），表示人坐下時所用之肌肉；小篆去「肉」加「几」（矮桌，休息時所倚）。"
    "轉義：由屁股的墊坐作用，比喻指器物的底部（《韻會》底也）。音源：本「丌」聲，義音同「奠」亦同「定」（王筠謂澱、淀相通）。字族衍義：①指打屁股 ②指底部。")
N="字形：古文字字形庫未收；原稿本段有插圖，可參。"
D=[
("奠","diàn",B1,"部頭本字：从酉（酒）丌聲，擺酒而祭。","①組之正：與㞟（儲備）、鄭（平町）、橂（木理堅密）、㽀（瓶屬）同取「放置平定」，以酉定落點——酒置而祭。","d「囤動」取「囤」：酒聚而置。"),
("㞟","diàn",B1,"从尸奠聲，《說文》「偫也」（儲備），堂練切；《廣韻》待也；俗用「殿」。","①組：以尸（人）定落點——人有所待而止。","d「囤動」取「囤」：所儲囤積。"),
("鄭","zhèng",B1,"从邑奠聲，《說文》京兆縣、周厲王子友所封；《釋名》「鄭，町也，地多平町町然」。","①組：地平町町然，正「平定」之落點，以邑定類。","zh「鑿總」取「總」：地總而平。"),
("橂","diàn",B1,"从木奠聲，《集韻》「木理堅密」。","①組：木理密而安，以木定落點。","d「囤動」取「囤」：木質囤實。"),
("㽀","zhèng",B1,"从瓦奠聲，《方言》「甖，秦之舊都謂之㽀」，《集韻》瓶屬——盛水酒的瓦器。","①組：器用以盛而置，以瓦定落點。","zh「鑿總」取「總」：瓶總受水。"),
("躑","zhí",B1,"从足奠聲，《說文》「住足也」；《廣韻》「躑躅，行不進也」。","①組之反：住足即「停駐」，正是平定之義在足上的落點。","zh「鑿總」取「總」：足總而不前。"),
("𧓸","zhí",B1,"从虫奠聲，《唐韻》「直炙切，音擲」，𧓸蠋蟲名；《正字通》謂俗譌。","①組：記蟲名，形符標類，不強解。","zh「鑿總」取「總」：蟲總聚。"),
("擲","zhì",B1,"从手奠聲，《廣韻》「投也、搔也、振也」——投、拋、騰躍。","②組：以手定落點——所奠之物投而出之。","zh「鑿總」取「鑿」：擲如鑿地。"),
("𡱂","tún",B2,"部頭本字：甲骨文在臀位作標記，金文从尸肉丌。","②組之正：與臀、澱、壂同取「底部」，以尸肉丌定形。","t「涂突」取「涂」：肉著於底。"),
("殿","diàn",B2,"从殳𡱂聲，《說文》「擊聲也」（打屁股之刑）；《廣雅》後也，《玉篇》大堂也。","①組：以殳（擊）定落點——打在臀上；又「軍後曰殿」取在後之義。","d「囤動」取「囤」：擊而囤響。"),
("𥴫","tún",B2,"从竹殿聲，《說文》「榜也」（榜=捶擊之具），揉制弓弩之器；diàn 打屁股的竹板。","①組：以竹定落點——打臀之板。","t「涂突」取「突」：擊而突出聲。"),
("癜","diàn",B2,"从疒殿聲，《正字通》「風斑片也，有紫白二種」——斑如被打傷淤血的屁股。","①組：以疒定落點，取「打傷」之象。","d「囤動」取「囤」：瘀血囤積。"),
("臀","tún",B2,"从肉殿聲，《集韻》引《說文》「髀也」，或作𦞠、𩪡。","②組：即部頭本義之通行字，以肉定落點。","t「涂突」取「涂」：肉附於骨。"),
]
def card(ch,p,B,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,B,a,b,c in D:
    json.dump(card(ch,p,B,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"奠":"从酉（酒）丌声，摆酒而祭，《说文》「置祭也」。","㞟":"《说文》「偫也」（储备），堂练切；《广韵》待也；俗用「殿」。","鄭":"《说文》京兆县、周厉王子友所封；《释名》「郑，町也，地多平町町然」。","橂":"《集韵》「木理坚密」。","㽀":"《方言》「甖，秦之旧都谓之㽀」，《集韵》瓶属，盛水酒的瓦器。","躑":"《说文》「住足也」；《广韵》「躑躅，行不进也」。","𧓸":"《唐韵》「直炙切，音掷」，𧓸蠋虫名；《正字通》谓俗讹。","擲":"《广韵》「投也、搔也、振也」——投、抛、腾跃。","𡱂":"甲骨文在臀位作标记，金文从尸肉丌，「髀也」。","殿":"从殳𡱂声，《说文》「击声也」（打屁股之刑）；《广雅》后也、《玉篇》大堂也。","𥴫":"《说文》「榜也」（捶击之具），揉制弓弩之器；diàn 打屁股的竹板。","癜":"《正字通》「风斑片也，有紫白二种」——斑如被打伤淤血的屁股。","臀":"《集韵》引《说文》「髀也」，或作𦞠、𩪡。"}
BK1="源自《系統漢語》第392部「奠部」；字卡五步规程。"
BK2="源自《系統漢語》第393部「𡱂部」；字卡五步规程。"
cl=[]
for i,(ch,p,B,a,b,c) in enumerate(D,1):
    cl.append({"id":f"bt8-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK1 if i<=8 else BK2,
      "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡392奠部393𡱂部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡392-393.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡392-393.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))