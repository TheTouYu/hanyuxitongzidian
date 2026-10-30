import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「也部」（第360部）；字卡五步规程。"
rows=[
("zk-197","也本義：象眼鏡蛇頸褶膨起，虵之初文；轉義語氣詞","也（𠃟𦫴𦬀𠔄𠃒，yě）甲骨文象眼鏡蛇頸部皮褶兩側膨起，與它、虫同源，虵之初文（《唐韻》「俗蛇字」）。轉義：見蛇驚止→停頓、判斷、肯定、反問、感歎、命令、強調、轉折等語氣；外形相似之物（匜）；爬行→逶迤。辯證：《說文》「女陰也」析形不確，然女陰與眼鏡蛇頭有形似（陰唇如頸褶、泌尿如噴毒）。音源：眼鏡蛇哈氣聲。"),
("zk-198","酏本義：从酉也聲，黍酒也","酏（𨠑𨡪，yǐ）从酉、也聲，轉注。《說文》「黍酒也，一曰甜也」；《玉篇》「米酒也、清酒也」濾出的清酒——應指用匜濾酒；《集韻》「粥稀之清」稀粥。"),
("zk-199","釶本義：从金也聲，短矛也；同匜","釶（鍦鉇𥍸，shī）从金、也聲，轉注。《字彙補》「同鍦」；《集韻》「短矛也」；yí 同匜（盛酒水器）。"),
("zk-200","池本義：从水也聲，城池也","池（湤，chí）从水、也聲，轉注。《說文》「城池也，有水曰池，無水曰隍」護城河；《廣韻》「停水為池」水塘；《玉篇》「差池」意外差錯；《集韻》「穿地鐘水」溝渠。"),
("zk-201","㒾本義：从衣也聲，面衣","㒾（shì）从衣、也聲，轉注。《廣韻》「𣈯㒾，面衣」——覆面之衣（面幕）。"),
("zk-202","袘本義：从衣也聲，衣中也；衣袖","袘（袉衪，yí）从衣、也聲，轉注。《類篇》「衣中謂之袘」；《玉篇》「衪，衣袖也」；yì 裳下緣；tuó 前襟。"),
("zk-203","椸本義：从木施聲，衣架也","椸（yí）从木、施聲，轉注。《新附》「衣架也。从木施聲，以支切」；《方言》「榻前几，趙魏之間謂之椸」。"),
("zk-204","匜本義：从匚也聲，似羹魁，柄中有道可注水","匜（yí）从匚、也聲，轉注。《說文》「似羹魁，柄中有道，可以注水」——象湯勺、柄中有槽可注水；《左傳》「奉匜沃盥」；原稿配西周應國應侯筒匜圖。"),
("zk-205","𦧇本義：从舌也聲，以舌取食","𦧇（𦧓舓，shì）从舌、也聲，轉注，取吐信。《說文》「舓，以舌取食也」——用舌舔取食物。"),
("zk-206","訑本義：从言也聲，詑詑自得","訑（𧩹𧦧𧪁詑，yí）从言、也聲，轉注。《集韻》「詑詑，自得也」；dàn 慢訑放縱；shī 多言；tuó 欺也。"),
("zk-207","忚本義：从心也聲，㦒忚欺慢","忚（xī）从心、也聲，轉注。《方言》「㦒忚，欺慢也」；liě「忚忚，心不欲皃」。"),
("zk-208","灺本義：从火也聲，燭㶳也","灺（炧，xiè）从火、也聲，轉注，取蛇舌。《說文》「燭㶳也」——燭燼，紅而開衩如蛇舌。"),
("zk-209","阤本義：从阜也聲，小崩也","阤（zhì）从阜、也聲，轉注。《說文》「小崩也」；《集韻》「崖際」岸邊；yǐ 山勢綿延；tuó 壞也（陂阤險阻）。"),
]
draft={"schema_version":1,"intent":"字卡也部13条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二十二批.json"
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