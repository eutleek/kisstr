# Kisstr

书影音 · 优质网站收藏导航站。纯静态页面，无需构建，开箱即用。

官网：[kisstr.com](https://kisstr.com)

## 特性

- 无广告、无弹窗、无盈利
- 支持主题、布局（清晰/杂志）、背景壁纸切换
- 分类清晰：书籍、影视、音乐、AI、设计、ACG 等 45+ 主题页

## 目录结构

```
├── index.html             # 首页（书影音）
├── *.html                 # 各分类导航页（ai、design_architecture、manga_sites 等）
├── disclaimer.html        # 免责声明
├── wallpapers_webp/       # 壁纸资源
├── wrangler.jsonc         # Cloudflare 部署配置
└── robots.txt
```

## 本地预览

直接用浏览器打开 `index.html` 即可，或起一个本地静态服务器：

```bash
npx serve .
```

## 部署

基于 Cloudflare Workers/Pages，使用 Wrangler：

```bash
npx wrangler deploy
```

## 免责声明

站点内链接均来自网络整理，仅供学习交流，请遵守相关法律法规。详见 [disclaimer.html](disclaimer.html)。
