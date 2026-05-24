import hashlib
import time
from typing import Any, Dict

import requests


class TaobaoClient:
    def __init__(self, app_key: str, app_secret: str, session_key: str, gateway: str):
        self.app_key = app_key
        self.app_secret = app_secret
        self.session_key = session_key
        self.gateway = gateway

    def sign(self, params: Dict[str, Any]) -> str:
        sorted_items = sorted(params.items(), key=lambda item: item[0])
        raw = self.app_secret
        for key, value in sorted_items:
            if value is not None and key != "sign":
                raw += f"{key}{value}"
        raw += self.app_secret
        return hashlib.md5(raw.encode("utf-8")).hexdigest().upper()

    def request(self, method: str, biz_params: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
        common_params = {
            "method": method,
            "app_key": self.app_key,
            "session": self.session_key,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "format": "json",
            "v": "2.0",
            "sign_method": "md5",
        }
        params = {**common_params, **biz_params}
        params["sign"] = self.sign(params)

        if dry_run:
            return {
                "dry_run": True,
                "method": method,
                "params_preview": {k: ("***" if k in {"session", "sign"} else v) for k, v in params.items()},
                "message": "DRY_RUN=true，未真实请求淘宝接口。"
            }

        response = requests.post(self.gateway, data=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def create_item(self, product: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
        biz_params = {
            "title": product["title"],
            "cid": product["cid"],
            "price": product["price"],
            "num": product["num"],
            "type": "fixed",
            "stuff_status": "new",
            "location.state": product["location_state"],
            "location.city": product["location_city"],
            "desc": product["description"],
            "props": product.get("props", ""),
            "outer_id": product.get("outer_id", ""),
        }
        return self.request("taobao.item.add", biz_params, dry_run=dry_run)
