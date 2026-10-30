import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「乙部」（第361部）；字卡五步规程。"
rows=[
("zk-258","釔本義：从金乙聲，稀土金屬元素Y（音譯）","釔（yǐ）从金、乙聲。一種金屬元素，稀土金屬，灰黑色粉末，有金屬光澤，可制特種玻璃和合金，元素符號Y。音譯字。"),
("zk-259","釓本義：从金乙聲，弩機；元素Gd音譯","釓（釚，qiǔ）从金、乙聲，轉注（兼形近丩之訛）。《篇海》「與釚同」；《集韻》「弩機謂之釚」弩的扳機；gá 金屬元素Gd音譯。"),
("zk-260","糺本義：从糸丩聲，繩三合也","糺（𤓱糾，jiū）从糸、丩聲，轉注。《集韻》引《說文》「繩三合也」——三股繩絞合；纏繞。"),
("zk-261","𤴥本義：从疒丩聲，腹中急也","𤴥（㽱，jiū）从疒、丩聲，轉注。《川篇》「音鳩，病也」；《說文》「腹中急也」——絞腸痧之類。"),
("zk-262","𧢳本義：从角丩聲，角曲皃","𧢳（觓觩，qiú）从角、丩聲，轉注。《正字通》「同觓，俗省」；《集韻》「觓，角曲皃」——角上曲。"),
("zk-263","𧺇本義：从走丩聲，赳，武也","𧺇（赳，jiū）从走、丩聲，轉注。《篇韻》「與赳同」；《玉篇》「赳，武也，輕勁有才力也」。"),
("zk-264","𧾹本義：从走丩聲，蹌行皃","𧾹（𧾻，jiù）从走、丩聲，轉注。《字彙》「同𧾻」；《玉篇》「𧾻䠗，蹌行皃」——走路踉蹌。"),
]
draft={"schema_version":1,"intent":"字卡乙部余7条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第二十七批.json"
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