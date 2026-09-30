# lhg-ui-review · 网页 UI 专家走查

给网页做专家级设计走查的 skill：**截图/代码/链接三种输入，五支柱（可用性/视觉层级/一致性/无障碍/文案）系统找缺点，P0–P2 分级 + 百分制评分，每条意见按"观察→影响→修复"输出可执行指导**（lhg-skills 出品；五阶段评审流程借鉴 duboc/agy-skills 的 design-critique（Apache-2.0），眯眼测试与一致性审计借鉴 black141312/ada 的 ui-review（MIT），"AI 味"反模式清单为独立撰写）。

**流程**：Phase 0 判模式（NOT for 清单）→ Phase 1 输入定级与证据边界（截图确立不了的标"未验证"）→ Phase 2 第一印象扫描（2 秒 + 眯眼测试）→ Phase 3 五支柱走查（可用性/视觉层级/一致性/无障碍/文案 + 中文排版专项 + "AI 味"反模式清单）→ Phase 4 分级与评分（P0/P1/P2 + 百分制，3 个高影响修复置顶）→ Phase 5 输出（每条"观察→影响→修复"三件套，先肯定优点）→ Phase 6 双模式交付（评审报告版 / 可执行修复清单版）。

**触发**：用户说"看看这个页面 / 评审一下这个 UI / 这个设计有什么问题 / 帮我走查一下 / 上线前检查一下"时使用。

## 安装

一键安装：`npx skills add lhg-skills/lhg-ui-review`

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/lhg-ui-review/`，注意 SKILL.md 须在目录根）。
- Coze：在扣子编程（code.coze.cn）→ 导入项目 → 本地上传本仓库 zip 包，平台会识别为 skill 类型。
- Trae：设置 → 技能 → 上传技能，选择本仓库 zip 包（或把目录放到 `~/.trae-cn/skills/`，国区版注意路径）。
- 平台无关：本 skill 写法平台中立（联网搜索/抓取页面/读取图片/代码检索/文件读写），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检（对照输出四铁律 + 证据边界）；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.0（2026-10-01）：首版。内化 duboc/agy-skills design-critique（Apache-2.0）五阶段流程 + black141312/ada ui-review（MIT）眯眼测试与一致性审计；升级点：输入保真度三档与证据边界诚实门、中文排版专项、中文语境"AI 味"反模式清单（独立撰写）、百分制评分、双模式交付、自迭代质检协议。

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
