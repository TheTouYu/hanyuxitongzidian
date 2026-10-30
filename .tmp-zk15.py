import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部之「囪部」（第355部）；字卡五步规程。"
rows=[
("zk-116","囪本義：灶突煙洞，與煴同源","囪（囱窗匆）：據甲骨文構件與「煴」同——「昷」本「人」在「函」中形，从火即煙洞；煴《說文》「鬱煙也」，囪《玉篇》「灶突也」，本為排煙之器，與煴同源。後戰國古文與「囟」訛混，加土成「垔」。辯證：《說文》「在牆曰牖，在屋曰囪，象形」不確——囧甲文乃剖心之形非窗，悤从心亦與囪無涉。音源：借音字，囪囟混同兼因音義相通。"),
("zk-117","𢈣本義：从广怱聲，屋階中會","𢈣（𢊕，cōng）从广、怱聲，轉注。《說文》「𢊕屋階中會也。从广怱聲，倉紅切」，屋階的中央交會處。"),
("zk-118","總本義：从糸悤聲，聚束也","總（摠，zǒng）从糸、悤聲，轉注。《釋名》「束髮也，總而束之也」；《廣韻》「聚束也、合也、皆也、眾也」。"),
("zk-119","鏦本義：从金悤聲，矛也","鏦（𥎋䤸，cōng）从金、悤聲，轉注。《集韻》引《方言》「矛，吳楚之間謂之鏦」。"),
("zk-120","蔥本義：从艸悤聲，中空色青","蔥（葱，cōng）从艸、悤聲，轉注，取中空色青一路。《正字通》「蔥本字」。"),
("zk-121","窗本義：从穴悤聲，通孔也","窗（牕牎囪，chuāng）从穴、悤聲，轉注，囪之後起分別文。《正韻》「初莊切，音瘡，通孔也，亦作窗、囪」。"),
("zk-122","聰本義：从耳悤聲，耳竅通則聰","聰（𦕻，cōng）从耳、悤聲，轉注，取通孔。《廣韻》「聞也、明也、察也、聽也」。"),
("zk-123","蟌本義：从虫悤聲，蜻蜓也","蟌（𧋙，cōng）从虫、悤聲，轉注。《六書故》「蜻蜓也」；《篇海》「毛蟲也」。"),
("zk-124","驄本義：从馬悤聲，馬青白雜毛","驄（𩣢，cōng）从馬、悤聲，轉注。《說文》「馬青白雜毛也」。"),
("zk-125","垔本義：从土囪聲，煙囪煙塵，煙之初文","垔（𡎱堙，yīn）从土、囪聲，轉注。本指煙囪裡的煙塵，為「煙」之初文（《正字通》「同煙，火鬱氣」）；引申堵塞（《廣韻》「塞也」）。辯證：小篆訛囪為西，故《說文》「从土西聲」析形不確。"),
("zk-126","闉本義：从門垔聲，城內重門","闉（yīn）从門、垔聲，轉注，取堵塞。《說文》「城內重門也。从門垔聲，《詩》出其闉闍，於眞切」，保護城門的月城之門；《集韻》「曲也」。"),
("zk-127","湮本義：从水垔聲，沒也","湮（yān/yīn）从水、垔聲，轉注。《說文》「沒也。从水垔聲，於眞切」；《廣韻》「落也、沈也」，沒落沉沒；《集韻》「塞也」；yīn 指液體著物向四外散開（後作洇）。"),
]
draft={"schema_version":1,"intent":"字卡囪部12条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十五批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print("applied", '"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))