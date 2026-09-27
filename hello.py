"""环境自检脚本。

用 .venv 里的解释器运行本文件（命令面板 → Python: Run Python File，或右下角选择解释器后按 Ctrl+F5），
能正常打印出解释器路径且虚拟环境显示"是"，就说明 Python 环境配置成功。
"""

import platform
import sys
from datetime import datetime


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    print("=" * 52)
    print("  Python 环境自检")
    print("=" * 52)
    print(f"  解释器    : {sys.executable}")
    print(f"  Python    : {sys.version.split()[0]}")
    print(f"  虚拟环境  : {'是（正在使用 .venv）' if in_venv else '否（用的是全局解释器）'}")
    print(f"  操作系统  : {platform.system()} {platform.release()}")
    print(f"  当前时间  : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("=" * 52)
    print("  下面做一次冒烟计算：1 到 100 的平方和")
    print(f"  sum(i*i for i in range(1, 101)) = {sum(i * i for i in range(1, 101))}")
    print("=" * 52)


if __name__ == "__main__":
    main()
