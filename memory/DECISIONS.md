# 决策记录

## 2026-10-20 建库

- **空库起步**：只建结构骨架，不放任何示例知识，避免「示例」被当成事实。
- **路径用英文 slug，内容用中文**：`knowledge/hanzi-origin/etymology.md` 这类路径跨平台、对 git 和 URL 都安全；中文只放在标题、摘要、关键词里。
- **对外内容统一 `public`**：网页 / 微信要用的知识放在 `permission=public` 的主题下；内部资料另建 `internal` 主题，不混放。
- **问答只认 Claim**：回答用户只依据 active + public 的 Claim，没有依据就说没有，不用模型常识兜底。
- **变动走 `knowledge-plan`**：知识增删改一律通过 `pkc knowledge-plan`，先预览、再批准精确哈希、再应用。
