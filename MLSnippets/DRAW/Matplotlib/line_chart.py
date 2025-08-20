# 折线图：line_chart.py
import numpy as np
import matplotlib.pyplot as plt
from self_mpl_config import setup_matplotlib_config

setup_matplotlib_config()
# 1. 创建figure实例 (找对象：画板)
fig = plt.figure(figsize=(12, 6), dpi=100)

# 2. 在figure上创建axes (找对象：坐标纸)
ax = fig.add_subplot(121) # (行，列，第几个)

# 准备数据
x = np.linspace(0, 2 * np.pi, 400)
y_sin = np.sin(x)

# 画线
ax.plot(x, y_sin, label='正弦曲线', color='blue')
# 添加标题和标签
ax.set_title('正弦函数')
ax.set_xlabel('X轴 (弧度)')
ax.set_ylabel('Y轴')

# 添加图例和网格
ax.legend()
ax.grid(True)

ax = fig.add_subplot(122) # (行，列，第几个)

y_cos = np.cos(x)

# 画线
ax.plot(x, y_cos, label='余弦曲线', color='red', linestyle='--')
# 添加标题和标签
ax.set_title('余弦函数')
ax.set_xlabel('X轴 (弧度)')
ax.set_ylabel('Y轴')

# 最终展示
plt.show()

# 导出图
fig.savefig('example.svg', format='svg', bbox_inches='tight')
