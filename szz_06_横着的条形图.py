# 绘制横着的条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

a = ["电影", "信", "微信", "新媒体", "报纸", "电视", "广播"]
b = [100, 130, 120, 23, 14, 144, 145]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置坐标轴刻度
# 横着的时候对应的坐标轴也要变
plt.yticks(range(len(a)), a, fontproperties=my_font, fontsize=20)
plt.xticks(fontsize=20)

# 注意这里的参数
plt.barh(range(len(a)), b, height=0.3,color="orange")
# 绘制网格
plt.grid(alpha=0.3)


plt.show()

