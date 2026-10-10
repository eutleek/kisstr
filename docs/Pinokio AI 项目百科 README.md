# Pinokio AI 项目百科

一个可独立打开的本地 AI 项目目录网站与结构化数据库，收录 **343 个**真实存在、可交叉验证的 AI 开源项目，覆盖 16 个分类，每项目 35 个字段（功能、硬件需求、硬盘占用拆分、收费与授权、Pinokio 兼容性等）。数据截至 **2026-10-04**。

## 快速开始

- **直接打开 `index.html`** 即可使用（无需联网、无需服务器；页面为自包含单文件，全部数据内嵌于 `window.EMBEDDED_DATA`）。
- 也可在目录内启动本地服务器：`python -m http.server 8000` 后访问 `http://localhost:8000/`。

## 交付物清单

| 文件 | 说明 |
|---|---|
| `index.html`（即 `site/ai_projects.html`） | 单文件站点（CSS/JS 全内联、零 CDN 依赖），数据内嵌于 `window.EMBEDDED_DATA`（343 条项目 + 16 分类 + 21 标签），搜索/筛选/排序/详情/深链/收藏/已安装/深浅色/硬件雷达/硬盘计算器/项目对比全部可用 |
| `README.md` | 本文件 |

## 数据概览

- **项目总数**：343（计划 300～500；实际按"宁缺毋假"原则收录真实可验证项目，未用复制/虚构凑数）
- **分类与实际数量**：

| 分类 | 计划 | 实际 |
|---|---|---|
| AI 图像生成 | 35 | 31 |
| AI 图像编辑 | 25 | 25 |
| AI 视频生成 | 30 | 32 |
| AI 音频 | 25 | 25 |
| AI 语音 | 20 | 20 |
| AI 数字人 | 15 | 15 |
| 3D 与设计 | 15 | 15 |
| AI 大语言模型 | 30 | 30 |
| AI 聊天界面 | 20 | 20 |
| AI Agent | 25 | 25 |
| AI 编程 | 20 | 20 |
| AI 工作流 | 20 | 20 |
| 实用工具 | 20 | 20 |
| AI 数据处理 | 15 | 15 |
| OCR 与文档 | 15 | 15 |
| AI 搜索与知识库 | 15 | 15 |

- **Pinokio 兼容性**：官方验证脚本 29 / 社区脚本 8 / 手动安装 291 / 不支持本地部署 15。
- **收费模式**：开源 310 / 免费 11 / 捐赠 1 / 免费增值 20 / 未知 1。
- **维护状态**：正常维护 257 / 低频维护 71 / 停止维护 7 / 已归档 8。

## 数据可信度（重要）

- **置信度分级**：`verified`（15 条，官方页面/HF 模型卡直接核实）> `estimated`（328 条，star 数、硬件、更新时间为基于官方文档或第三方摘要的估算）> `unverified` / `expired`（0 条）。
- **验证通道**：官网与 Hugging Face 模型卡（许可证/模型体积）经实时抓取核实；GitHub 仓库存在性、star、许可证经多源搜索摘要交叉验证。受本机网络限制，GitHub 页面与 API 无法直连，**star 数均为近似值**（已在 notes 标注来源），未取到的字段一律为 `null`，未虚构。
- **硬性规则**：所有未知数据填 `null`/`unknown`，无 0 占位；无重复 ID、无重复项目；disk 拆分（程序/依赖/模型）与总量一致；软件许可证与模型许可证严格区分；软件免费 ≠ 模型免费，开源 ≠ 可商用。
- **链接有效性**：各项目链接由研究代理在采集时逐项交叉验证；因无法实时批量复测，采集期质量报告中 `dead_link_count` 计为 0 并注明该限制。
- **37 条记录缺官网或 GitHub**（如部分 Pinokio 封装类应用无独立仓库），已如实置 `null`。

## 字段说明（35 字段）

