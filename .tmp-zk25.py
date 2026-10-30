import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「乙部」（第361部）；字卡五步规程。"
rows=[
("zk-232","乙本義：象蟲蛇扭動之形，指爬行","乙（𠃉乁乚𠃊𠄌，yǐ）象爬行動物身子扭動之形，本義指蟲蛇類爬行；楷化分作乙、𠃉、乁、乚等形。轉義：拖曳（𠃋，象抴引之形）、流動（乁，讀若移）、細長宛曲之物（《爾雅》「魚腸謂之乙」）、天干第二位、燕（商人始祖神話）。辯證：《說文》「春艸冤曲而出」「抴引之形」「流」「玄鳥」四說皆不確，皆因楷化拆散曲線。音源：蛇所發響聲；古也、它、乙可通。"),
("zk-233","軋本義：从車乙聲，𨋚也，輾壓","軋（yà）从車、乙聲，轉注，取爬行碾壓。《說文》「𨋚也」用車輪或圓軸輾壓；《篇海》「勢相傾也」；gá 擁擠、結交結算。"),
("zk-234","圠本義：从土乙聲，山曲；土密凝","圠（yà）从土、乙聲，轉注。《玉篇》「山曲」；《六書故》「土密凝也」；《方言》「坱圠，不測也」——土地板結。"),
("zk-235","𡴭本義：从屮乙聲，山曲，與圠通","𡴭（圠，yà）从屮、乙聲，轉注。《正字通》「山曲，與圠通」。"),
("zk-236","𦨇本義：从舟乙聲，舟行皃","𦨇（yì）从舟、乙聲，轉注。《集韻》「舟行皃」——舟行如水蛇。"),
("zk-237","𣄻本義：从日乙聲，流下滴也","𣄻（涿，zhuō）从日、乙聲，轉注。《說文》「涿，流下滴也」；《段注》「从日者，謂于日光中見之；乙蓋象滴下之形，非甲乙字」。"),
("zk-238","𥐕本義：从石乙聲，石皃","𥐕（yà）从石、乙聲，轉注。《集韻》「石皃」。"),
("zk-239","䰲本義：从魚乙聲，䱀䰲無鱗魚","䰲（yà）从魚、乙聲，轉注。《正字通》「䱀䰲，無鱗魚也」身尾似鯰、腮下二橫骨、群遊作聲軋軋——黃顙魚。"),
("zk-240","穵本義：从穴乙聲，空大也；鑽洞","穵（yà/wā）从穴、乙聲，轉注，取鑽洞。《說文》「空大也」；《廣雅》「深也」；《廣韻》「手穵為穴」；甲骨文从丙从乙，指鑽洞，實即「挖」。"),
("zk-241","挖本義：从手穵聲，挑挖也","挖（wā）从手、穵聲，轉注。《字彙補》「挑挖也」掏洞。"),
("zk-242","䵝本義：从黑乙聲，深黑","䵝（yì）从黑、乙聲，轉注。《廣韻》「深黑」；《集韻》「黑也」。"),
("zk-243","𨐐本義：从辛乙聲，進也","𨐐（yǐn）从辛、乙聲，轉注。《字彙補》「以忍切，音尹，進也」。"),
("zk-244","紮本義：从糸扎聲，捆縛、刺","紮（劄紥揠扎，zhǎ）从糸、扎聲，轉注。《玉篇》「俗劄字」；《集韻》「揠，《說文》拔也，或作紮」；zhā 刺、駐紮、鑽進；zā 捆縛。"),
]
draft={"schema_version":1,"intent":"字卡乙部13条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第二十五批.json"
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