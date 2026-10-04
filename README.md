# Kisstr

书影音 · 优质网站收藏导航站 — 63 个分类支页 + 首页 + 免责声明，纯静态、零构建，部署于 Cloudflare Workers。

官网：<https://kisstr.com>

## 技术栈

| 项       | 说明                                  |
| -------- | ------------------------------------- |
| 语言     | 原生 HTML / CSS / JavaScript          |
| 部署     | Cloudflare Workers Static Assets      |
| 构建     | 无（零构建，开箱即用）                |
| 统计     | Umami（轻量脚本）                     |
| 资源     | 本地静态资源，无 CDN 依赖             |

## 特性

- **65 个页面**：首页 + 63 个分类导航支页（AI / 学术资料 / 大学公开课 / 设计 / 时尚 / 书影音 / 小游戏 / 独立开发者 / 电台 / 复古网络 / vibe coding 等）+ 免责声明
- **2 种布局**：Minimal（清晰） / Magazine（杂志）
- **54 张单字名壁纸**（`01_星.webp` ~ `54_黛.webp`，2560×1440 WebP + 300×169 缩略图；默认从「荷 / 墨 / 锦 / 庭 / 契」五张中随机）；14 个纯色主题数据保留（当前隐藏，仅显示壁纸背景）
- **内置 lofi 电台播放**
- 无广告 · 无弹窗 · 无盈利

## 快速开始

```bash
# 本地预览
npx serve site

# 部署至 Cloudflare
npx wrangler deploy
```

## 目录结构

```text
site/                  # 部署根目录（wrangler assets.directory = "site"）
├── index.html         # 首页
├── *.html             # 63 个分类支页 + disclaimer.html
├── wallpapers/        # 壁纸主图（54 张，2560×1440）
└── thumbs/            # 壁纸缩略图（54 张，300×169）

docs/                  # 开发档案（开发档案.md）
README.md              # 本文件（根目录）
wrangler.jsonc         # Cloudflare 部署配置
```

## 壁纸与背景机制

- 每个页面内嵌 `imageBackgrounds` 数组（`id / name / url / thumb` 四字段），运行时经 `anime_wallpapers/ → wallpapers/`、`.jpg → .webp` 路径改写后作为页面背景。
- 背景选择器当前**仅展示壁纸**（`pureBackgrounds` 14 个纯色主题已注释渲染、数据保留，取消注释即可恢复）。
- 无用户选择时默认从「荷 / 墨 / 锦 / 庭 / 契」中随机一张（默认池壁纸位于数组前端，竹晨之后）；用户选择保存在 `localStorage`（`kisstr_background_picker_selection_v1`）。
- 壁纸按 `NN_单字.webp` 命名（编号 01 起连续，单字意象名），素材经 cover 居中裁切（个别按需求填充拉伸）生成。

## 免责声明

站内链接整理自网络，仅供学习交流，请遵守相关法律法规。详见 [disclaimer.html](https://kisstr.com/disclaimer.html)。
