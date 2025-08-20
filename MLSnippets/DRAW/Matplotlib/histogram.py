# 直方图：histogram.py
import numpy as np
import matplotlib.pyplot as plt
from self_mpl_config import setup_matplotlib_config

setup_matplotlib_config()

# 1. 创建figure实例 (找对象：画板)
fig = plt.figure(figsize=(8, 5), dpi=100)

# 2. 在figure上创建axes (找对象：坐标纸)
ax = fig.add_subplot(111)

# 准备数据
np.random.seed(42)  # 保证每次运行结果一致
data = np.random.randn(1000)  # 生成1000个符合正态分布的随机数

# 画直方图
ax.hist(data, bins=30, color='#9ecae1', edgecolor='black')

# 添加标题和标签
ax.set_title('直方图示例')
ax.set_xlabel('数值范围')
ax.set_ylabel('频数')

# 添加网格
ax.grid(True)

# 最终展示
plt.show()