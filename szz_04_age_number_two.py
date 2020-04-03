from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc", size=20)

# 数据
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1]
min = min(min(y_1), min(y_2))
max = max(max(y_1), max(y_2))

x = range(11, 31)

# 设置图像大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置x轴刻度
_xticks_label = ["{}岁".format(i) for i in range(11, 31)]
_yticks_label = [i / 2 for i in range(min, max * 2 + 4)]
plt.xticks(x, _xticks_label, fontproperties=my_font)
plt.yticks(_yticks_label, fontsize=20)
# 设置x y轴的标题
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("数量", fontproperties=my_font)
plt.title("年龄和数量的关系", fontproperties=my_font)

# 设置网格线
plt.grid(alpha=0.5, linestyle=":")
# 增加图例
# 1. 增加图例名称
# 线的类型
# '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

# 颜色的话可以用颜色表
plt.plot(x, y_1, label="自己", color="orange", linestyle=":", linewidth="6")
plt.plot(x, y_2, label="同桌", color="cyan", linestyle="-")
# 2. 显示图例，注意这里的字体配置文件是prop
# loc 参数是表示图例的位置:
# 'best'： 系统自动识别的线少的地方
# 'upper right'
# 'lower left'
# 'lower tight'
# 'right'
# 'center left'
# 'center right'
# 'lower center'
# 'upper center'
# 'center'
plt.legend(prop=my_font, loc="upper left")

plt.show()
