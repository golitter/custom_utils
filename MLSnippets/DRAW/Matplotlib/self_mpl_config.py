import matplotlib.pyplot as plt
import numpy as np

# https://zhuanlan.zhihu.com/p/113842270

# 自定义绘图颜色：https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3

###############################################
# 散点图：scatter_plot.py
# 折线图：line_chart.py
# 柱状图：bar_graph.py
# 饼图：pie_chart.py
# 直方图：histogram.py
# 箱线图：box_plot.py
###############################################

def setup_matplotlib_config(os_name="windows"):
    """设置matplotlib的配置，包括主题和中文显示。"""
    # 先设置主题，再设置其他的
    
    # 设置主题
    # plt.style.use('ggplot')
    plt.style.use('seaborn-v0_8-darkgrid')

    # 中文
    # windows
    if os_name == "windows":
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者 'Microsoft YaHei'
    # macOS
    if os_name == 'macos':
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
    # linux
    if os_name == "linux":
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC']

    # --- 解决负号'-'显示为方块的问题 ---
    plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

    setup_matplotlib_config()

    # 1. 创建figure实例 (找对象：画板)
    fig = plt.figure(figsize=(8, 5), dpi=100)

    # 2. 在figure上创建axes (找对象：坐标纸)
    ax = fig.add_subplot(111)

    # 准备数据
    x = np.linspace(0, 2 * np.pi, 400)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 画线
    ax.plot(x, y_sin, label='正弦曲线', color='blue')
    ax.plot(x, y_cos, label='余弦曲线', color='red', linestyle='--')
    # 添加标题和标签
    ax.set_title('正弦与余弦函数')
    ax.set_xlabel('X轴 (弧度)')
    ax.set_ylabel('Y轴')

    # 添加图例和网格
    ax.legend()
    ax.grid(True)

    # 最终展示
    plt.show()

    # 导出图
    fig.savefig('example.svg', format='svg', bbox_inches='tight')
