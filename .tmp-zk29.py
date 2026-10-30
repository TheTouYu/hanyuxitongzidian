import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「虒部」（第363部）；字卡五步规程。"
rows=[
("zk-273","虒本義：从虍乙聲，象如蛇吐舌爬行之虎，即壁虎","虒（sī）从虍、乙聲，象意兼聲，取虎形與蛇行。本義壁虎（螔之初文，《方言》「守宮在澤者，海岱之間謂之螔䗔」）；轉義逶迤（委虒連綿詞，音義同逶迤，彎曲迴旋）。辯證：《說文》「委虒，似虎，有角，能行水中」以虎為核心義不確。"),
("zk-274","螔本義：从虫虒聲，守宮（壁虎）／蝸牛","螔（yí/sī）从虫、虒聲，轉注。蝸牛（《玉篇》「蚹蠃，螔蝓也」）；壁虎（《方言》「守宮在澤者…謂之螔䗔」）。"),
("zk-275","禠本義：从示虒聲，福也，跪拜祈福","禠（sī）从示、虒聲，轉注。《說文》「福也」——跪拜祈福。"),
("zk-276","䖙本義：从虍虒聲，虎臥息微","䖙（tī）从虍、虒聲，轉注。《集韻》「臥也，一曰虎臥息微」。"),
("zk-277","蹏本義：从足虒聲，足也（蹄）","蹏（tí）从足、虒聲，轉注。《說文》「足也」蹄；《集韻》「蹋也」——牲畜抬蹄攻擊。"),
("zk-278","傂本義：从人虒聲，佌傂參差","傂（zhì）从人、虒聲，轉注。《集韻》「佌傂，參差也，一曰別植皃」；sī 車輪（《太玄》作傂）。"),
("zk-279","𩤽本義：从馬虒聲，駿馬名","𩤽（tī）从馬、虒聲，轉注。《字彙》「駿馬名」。"),
("zk-280","搋本義：从手虒聲，以拳加人","搋（chuāi）从手、虒聲，轉注。《玉篇》「以拳加人也」；《集韻》「析也，或作扡、拸」「又拽也」；yí 輕笑（同歋）。"),
("zk-281","歋本義：从欠虒聲，人相笑相歋瘉（揶揄）","歋（yí）从欠、虒聲，轉注。《說文》「人相笑相歋瘉」；《廣韻》「手相弄人」——揶揄、互相捉弄。"),
("zk-282","䞾本義：从走虒聲，輕薄","䞾（chí）从走、虒聲，轉注。《說文》「䞾騭，輕薄也」；dì 輕也。"),
("zk-283","遞本義：从辵虒聲，更易也","遞（dì）从辵、虒聲，轉注。《說文》「更易也」更易反覆運算；《增韻》「傳遞也」；shì 往也；dài 繞也。"),
("zk-284","㴲本義：从水虒聲，水名（湡水支流）","㴲（sī）从水、虒聲，轉注。《說文》「水，出趙國襄國，東入湡」；《集韻》「水厓」水邊。"),
("zk-285","㥴本義：从心虒聲，不憂事","㥴（yí）从心、虒聲，轉注。《說文》「忯㥴，不憂事也」；tí 楚人謂慚曰㦦㥴。"),
]
draft={"schema_version":1,"intent":"字卡虒部13条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第二十九批.json"
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