# 操作入口

一句话：这个库的任何内容变动都走 `pkc knowledge-plan`——先预览、再由主人批准精确哈希、再应用，最后 `rebuild` + `validate`。

## 1. 读的顺序

1. 本文件 → `memory/CURRENT.md` → `memory/DECISIONS.md`
2. `pkc capabilities`：确认运行时可用
3. `pkc validate`：配置和知识树是否自洽
4. `pkc tree --format text`：看结构
5. `pkc knowledge-search "问题关键词" --format json --limit 5`：拿 L2 摘要

## 2. 回答别人的问题（网页 / 微信场景）

- 只用 `lifecycle=active` 且 `permission=public` 的 Claim 内容作答。
- 每条结论都要能对上具体 Claim（标题 + `clm_…` ID）。
- 检索不到、或只有 internal 内容时，直接说「知识库里还没有这个内容」，不要用模型自己的常识补。
- 不要先把 internal 内容改写再对外输出。

## 3. 录入知识（唯一正规路径）

1. 起草草稿：`intake/xxx.json`（格式见 `intake/README.md`）。每条 Claim 必填 `node`、`topic_id`、`title`、`statement`、`boundary`、`permission`、`fact_classes`
2. 预览（不写任何东西）：`pkc knowledge-plan capture --file intake/xxx.json --preview-only`
3. 定稿：`pkc knowledge-plan capture --file intake/xxx.json`（去掉 `--preview-only` 会自动做 delta 校验并生成 Bundle，输出 `bundle_id` 与 64 位 `content_hash`）
4. 看 Bundle 内容：`pkc bundle-inspect bnd_xxx --format json`
5. 主人批准精确哈希：`pkc bundle-approve bnd_xxx --content-hash <64 位哈希> --apply`
6. 应用同一哈希：`pkc bundle-apply bnd_xxx --content-hash <64 位哈希> --apply`
7. 验收：`pkc rebuild` → `pkc validate` → 一条代表性 `knowledge-search` → `pkc knowledge-check`
8. 提交：`git add` 精确路径 → `git commit`

修改已有条目用 `knowledge-plan revise-claim`，移动主题用 `move-topic`，不要手改文件。

**汉字知识的 fact_class 约定**：统一用 `evidence_scope`。PKC 的 Authority Ref 是给代码契约类事实用的（设计意图、实现、文档契约），汉字知识是文献证据型，用 `evidence_scope` 表示「以实际资料为界」；这样无需为每条知识伪造 Authority Ref。需要出处时，把原文摘录放进 `sources/` 并 `register-source` + `add-evidence`，走证据面。

**intent 即计划身份**：同一句 intent 重复提交会被当成旧计划（`PLAN_ABANDONED`），失败重试要换一句新的 intent。

## 4. 禁止

- 不用编辑器直接改 `knowledge/**/*.md` 和 `data/knowledge/*.json`
- 不读、不改 `.local/`（包括 SQLite），那是可以丢弃的检索投影
- 不跳过 `validate`；不用 `bundle-create --manifest`；不跳过批准直接用低层命令写库
- 不擅自改动 `project-intelligence.json` 里的身份、权限与 Authority 语义

## 5. 权限约定

- `public`：可以对外发布给网页 / 微信用户的内容
- `internal`：只给内部看的内容，默认不对外
- 同一条 Claim 的 permission 必须和它所属 Topic 一致
