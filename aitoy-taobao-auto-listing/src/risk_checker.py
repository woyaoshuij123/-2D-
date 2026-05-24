from typing import Dict, List


HIGH_RISK_WORDS = [
    "官方正版", "授权正品", "明星同款", "原版", "迪士尼", "漫威", "宝可梦",
    "冰河世纪", "维斯塔潘", "F1", "奥特曼", "哈利波特", "三丽鸥"
]

LIMIT_WORDS = ["最", "第一", "顶级", "全网最低", "永久", "100%"]


def scan_text(text: str, words: List[str]) -> List[str]:
    return [word for word in words if word and word in text]


def check_product_risk(product: Dict) -> Dict:
    title = product.get("title", "")
    description = product.get("description", "")
    text = f"{title}\n{description}"

    high_hits = scan_text(text, HIGH_RISK_WORDS)
    limit_hits = scan_text(text, LIMIT_WORDS)

    return {
        "passed": not high_hits,
        "high_risk_words": high_hits,
        "limit_words": limit_hits,
        "suggestion": "通过" if not high_hits else "发现高风险词，建议改成通用描述后再上架"
    }
