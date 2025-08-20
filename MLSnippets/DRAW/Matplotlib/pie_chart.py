# 饼图：pie_chart.py
import numpy as np
import matplotlib.pyplot as plt
from self_mpl_config import setup_matplotlib_config

setup_matplotlib_config()

# 1. 创建figure实例（画板）
fig = plt.figure(figsize=(8, 5), dpi=100)

# 2. 在figure上创建axes（坐标纸）
ax = fig.add_subplot(111)

# 准备数据
labels = ['分类A', '分类B', '分类C', '分类D', '分类E']  # 标签
sizes = np.random.randint(10, 100, size=5)  # 随机生成每个分类的值
colors = ["#a8ddb5", "#fdbb84", "#c994c7", "#bdbdbd", "#7fcdbb"]

# 画饼图
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# 添加标题
ax.set_title('饼图示例')

# 保证饼图是正圆
ax.axis('equal')

# 最终展示
plt.show()