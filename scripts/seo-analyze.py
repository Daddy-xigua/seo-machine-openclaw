#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO Machine - 内容分析工具
分析文章的 SEO 质量、关键词密度、可读性等

用法：
    python3 scripts/seo-analyze.py '{"content":"文章内容","primary_keyword":"主关键词"}'
"""

import sys
import json
import re
from datetime import datetime


def calculate_flesch_reading_ease(text: str) -> float:
    """计算 Flesch Reading Ease 可读性分数"""
    # 简化版计算（中文需要特殊处理）
    sentences = len(re.split(r'[。！？.!?]', text))
    words = len(text)  # 中文字符数
    syllables = len(text)  # 中文每个字算一个音节
    
    if sentences == 0 or words == 0:
        return 0.0
    
    # 中文调整公式
    score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return max(0, min(100, score))


def analyze_seo(content: str, primary_keyword: str = "") -> dict:
    """
    分析内容的 SEO 质量
    
    Args:
        content: 文章内容
        primary_keyword: 主关键词
    
    Returns:
        分析报告字典
    """
    
    # 基础统计
    char_count = len(content)
    word_count = len(content)  # 中文按字符算
    
    # 标题分析
    h1_match = re.findall(r'^#\s+(.+)$', content, re.MULTILINE)
    h2_matches = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    h3_matches = re.findall(r'^###\s+(.+)$', content, re.MULTILINE)
    
    # 关键词密度
    keyword_count = content.count(primary_keyword) if primary_keyword else 0
    keyword_density = (keyword_count / word_count * 100) if word_count > 0 else 0
    
    # 段落分析
    paragraphs = re.split(r'\n\s*\n', content)
    avg_paragraph_length = sum(len(p) for p in paragraphs) / len(paragraphs) if paragraphs else 0
    
    # 链接分析
    internal_links = len(re.findall(r'\[([^\]]+)\]\((/[^)]+)\)', content))
    external_links = len(re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', content))
    
    # 列表分析
    unordered_lists = len(re.findall(r'^\s*[-*]\s+', content, re.MULTILINE))
    ordered_lists = len(re.findall(r'^\s*\d+\.\s+', content, re.MULTILINE))
    
    # Meta 元素检查
    has_key_takeaways = '> **Key Takeaways**' in content or '> **核心要点**' in content
    has_introduction = '引言' in content[:500] or '介绍' in content[:500]
    has_conclusion = '结论' in content[-500:] or '总结' in content[-500:]
    
    # 可读性
    reading_ease = calculate_flesch_reading_ease(content)
    
    # SEO 评分（0-100）
    seo_score = 0
    
    # 标题结构（20 分）
    if h1_match:
        seo_score += 10
        if primary_keyword and primary_keyword in h1_match[0]:
            seo_score += 10
    
    # H2 标题（15 分）
    if len(h2_matches) >= 4:
        seo_score += 10
        if primary_keyword and any(primary_keyword in h2 for h2 in h2_matches[:3]):
            seo_score += 5
    
    # 关键词密度（15 分）
    if 0.5 <= keyword_density <= 2.5:
        seo_score += 15
    elif 0.3 <= keyword_density < 0.5 or 2.5 < keyword_density <= 3.5:
        seo_score += 8
    
    # 内容长度（15 分）
    if word_count >= 2000:
        seo_score += 15
    elif word_count >= 1500:
        seo_score += 10
    elif word_count >= 1000:
        seo_score += 5
    
    # Key Takeaways（10 分）
    if has_key_takeaways:
        seo_score += 10
    
    # 内链外链（10 分）
    if internal_links >= 3:
        seo_score += 5
    if external_links >= 2:
        seo_score += 5
    
    # 段落结构（10 分）
    if 50 <= avg_paragraph_length <= 200:
        seo_score += 10
    elif 30 <= avg_paragraph_length < 50 or 200 < avg_paragraph_length <= 300:
        seo_score += 5
    
    # 列表使用（5 分）
    if unordered_lists + ordered_lists >= 3:
        seo_score += 5
    
    # 结论（10 分）
    if has_conclusion:
        seo_score += 10
    
    report = {
        "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content_stats": {
            "character_count": char_count,
            "word_count": word_count,
            "estimated_read_time_minutes": round(word_count / 500, 1)
        },
        "structure": {
            "h1_count": len(h1_match),
            "h1_title": h1_match[0] if h1_match else None,
            "h2_count": len(h2_matches),
            "h2_titles": h2_matches,
            "h3_count": len(h3_matches),
            "heading_hierarchy_valid": len(h1_match) == 1 and len(h2_matches) >= 3
        },
        "keyword_analysis": {
            "primary_keyword": primary_keyword,
            "keyword_count": keyword_count,
            "keyword_density_percent": round(keyword_density, 2),
            "keyword_in_h1": primary_keyword in h1_match[0] if h1_match and primary_keyword else False,
            "keyword_in_h2": [h2 for h2 in h2_matches if primary_keyword in h2] if primary_keyword else [],
            "keyword_distribution": "良好" if 0.5 <= keyword_density <= 2.5 else "需优化"
        },
        "link_analysis": {
            "internal_links": internal_links,
            "external_links": external_links,
            "total_links": internal_links + external_links,
            "recommendation": "建议添加更多内链" if internal_links < 3 else "内链数量合适"
        },
        "readability": {
            "flesch_reading_ease": round(reading_ease, 1),
            "avg_paragraph_length": round(avg_paragraph_length, 0),
            "paragraph_count": len(paragraphs),
            "list_count": unordered_lists + ordered_lists
        },
        "seo_elements": {
            "has_key_takeaways": has_key_takeaways,
            "has_introduction": has_introduction,
            "has_conclusion": has_conclusion,
            "complete_structure": has_key_takeaways and has_introduction and has_conclusion
        },
        "seo_score": {
            "total": seo_score,
            "max": 100,
            "rating": "优秀" if seo_score >= 85 else "良好" if seo_score >= 70 else "需优化" if seo_score >= 50 else "差"
        },
        "recommendations": generate_recommendations(
            seo_score, h1_match, h2_matches, keyword_density, 
            internal_links, external_links, has_key_takeaways, has_conclusion
        )
    }
    
    return report


def generate_recommendations(seo_score, h1, h2, keyword_density, internal_links, 
                           external_links, has_takeaways, has_conclusion) -> list:
    """生成优化建议"""
    recommendations = []
    
    if seo_score < 70:
        recommendations.append("【优先】完善文章结构：确保有引言、Key Takeaways 和结论")
    
    if not h1:
        recommendations.append("【优先】添加 H1 标题，并包含主关键词")
    
    if len(h2) < 4:
        recommendations.append("【优先】增加 H2 章节，建议至少 4-6 个主要部分")
    
    if keyword_density < 0.5:
        recommendations.append("【优化】适当增加主关键词出现频率（当前密度偏低）")
    elif keyword_density > 2.5:
        recommendations.append("【优化】减少主关键词使用频率（当前密度偏高，有关键词堆砌风险）")
    
    if internal_links < 3:
        recommendations.append("【优化】添加更多内链（建议 3-5 个相关页面）")
    
    if external_links < 2:
        recommendations.append("【优化】添加权威外链引用（建议 2-3 个）")
    
    if not has_takeaways:
        recommendations.append("【优化】在引言后添加 Key Takeaways 模块")
    
    if not has_conclusion:
        recommendations.append("【优化】添加结论部分，总结要点并给出行动号召")
    
    return recommendations


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "缺少参数",
            "usage": "python3 seo-analyze.py '{\"content\":\"文章内容\",\"primary_keyword\":\"主关键词\"}'"
        }, ensure_ascii=False))
        sys.exit(1)
    
    try:
        params = json.loads(sys.argv[1])
        content = params.get("content", "")
        primary_keyword = params.get("primary_keyword", "")
        
        if not content:
            print(json.dumps({"error": "content 参数不能为空"}, ensure_ascii=False))
            sys.exit(1)
        
        result = analyze_seo(content, primary_keyword)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON 解析错误：{str(e)}"}, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"执行错误：{str(e)}"}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
