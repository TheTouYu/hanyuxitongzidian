import sys,json,glob,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
KEYS=["bengen","zigen","xingpang","hengxiang","shengmu"]
fixed=[];std=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8"))
    have={s["key"] for s in d["sections"]}
    for k in KEYS:
        if k not in have:
            d["sections"].append({"key":k,"label":{"bengen":"字根本义","zigen":"字形","xingpang":"形旁声旁","hengxiang":"横向对照","shengmu":"声母义"}[k],
                                  "text":"原稿此部无对应段落，暂缺。","cites":[]}); fixed.append(d["char"])
    ch=False
    for s in d["sections"]:
        if "待按緒論" in s["text"] or "按緒論取一面待補" in s["text"] or "待補" in s["text"]:
            s["text"]=s["text"].replace("待補","未判（02z 未收）").replace("待按緒論取一面待補","未判（02z 未收）"); ch=True
    if ch: std+=1
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("补栏",fixed,"措辞统一",std)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 补最后一处缺栏+未判措辞统一"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:70])