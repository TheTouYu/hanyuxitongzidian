# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\示.json"
d=json.load(io.open(p,encoding="utf-8"))
secs=d["sections"]
if not any(s["key"]=="bianzheng" for s in secs):
    txt=("「示」的本義是指神靈，這沒有疑問；但它的字形具體所指到底是什麼？眾說紛紜：\n"
"丁山《甲骨文所見氏族及其制度》認為：「示氏」同源，「示所从二或一，是上帝的象徵。其所从丨，正象祭天杆，杆旁之八，蓋象所挂的彩帛，示之本義就是設杆祭天的象徵。」即氏族所設立的圖騰柱。\n"
"明義士《柏根氏舊藏甲骨文字考釋》謂：為祭壇之几。象祭台形。類似于滿族祭天用的「索倫杆」，豎立一直杆，上端一橫為几（索倫杆上面是錫斗），用以放置祭品。\n"
"馬敘倫《說文解字六書疏證》認為：「从一十聲」。「一」為「上」，指天空；下面一豎為「十」，指日月星辰等光明之象。此說與《說文》近似。葉玉森《說契》看法近似，但認為下面的「丨」表示「神恍惚自天而降」。\n"
"唐蘭《釋示宗及主》認為「示主」同為一字，「用木或石以擬鬼神而祭之，藏于廟謂之宗。」徐中舒《甲骨文》看法差不多：「象以木表或石柱為神主之形。」商承祚《甲骨文字研究》明確：「皆栗主之象。」姜亮夫《漢字結構的基本精神》所解最為具體。\n"
"此外，郭沫若認為系雄性生殖器倒置。與本文觀點差不多。\n"
"本人初版認為：「示」从「工」，或作，專指引出經線的部分，即「綜」義。或作，下从「巾」，指織好的布；上面的小點指經線。或作，象有經線斷了的樣子；經線斷了，會造成瑕疵，所以有不祥之義。或作，从（上），指上天；則經線的斷與否，帶有預卜吉凶的意味；故有警示之義。仍留以備考。")
    idx=[i for i,s in enumerate(secs) if s["key"]=="yinyuan"]
    pos=idx[0] if idx else len(secs)-1
    secs.insert(pos,{"key":"bianzheng","label":"辩证","text":txt,"cites":[]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("示 补回辩证，栏数",len(secs))
else: print("已有辩证")