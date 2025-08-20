# 散点图：scatter_plot.py
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
x = np.random.rand(50) * 10  # 50个0到10之间的随机数
y = np.random.rand(50) * 10  # 50个0到10之间的随机数
colors = np.random.rand(50)  # 每个点的颜色
sizes = 100 * np.random.rand(50)  # 每个点的大小

# 画散点图
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

# 添加标题和标签
ax.set_title('随机散点图示例')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')

# 添加颜色条
plt.colorbar(scatter, label='颜色值')

# 添加网格
ax.grid(True)

# 最终展示
plt.show()