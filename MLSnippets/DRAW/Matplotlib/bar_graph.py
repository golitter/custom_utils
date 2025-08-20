# 柱状图：bar_graph.py
import numpy as np
import matplotlib.pyplot as plt
from self_mpl_config import setup_matplotlib_config

setup_matplotlib_config()

# 1. 创建figure实例 (找对象：画板)
fig = plt.figure(figsize=(8, 5), dpi=100)

# 2. 在figure上创建axes (找对象：坐标纸)
ax = fig.add_subplot(111)

# 准备数据
categories = ['分类A', '分类B', '分类C', '分类D', '分类E']  # 类别
values = np.random.randint(10, 100, size=5)  # 随机生成每个类别的值
colors = ["#a8ddb5", "#fdbb84", "#c994c7", "#bdbdbd", "#7fcdbb"]

# 画柱状图
bars = ax.bar(categories, values, color=colors)

# 添加标题和标签
ax.set_title('柱状图示例')
ax.set_xlabel('分类')
ax.set_ylabel('值')

# 添加数值标签
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # va: vertical alignment

# 添加网格
ax.grid(True)

# 最终展示
plt.show()