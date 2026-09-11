# Kisstr

书影音 · 优质网站收藏导航站 — 46 个分类页，纯静态、零构建，部署于 Cloudflare Workers。

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

- 46 个分类导航页（AI / ACGN / 设计 / 时尚 / 书影音等）
- 13 种主题色 · 2 种布局（清晰 / 杂志）· 43 张壁纸背景
- 内置 lofi 电台播放
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
├── *.html             # 46 个分类页
├── disclaimer.html    # 免责声明
├── wallpapers_webp/   # 壁纸资源
└── robots.txt

wrangler.jsonc         # Cloudflare 部署配置
README.md
```

## 免责声明

站内链接整理自网络，仅供学习交流，请遵守相关法律法规。详见 [disclaimer.html](https://kisstr.com/disclaimer.html)。
