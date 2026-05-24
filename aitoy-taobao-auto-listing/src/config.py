import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    taobao_app_key: str
    taobao_app_secret: str
    taobao_session_key: str
    taobao_gateway: str
    default_state: str
    default_city: str
    default_category_id: str
    default_shipping_template_id: str
    dry_run: bool = True


def get_settings() -> Settings:
    return Settings(
        taobao_app_key=os.getenv("TAOBAO_APP_KEY", ""),
        taobao_app_secret=os.getenv("TAOBAO_APP_SECRET", ""),
        taobao_session_key=os.getenv("TAOBAO_SESSION_KEY", ""),
        taobao_gateway=os.getenv("TAOBAO_GATEWAY", "https://eco.taobao.com/router/rest"),
        default_state=os.getenv("DEFAULT_STATE", "浙江"),
        default_city=os.getenv("DEFAULT_CITY", "金华"),
        default_category_id=os.getenv("DEFAULT_CATEGORY_ID", ""),
        default_shipping_template_id=os.getenv("DEFAULT_SHIPPING_TEMPLATE_ID", "0"),
        dry_run=os.getenv("DRY_RUN", "true").lower() in {"1", "true", "yes", "y"},
    )
