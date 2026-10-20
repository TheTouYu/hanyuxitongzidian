# 知识录入草稿

这里放「待录入」的草稿。草稿只是输入，不是知识；只有走完 `knowledge-plan capture` → 批准 → apply 之后，内容才进库。

## 起草规则

- 一条 Claim = 一句可以独立成立、能被引用的话。不要把三件事塞进一条。
- `statement` 写事实本身；`boundary` 写它成立的范围和不证明什么（防止被当成万能的）。
- 已经存在的主题，只写 `topic_id`；要建新主题，才补 `topic_path` / `topic_title` / `topic_summary` / `topic_keywords`。
- 权限：对外发布用 `public`，内部资料用 `internal`，且必须与主题权限一致。
- 文件用 UTF-8 保存，文件名建议 `20261020-人字.json`。

## 最小草稿（写进已有主题）

```json
{
  "schema_version": 1,
  "intent": "新增：人字的本义",
  "risk": "low",
  "claims": [
    {
      "topic_id": "topic-etymology",
      "title": "「人」的本义是侧立的人形",
      "statement": "「人」的甲骨文像侧立的人形，本义就是人。",
      "boundary": "只说明古文字形与本义的关系，不涉及现代用法。",
      "permission": "public"
    }
  ]
}
```

已有主题 ID：

| topic_id | 主题 |
| --- | --- |
| `topic-etymology` | 字源与形体演变 |
| `topic-components` | 部件与偏旁部首 |
| `topic-reading-meaning` | 读音与字义 |
| `topic-standards` | 规范与易错辨析 |

## 建新主题 / 新节点的草稿

```json
{
  "schema_version": 1,
  "intent": "新增：部件教学法",
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
      "permission": "public"
    }
  ]
}
```

要连节点一起建时，再补 `node_name`、`node_path`、`node_boundary`、`node_keywords`。

## 预览与定稿

```powershell
cd ..
.\tools\pkc.cmd knowledge-plan capture --file intake\20261020-人字.json --preview-only
```

预览会打印语义差异、预计改动的文件和精确 `content_hash`，但什么都不写。
确认无误后去掉 `--preview-only` 生成 Bundle，再把哈希交给主人批准。
