import json
from pathlib import Path
from typing import Dict, Any


BASE_DIR = Path(__file__).resolve().parent


def load_schema() -> Dict[str, Any]:
    schema_path = BASE_DIR / "plush_pattern_schema.json"
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_pattern_prompt(schema: Dict[str, Any]) -> str:
    toy = schema["toy_profile"]
    parts = schema["pattern_parts"]
    embroidery = schema["embroidery_points"]

    parts_text = "\n".join(
        f"- {p['part_name']}：数量{p['quantity']}，材质{p['material']}，缝份{p['seam_allowance_mm']}mm，说明：{p['notes']}"
        for p in parts
    )
    embroidery_text = "\n".join(f"- {item}" for item in embroidery)

    return f"""
你是一位有15年以上经验的毛绒玩具工业开版师傅。

请根据上传的毛绒玩具图片，生成一张可落地打样的完整毛绒玩具拆分纸样图。

产品信息：
- 名称：{toy['name']}
- 目标高度：{toy['target_height_cm']}cm
- 风格：{'、'.join(toy['style'])}
- 面料：{toy['fabric']}
- 填充：{toy['filling']}

必须输出：
1. 正面图
2. 侧面图
3. 背面图
4. 完整纸样拆分
5. 头部纸样
6. 脸部纸样
7. 身体纸样
8. 手臂纸样
9. 腿部纸样
10. 配件纸样
11. 五官刺绣定位图
12. 组装顺序图
13. 制作说明

纸样拆片要求：
{parts_text}

刺绣定位要求：
{embroidery_text}

工艺要求：
- 所有纸样必须为闭合曲线。
- 每个裁片需要编号、名称、数量、布纹方向、对位牙口。
- 默认缝份为5mm。
- 左右对称裁片需要标注镜像裁剪。
- 头部必须有中片、侧片、脸颊片、后脑片，不能只做简单圆形。
- 身体必须区分前片、后片、服装覆盖层和配件定位。
- 输出应符合毛绒玩具打样师傅可理解的工业纸样逻辑。
""".strip()


if __name__ == "__main__":
    schema = load_schema()
    prompt = build_pattern_prompt(schema)
    print(prompt)
