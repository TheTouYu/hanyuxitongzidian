# 当前状态

Primary Context: `default`

## 现在是什么状态

- 知识库为**空库**：0 条 Claim，等待主人录入第一批知识。
- 结构骨架已建：4 个节点、4 个主题，见 `data/knowledge/registry.json`。
- 项目位置：`D:\系统汉字`（2026-10-20 从 C 盘迁到 D 盘，运行环境一并搬到 `.runtime\`）。
- 运行时：PKC 0.2.0rc5，位于 `.runtime\venv`（`tools\pkc.cmd` 可直接调用）；Python 是 `.runtime\python` 里的 3.12.10 便携安装，git 在 `.runtime\mingit`。整个目录不依赖 C 盘。
- 录入链路已在副本上完整跑通：草稿 → 预览 → 定稿 → 批准 → 应用 → `validate` 通过（验证用的副本已删除）。
- 对外服务（网页 / 微信）：还没开始，等知识录入成型后再接。

## 下一步

1. 主人用中文讲知识（可以很口语）→ 整理成 `intake/*.json` 草稿（`node` + `fact_classes: ["evidence_scope"]` 必填）
2. `knowledge-plan capture --preview-only` 预览
3. 主人确认后，按精确哈希批准 → apply → 验证 → 提交

## 计数

4 个节点 / 4 个主题 / 0 条 Claim
