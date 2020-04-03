from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# !!! 别忘了fname
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc", size=30)

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
x = range(11, 31)

# ?如何改变x周的刻度
plt.figure(figsize=(20, 8), dpi=80)
# -- 使用下面的方式

_xtick_label = ["{}岁".format(i) for i in range(11, 31)]
_ytick_label = [i / 2 for i in range(min(y), max(y) * 2 + 4)]

# 不论是刻度还是标签，只要是使用了中文，都需要加上fontproperties这个关键字
# !!! 注意如果设置了fontproperties 之后再设置x轴的字体大小会失败，需要在my_font中用size设置大小
plt.xticks(list(x), _xtick_label, rotation=270, fontproperties=my_font)
plt.yticks(_ytick_label, fontsize=30)

plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("数量", fontproperties=my_font)
plt.title("年龄和数量的对应关系",fontproperties=my_font)

# 设置网格和网格线的透明度
plt.grid(alpha=0.4)

plt.plot(x, y)
plt.show()

# 设置图形大小
# 设置x轴刻度
#   1. 设置x轴内容
# 设置中文
