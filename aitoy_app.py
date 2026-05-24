"""
AIToy PlushLab 总入口

功能：
1. 调用毛绒玩具AI开版提示词模块
2. 调用淘宝自动上架参数生成模块
3. 执行风险检测
4. 输出 DRY_RUN 预览

运行方式：
python aitoy_app.py
"""

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TAOBAO_DIR = ROOT / "aitoy-taobao-auto-listing"
PATTERN_DIR = ROOT / "aitoy-plush-pattern"


def run_python(script_path: Path) -> str:
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(script_path.parent),
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout


def main() -> None:
    print("==============================")
    print("AIToy PlushLab 一键流程预览")
    print("==============================")

    print("\n[1/2] 生成毛绒玩具工业开版提示词...\n")
    pattern_output = run_python(PATTERN_DIR / "pattern_prompt_builder.py")
    print(pattern_output)

    print("\n[2/2] 生成淘宝自动上架参数 DRY_RUN 预览...\n")
    taobao_output = run_python(TAOBAO_DIR / "src" / "main.py")
    print(taobao_output)

    print("\nAIToy 流程完成。当前为预览模式，不会真实发布商品。")


if __name__ == "__main__":
    main()
