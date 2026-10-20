# 决策记录

## 2026-10-20 建库

- **空库起步**：只建结构骨架，不放任何示例知识，避免「示例」被当成事实。
- **路径用英文 slug，内容用中文**：`knowledge/hanzi-origin/etymology.md` 这类路径跨平台、对 git 和 URL 都安全；中文只放在标题、摘要、关键词里。
- **对外内容统一 `public`**：网页 / 微信要用的知识放在 `permission=public` 的主题下；内部资料另建 `internal` 主题，不混放。
- **问答只认 Claim**：回答用户只依据 active + public 的 Claim，没有依据就说没有，不用模型常识兜底。
- **变动走 `knowledge-plan`**：知识增删改一律通过 `pkc knowledge-plan`，先预览、再批准精确哈希、再应用。
- **汉字知识用 `fact_classes: ["evidence_scope"]`**：PKC 的 Authority Ref 面向代码契约类事实（设计意图 / 实现 / 文档契约），库里只有 8 个固定 fact class；汉字知识是文献证据型，用 `evidence_scope` 表达「以实际资料为界」，既满足校验，又不必为每条知识伪造 Authority Ref。需要严格出处时改用 `sources/` + `register-source` + `add-evidence`。
