import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「夂」部（第350部）；字卡五步规程。"
items=[
("zk-035","𡰿本義：从夂𡱂聲，行促迫，緊隨人後","𡰿（pú/qū）从夂、𡱂聲。《說文》「行𡰿𡰿也。从夊，闕。讀若僕。又卜切」；qū《集韻》「衢六切，行迫促也」。原稿以為應从𡱂（臀）得聲，即緊隨在前人屁股後面走，義音同「趨」；《正字通》疑為譌字。"),
("zk-036","𡕢本義：象皮包覆腦，指腦蓋與首飾","𡕢（mǎn/wàn）《說文》「瑙蓋也。象皮包覆瑙，下有兩臂，而夊在下。讀若範。亡範切」，指腦蓋；《集韻》「首飾也」，馬頭上的裝飾品。象意兼聲。"),
("zk-037","𡶣本義：同歲，借聲之字","𡶣（suì）从山、歲省聲，《龍龕》「音歲」，同「歲」。借聲用之，不取夂之義。"),
("zk-038","𦲯本義：草木無蔓，荒蕪","𦲯（wàn）从艸、夂聲，屬轉注，聲旁取「往後、阻行」之反——草不蔓生、不止不行。《玉篇》「草木無蔓也」，《廣雅》「薉也」，荒蕪。"),
("zk-039","後本義：从彳幺夂，行遲而落在後","後（hòu）＝彳（行）＋幺（小）＋夂（倒止，後退）。甲骨文从幺夂聲：夂即倒止指後退，幺本小義——既可指晚出生的，也可指小孩子行走慢，故有落後之意。《說文》「遲也」，段注「幺者小也，小而行遲，後可知矣」。轉義：晚生引申子孫、後代、將來。"),
("zk-040","退本義：从皀夊，吃完退席、離開","退（tuì）＝辵（行）＋皀（食器）＋夊（離開）。甲骨文从皀夊聲：「皀」同即、既所从，指裝有食物的器皿；「夊」指離開——象意吃後離開、退席；周初金文疊加「彳」表往後走。《玉篇》「卻也、去也」；引申謙讓、返回、衰減、脫去；《方言》「退，緩也」。"),
("zk-041","各本義：从凵夂，返回、進巢、歸家；落之初文","各（gè）＝凵（或口，坎穴居室）＋夂（後退、返回），與「出」相反，象意返回、進巢、歸家，為「落（luó）」之初文（《集韻》「落居也」）。轉義：不同個體返回各自處所，故引申異、分離——《正字通》「凡事物離析不相合皆謂之各」；《說文》「異辭，从口夂，古洛切」。"),
("zk-042","路本義：从足从各，人所各適之道路","路（lù）＝足＋各（聲兼義，取各自所適）。《說文》「道也。从足从各。洛故切」，徐鉉注「言道路人各有適也」，象意通向各自處所的道路。轉義：路為踩踏而成之軌跡，引申顯露（《釋名》「路，露也」）、大（《爾雅》「路，大也」）、條理規律（思路）、類別方面（路數）。"),
("zk-043","咎本義：从人夂，災禍降落反諸於人","咎（jiù）＝人＋夂（返回、降落），或加口作各，義同。甲骨文从人夂聲，象意某事降落、反諸於人身上。轉義：反諸本人多指不好之事，故引申疾病、責任、災禍、過失——《說文》「災也。从人从各，各者相違也，其久切」；又引申指責、追究、憎惡（《方言》「謗也」）。"),
("zk-044","𩰫本義：側邊開口的鬲器，即土釜","𩰫（𩰬，guō/wāi）＝鬲上開斜口，象意側邊開口的鬲器：鬲開口朝上、下有足可燒火，故𩰫當為陶爐與釜的組合；周金文寫如爐身與酉之上部組合，旁或加口。《玉篇》「秦名土釜曰𩰫」。轉義：因旁開火口，比喻歪嘴——wāi《集韻》「咼，《說文》口戾不正也，或作𩰬」。"),
]
draft={"schema_version":1,"intent":"字卡夂部十条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第七批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out); print("PLAN",pid.group(0) if pid else out[-400:]); pid=pid.group(0)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin); print("BUNDLE",b.group(0) if b else fin[-400:]); b=b.group(0)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
print("done")