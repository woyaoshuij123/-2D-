from typing import Any, Dict


def build_taobao_product(raw: Dict[str, Any], settings) -> Dict[str, Any]:
    name = raw.get("product_name", "国风毛绒玩具")
    size = raw.get("size", "20cm")
    material = raw.get("material", "短毛绒 + PP棉")
    price = raw.get("price", "89.00")
    stock = int(raw.get("stock", 100))
    style = raw.get("style", "国风 / Q版 / 软萌")
    package = raw.get("package", "OPP袋")

    title = raw.get("title") or f"{name} Q版公仔 古风棉花娃娃 生日礼物 桌面摆件"
    description = raw.get("description") or (
        f"{name}，采用{material}，尺寸约{size}。整体为{style}风格，"
        "适合作为生日礼物、桌面摆件、拍照道具和收藏玩偶。"
        f"包装方式：{package}。建议局部擦洗，避免机洗损坏装饰件。"
    )

    return {
        "title": title[:60],
        "cid": raw.get("cid", settings.default_category_id),
        "price": price,
        "num": stock,
        "location_state": raw.get("location_state", settings.default_state),
        "location_city": raw.get("location_city", settings.default_city),
        "description": description,
        "props": raw.get("props", ""),
        "outer_id": raw.get("outer_id", "AITOY-PLUSH-001"),
        "skus": raw.get("skus", [])
    }
