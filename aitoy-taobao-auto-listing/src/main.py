import json
from pathlib import Path

from config import get_settings
from listing_builder import build_taobao_product
from risk_checker import check_product_risk
from taobao_client import TaobaoClient


BASE_DIR = Path(__file__).resolve().parent.parent


def load_product_example() -> dict:
    product_path = BASE_DIR / "data" / "product_example.json"
    with product_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    settings = get_settings()
    raw_product = load_product_example()
    product = build_taobao_product(raw_product, settings)

    print("\n=== AIToy 生成的淘宝商品参数 ===")
    print(json.dumps(product, ensure_ascii=False, indent=2))

    risk = check_product_risk(product)
    print("\n=== 风险检测结果 ===")
    print(json.dumps(risk, ensure_ascii=False, indent=2))

    if not risk["passed"]:
        print("\n发现高风险词，已停止上架。请修改标题/详情后重试。")
        return

    if not settings.taobao_app_key or not settings.taobao_app_secret or not settings.taobao_session_key:
        print("\n未填写淘宝 API 配置。当前只完成本地生成和风险检测。")
        return

    client = TaobaoClient(
        app_key=settings.taobao_app_key,
        app_secret=settings.taobao_app_secret,
        session_key=settings.taobao_session_key,
        gateway=settings.taobao_gateway,
    )
    result = client.create_item(product, dry_run=settings.dry_run)

    print("\n=== 淘宝 API 调用结果 ===")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
