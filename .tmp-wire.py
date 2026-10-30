import io,re
p=r"web\server.mjs"; t=io.open(p,encoding="utf-8").read()
if "loadPresetCard" not in t:
    anchor="async function handleCard(emit, res, question, ch, ip, meter) {\n  let glyph = glyphInfo(ch);"
    add=("const CARD_DIR = join(PUBLIC, 'cards');\n"
         "const presetCache = new Map();\n"
         "function loadPresetCard(ch) {\n"
         "  const alias = loadVariantMap()[ch] || ch;\n"
         "  for (const key of new Set([ch, alias])) {\n"
         "    const p = join(CARD_DIR, key + '.json');\n"
         "    try { if (existsSync(p)) return JSON.parse(readFileSync(p, 'utf8')); } catch (e) { log('字卡读取失败', key, e.message); }\n"
         "  }\n"
         "  return null;\n"
         "}\n\n"
         "async function handleCard(emit, res, question, ch, ip, meter) {\n  let glyph = glyphInfo(ch);\n"
         "  const preset = loadPresetCard(ch);\n"
         "  if (preset) {\n"
         "    emit({ type: 'card', card: { char: ch, mode: 'preset', sections: preset.sections || [], photos: (glyphInfo(ch) || {}).photos || [], roots: [] } });\n"
         "    return res.end();\n"
         "  }")
    assert anchor in t
    t=t.replace(anchor,add,1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
    print("patched")
else: print("already")