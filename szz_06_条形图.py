# 绘制条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

a = ["电影", "信", "微信", "新媒体", "报纸", "电视", "广播"]
b = [100, 130, 120, 23, 14, 144, 145]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(len(a)), b, width=0.3)

plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=45, fontsize=20)
plt.yticks(fontsize=20)

plt.show()

