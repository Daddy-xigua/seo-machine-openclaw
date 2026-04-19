# SEO Machine for OpenClaw

🚀 专业的 SEO 内容创作技能，基于 [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) 转换为 OpenClaw 格式。

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)]()

---

## ✨ 功能特性

- 🔍 **关键词研究** - 全面的 SEO 关键词和竞争分析
- ✍️ **内容创作** - 2000-3000+ 字 SEO 优化长文
- 📊 **SEO 审计** - 内容质量评分（0-100）和优化建议
- 🔗 **链接策略** - 内链外链智能建议
- 📝 **Meta 生成** - 自动创建标题/描述/关键词
- 🚀 **WordPress 发布** - 一键发布（可选配置）

---

## 📦 安装

### 方法 1：从 ClawHub 安装

```bash
openclaw skills install seo-machine
```

### 方法 2：手动安装

```bash
# 克隆到 skills 目录
cd ~/.openclaw/workspace/skills
git clone https://github.com/YOUR_USERNAME/seo-machine-openclaw.git seo-machine

# 添加技能配置
# 在 openclaw.json 中添加技能引用
```

### 方法 3：从 GitHub Releases 下载

```bash
# 下载最新版本
curl -L https://github.com/YOUR_USERNAME/seo-machine-openclaw/releases/latest/download/seo-machine.tar.gz \
  | tar -xz -C ~/.openclaw/workspace/skills/
```

---

## 🚀 快速开始

### 1️⃣ 关键词研究

```bash
python3 ~/.openclaw/workspace/skills/seo-machine/scripts/seo-research.py \
  '{"query":"数据中心液冷技术","industry":"数据中心"}'
```

### 2️⃣ 撰写文章

在 OpenClaw 中使用：

```
seo write 数据中心液冷技术
```

### 3️⃣ 分析优化

```bash
python3 ~/.openclaw/workspace/skills/seo-machine/scripts/seo-analyze.py \
  '{"content":"文章内容...","primary_keyword":"数据中心液冷"}'
```

---

## 📖 命令参考

### 核心命令

| 命令 | 描述 | 示例 |
|------|------|------|
| `seo research [主题]` | 关键词研究 | `seo research B2B 内容营销` |
| `seo write [主题]` | 撰写文章 | `seo write 液冷技术` |
| `seo optimize [文件]` | SEO 优化 | `seo optimize drafts/article.md` |
| `seo analyze [URL/文件]` | 内容分析 | `seo analyze https://...` |
| `seo rewrite [主题]` | 重写更新 | `seo rewrite 营销指南` |

### 研究命令

| 命令 | 描述 |
|------|------|
| `seo serp [关键词]` | SERP 分析 |
| `seo gaps` | 内容差距分析 |
| `seo trending` | 热门主题 |
| `seo topics` | 主题集群 |

---

## 📁 目录结构

```
seo-machine/
├── SKILL.md              # 技能定义
├── README.md             # 本文档
├── scripts/
│   ├── seo-research.py   # 关键词研究
│   ├── seo-analyze.py    # 内容分析
│   └── seo-optimize.py   # SEO 优化（开发中）
├── context/              # 上下文模板（可选）
│   ├── brand-voice.md
│   ├── style-guide.md
│   └── seo-guidelines.md
└── examples/             # 示例输出
    └── sample-research.md
```

---

## 🔧 配置（可选）

### 上下文文件

创建 `~/.openclaw/workspace/skills/seo-machine/context/` 目录，添加以下文件：

- `brand-voice.md` - 品牌语调
- `style-guide.md` - 写作规范
- `seo-guidelines.md` - SEO 规则
- `internal-links-map.md` - 内链映射
- `target-keywords.md` - 目标关键词

### API 集成（可选）

编辑 `~/.openclaw/workspace/.config/seo-machine.json`：

```json
{
  "dataforseo": {
    "login": "your_login",
    "password": "your_password"
  },
  "wordpress": {
    "url": "https://yoursite.com",
    "username": "your_username",
    "app_password": "your_app_password"
  }
}
```

---

## 📊 SEO 评分标准

| 分数 | 等级 | 说明 |
|------|------|------|
| 85-100 | 优秀 | 可直接发布 |
| 70-84 | 良好 | 少量优化后发布 |
| 50-69 | 需优化 | 需要中等程度修改 |
| 0-49 | 差 | 需要大量重写 |

### 评分维度

- 标题结构（20 分）
- H2 章节（15 分）
- 关键词密度（15 分）
- 内容长度（15 分）
- Key Takeaways（10 分）
- 内链外链（10 分）
- 段落结构（10 分）
- 列表使用（5 分）
- 结论（10 分）

---

## 🎯 最佳实践

### 文章结构

```markdown
# H1: 包含主关键词的标题

> **Key Takeaways**
> - 核心发现 #1
> - 核心发现 #2
> - 核心发现 #3

## 引言
- 直接回答问题（AI 搜索优化）
- Hook 钩子
- 价值主张

## H2: 主体部分 1
## H2: 主体部分 2
...

## 结论
- 总结要点
- 行动号召
```

### 关键词优化

- 密度：1-2%（自然分布）
- 位置：H1、前 100 字、2-3 个 H2、结论
- 变体：使用同义词和长尾词

---

## 🤝 贡献

欢迎贡献！请参考以下步骤：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

---

## 📄 许可证

MIT License - 与原 [seomachine](https://github.com/TheCraigHewitt/seomachine) 项目保持一致

---

## 🙏 致谢

- 原始项目：[TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) by Craig Hewitt
- OpenClaw 框架：[openclaw/openclaw](https://github.com/openclaw/openclaw)

---

## 📬 联系方式

- GitHub Issues: [提交问题](https://github.com/YOUR_USERNAME/seo-machine-openclaw/issues)
- 邮箱：your@email.com

---

**Made with ❤️ for OpenClaw Community**
