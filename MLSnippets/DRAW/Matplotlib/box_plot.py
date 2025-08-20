# 箱线图：box_plot.py
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
data1 = np.random.normal(0, 1, 100)  # 均值0，标准差1，100个数据点
data2 = np.random.normal(1, 1.5, 100)  # 均值1，标准差1.5，100个数据点
data3 = np.random.normal(-1, 0.8, 100)  # 均值-1，标准差0.8，100个数据点
data = [data1, data2, data3]  # 将三组数据放入列表

# 画箱线图
ax.boxplot(data, patch_artist=True, labels=['组1', '组2', '组3'])

# 添加标题和标签
ax.set_title('箱线图示例')
ax.set_xlabel('数据组')
ax.set_ylabel('数值')

# 添加网格
ax.grid(True)

# 最终展示
plt.show()