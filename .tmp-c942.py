import sys,json,glob,re,subprocess,os,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
rows=[]
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8"))
    sm=[s for s in d["sections"] if s["key"]=="shengmu"]
    if sm and "待回中古反切核定" in sm[0]["text"]:
        rows.append((d["char"],d.get("pinyin",""),fp))
print("待核",len(rows))
print(collections.Counter((p[:1] or "∅") for _,p,_ in rows))
MAP={"r":("柔锐","锐"),"y":("零声母·喻影",None),"w":("零声母·喻影",None)}
n=0
for ch,p,fp in rows:
    d=json.load(open(fp,encoding="utf-8")); sm=[s for s in d["sections"] if s["key"]=="shengmu"][0]
    ini=p[:1]
    if ini in MAP:
        a,b=MAP[ini]
        sm["text"]=(f"聲母義：聲母 r（擬態「{a}」），取「{b}」一面。" if ini=="r" else
                    f"聲母義：零聲母（今讀 {p}）——古屬影／喻／疑一系，無輔音擬態可系，義靠義類與字形。")
    else:
        sm["text"]=f"聲母義：今讀 {p or '無'}；未列 02z，按緒論取一面待補。"
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("处理",n)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 待核声母义128张按声母归类"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:70])