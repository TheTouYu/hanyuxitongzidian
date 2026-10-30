import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「它部」（第359部）；字卡五步规程。"
rows=[
("zk-184","𩉺本義：从革它聲，馬尾駝（般緧）","𩉺（tuó）从革、它聲，轉注。《說文》「馬尾駝也。从革它聲，今之般緧，徒何切」，拖車時拴在馬尾上的皮帶。"),
("zk-185","袉本義：从衣它聲，裾也","袉（tuó）从衣、它聲，轉注。《說文》「裾也。从衣它聲，《論語》曰朝服袉紳，唐左切」，衣服前襟；tuō 通拖、長舒皃。"),
("zk-186","䡐本義：从車它聲，車疾馳","䡐（tuó）从車、它聲，轉注。《集韻》「車疾馳」——車行如蛇竄而迅疾。"),
("zk-187","柁本義：从木它聲，正船木","柁（duó/tuó/tuǒ）从木、它聲，轉注。《集韻》「正船木，或作柂、舵」；《釋名》「舟尾曰柂。柂，拖也」；tuó 木葉落；tuǒ 木堅皃。"),
("zk-188","迱本義：从辵它聲，逶迱行皃","迱（迤佗他，tuó）从辵、它聲，轉注。《集韻》「逶迱，行皃，或作迤」；yí 與委蛇之蛇同（《韓詩》「委蛇，公正貌」）。"),
("zk-189","紽本義：从糸它聲，絲數也","紽（tuó）从糸、它聲，轉注，取盤繞。《類篇》「絲數也」，絲的束數。"),
("zk-190","䍫本義：从羊它聲，羊無角者","䍫（tuó）从羊、它聲，轉注。《正字通》「䍸䍫，獸似羊，四耳九尾」；《本草》「羊無角曰䍫」。"),
("zk-191","𡩆本義：从宀它聲，囊也；馬上連囊","𡩆（tuó）从宀、它聲，轉注，取蛇身之長。《集韻》「囊也，一曰馬上連囊」——似蛇身的長袋子。"),
("zk-192","㼠本義：从瓦它聲，瓦盌／缶","㼠（tuó）从瓦、它聲，轉注。《廣韻》「瓦盌」；《集韻》「缶也」。"),
("zk-193","鼧本義：从鼠它聲，鼧鼥鼠（土撥鼠）","鼧（tuó）从鼠、它聲，轉注。《正字通》「鼧鼥鼠，生西番山澤中，穴土為窠，形似獺」；蒙古名答剌不花；鼧鼥言其肥。"),
("zk-194","砣本義：从石它聲，碾輪石；秤錘","砣（堶𥓿𤭨𤬾，tuó）从石、它聲，轉注，取團塊。《集韻》「堶，飛磚戲也，或作砣」；《字彙》「碾輪石也」——碾盤石輪、秤錘、打磨、成團之物。"),
("zk-195","詑本義：从言它聲，沇州謂欺曰詑","詑（tuó）从言、它聲，轉注，取吐信。《說文》「沇州謂欺曰詑。从言它聲，托何切」；yī 自得；xī 自多；duò 輕也。"),
("zk-196","鉈本義：从金它聲，短矛也","鉈（shī/shé）从金、它聲，轉注。《說文》「短矛也。从金它聲，食遮切」；tuó 鐵質砂輪、秤錘；yí 同匜（盛酒水器）。"),
]
draft={"schema_version":1,"intent":"字卡它部余13条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二十一批.json"
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