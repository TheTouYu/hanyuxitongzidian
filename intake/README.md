# 知识录入草稿

这里放「待录入」的草稿。草稿只是输入，不是知识；只有走完 `knowledge-plan capture` → 主人批准 → `bundle-apply` 之后再提交，内容才真正进库。

## 起草规则

- 一条 Claim = 一句能独立成立、能被引用的话。不要把三件事塞进一条。
- `statement` 写事实本身；`boundary` 只写出处部次，不写「非学界共识」一类声明：部内条目写 `源自《系统汉语》第16部「矢部」。`，卷首条目写 `源自《系统汉语》卷四「弋」卷首。`，绪论写 `源自《系统汉语》绪论。`，目录写 `源自《系统汉语》全书目录。`。部号与部首字以「全书目录与结构」主题里的 Claim 为准。
- `node` 与 `topic_id` 必填：即使写进已有主题，也要写它所属的节点 ID。
- `fact_classes` 必填且不能是空数组。汉字知识统一用 `["evidence_scope"]`（含义：这条知识以实际资料为界，不声明代码/接口层面的权威性）。
- `permission` 必须与所在 Topic 的权限一致；对外发布一律 `public`。
- `intent` 要写成这一批的具体意图（例如「新增：人字的本义」）。**intent 是计划的身份**：同一 intent 重复提交会被判为已放弃的旧计划，需要换一句新的 intent。
- 文件保存为 UTF-8（不要带 BOM），文件名建议 `20261020-人字.json`。

## 最小草稿（写进已有主题）

```json
{
  "schema_version": 1,
  "intent": "新增：人字的本义",
  "risk": "low",
  "claims": [
    {
      "node": "hanzi-origin",
      "topic_id": "topic-etymology",
      "title": "「人」的本义是侧立的人形",
      "statement": "「人」的甲骨文像侧立的人形，本义就是人。",
      "boundary": "只说明古文字形与本义的关系，不涉及现代用法。",
      "permission": "public",
      "fact_classes": ["evidence_scope"]
    }
  ]
}
```

已有节点 / 主题：

| node | node 名称 | topic_id | 主题 |
| --- | --- | --- | --- |
| `hanzi-origin` | 汉字本源 | `topic-etymology` | 字源与形体演变 |
| `hanzi-structure` | 汉字结构 | `topic-components` | 部件与偏旁部首 |
| `hanzi-sound-meaning` | 汉字音义 | `topic-reading-meaning` | 读音与字义 |
| `hanzi-usage` | 汉字应用 | `topic-standards` | 规范与易错辨析 |

## 建新主题 / 新节点的草稿

补 `topic_path` / `topic_title` / `topic_summary` / `topic_keywords`；要连节点一起建，再补 `node_name` / `node_path` / `node_boundary` / `node_keywords`。

```json
{
  "schema_version": 1,
  "intent": "新增：部件教学法主题",
  "risk": "medium",
  "claims": [
    {
      "node": "hanzi-structure",
      "topic_id": "topic-teaching",
      "topic_path": "knowledge/hanzi-structure/teaching.md",
      "topic_title": "部件教学法",
      "topic_summary": "按部件拆解教汉字的顺序与方法",
      "topic_keywords": ["部件教学", "拆字", "教学顺序"],
      "title": "先认部件再认整字",
      "statement": "……",
      "boundary": "……",
      "permission": "public",
      "fact_classes": ["evidence_scope"]
    }
  ]
}
```

## 预览 → 定稿 → 批准

```powershell
cd ..
.\tools\pkc.cmd knowledge-plan capture --file intake\20261020-人字.json --preview-only
```

`--preview-only` 只打印语义差异和将要改动的文件，不写任何东西。
确认无误后去掉 `--preview-only`：这一步会自动做 delta 校验并**定稿**，输出 `bundle_id` 和 64 位 `content_hash`。

```powershell
.\tools\pkc.cmd knowledge-plan capture --file intake\20261020-人字.json
.\tools\pkc.cmd bundle-inspect bnd_xxxxxxxx --format json
```

然后把 `content_hash` 交给主人确认；批准和应用必须是同一个哈希：

```powershell
.\tools\pkc.cmd bundle-approve bnd_xxxxxxxx --content-hash <64 位哈希> --apply
.\tools\pkc.cmd bundle-apply   bnd_xxxxxxxx --content-hash <64 位哈希> --apply
.\tools\pkc.cmd validate
```

## 有原文出处时（可选，更严谨）

把原文摘录存成 `sources/xxx.md`（UTF-8），登记来源并给 Claim 挂证据：

```powershell
.\tools\pkc.cmd register-source --source-path sources\说文解字-示部.md --title "《说文解字》示部" --representation text --permission public --apply
.\tools\pkc.cmd add-evidence --claim-id clm_xxx --source-id src_xxx --locator "示部·示字条" --support-type supports --summary "原文见示部「示」字条" --permission public --apply
```

这一步把「哪句话出自哪本书」固定下来，对外回答时可以一并给出处。
