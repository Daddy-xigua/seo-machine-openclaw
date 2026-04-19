# SEO Machine Skill for OpenClaw

## 技能概述

**SEO Machine** 是一个专业的 SEO 内容创作技能，基于 Claude Code 的 seomachine 项目转换为 OpenClaw 格式。

**用途：** 创建、优化和发布 SEO 优化的长文博客内容

**核心功能：**
- 🔍 关键词研究和竞争分析
- ✍️ 2000-3000+ 字 SEO 文章创作
- 📊 内容优化和 SEO 审计
- 🔗 内链外链策略
- 📝 Meta 元素生成
- 🚀 WordPress 发布（可选）

---

## 命令列表

### 核心命令

| 命令 | 描述 | 输出 |
|------|------|------|
| `seo research [主题]` | 关键词和竞争分析 | `research/` 目录中的研究简报 |
| `seo write [主题]` | 创建完整的 SEO 文章 | `drafts/` 目录中的文章 |
| `seo optimize [文件]` | 最终 SEO 优化审计 | 优化报告和评分 |
| `seo analyze [URL 或文件]` | 分析现有内容 | 内容健康度报告 |
| `seo rewrite [主题]` | 更新/重写现有内容 | `rewrites/` 目录中的更新版本 |

### 研究命令

| 命令 | 描述 |
|------|------|
| `seo serp [关键词]` | SERP 分析 |
| `seo gaps` | 竞争内容差距分析 |
| `seo trending` | 热门主题机会 |
| `seo topics` | 主题集群研究 |

### 落地页命令

| 命令 | 描述 |
|------|------|
| `seo landing-write [主题]` | 创建转化优化的落地页 |
| `seo landing-audit [文件]` | 落地页 CRO 审计 |
| `seo landing-research [主题]` | 竞争定位研究 |

---

## 使用方法

### 1️⃣ 关键词研究

```
seo research [主题]
```

**示例：**
```
seo research B2B SaaS 内容营销策略
```

**输出内容：**
- 主关键词（搜索量、难度）
- 3-5 个次要关键词
- 前 10 名 SERP 竞争分析
- 内容差距和机会
- 推荐大纲结构
- 内链外链策略

---

### 2️⃣ 撰写文章

```
seo write [主题或研究简报]
```

**示例：**
```
seo write B2B SaaS 内容营销策略
```

**自动触发 Agent：**
- SEO 优化器
- Meta 创建器
- 内链建议器
- 关键词映射器

**文章特点：**
- 2000-3000+ 字
- H1/H2/H3 结构完整
- 关键词自然分布（1-2% 密度）
- 包含 Key Takeaways 模块
- Meta 标题/描述/关键词

---

### 3️⃣ 优化文章

```
seo optimize [文章文件]
```

**示例：**
```
seo optimize drafts/内容营销策略 -2026.md
```

**输出：**
- SEO 评分（0-100）
- 优先修复项
- 快速优化建议
- Meta 元素选项
- 发布就绪评估

---

### 4️⃣ 分析现有内容

```
seo analyze [URL 或文件路径]
```

**示例：**
```
seo analyze https://yoursite.com/blog/marketing-guide
seo analyze published/marketing-guide-2024.md
```

**输出：**
- 内容健康度评分（0-100）
- 快速优化机会
- 战略性改进建议
- 重写优先级和范围

---

## Agent 列表

SEO Machine 包含以下专业 Agent：

| Agent | 职责 |
|-------|------|
| **content-analyzer** | 内容综合分析（搜索意图、关键词密度、可读性） |
| **seo-optimizer** | 页面 SEO 优化建议 |
| **meta-creator** | 生成 Meta 标题/描述选项 |
| **internal-linker** | 内链策略和具体建议 |
| **keyword-mapper** | 关键词位置和密度分析 |
| **editor** | 内容编辑和润色 |
| **headline-generator** | 标题生成和优化 |
| **cro-analyst** | 转化率优化分析 |
| **performance** | 性能数据分析 |
| **cluster-strategist** | 主题集群策略 |

---

## 上下文文件

在使用 SEO Machine 前，建议准备以下上下文文件（可选但推荐）：

| 文件 | 描述 |
|------|------|
| `brand-voice.md` | 品牌语调和消息传达 |
| `style-guide.md` | 格式和语法规范 |
| `seo-guidelines.md` | 关键词和结构规则 |
| `internal-links-map.md` | 关键页面内链映射 |
| `features.md` | 产品/服务特性 |
| `competitor-analysis.md` | 竞争情报 |
| `target-keywords.md` | 目标关键词列表 |
| `writing-examples.md` | 写作示例（3-5 篇） |

---

## SEO 最佳实践

### 文章结构

```markdown
# H1: 包含主关键词的标题（<60 字符）

> **Key Takeaways**
> - 核心发现 #1
> - 核心发现 #2
> - 核心发现 #3

## 引言（150-250 字）
- 直接回答问题（AI 搜索优化）
- Hook 钩子
- 价值主张

## H2: 主体部分 1
## H2: 主体部分 2
## H2: 主体部分 3
...

## 结论
- 关键要点总结
- 行动号召
```

### 关键词优化

- **密度：** 1-2%（自然分布）
- **位置：**
  - H1 标题
  - 前 100 字
  - 2-3 个 H2 标题
  - 结论
  - Meta 元素

### Meta 元素

| 元素 | 长度 | 要求 |
|------|------|------|
| 标题 | 50-60 字符 | 包含主关键词，有吸引力 |
| 描述 | 150-160 字符 | 包含关键词，价值主张，CTA |
| URL Slug | 简洁 | 小写，连字符，含关键词 |

---

## 输出目录结构

```
seo-machine/
├── topics/          # 主题创意
├── research/        # 研究简报
├── drafts/          # 草稿文章
├── review-required/ # 待审核
├── published/       # 已发布
├── rewrites/        # 重写版本
├── landing-pages/   # 落地页
├── audits/          # 审计报告
└── repurposed/      # 改编内容
```

---

## 集成 API（可选）

SEO Machine 支持以下数据集成：

| 服务 | 用途 |
|------|------|
| Google Analytics 4 | 流量和参与数据 |
| Google Search Console | 排名和展示数据 |
| DataForSEO | SERP 位置和关键词指标 |
| WordPress REST API | 内容发布 |

---

## 示例工作流

### 创建新内容

```bash
# 1. 研究
seo research 数据中心液冷技术

# 2. 撰写
seo write 数据中心液冷技术

# 3. 优化
seo optimize drafts/数据中心液冷技术 -2026-04-19.md

# 4. 发布（手动或自动）
# 审核后发布到网站
```

### 更新现有内容

```bash
# 1. 分析
seo analyze published/液冷技术指南 -2024.md

# 2. 重写
seo rewrite 液冷技术指南

# 3. 优化
seo optimize rewrites/液冷技术指南 -rewrite-2026.md
```

---

## 注意事项

1. **上下文定制：** 首次使用时，建议填写品牌语调和 SEO 指南等上下文文件
2. **内容审核：** 所有 AI 生成的内容在发布前需要人工审核
3. **数据准确性：** 统计数据和研究结果需要验证
4. **品牌一致性：** 确保内容符合品牌语调
5. **合规性：** 遵守搜索引擎指南，避免过度优化

---

## 版本信息

- **原始项目：** https://github.com/TheCraigHewitt/seomachine
- **OpenClaw 适配：** 2026-04-19
- **版本：** 1.0.0

---

## 许可证

MIT License - 与原 seomachine 项目保持一致
