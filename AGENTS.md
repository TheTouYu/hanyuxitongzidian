# 系统汉字 · 项目契约

这是「系统汉字」知识库项目：把主人录入的汉字知识固化成可追溯的 Claim，供网页、微信等对外问答使用。

## 必读顺序

`memory/OPERATING.md` → `memory/CURRENT.md` → `memory/DECISIONS.md`

## 工具

- 运行时：`..\portable-knowledge\.venv\Scripts\pkc.exe`；本目录 `tools\pkc.cmd` 是它的包装
- 版本：PKC 0.2.0rc5（不要用别的副本，也不要把 `PYTHONPATH` 指向源码目录）
- git：`tools\git.cmd`（便携版 MinGit）；提交前先 `git diff --check`

## 硬规则

1. 任何知识变动只走 `pkc knowledge-plan`（`capture` / `add-claim` / `revise-claim` / `move-topic` / `update-topic`）。先 `--preview-only` 预览，再由主人批准精确的 64 位 `content_hash`，才允许 `bundle-approve --apply` 和 `bundle-apply --apply`。
2. 不要手工编辑 `knowledge/**/*.md` 和 `data/knowledge/*.json`；不要读 `.local/`（含 SQLite）。
3. 改完必须跑 `pkc rebuild`、`pkc validate`，再做一条代表性 `pkc knowledge-search`。
4. 对外回答只用 `lifecycle=active` 且 `permission=public` 的 Claim；没有依据就说没有，不要用模型常识兜底。
5. 用中文交流，先说结论，再讲原因。
