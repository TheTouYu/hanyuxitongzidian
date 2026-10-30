import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尔.json"; d=json.load(open(p,encoding="utf-8"))
z=[s for s in d["sections"] if s.get("groups")][0]
S=[{"key":"benyi","label":"本义","text":"甲骨文上部象囟門未合攏的人形；下部跟“舞”所从相同，象草編形。本義當指穿草裙的幼兒。這樣穿著的功用，相當于後來的尿布，既能保護幼兒的身體，又方便換洗。“彌（mí）”的初文，《集韻》：“嫛彌，嬰兒皃。”","cites":[]},
{"key":"zhuanyi","label":"转义","text":"由幼兒引申指第二人稱，含有輕蔑的意味。ěr，《玉篇》：“汝也。”故或引申作語氣詞，表示罷了。《玉篇》：“詞之畢也。”\n由草裙的層疊之狀，引申指繁盛、滿、眾。mǐ，《集韻》：“濔，《說文》：‘滿也。’一曰濔濔，眾也。或省。”","cites":[]},
{"key":"bianzheng","label":"辩证","text":"“尒”本來是由“爾”演變過來的，戰國古文將下面的網狀草裙寫成“小”狀。故《說文》：“爾，麗爾，猶靡麗也。从冂从㸚，其孔㸚，尒聲。此與爽同意。兒氏切。”《說文》：“尒，詞之必然也。从入丨八。八象氣之分散。兒氏切。”析形皆不確。\n另从“璽”的戰國古文看，所从“爾”本从圭从巾，指印信，形近而混同。","cites":[]},
{"key":"yinyuan","label":"音源","text":"音源字，源自嬰兒的哭聲。義音同“兒”：段玉裁注《說文》“弭”字云：“爾、兒聲同。”","cites":[]},
{"key":"shengmu","label":"声母拟态","text":"爾今读 ěr，零聲母；绪论七组声母未列零聲母，本部不系拟态声母义（见 02z「零聲母諸部」條）。","cites":[]},
{"key":"zizu","label":"字族衍义","text":"","groups":z["groups"]}]
d["sections"]=S
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")