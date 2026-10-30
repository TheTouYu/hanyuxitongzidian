import json,subprocess,os,glob
B6=("部首几（𠀃jī）：象几案形（古人憑坐之小案，非進食之大案）；甲骨文上加小點，表示體積小或放置小物；《說文》「踞几也，象形」。"
    "轉義：由憑靠放置引申安穩盛大（《廣雅》几几，盛也）、偕同一起、差不多（幾乎）。辯證：几與丌本兩種東西，因表面平整可置物故音義可通。音源：借音字，今「幾」簡化作「几」。"
    "字族衍義：①指几狀，表示形似之物 ②指憑靠几，表示附著、依止。")
B7=("部首启（𢼄啟啓唘𠶶qǐ）：从戶从口，象意門被打開；《說文》「启，開也」，康禮切。𢼄之甲骨文从戶从又，象意用手開門（《六書故》「開戶也」）。"
    "兩字意義本不同而結果都是開門，故合併一處；周代或从戶从攴（攴或作戈），本應是「𠶶」，指打門。"
    "轉義：開發開始、教導開導（《說文》啟，教也）、別與分移（《廣韻》別也刻也）、看與白色（前右足白曰啓、雨而晝晴曰啓）、跪跽（《爾雅》啓，跪也，郭注小跽）。"
    "音源：源自開門聲；因有跪跽義，或義音同「己」（郝懿行謂𢼄者跽之叚音）。字族衍義：指開門，表示打開、開始。")
N="字形：古文字字形庫未收；原稿該部有插圖可參。"
D=[
("䢳","jǐ",B6,"从邑几聲，《說文》「地名」（居履切）。","①組：地名只借聲，邑定其類。","j「聚決」取「聚」：邑聚而居。"),
("机","jī",B6,"从木几聲，《說文》「木也」（居履切）；郭注似榆，可燒以糞稻田，即榿木。","①組：木形如几，以木定落點。","j「聚決」取「聚」：木聚成林。"),
("麂","jǐ",B6,"从鹿几聲，《說文》「大麋也，狗足」（居履切）；《龍龕》黃鹿；其角如几。","①組之顯例：角形如几，以鹿定落點。","j「聚決」取「聚」：鹿聚成群。"),
("肌","jī",B6,"从肉几聲，《說文》「肉也」（居夷切）；《正字通》「人身四支附骨者皆曰肌」，《釋名》「肌，懻也，膚幕堅懻也」。","②組之要：肉附骨而依止，猶人憑几，以肉定落點。","j「聚決」取「聚」：肉聚附骨。"),
("㞦","jǐ",B6,"从山几聲，《說文》「山也，或曰弱水之所出」（居履切）；柳宗元謂西海之山有水散涣無力不能負芥。","②組：山低如几、水弱不能負物，以山定落點。","j「聚決」取「聚」：山聚而矮。"),
("𤜝","jǐ",B6,"从犬几聲，《廣韻》「獸名，如兔喙、蛇尾，見則有蝗災」。","①組：記異獸，形符定類，不強解。","j「聚決」取「聚」：獸聚而見。"),
("飢","jī",B6,"从食几聲，《說文》「餓也」（居夷切）；《爾雅》「穀不熟為飢」；原稿謂饑餓無力而須憑几。","②組：餓極而須憑几，以食定落點。","j「聚決」取「聚」：腹空無所聚。"),
("凥","jū",B6,"从尸得几而止，《說文》「處也」（九魚切），《孝經》「仲尼凥」謂閒居；《玉篇》與居同。","②組之正：人憑几而止息，即「居」之初文。","j「聚決」取「聚」：居而聚處。"),
("処","chǔ",B6,"从几从夂，《說文》「止也，得几而止」（昌與切）；《廣韻》居也、止也、制也、息也、留也、定也。","②組：與凥同取「得几而止」，处為其通行字。","ch「刺持」取「持」：持身而止。"),
("启","qǐ",B7,"部頭本字：从戶从口，象意門被打開；《說文》「開也」。","启部之根：與棨、綮、䁈、晵、闙等同取「打開、開始」，各以形符定落點。","q「親缺」取「缺」：門開而缺。"),
("䏿","qǐ",B7,"从肉啓省聲，《說文》「肥腸也」（康禮切）；《廣雅》腨也——小腿肚，分張如打開的門。","主組：小腿肚分張如開門，以肉定落點。","q「親缺」取「缺」：肉分而見。"),
("棨","qǐ",B7,"从木啟省聲，《說文》「傳，信也」（康禮切），木製通行符信；形如戟有幡書之，吏執為信。","主組：符信剖分為二以相合，以木定落點。","q「親缺」取「缺」：符分而合。"),
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
ST={"䢳":"《说文》「地名」。","机":"《说文》「木也」；郭注似榆，可烧以粪稻田，即榿木。","麂":"《说文》「大麋也，狗足」；《龙龛》黄鹿；其角如几。","肌":"《说文》「肉也」；《正字通》「人身四支附骨者皆曰肌」。","㞦":"《说文》「山也，或曰弱水之所出」。","𤜝":"《广韵》「兽名，如兔喙、蛇尾，见则有蝗灾」。","飢":"《说文》「饿也」；《尔雅》「谷不熟为饥」；原稿谓饥饿无力而须凭几。","凥":"从尸得几而止，《说文》「处也」；《玉篇》与居同。","処":"从几从夂，《说文》「止也，得几而止」；即处之古字。","启":"从户从口，象意门被打开；《说文》「开也」。","䏿":"《说文》「肥肠也」；《广雅》腨也——小腿肚，分张如打开的门。","棨":"《说文》「传，信也」，木制通行符信；形如戟有幡书之，吏执为信。"}
cl=[]
for i,(ch,p,Bx,a,b,c) in enumerate(D,1):
    BK="源自《系統漢語》第396部「几部」；字卡五步规程。" if i<=9 else "源自《系統漢語》第397部「启部」；字卡五步规程。"
    cl.append({"id":f"btd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡396几部清397启部头2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡396清397头.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡396清397头.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))