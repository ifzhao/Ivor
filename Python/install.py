import os

# 定义依赖包的文本文件路径
requirements_file = "bkg.txt"

# 安装依赖包
os.system(f"pip install -r {requirements_file}")
