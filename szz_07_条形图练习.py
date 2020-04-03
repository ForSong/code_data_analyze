# 多个条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
my_font2 = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=20)

# 准备数据
a = ["星球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 159, 2045, 168]
b_14 = [2358, 399, 2358, 362]

# 这里的数字乘以三以后要比1小，否则会重叠
bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width * 2 for i in x_14]

# 设置图形大小
plt.figure(figsize=(10, 8), dpi=60)

# 绘制条形图，关键部分，要往右移动，但是要小于0.4 否则会重叠
plt.bar(x_14, b_14, width=bar_width,label="9月14日")
plt.bar(x_15, b_15, width=bar_width,label="9月15日")
plt.bar(x_16, b_16, width=bar_width,label="9月16日")

# 设置x轴刻度
plt.xticks(x_15, a, fontproperties=my_font, fontsize=20)
plt.yticks(fontsize=20)

# 设置图例,注意这里引入中文用的是prop
# 如果想修改图例中的字体，可以另外设置一个字体的properties
plt.legend(loc='upper center',prop=my_font2)


plt.show()
