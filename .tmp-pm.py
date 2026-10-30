# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
old="""  emit({
    type: 'card',
    card: {
      char: ch,
      question,"""
new="""  let presetMeta = null;
  try {
    const pf = join(CARDDIR, ch + '.json');
    if (existsSync(pf)) {
      const pd = JSON.parse(readFileSync(pf, 'utf8'));
      if (pd && !Array.isArray(pd)) presetMeta = { head: pd.head, pinyin: pd.pinyin, level: pd.level, parent: pd.parent, bus: pd.bus, aliases: pd.aliases };
    }
  } catch (e) {}
  emit({
    type: 'card',
    card: {
      ...(presetMeta || {}),
      char: ch,
      question,"""
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched ad-hoc meta")