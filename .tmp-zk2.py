import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「冎」部（第347部）；字卡五步规程。"
items=[
("zk-007","咼本義：从口从冎，口戾不正","咼（wāi）从口从冎，屬第347部部內二級字根。冎象三節相連之腿骨，為骨之初文；口戾不正——骨節外突、其形偏斜不正。部內字族（p72）窩、鍋、堝、瘑、蝸、媧、渦、禍、剮、騧、喎、萵諸字，皆取「斜而凹」一面，由形符定其落點。"),
("zk-008","禍本義：从示咼聲，神不福也，指骨頭作祟","禍（huò）从示、咼聲，屬轉注。《說文》「害也，神不福也。从示，咼聲。胡果切」，禍害。原稿點破取義：「骨頭作祟，義即死去的先人為害」；《釋名》「毀也，言毀滅也」。同取曲折不順者：渦（水）回旋、窩（穴）凹處、鍋（金）凹而盛、蝸（虫）旋殼、剮（刀）剔骨。"),
("zk-009","剮本義：从刀咼聲，剔肉置骨","剮（guǎ）从刀、咼聲，咼即冎之俗寫（骨），屬轉注。《玉篇》「剔肉置骨也」，《說文》作冎，《廣韻》「俗咼字」，《正字通》「本作冎」；義為將骨頭上的肉用刀剔掉，同「刮」。同取分骨者：冎（骨）、骾（骨）骨鯁、咼（口）骨節外突、別（刀）分解。"),
("zk-010","骷本義：从骨古聲，髆䯊也，指骷髏","骷（kū）从骨、古聲，屬轉注，聲旁「古」取「枯」之乾枯中空一面。《廣韻》「骷，髆䯊也」；骷髏，只有骨頭的屍首或頭骨。同取枯骨者：骼（骨）骨骼、骾（骨）骨鯁、髓（骨）骨髓、體（骨）身體。"),
]
draft={"schema_version":1,"intent":"字卡卷六十第二批四条 2026-10-22","risk":"low","claims":[]}
for i,(cid,title,stmt) in enumerate(items):
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out)
print("PLAN",pid.group(0) if pid else out[-300:]); pid=pid.group(0)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin); print("BUNDLE",b.group(0) if b else fin[-300:]); b=b.group(0)
st=run("bundle-status",b,"--format","json"); h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',st).group(1)
print("HASH",h)
print(run("bundle-approve",b,"--apply","--content-hash",h)[-80:].strip())
print(run("bundle-apply",b,"--apply","--content-hash",h)[-80:].strip())
print(run("pkc","validate","--format","json")[:0] or "validate next")