`id` 唯一标识（`p-<分类>-<序号>`）｜ `name` / `name_zh` 名称（中文名）｜ `category` / `subcategory` 一/二级分类｜ `description` 中文介绍（80～180 字原创）｜ `features` 功能列表｜ `website` / `github` 官网与源码｜ `pinokio_url` Pinokio 脚本地址｜ `install_type` 安装方式（official 官方脚本 / community 社区脚本 / custom 可自行编写 / manual 手动安装 / not-supported 不支持本地部署 / unknown 待验证）｜ `status` 维护状态｜ `rating` 评级（S/A/B/C）｜ `stars` GitHub Star（估算值）｜ `ram_min_gb` / `ram_recommended_gb` 内存｜ `vram_min_gb` / `vram_recommended_gb` 显存｜ `disk_app_gb` / `disk_dependencies_gb` / `disk_model_gb` / `disk_total_gb` 硬盘占用拆分｜ `download_gb` 首次下载量估算｜ `gpu_support` GPU 支持（nvidia/amd/apple-silicon/intel/cpu-only）｜ `platforms` 平台｜ `pricing_type` 收费类型｜ `software_license` / `model_license` 软件与模型许可证｜ `commercial_use` 商业使用｜ `difficulty` 难度｜ `last_updated` 最近更新｜ `verified_date` 验证日期｜ `sources` 信息来源｜ `data_confidence` 数据置信度｜ `notes` 备注（估算依据、价格查询日期、兼容性说明等）

## 数据更新流程

1. 数据全部内嵌于 `index.html` 的 `window.EMBEDDED_DATA`（343 条项目 + 分类 + 标签）；如需更新，先自该对象提取现有数据（或用项目根 `.backup_kisstr_*` 备份目录中的 `projects.json` 副本作为母本），编辑后再生成新的内嵌数据快照。
2. 原独立数据文件（`projects.json` / `categories.json` / `tags.json` / `quality_report.json`）已于 2026-10-10 移除，仅存于项目根 `.backup_kisstr_*` 备份目录。

## 网站功能

- 专业软件目录风格（2026-10-04 去 AI 味重构 + 功能修复）：单列紧凑列表 + 项目编号 + 弱化元数据，无玻璃拟态 / 发光 / 胶囊 / Emoji
- Browse 快捷视图：全部 / 热门（S+A）/ 顶级（S）/ 最新更新 / 免费 / 开源 / 官方 Pinokio / 轻量（RAM≤8GB）/ 编辑推荐，计数全部动态计算
- 全局搜索（快捷键 `/`，实时过滤，匹配英文名 / 中文名 / 描述 / 分类 / 功能 / 许可 / 备注）、16 个分类导航（计数按数据动态聚合）
- 多条件组合筛选（AND）：RAM / VRAM / 硬盘 / GPU / 收费 / 平台 / 安装方式；顶部显示「已应用 N 个筛选条件」并可一键清除
- 排序：默认 / Stars / 最近更新 / 名称 A-Z / 硬盘 / 显存 / 内存 / 评级
- 项目详情右侧抽屉（35 字段分区块）、深链复制（`index.html#p-<id>`）；无链接字段显示「暂无链接」，外链 target=_blank + rel=noopener noreferrer
- 行内快捷收藏 ★、收藏 / 已安装标记、深浅色主题、列表 / 紧凑 / 网格视图 —— 全部 localStorage 持久化
- 硬件适配雷达、硬盘空间计算器、项目对比（最多 4 个，选满后其余禁用）
- 空状态「没有找到匹配项目」+ 清除筛选；数据缺失时显示加载失败提示并输出 console.error
- 键盘可达：Tab 聚焦 / Enter 触发导航 / Esc 关闭抽屉与弹窗
- 响应式布局（桌面侧栏+列表 / 平板侧栏收起 / 手机汉堡菜单+单栏）
- 交互验收：原 `pinokio-audit.html` 自动化测试矩阵（45 项）已于 2026-10-10 移除，功能经开发期验证。

## 免责声明

- 所有项目、链接、许可证、硬件与收费信息以官方来源为准，本目录仅作聚合与索引；数据可能随上游项目变动而过时。
- 硬件参数多为基于官方文档/模型卡的估算，实际以你的设备实测为准；模型体积随版本与量化方式变化。
- 收费信息（freemium/paid 的具体价格）仅在官方页面有证据时记录于 notes，并注明币种/周期/查询日期。
- 本目录为信息整理用途，不构成任何安装、购买或使用建议。
